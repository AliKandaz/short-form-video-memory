#!/usr/bin/env python3
"""Compact saturation report for candidate topics: run YouTube searches and summarise each in a few lines.

    python3 yt_saturation.py <work_dir> "query one" "query two" ...

For each query prints how many Shorts the results page shows, the top Shorts by views, and the top long videos by
views (with age and channel). Uses yt_search.py's fetch and parsing; needs www.youtube.com on the allowlist.
Pace: one search every ~3 s.
"""
import json
import re
import subprocess
import sys
import time
import urllib.parse
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from yt_search import fetch, text_of, walk  # noqa: E402


def views_to_int(text):
    if not text:
        return 0
    t = text.lower().replace(",", "")
    m = re.search(r"([\d.]+)\s*([km]?)", t)
    if not m:
        return 0
    n = float(m.group(1))
    return int(n * {"": 1, "k": 1_000, "m": 1_000_000}[m.group(2)])


def summarise(data):
    shorts = []
    for s in walk(data, "shortsLockupViewModel", []):
        om = s.get("overlayMetadata", {})
        v = (om.get("secondaryText") or {}).get("content") or ""
        shorts.append((views_to_int(v.split("·")[0]), v, (om.get("primaryText") or {}).get("content") or ""))
    seen, uniq = set(), []
    for row in sorted(shorts, reverse=True):
        if row[2] not in seen:
            seen.add(row[2])
            uniq.append(row)
    vids = []
    for v in walk(data, "videoRenderer", []):
        vids.append((views_to_int(text_of(v.get("viewCountText"))), text_of(v.get("viewCountText")) or "",
                     text_of(v.get("publishedTimeText")) or "", text_of(v.get("ownerText")) or "",
                     text_of(v.get("title")) or ""))
    return uniq, sorted(vids, reverse=True)


def main(out_dir, queries):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    for i, q in enumerate(queries):
        dest = out / f"sat_{i}.html"
        status = fetch("https://www.youtube.com/results?search_query=" + urllib.parse.quote_plus(q), dest)
        if not status.startswith("200"):
            print(f"\n## {q}: http {status}")
            continue
        html = dest.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"var ytInitialData\s*=\s*(\{.*?\});</script>", html, re.S)
        if not m:
            print(f"\n## {q}: no data")
            continue
        shorts, vids = summarise(json.loads(m.group(1)))
        print(f"\n## {q}  [{len(shorts)} distinct Shorts on page]")
        for n, v, t in shorts[:4]:
            print(f"   S {v[:22]:<22} {t[:80]}")
        for n, v, age, ch, t in vids[:3]:
            print(f"   V {v[:16]:<16} {age[:12]:<12} {ch[:22]:<22} {t[:60]}")
        time.sleep(3)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
