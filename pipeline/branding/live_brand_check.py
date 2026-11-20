#!/usr/bin/env python3
"""Which files in branding/ are the live YouTube profile picture and banner? Written 20 Nov 2026 (CLAUDE.md 8.3, 12.2).

    python3 -I live_brand_check.py <avatar url> <banner url> <branding dir> <work dir>

Take the two urls from the "avatar" and "banner" lines that yt_snapshot.py prints. Both images are downloaded into
<work dir> (use a new, empty one), compared at low resolution with every avatar-* and banner-* file (mean absolute
difference, 0-255; the lowest is the match, but near-twins such as the two cutaway icons differ by only ~2, so look at
the sheet), and drawn beside their closest files in <work dir>/live-brand.png.
YouTube serves the banner as the band it shows on computers (fcrop64 in the url, rows 35.3%-64.7% of a 2560x1440
upload), so the files are compared on that band. TikTok's picture can't be fetched from a session (CLAUDE.md 7.7).
Needs Pillow and numpy.
"""
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/126.0.0.0 Safari/537.36")
Y0, Y1 = 0x5a57 / 65535, 0xa5a8 / 65535


def fetch(url, path):
    subprocess.run(["curl", "-sS", "-L", "-A", UA, "-o", str(path), url], check=True)
    return Image.open(path).convert("RGB")


def band(img):
    w, h = img.size
    return img.crop((0, round(Y0 * h), w, round(Y1 * h)))


def diff(a, b, size):
    return float(np.abs(np.asarray(a.resize(size, Image.LANCZOS), np.float32)
                        - np.asarray(b.resize(size, Image.LANCZOS), np.float32)).mean())


def main():
    if len(sys.argv) != 5:
        sys.exit(__doc__)
    avatar_url, banner_url, brand, work = sys.argv[1], sys.argv[2], Path(sys.argv[3]), Path(sys.argv[4])
    work.mkdir(parents=True, exist_ok=True)
    live_av, live_bn = fetch(avatar_url, work / "live-avatar.jpg"), fetch(banner_url, work / "live-banner.jpg")
    best = {}
    for kind, live, prep, size in (("avatar", live_av, lambda i: i, (96, 96)), ("banner", live_bn, band, (512, 85))):
        rows = sorted((diff(live, prep(Image.open(p).convert("RGB")), size), p.name)
                      for p in sorted(brand.glob(f"{kind}-*")))
        print(f"{kind} (mean abs diff, 0-255; lowest = closest, check the sheet):")
        for score, name in rows:
            print(f"  {score:6.1f}  {name}")
        best[kind] = rows[0][1]
    sheet = Image.new("RGB", (1200, 760), "white")
    d = ImageDraw.Draw(sheet)
    d.text((10, 8), "LIVE avatar", fill="black")
    d.text((330, 8), f"closest: {best['avatar']}", fill="black")
    sheet.paste(live_av.resize((300, 300)), (10, 28))
    sheet.paste(Image.open(brand / best["avatar"]).convert("RGB").resize((300, 300)), (330, 28))
    strip = (1180, round(1180 * 424 / 2560))
    d.text((10, 345), "LIVE banner (the band YouTube shows on computers)", fill="black")
    sheet.paste(live_bn.resize(strip), (10, 365))
    d.text((10, 565), f"closest, same band: {best['banner']}", fill="black")
    sheet.paste(band(Image.open(brand / best["banner"]).convert("RGB")).resize(strip), (10, 585))
    sheet.save(work / "live-brand.png")
    print("sheet:", work / "live-brand.png")


if __name__ == "__main__":
    main()
