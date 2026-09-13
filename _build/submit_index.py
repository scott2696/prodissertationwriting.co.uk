#!/usr/bin/env python3
"""Send this site's URLs to RalfyIndex for indexing.

    python3 _build/submit_index.py --status    # check the key, send nothing
    python3 _build/submit_index.py --dry-run   # show what would go, send nothing
    python3 _build/submit_index.py             # submit whatever is new
    python3 _build/submit_index.py --all       # resubmit every sitemap URL

sitemap.xml is the authoritative list of what this site wants indexed, so the
delta between it and _build/indexed.json is exactly what is worth sending.
Nothing is sent twice: a URL is recorded only once the API has actually
accepted it, so a failed run leaves the state untouched and simply goes again.

Unlike the keno-results build there is no page-kind filter here. This site is
39 static pages, all of them worth indexing, and there is no dated archive
generating hundreds of low-value URLs a year.

Submission costs one credit per URL.

The API key is NEVER stored in this repo, which is public and is itself the
web root. It comes from the macOS keychain (service `ralfyindex-api`) or the
RALFY_API_KEY environment variable.

Stdlib only.
"""
import argparse, json, os, subprocess, sys, urllib.error, urllib.request
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITEMAP = os.path.join(ROOT, "sitemap.xml")
STATE = os.path.join(ROOT, "_build", "indexed.json")
ENDPOINT = "https://api.ralfyindex.com/project"
STATUS_URL = "https://api.ralfyindex.com/status"
PROJECT = "prodissertationwriting.co.uk"
BATCH = 100
NS = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}


def api_key():
    env = os.environ.get("RALFY_API_KEY")
    if env:
        return env.strip()
    try:
        r = subprocess.run(["security", "find-generic-password", "-s", "ralfyindex-api", "-w"],
                           capture_output=True, text=True, timeout=15)
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        pass
    return None


def post(url, payload, timeout=30):
    req = urllib.request.Request(
        url, data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json", "User-Agent": PROJECT + "/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        body = r.read().decode("utf-8", "replace")
    status = getattr(r, "status", 200)
    try:
        return status, json.loads(body)
    except json.JSONDecodeError:
        return status, {"raw": body[:400]}


def accepted_ok(body):
    """RalfyIndex answers a bad key with HTTP 200 and an errorCode, so success
    has to be read out of the body rather than off the status line."""
    if not isinstance(body, dict):
        return False
    if body.get("errorCode"):
        return False
    if "error" in body:
        return False
    return body.get("status") in ("ok", "success", True) or "creditsUsed" in body


def sitemap_urls():
    root = ET.parse(SITEMAP).getroot()
    return [u.find("s:loc", NS).text.strip() for u in root.findall("s:url", NS)]


def load_state():
    try:
        with open(STATE, encoding="utf-8") as fh:
            return json.load(fh)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"submitted": []}


def save_state(state):
    with open(STATE, "w", encoding="utf-8") as fh:
        json.dump(state, fh, indent=1, ensure_ascii=False)
        fh.write("\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--all", action="store_true", help="resubmit every sitemap URL")
    args = ap.parse_args()

    key = api_key()
    if not key:
        print("index: no key in the keychain ('ralfyindex-api') or RALFY_API_KEY", file=sys.stderr)
        return 1

    if args.status:
        try:
            code, body = post(STATUS_URL, {"apikey": key})
            print("index: status %s -> %s" % (code, json.dumps(body)[:300]))
        except urllib.error.URLError as e:
            print("index: status check failed -> %s" % e, file=sys.stderr)
            return 1
        return 0

    urls = sitemap_urls()
    state = load_state()
    done = set(state.get("submitted", []))
    todo = urls if args.all else [u for u in urls if u not in done]

    print("index: %d URLs in sitemap, %d already submitted, %d to send"
          % (len(urls), len(done), len(todo)))
    if not todo:
        print("index: nothing new.")
        return 0

    if args.dry_run:
        for u in todo:
            print("   would send:", u)
        print("index: dry run, nothing sent. %d credits would be used." % len(todo))
        return 0

    sent = []
    for i in range(0, len(todo), BATCH):
        chunk = todo[i:i + BATCH]
        payload = {"apikey": key, "projectName": PROJECT, "urls": chunk}
        try:
            code, body = post(ENDPOINT, payload)
        except urllib.error.URLError as e:
            print("index: request failed -> %s" % e, file=sys.stderr)
            break
        if not accepted_ok(body):
            print("index: API rejected the batch -> %s" % json.dumps(body)[:300], file=sys.stderr)
            break
        sent += chunk
        print("index: accepted %d URLs -> %s" % (len(chunk), json.dumps(body)[:200]))

    if sent:
        state["submitted"] = sorted(done | set(sent))
        save_state(state)
        print("index: recorded %d submitted URLs in %s" % (len(sent), os.path.relpath(STATE, ROOT)))
    return 0 if sent or not todo else 1


if __name__ == "__main__":
    sys.exit(main())
