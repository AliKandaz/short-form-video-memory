#!/usr/bin/env python3
"""Snapshot a YouTube channel's Shorts: channel facts, per-video stats, and a made-for-kids check.

    python3 yt_snapshot.py @handle [work_dir]

Needs these hosts on the environment's allowlist: www.youtube.com, i.ytimg.com, yt3.ggpht.com,
yt3.googleusercontent.com. Reads public pages only (no login, no API key).

Notes from the 9 Nov 2026 audit:
- /watch?v=<id> redirects cloud IPs to google.com/sorry (blocked); /shorts/<id> works.
- The player response is bot-gated ("Sign in to confirm you're not a bot"), so there are no captions,
  storyboards or downloads. Likes, views, dates and comments come from ytInitialData instead.
- A Short that YouTube serves in made-for-kids mode has no comment button, no "Save to playlist" menu
  item, no "Original Sound" pivot (it says "Feature not available for this video"), and the hashtags in
  its title are not links. The audience setting itself is only visible to the owner in Studio; this is
  the public signature of it.
- First frame: https://i.ytimg.com/vi/<id>/frame0.jpg   cover frame: https://i.ytimg.com/vi/<id>/oar2.jpg
"""
import json
import re
import subprocess
import sys
import time
from pathlib import Path

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/126.0.0.0 Safari/537.36")
HDRS = ["-H", "Accept-Language: en-US,en;q=0.9", "-H", "Cookie: SOCS=CAI; CONSENT=YES+1", "-A", UA]


def walk(node, key, out):
    """Collect every value stored under `key` anywhere in a JSON tree."""
    if isinstance(node, dict):
        for k, v in node.items():
            if k == key:
                out.append(v)
            walk(v, key, out)
    elif isinstance(node, list):
        for v in node:
            walk(v, key, out)
    return out


def text_of(node):
    if node is None:
        return None
    if isinstance(node, str):
        return node
    if "simpleText" in node:
        return node["simpleText"]
    if "content" in node and isinstance(node["content"], str):
        return node["content"]
    if "runs" in node:
        return "".join(r.get("text", "") for r in node["runs"])
    return None


def get(url, dest):
    cmd = ["curl", "-sS", "-o", str(dest), "-w", "%{http_code}", "--max-redirs", "0", *HDRS, url]
    return subprocess.run(cmd, capture_output=True, text=True).stdout.strip()


def post(endpoint, key, body, dest):
    url = f"https://www.youtube.com/youtubei/v1/{endpoint}?prettyPrint=false&key={key}"
    cmd = ["curl", "-sS", "-o", str(dest), "-w", "%{http_code}", "-X", "POST",
           "-H", "Content-Type: application/json", "-H", "Origin: https://www.youtube.com", *HDRS,
           "--data-binary", json.dumps(body), url]
    return subprocess.run(cmd, capture_output=True, text=True).stdout.strip()


def initial(html):
    m = re.search(r"var ytInitialData\s*=\s*(\{.*?\});</script>", html, re.S)
    return json.loads(m.group(1)) if m else None


def ytcfg(html):
    cfg = {}
    for m in re.finditer(r"ytcfg\.set\((\{.*?\})\);", html, re.S):
        try:
            cfg.update(json.loads(m.group(1)))
        except json.JSONDecodeError:
            pass
    return cfg


def channel(handle, work):
    dest = work / "channel_shorts.html"
    code = get(f"https://www.youtube.com/{handle}/shorts", dest)
    if code != "200":
        sys.exit(f"channel page: http {code}")
    data = initial(dest.read_text(encoding="utf-8", errors="replace"))
    meta = data.get("metadata", {}).get("channelMetadataRenderer", {})
    header = data.get("header", {})
    parts = []
    for vm in walk(header, "contentMetadataViewModel", []):
        for row in vm.get("metadataRows", []):
            parts += [text_of(p.get("text")) for p in row.get("metadataParts", [])]
    print(f"CHANNEL  {meta.get('title')!r}  {' | '.join(p for p in parts if p)}")
    print(f"  id          {meta.get('externalId')}")
    print(f"  description {meta.get('description')!r}")
    print(f"  keywords    {meta.get('keywords')!r}")
    print(f"  avatar      {(meta.get('avatar', {}).get('thumbnails') or [{}])[0].get('url')}")
    banners = walk(header, "imageBannerViewModel", [])
    burl = None
    if banners:
        srcs = banners[0].get("image", {}).get("sources", [])
        burl = srcs[-1].get("url") if srcs else None
    print(f"  banner      {burl}")
    print(f"  tabs        {[t.get('title') for t in walk(data, 'tabRenderer', [])]}")
    shorts = []
    for s in walk(data, "shortsLockupViewModel", []):
        ids = walk(s, "videoId", [])
        om = s.get("overlayMetadata", {})
        shorts.append((ids[0] if ids else None, (om.get("primaryText") or {}).get("content")))
    return shorts


def short(vid, work, with_comments):
    dest = work / f"short_{vid}.html"
    code = get(f"https://www.youtube.com/shorts/{vid}", dest)
    if code != "200":
        print(f"  {vid}: http {code}")
        return
    html = dest.read_text(encoding="utf-8", errors="replace")
    data = initial(html)
    raw = json.dumps(data)
    hdr = walk(data, "videoDescriptionHeaderRenderer", [])
    views = text_of(hdr[0].get("views")) if hdr else None
    date = text_of(hdr[0].get("publishDate")) if hdr else None
    likes = next((f.get("accessibilityText") for f in walk(data, "factoidRenderer", [])
                  if "like" in (f.get("accessibilityText") or "").lower()), None)
    title = next((text_of(t.get("videoTitle")) for t in walk(data, "videoTitleHeaderViewModel", [])), None)
    desc = next((text_of(d.get("attributedDescriptionBodyText")) or text_of(d.get("descriptionBodyText"))
                 for d in walk(data, "expandableVideoDescriptionBodyRenderer", [])), None)
    overlay = (walk(data, "reelPlayerOverlayRenderer", []) or [{}])[0]
    menu = [text_of(li.get("title")) for li in walk(overlay.get("menu"), "listItemViewModel", [])]
    has_comment_button = "id.reel_comment_button" in raw
    has_save = "Save to playlist" in menu
    sound_blocked = "soundAttributionTitle" not in raw      # normal Shorts carry an "Original Sound" pivot
    kids_mode = (not has_comment_button) and (not has_save)
    print(f"\n  {vid}  {date}  {views}  {likes}")
    print(f"    title        {title!r}")
    print(f"    description  {('(empty)' if not desc else repr(desc[:160]))}")
    print(f"    comments {'on' if has_comment_button else 'OFF'} | save-to-playlist {'yes' if has_save else 'NO'}"
          f" | sound page {'BLOCKED' if sound_blocked else 'ok'} | hashtag links {raw.count('/hashtag/')}")
    if kids_mode:
        print("    >>> served in MADE-FOR-KIDS mode: fix in Studio > Content > Details > Audience")
    if with_comments and has_comment_button:
        cfg = ytcfg(html)
        token = None
        for p in data.get("engagementPanels", []):
            r = p.get("engagementPanelSectionListRenderer", {})
            if r.get("targetId") == "engagement-panel-comments-section":
                toks = walk(r.get("content"), "token", [])
                token = toks[0] if toks else None
        if cfg.get("INNERTUBE_API_KEY") and token:
            cdest = work / f"comments_{vid}.json"
            if post("browse", cfg["INNERTUBE_API_KEY"],
                    {"context": cfg["INNERTUBE_CONTEXT"], "continuation": token}, cdest) == "200":
                resp = json.loads(cdest.read_text(encoding="utf-8"))
                for c in walk(resp, "commentEntityPayload", []):
                    props, author = c.get("properties", {}), c.get("author", {})
                    print(f"    comment  {author.get('displayName')}: {text_of(props.get('content'))!r}"
                          f" ({props.get('publishedTime')})")


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    handle = sys.argv[1] if sys.argv[1].startswith("@") else "@" + sys.argv[1]
    work = Path(sys.argv[2] if len(sys.argv) > 2 else "yt_snapshot_work")
    work.mkdir(parents=True, exist_ok=True)
    shorts = channel(handle, work)
    print(f"\nSHORTS ({len(shorts)} on the first page, newest first)")
    for vid, _ in shorts:
        time.sleep(2)                      # stay polite: fast bursts trigger YouTube's bot check
        short(vid, work, with_comments=True)


if __name__ == "__main__":
    main()
