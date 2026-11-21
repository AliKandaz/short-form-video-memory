#!/usr/bin/env python3
"""The first seconds of every video of an account, one row a video, ranked by views: what the hits and the flops open on.
Written 21 Nov 2026 for the @whatifplus study (CLAUDE.md 1.7, 12.5).

    python3 hooks_sheet.py <flat.json> <videos_dir> <out_prefix> [--times 0 0.5 1 2 3 4.5] [--rows 7] [--tile 170]

<flat.json> is yt-dlp's flat list for the account (tt_items.py writes it as _flat.json). <videos_dir> holds the downloads,
named <id>.mp4 or <anything>_<id>.mp4 (ttdl.py). Writes <out_prefix>_01.jpg, _02.jpg, …: each row carries the rank, the
views, the date, the caption, likes per view and shares, saves and comments per 1,000 views, then a frame at each time.

Needs ffmpeg on PATH and: pip install pillow
"""
import argparse
import datetime
import glob
import json
import os
import subprocess
import tempfile

from PIL import Image, ImageDraw, ImageFont


def font(size):
    for p in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"):
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("flat"); ap.add_argument("videos_dir"); ap.add_argument("out_prefix")
    ap.add_argument("--times", nargs="+", type=float, default=[0, 0.5, 1, 2, 3, 4.5])
    ap.add_argument("--rows", type=int, default=7); ap.add_argument("--tile", type=int, default=170)
    a = ap.parse_args()
    tw, th, lw = a.tile, round(a.tile * 16 / 9), 300
    entries = [e for e in json.load(open(a.flat)).get("entries", []) if e.get("id")]
    entries.sort(key=lambda e: -(e.get("view_count") or 0))
    big, small = font(15), font(12)
    tmp = tempfile.mkdtemp()

    def frame(e, t):
        src = (glob.glob(os.path.join(a.videos_dir, f"*{e['id']}*.mp4")) or [None])[0]
        out = os.path.join(tmp, f"{e['id']}_{t}.jpg")
        if src:
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", src, "-frames:v", "1",
                            "-vf", f"scale={tw}:{th}", "-q:v", "3", out])
        return Image.open(out) if os.path.exists(out) else Image.new("RGB", (tw, th), (40, 40, 40))

    for s in range(0, len(entries), a.rows):
        rows = entries[s:s + a.rows]
        sheet = Image.new("RGB", (lw + tw * len(a.times), th * len(rows)), (18, 18, 18))
        d = ImageDraw.Draw(sheet)
        for r, e in enumerate(rows):
            y, v = r * th, max(e.get("view_count") or 0, 1)
            when = datetime.datetime.fromtimestamp(e.get("timestamp") or 0, datetime.UTC)
            title = (e.get("description") or e.get("title") or "").split("#")[0].strip()
            lines, cur = [], ""
            for w in title.split():
                if len(cur) + len(w) + 1 > 30:
                    lines.append(cur); cur = w
                else:
                    cur = (cur + " " + w).strip()
            lines.append(cur)
            d.text((8, y + 8), f"#{s + r + 1} by views", font=small, fill=(255, 210, 60))
            d.text((8, y + 28), f"{e.get('view_count') or 0:,} views", font=big, fill=(255, 255, 255))
            d.text((8, y + 50), f"{when:%d %b %H:%M} UTC  {e.get('duration')}s", font=small, fill=(200, 200, 200))
            for k, line in enumerate(lines[:5]):
                d.text((8, y + 74 + k * 18), line, font=small, fill=(170, 220, 255))
            for k, (name, key, per) in enumerate((("likes", "like_count", 100), ("shares", "repost_count", 1000),
                                                  ("saves", "save_count", 1000), ("comments", "comment_count", 1000))):
                val = per * (e.get(key) or 0) / v
                d.text((8, y + 180 + k * 18), f"{name} {val:.1f}%" if per == 100 else f"{name} {val:.2f}/1k",
                       font=small, fill=(200, 200, 200))
            for c, t in enumerate(a.times):
                sheet.paste(frame(e, t), (lw + c * tw, y))
                d.rectangle((lw + c * tw, y, lw + c * tw + 46, y + 16), fill=(0, 0, 0))
                d.text((lw + c * tw + 3, y + 1), f"{t:g}s", font=small, fill=(255, 220, 0))
            d.line((0, y, sheet.width, y), fill=(90, 90, 90))
        out = f"{a.out_prefix}_{s // a.rows + 1:02d}.jpg"
        sheet.save(out, quality=88)
        print(out, sheet.size)


if __name__ == "__main__":
    main()
