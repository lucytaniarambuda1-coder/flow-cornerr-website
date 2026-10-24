#!/usr/bin/env python3
"""Checks every external link used in the Start a Business section (and any https link in generated HTML)
and prints the HTTP status. Run before deploying:  python3 tools/check_links.py
Exit code is 1 if any link fails, so it can be used as a pre-deploy gate."""
import os
import re
import ssl
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINK = re.compile(r'href="(https?://[^"]+)"')
SKIP = ("wa.me", "linkedin.com", "instagram.com", "fonts.googleapis.com", "flowcornerr.netlify.app")


def collect():
    links = {}
    for dirpath, _, files in os.walk(ROOT):
        if ".git" in dirpath:
            continue
        for f in files:
            if f.endswith(".html"):
                path = os.path.join(dirpath, f)
                for m in LINK.finditer(open(path, encoding="utf-8").read()):
                    url = m.group(1)
                    if not any(x in url for x in SKIP):
                        links.setdefault(url, []).append(os.path.relpath(path, ROOT))
    return links


def check(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=20, context=ssl.create_default_context()) as r:
            return url, r.status
    except Exception as e:  # noqa: BLE001
        code = getattr(e, "code", None)
        return url, code or f"ERR {type(e).__name__}"


if __name__ == "__main__":
    links = collect()
    bad = 0
    with ThreadPoolExecutor(8) as ex:
        for url, status in sorted(ex.map(check, links)):
            ok = status == 200
            warn = status in (403, 429)  # site blocks scripts; open it in a browser to confirm
            bad += 0 if (ok or warn) else 1
            tag = "OK   " if ok else ("WARN " if warn else "FAIL ")
            print(tag + str(status).ljust(14) + url + ("" if ok else "   <- " + links[url][0]))
    print(f"\n{len(links)} links checked, {bad} failing")
    sys.exit(1 if bad else 0)
