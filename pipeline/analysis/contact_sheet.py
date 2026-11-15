#!/usr/bin/env python3
"""Timestamped contact sheets of a video, for reading it shot by shot.

    python3 contact_sheet.py <video.mp4> <out_prefix> [--every 1.0] [--cols 6] [--rows 3] [--tile 300]

Writes <out_prefix>_01.jpg, _02.jpg, ... Each tile carries its time in seconds. At the defaults a 78 s
video makes five sheets of 18 frames, one frame a second.

Needs ffmpeg on PATH and: pip install pillow
"""
import argparse
import glob
import os
import subprocess
import tempfile

from PIL import Image, ImageDraw, ImageFont


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('video'); ap.add_argument('out_prefix')
    ap.add_argument('--every', type=float, default=1.0, help='seconds between frames')
    ap.add_argument('--cols', type=int, default=6); ap.add_argument('--rows', type=int, default=3)
    ap.add_argument('--tile', type=int, default=300, help='tile width in px')
    a = ap.parse_args()
    try:
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 22)
    except OSError:
        font = ImageFont.load_default()
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(['ffmpeg', '-v', 'error', '-i', a.video, '-vf', f'fps={1 / a.every},scale={a.tile * 2}:-2', '-q:v', '3',
                        os.path.join(tmp, 'f_%05d.jpg')], check=True)
        files = sorted(glob.glob(os.path.join(tmp, 'f_*.jpg')))
        per = a.cols * a.rows
        for n, i in enumerate(range(0, len(files), per), 1):
            chunk = files[i:i + per]
            first = Image.open(chunk[0]); th = round(a.tile * first.height / first.width)
            sheet = Image.new('RGB', (a.cols * a.tile, a.rows * th), (20, 20, 20))
            d = ImageDraw.Draw(sheet)
            for j, f in enumerate(chunk):
                t = (i + j) * a.every
                x, y = (j % a.cols) * a.tile, (j // a.cols) * th
                sheet.paste(Image.open(f).resize((a.tile, th)), (x, y))
                d.rectangle([x, y, x + 86, y + 28], fill=(0, 0, 0))
                d.text((x + 4, y + 2), f'{t:05.1f}s', fill=(255, 220, 60), font=font)
            path = f'{a.out_prefix}_{n:02d}.jpg'
            sheet.save(path, quality=85)
            print(path, len(chunk))


if __name__ == '__main__':
    main()
