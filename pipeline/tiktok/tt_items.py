#!/usr/bin/env python3
"""Save a TikTok account's public data for later reading: the video list with stats, the profile, and each video's detail.
Written 21 Nov 2026 for the @whatifplus study (CLAUDE.md 1.7, 12.5).

    PYTHONPATH=<dir with yt_dlp> python3 tt_items.py <handle> <out_dir>

Writes <out_dir>/_flat.json (yt-dlp's flat list: views, likes, comments, shares as repost_count, saves, timestamp, duration,
caption), <out_dir>/_profile.json (followers, likes, bio, bio link, creation time) and <out_dir>/<video id>.json (the
"webapp.video-detail" block: category, registered hashtags, AI labels, moderation fields, served resolutions, loudness).
Read-only, paced at about one request a second. Needs www.tiktok.com reachable.
"""
import json
import os
import re
import subprocess
import sys
import time

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/126.0.0.0 Safari/537.36")


def page_json(url):
    html = subprocess.run(["curl", "-sS", "-L", "-m", "40", "-A", UA, "-H", "Accept-Language: en-US,en;q=0.9", url],
                          capture_output=True, text=True).stdout
    m = re.search(r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__"[^>]*>(.*?)</script>', html, re.S)
    return json.loads(m.group(1))["__DEFAULT_SCOPE__"] if m else {}


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    handle, out = sys.argv[1].lstrip("@"), sys.argv[2]
    os.makedirs(out, exist_ok=True)
    flat_path = os.path.join(out, "_flat.json")
    if not os.path.exists(flat_path):
        r = subprocess.run([sys.executable, "-m", "yt_dlp", "--flat-playlist", "-J", f"https://www.tiktok.com/@{handle}"],
                           capture_output=True, text=True)
        open(flat_path, "w").write(r.stdout)
    entries = sorted(json.load(open(flat_path)).get("entries", []), key=lambda e: e.get("timestamp") or 0)
    prof = page_json(f"https://www.tiktok.com/@{handle}")
    json.dump(prof, open(os.path.join(out, "_profile.json"), "w"))
    info = prof.get("webapp.user-detail", {}).get("userInfo", {})
    st, user = info.get("stats", {}), info.get("user", {})
    print(f"@{handle} ({user.get('nickname')!r}): {st.get('followerCount')} followers, {st.get('heartCount')} likes, "
          f"{len(entries)} videos, {sum(e.get('view_count') or 0 for e in entries):,} views | created {user.get('createTime')} "
          f"| bio {user.get('signature')!r} | link {(user.get('bioLink') or {}).get('link')}")
    saved = 0
    for e in entries:
        p = os.path.join(out, e["id"] + ".json")
        if os.path.exists(p) and os.path.getsize(p) > 2000:
            saved += 1
            continue
        for _ in range(2):
            d = page_json(f"https://www.tiktok.com/@{handle}/video/{e['id']}").get("webapp.video-detail", {})
            if d.get("itemInfo", {}).get("itemStruct"):
                json.dump(d, open(p, "w"))
                saved += 1
                break
            time.sleep(3)
        else:
            print("no detail for", e["id"])
        time.sleep(1.2)
    print(f"saved {saved} of {len(entries)} video records in {out}")


if __name__ == "__main__":
    main()
