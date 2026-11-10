"""Check whether candidate handles are in use on YouTube (and optionally TikTok).

YouTube: GET /@handle -> 404 means no channel uses it; 200 means taken (prints the channel title and size).
TikTok:  GET /@handle -> the embedded JSON carries statusCode 10221/10202 for a missing user, 0 with userInfo for a real one.
Usage: handles.py <out_dir> yt|tt handle [handle ...]
"""
import json
import re
import subprocess
import sys
import time
from pathlib import Path

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/126.0.0.0 Safari/537.36")


def get(url, dest):
    cmd = ["curl", "-sS", "-o", str(dest), "-w", "%{http_code}", "--max-redirs", "2", "-L",
           "-H", "Accept-Language: en-US,en;q=0.9", "-H", "Cookie: SOCS=CAI; CONSENT=YES+1", "-A", UA, url]
    return subprocess.run(cmd, capture_output=True, text=True).stdout.strip()


def yt(out, handle):
    dest = out / f"yt_{handle}.html"
    code = get(f"https://www.youtube.com/@{handle}", dest)
    info = ""
    if code == "200":
        html = dest.read_text(encoding="utf-8", errors="replace")
        t = re.search(r'<meta property="og:title" content="([^"]*)"', html)
        subs = re.search(r'"([\d.,]+[KM]? subscribers?)"', html)
        vids = re.search(r'"content":\s*"([\d.,]+[KM]? videos?)"', html)
        info = f"TAKEN by {t.group(1) if t else '?'} | {subs.group(1) if subs else 'subs hidden/none'} | {vids.group(1) if vids else 'no videos shown'}"
    elif code == "404":
        info = "not in use"
    dest.unlink(missing_ok=True)
    print(f"YT @{handle:<24} {code} {info}")


def tt(out, handle):
    dest = out / f"tt_{handle}.html"
    code = get(f"https://www.tiktok.com/@{handle}", dest)
    info = ""
    if code == "200":
        html = dest.read_text(encoding="utf-8", errors="replace")
        m = re.search(r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__"[^>]*>(.*?)</script>', html, re.S)
        if m:
            try:
                data = json.loads(m.group(1))
                detail = data.get("__DEFAULT_SCOPE__", {}).get("webapp.user-detail", {})
                sc = detail.get("statusCode")
                user = (detail.get("userInfo") or {}).get("user") or {}
                stats = (detail.get("userInfo") or {}).get("stats") or {}
                if user.get("uniqueId"):
                    info = (f"TAKEN by {user.get('nickname')!r} | followers {stats.get('followerCount')} | "
                            f"videos {stats.get('videoCount')} | likes {stats.get('heartCount')} | bio {user.get('signature')!r}")
                else:
                    info = f"no user (statusCode {sc})"
            except json.JSONDecodeError:
                info = "unparseable"
        else:
            info = "no data block (possibly a challenge page)"
    dest.unlink(missing_ok=True)
    print(f"TT @{handle:<24} {code} {info}")


def main(out_dir, site, handles):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    fn = yt if site == "yt" else tt
    for h in handles:
        fn(out, h)
        time.sleep(1.3)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3:])
