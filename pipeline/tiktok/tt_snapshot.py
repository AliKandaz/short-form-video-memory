#!/usr/bin/env python3
"""Snapshot a TikTok account from public pages: followers, then per video the stats, the category TikTok filed it under,
whether the caption's hashtags registered as hashtags, the AI labels and any penalty shown. Written 18 Nov 2026 (CLAUDE.md 12.1).

    PYTHONPATH=<dir with yt_dlp> python3 tt_snapshot.py <handle> [--limit N]

Needs yt-dlp importable (pip install --target <dir> yt-dlp) and www.tiktok.com reachable.
Columns: views, likes, comments, shares, saves; cat = diversificationLabels; tags = hashtags TikTok registered (0 = the caption's
hashtags are plain text); ai = TikTok's label (moderationAigcLabelType) / the creator's (IsAigc); pen = display_penalty_type;
mod = penaltyContext status/video_status/tns_status, reviewed, lifecycle (21 Nov 2026: 102/10/102 r0 L1100 on all 13 of ours,
hits included), then any of REVIEWING, PROHIBITED, PRIVATE, TAKEDOWN, NOINDEX and WARN that are set. Compare flops with hits.
"""
import datetime
import json
import re
import subprocess
import sys
import time

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/126.0.0.0 Safari/537.36")


def page_json(url):
    html = subprocess.run(["curl", "-sS", "-L", "-A", UA, "-H", "Accept-Language: en-US,en;q=0.9", url],
                          capture_output=True, text=True).stdout
    m = re.search(r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__"[^>]*>(.*?)</script>', html, re.S)
    return json.loads(m.group(1))["__DEFAULT_SCOPE__"] if m else {}


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    handle = args[0].lstrip("@")
    limit = int(args[args.index("--limit") + 1]) if "--limit" in args else None
    prof = page_json(f"https://www.tiktok.com/@{handle}").get("webapp.user-detail", {}).get("userInfo", {})
    st, user = prof.get("stats", {}), prof.get("user", {})
    print(f"@{handle} ({user.get('nickname')!r}): {st.get('followerCount')} followers, {st.get('heartCount')} likes, "
          f"{st.get('videoCount')} videos | bio {user.get('signature')!r}")
    print(f"account flags: privateAccount {user.get('privateAccount')}, secret {user.get('secret')}, "
          f"isEmbedBanned {user.get('isEmbedBanned')} (all False = nothing visible from outside)")
    flat = subprocess.run([sys.executable, "-m", "yt_dlp", "--flat-playlist", "-J", f"https://www.tiktok.com/@{handle}"],
                          capture_output=True, text=True)
    entries = sorted(json.loads(flat.stdout).get("entries", []), key=lambda e: e.get("timestamp") or 0, reverse=True)
    total = sum(e.get("view_count") or 0 for e in entries)
    print(f"{len(entries)} videos, {total:,} views\n")
    for e in entries[:limit]:
        when = datetime.datetime.fromtimestamp(e.get("timestamp") or 0, datetime.UTC).strftime("%m-%d %H:%M")
        it = page_json(f"https://www.tiktok.com/@{handle}/video/{e['id']}").get("webapp.video-detail", {}) \
            .get("itemInfo", {}).get("itemStruct", {})
        cat = ", ".join(it.get("diversificationLabels") or []) or "-"
        tags = len([x for x in it.get("textExtra") or [] if x.get("hashtagName")])
        ai = f"{it.get('moderationAigcLabelType') or '-'}/{'yes' if it.get('IsAigc') else 'no'}"
        pc = it.get("penaltyContext") or {}
        pen = pc.get("display_penalty_type", "?")
        mod = (f"{pc.get('status')}/{pc.get('video_status')}/{pc.get('tns_status')} r{pc.get('reviewed')} "
               f"L{pc.get('conclu_lifecycle_status')}")
        flags = [name for name, on in (("REVIEWING", it.get("isReviewing")), ("PROHIBITED", it.get("isProhibited")),
                                       ("PRIVATE", it.get("privateItem")), ("TAKEDOWN", it.get("takeDown")),
                                       ("NOINDEX", it.get("indexEnabled") is False), ("WARN", it.get("warnInfo"))) if on]
        print(f"{e['id']} {when} UTC {e.get('duration')}s  {e.get('view_count') or 0:>9,} views  "
              f"{e.get('like_count') or 0}/{e.get('comment_count') or 0}/{e.get('repost_count') or 0}/{e.get('save_count') or 0}"
              f"  cat [{cat}]  tags {tags}  ai {ai}  pen {pen}  mod {mod} {' '.join(flags)}".rstrip())
        print(f"    {(e.get('title') or '')[:110]}")
        time.sleep(1.5)


if __name__ == "__main__":
    main()
