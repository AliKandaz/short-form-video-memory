#!/usr/bin/env python3
"""List the words written on a video's picture above the captions (term labels, gauges, counters), with when and where.
Written 21 Nov 2026 for the @whatifplus study (CLAUDE.md 1.7, 12.5); also checks our own labels and counter after a build.

    PYTHONPATH=<dir with rapidocr_onnxruntime and cv2> python3 labels.py <video.mp4> [more videos...] [--band 0.03 0.52]

Setup: pip install --target <dir> rapidocr-onnxruntime opencv-python-headless   (the OCR models come inside the wheel)
It reads two frames a second in the band given as fractions of the frame height (default: from 3% to 52% down) and prints,
for each text seen at least twice: the text, first and last second, its centre as a share of the height, and its height as
a share of the frame. Small in-scene text and moving numbers are read less reliably than big labels.
"""
import re
import sys

import cv2
from rapidocr_onnxruntime import RapidOCR


def main():
    args = sys.argv[1:]
    band = (0.03, 0.52)
    if "--band" in args:
        i = args.index("--band")
        band = (float(args[i + 1]), float(args[i + 2]))
        args = args[:i] + args[i + 3:]
    if not args:
        sys.exit(__doc__)
    ocr = RapidOCR()
    for path in args:
        cap = cv2.VideoCapture(path)
        fps, n = cap.get(cv2.CAP_PROP_FPS) or 30, cap.get(cv2.CAP_PROP_FRAME_COUNT)
        seen, order, t = {}, [], 0.0
        while t < n / fps:
            cap.set(cv2.CAP_PROP_POS_MSEC, t * 1000)
            ok, frame = cap.read()
            if not ok:
                break
            h = frame.shape[0]
            y0 = int(h * band[0])
            crop = cv2.resize(frame[y0:int(h * band[1]), :], None, fx=1.6, fy=1.6)
            for box, text, conf in (ocr(crop)[0] or []):
                text = re.sub(r"\s+", " ", text).strip()
                if float(conf) < 0.6 or len(re.sub(r"[^A-Za-z0-9]", "", text)) < 2:
                    continue
                ys = [p[1] for p in box]
                key = text.upper()
                if key not in seen:
                    seen[key] = dict(text=text, first=t, last=t, n=0, cy=(sum(ys) / 4 / 1.6 + y0) / h,
                                     height=(max(ys) - min(ys)) / 1.6 / h)
                    order.append(key)
                seen[key]["last"] = t
                seen[key]["n"] += 1
            t += 0.5
        print(path)
        for key in order:
            s = seen[key]
            if s["n"] >= 2:
                print(f"  {s['first']:5.1f}-{s['last']:5.1f} s  {s['cy']:.0%} down  {s['height']:.1%} tall  {s['text']}")


if __name__ == "__main__":
    main()
