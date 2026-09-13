#!/usr/bin/env python3
"""Report where each target keyword appears on its page.

Checks, in priority order: the title tag, the H1, any H2-H4, and the FAQ
<summary> elements (which are headings in effect and are what the FAQPage
schema exposes). Anything found only in body copy is reported separately so
it is visible rather than assumed.

Matching is on normalised word sets, not exact strings, so "best UK casino
sites" matches a heading reading "the best UK casino sites" — but every word
must be present in that one heading.
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGETS = json.load(open(os.path.join(ROOT, "_build", "target_keywords.json")))
STOP = {"the", "a", "an", "and", "to", "of", "in", "is", "on", "for", "you", "with"}

def norm(t):
    t = re.sub(r"<[^>]+>", " ", t)
    t = (t.replace("&pound;", "£").replace("&amp;", "&").replace("&mdash;", " ")
          .replace("&middot;", " ").replace("&rsquo;", "'").replace("&ndash;", " ")
          .replace("&ldquo;", " ").replace("&rdquo;", " ").replace("&nbsp;", " "))
    return re.sub(r"\s+", " ", t).strip().lower()

def words(kw):
    return [w for w in re.findall(r"[a-z0-9£%']+", kw.lower()) if w not in STOP]

def hit(kw, text):
    return all(w in text for w in words(kw))

def audit():
    out = {}
    for url, spec in TARGETS.items():
        built = os.path.join(ROOT, url.strip("/"), "index.html") if url != "/" else os.path.join(ROOT, "index.html")
        s = open(built, encoding="utf-8").read()
        title = norm(re.search(r"<title>(.*?)</title>", s, re.S).group(1))
        h1 = norm(re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S).group(1))
        heads = [norm(m) for m in re.findall(r"<h[2-4][^>]*>(.*?)</h[2-4]>", s, re.S)]
        faqs = [norm(m) for m in re.findall(r"<summary>(.*?)</summary>", s, re.S)]
        body = norm(re.sub(r"<script.*?</script>", "", s[s.find("<body"):], flags=re.S))

        rows = []
        for kw in [spec["primary"]] + spec["targets"]:
            where = []
            if hit(kw, title): where.append("title")
            if hit(kw, h1): where.append("H1")
            if any(hit(kw, h) for h in heads): where.append("H2-4")
            if any(hit(kw, f) for f in faqs): where.append("FAQ")
            if not where and hit(kw, body): where.append("body only")
            rows.append((kw, where))
        out[url] = rows
    return out

if __name__ == "__main__":
    res = audit()
    total = covered = heading_only = 0
    for url, rows in res.items():
        miss = [k for k, w in rows if not w]
        bodyonly = [k for k, w in rows if w == ["body only"]]
        inhead = [k for k, w in rows if w and w != ["body only"]]
        total += len(rows); covered += len(inhead) + len(bodyonly); heading_only += len(inhead)
        print("%-40s %2d/%2d in headings" % (url, len(inhead), len(rows)))
        for k in bodyonly: print("      body only : %s" % k)
        for k in miss:     print("      MISSING   : %s" % k)
    print("\n%d keywords | %d in a heading | %d body only | %d missing"
          % (total, heading_only, covered - heading_only, total - covered))
