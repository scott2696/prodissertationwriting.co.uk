"""Check the uncontested opportunity queries are answered.

These are question-shaped queries derived from the competitor weaknesses in
research/COMPETITOR-ANALYSIS.md section 1.8 — things none of the pages ranking
top three for our head terms covers. Answering the 84 harvested competitor
questions buys parity; answering these is the part that is meant to win.

Same matching rule as qcheck.py: 70% of a question's content words must land in
one FAQ summary, heading, paragraph, list item or table cell.
"""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Q = json.load(open(os.path.join(ROOT, "_build", "opportunity_questions.json")))
STOP = {"the","a","an","and","or","to","of","in","is","are","do","does","did","i",
        "my","you","your","it","at","on","for","with","what","which","how","can",
        "be","that","this","there","they","them","from","by","me","we","us","really",
        "actually","right","now","up","s","t","don"}

def norm(t):
    t = re.sub(r"<[^>]+>", " ", t)
    for a, b in (("&pound;","£"),("&amp;","&"),("&mdash;"," "),("&middot;"," "),
                 ("&rsquo;","'"),("&ldquo;"," "),("&rdquo;"," "),("&ndash;"," "),("&nbsp;"," ")):
        t = t.replace(a, b)
    return re.sub(r"\s+", " ", t).strip().lower()

def content(q):
    return [w for w in re.findall(r"[a-z0-9£%']+", q.lower()) if w not in STOP and len(w) > 1]

def audit():
    results = {}
    for url, questions in Q.items():
        if url.startswith("_"):
            continue
        f = os.path.join(ROOT, url.strip("/"), "index.html") if url != "/" else os.path.join(ROOT, "index.html")
        s = open(f, encoding="utf-8").read()
        body = s[s.find("<body"):]
        body = re.sub(r"<script.*?</script>", "", body, flags=re.S)
        chunks = ([norm(x) for x in re.findall(r"<summary>(.*?)</summary>", body, re.S)] +
                  [norm(x) for x in re.findall(r"<h[1-4][^>]*>(.*?)</h[1-4]>", body, re.S)] +
                  [norm(x) for x in re.findall(r"<p[^>]*>(.*?)</p>", body, re.S)] +
                  [norm(x) for x in re.findall(r"<li[^>]*>(.*?)</li>", body, re.S)] +
                  [norm(x) for x in re.findall(r"<td[^>]*>(.*?)</td>", body, re.S)])
        rows = []
        for q in questions:
            w = content(q)
            need = max(1, int(len(w) * 0.7 + 0.999))
            best = max((sum(1 for x in w if x in c) for c in chunks), default=0)
            rows.append((q, best >= need, best, len(w)))
        results[url] = rows
    return results

if __name__ == "__main__":
    res = audit()
    tot = ans = 0
    for url, rows in res.items():
        miss = [r for r in rows if not r[1]]
        tot += len(rows); ans += len(rows) - len(miss)
        print("%-40s %2d/%2d answered" % (url, len(rows) - len(miss), len(rows)))
        for q, _, hit, n in miss:
            print("      NOT YET ANSWERED: %s  (%d/%d words matched)" % (q, hit, n))
    print("\n%d opportunity queries | %d answered | %d not" % (tot, ans, tot - ans))
