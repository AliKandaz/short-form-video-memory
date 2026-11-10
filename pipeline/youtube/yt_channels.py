"""Benchmark channels: header facts plus their Shorts sorted by Latest and (via the chip continuation) Popular.

Usage: yt_channels.py <out_dir> shorts:<videoId> ... handle:<@handle> ...
  shorts:<id>  -> resolve which channel posted a Short (prints handle, title, views, likes, date)
  handle:<@h>  -> channel header + latest shorts + popular shorts
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


def shorts_rows(node):
    rows = []
    for s in walk(node, "shortsLockupViewModel", []):
        om = s.get("overlayMetadata", {})
        ids = walk(s, "videoId", [])
        rows.append((ids[0] if ids else None, (om.get("secondaryText") or {}).get("content"),
                     (om.get("primaryText") or {}).get("content")))
    return rows


def do_short(out, vid):
    dest = out / f"short_{vid}.html"
    code = get(f"https://www.youtube.com/shorts/{vid}", dest)
    if code != "200":
        print(f"SHORT {vid}: http {code}")
        return
    data = initial(dest.read_text(encoding="utf-8", errors="replace"))
    if not data:
        print(f"SHORT {vid}: no data")
        return
    handle = None
    for bar in walk(data, "reelChannelBarViewModel", []):
        handle = text_of(bar.get("channelName"))
    title = [text_of(t.get("videoTitle")) for t in walk(data, "videoTitleHeaderViewModel", [])]
    hdr = walk(data, "videoDescriptionHeaderRenderer", [])
    views = text_of(hdr[0].get("views")) if hdr else None
    date = text_of(hdr[0].get("publishDate")) if hdr else None
    chan = text_of(hdr[0].get("channel")) if hdr else None
    likes = [f.get("accessibilityText") for f in walk(data, "factoidRenderer", []) if "like" in (f.get("accessibilityText") or "").lower()]
    desc = [text_of(d.get("attributedDescriptionBodyText")) or text_of(d.get("descriptionBodyText"))
            for d in walk(data, "expandableVideoDescriptionBodyRenderer", [])]
    print(f"SHORT {vid}: {chan} ({handle}) | {views} | {likes[:1]} | {date} | {title[:1]}")
    if desc and desc[0]:
        print("      desc:", repr(desc[0][:300]))


def do_handle(out, handle):
    safe = handle.strip("@").replace("/", "_")
    dest = out / f"chan_{safe}.html"
    code = get(f"https://www.youtube.com/{handle}/shorts", dest)
    if code != "200":
        print(f"\nCHANNEL {handle}: http {code}")
        return
    html = dest.read_text(encoding="utf-8", errors="replace")
    data = initial(html)
    if not data:
        print(f"\nCHANNEL {handle}: no data")
        return
    meta = data.get("metadata", {}).get("channelMetadataRenderer", {})
    parts = []
    for vm in walk(data.get("header", {}), "contentMetadataViewModel", []):
        for row in vm.get("metadataRows", []):
            for p in row.get("metadataParts", []):
                parts.append(text_of(p.get("text")))
    has_banner = bool(walk(data.get("header", {}), "imageBannerViewModel", []))
    avatar = (meta.get("avatar", {}).get("thumbnails") or [{}])[0].get("url")
    tabs = [t.get("title") for t in walk(data, "tabRenderer", [])]
    print(f"\nCHANNEL {handle}: {meta.get('title')!r} | {parts} | banner={has_banner} | tabs={tabs}")
    print("   desc:", repr((meta.get("description") or "")[:400]))
    print("   avatar:", avatar)
    latest = shorts_rows(data)
    print(f"   latest shorts ({len(latest)} on first page):")
    for r in latest[:12]:
        print("     ", r)
    # Popular sort via the chip continuation
    cfg = ytcfg(html)
    key, ctx = cfg.get("INNERTUBE_API_KEY"), cfg.get("INNERTUBE_CONTEXT")
    token = None
    for chip in walk(data, "chipViewModel", []):
        if (chip.get("text") or "") == "Popular":
            toks = walk(chip, "token", [])
            token = toks[0] if toks else None
    if not token:
        for chip in walk(data, "chipCloudChipRenderer", []):
            if text_of(chip.get("text")) == "Popular":
                toks = walk(chip, "token", [])
                token = toks[0] if toks else None
    if key and ctx and token:
        pdest = out / f"chan_{safe}.popular.json"
        pc = post("browse", key, {"context": ctx, "continuation": token}, pdest)
        if pc == "200":
            pop = shorts_rows(json.loads(pdest.read_text(encoding="utf-8")))
            print(f"   popular shorts ({len(pop)}):")
            for r in pop[:12]:
                print("     ", r)
        else:
            print("   popular: http", pc)
    else:
        print("   popular: no chip token")


def main(out_dir, args):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    for a in args:
        kind, _, val = a.partition(":")
        if kind == "shorts":
            do_short(out, val)
        elif kind == "handle":
            do_handle(out, val)
        time.sleep(2.5)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
