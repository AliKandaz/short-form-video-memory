"""Run YouTube searches (HTML results page) and list the results: who is already making this topic, and how big.

    python3 yt_search.py <work_dir> "how a pile of rocks becomes a castle" ["second query" ...]

Use it as the saturation check before Gate A: count the near-identical Shorts and note the best view count.
Needs www.youtube.com on the environment's allowlist. Shorts in search results carry no channel name; pass their ids to
yt_channels.py as shorts:<id> to see who posted them.
"""
import json
import re
import subprocess
import sys
import time
import urllib.parse
from pathlib import Path

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/126.0.0.0 Safari/537.36")


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


def fetch(url, dest):
    cmd = ["curl", "-sS", "-o", str(dest), "-w", "%{http_code} %{url_effective}", "--max-redirs", "0",
           "-H", "Accept-Language: en-US,en;q=0.9", "-H", "Cookie: SOCS=CAI; CONSENT=YES+1", "-A", UA, url]
    return subprocess.run(cmd, capture_output=True, text=True).stdout.strip()


def main(out_dir, queries):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    for i, q in enumerate(queries):
        dest = out / f"search_{i}.html"
        url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote_plus(q)
        status = fetch(url, dest)
        print(f"\n===== {q!r} -> {status}")
        if not status.startswith("200"):
            continue
        html = dest.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"var ytInitialData\s*=\s*(\{.*?\});</script>", html, re.S)
        if not m:
            print("  no data")
            continue
        data = json.loads(m.group(1))
        (out / f"search_{i}.json").write_text(json.dumps(data), encoding="utf-8")
        for v in walk(data, "videoRenderer", [])[:14]:
            owner = text_of(v.get("ownerText")) or text_of(v.get("longBylineText"))
            handle = None
            for u in walk(v.get("ownerText"), "canonicalBaseUrl", []):
                handle = u
            print("  VIDEO", v.get("videoId"), "|", text_of(v.get("viewCountText")), "|",
                  text_of(v.get("publishedTimeText")), "|", text_of(v.get("lengthText")), "|",
                  owner, handle, "|", text_of(v.get("title")))
        for s in walk(data, "shortsLockupViewModel", [])[:14]:
            om = s.get("overlayMetadata", {})
            ids = walk(s, "videoId", [])
            print("  SHORT", ids[0] if ids else None, "|", (om.get("secondaryText") or {}).get("content"), "|",
                  (om.get("primaryText") or {}).get("content"))
        for c in walk(data, "channelRenderer", [])[:5]:
            print("  CHANNEL", text_of(c.get("title")), "|", text_of(c.get("subscriberCountText")), "|",
                  text_of(c.get("videoCountText")), "|", walk(c, "canonicalBaseUrl", [])[:1])
        time.sleep(3)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
