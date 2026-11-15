#!/usr/bin/env python3
"""How much of a finished video is really moving, plus caption size and sharpness.

    python3 check_video.py <video.mp4> [--captions LO HI] [--json out.json]

Use it on the final MP4 before delivery (CLAUDE.md 3.4, rule 1 of the Cutaway look) and on any video we study.

What it reports
- Share of seconds in which something in the picture moves. The camera move is removed first (a similarity
  transform fitted to tracked points), so a still picture under a slow zoom or pan counts as not moving.
  Movement in a small part of the frame (a thin trickle, light rain in a wide shot) also counts as not moving.
- Every stretch of 4 s or more without movement, with its start and end time.
- Caption letter height and vertical position, for white one-word captions. --captions gives the band they
  sit in as fractions of the frame height (default 0.62 0.84).
- Sharpness (Laplacian variance of the upper picture area) for the moving seconds and for the still seconds.
  A large gap between the two means soft clips are intercut with sharp stills.

Reference values, measured 15 Nov 2026 (CLAUDE.md 7.5)
                                   moving   longest still stretch   caption letters   sharpness moving / still
  ours 03 fire hydrant (Lite)       33%      20 s                    44 px at 68%      43 / 85
  ours 04 seawater (Lite)           33%      26 s                    44 px at 73%      14 / 81
  @1hidden_by_design storm drain    84%       6 s                    62 px at 75%      54 / 68
  @1hidden_by_design roof           87%       4 s                    54 px at 77%      37 / 44
Target for our videos: 80% or more moving and no still stretch longer than about 6 s.

Needs ffmpeg on PATH and: pip install numpy opencv-python-headless
"""
import argparse
import json
import subprocess
import sys

import cv2
import numpy as np

MOVING = 0.8          # median residual per second at or above this counts as moving
FPS, W, H = 12, 270, 480


def frames(video, vf, pix, shape):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', video, '-vf', vf, '-f', 'rawvideo', '-pix_fmt', pix, '-'],
                         capture_output=True).stdout
    n = len(raw) // int(np.prod(shape))
    return np.frombuffer(raw[:n * int(np.prod(shape))], np.uint8).reshape((n,) + shape)


def motion(video, lo, hi):
    """Residual change per frame after the global camera move is taken out."""
    fr = frames(video, f'fps={FPS},scale={W}:{H}', 'gray', (H, W))
    mask = np.full((H, W), 255, np.uint8)
    mask[int(lo * H):int(hi * H), :] = 0                      # captions change every word: leave them out
    keep = mask > 0
    keep[:6, :] = keep[-6:, :] = False
    keep[:, :6] = keep[:, -6:] = False
    res = []
    for i in range(1, len(fr)):
        a, b = fr[i - 1], fr[i]
        M = None
        pts = cv2.goodFeaturesToTrack(a, 400, 0.01, 6, mask=mask)
        if pts is not None and len(pts) >= 12:
            nxt, st, _ = cv2.calcOpticalFlowPyrLK(a, b, pts, None, winSize=(21, 21), maxLevel=3)
            good = st.ravel() == 1
            if good.sum() >= 12:
                M, _ = cv2.estimateAffinePartial2D(pts[good], nxt[good], method=cv2.RANSAC, ransacReprojThreshold=1.5)
        if M is None:
            M = np.float32([[1, 0, 0], [0, 1, 0]])
        warped = cv2.warpAffine(a, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
        d = cv2.absdiff(cv2.GaussianBlur(warped, (5, 5), 0), cv2.GaussianBlur(b, (5, 5), 0))
        res.append(float(d[keep].mean()))
    res = np.array(res)
    secs = int(np.ceil(len(res) / FPS))
    per_sec = [float(np.median(res[s * FPS:(s + 1) * FPS])) for s in range(secs) if len(res[s * FPS:(s + 1) * FPS])]
    return per_sec


def runs(flags):
    out, i = [], 0
    while i < len(flags):
        j = i
        while j < len(flags) and flags[j] == flags[i]:
            j += 1
        out.append((i, j, bool(flags[i])))
        i = j
    return out


def captions_and_sharpness(video, moving, lo, hi):
    FW, FH = 1080, 1920
    fr = frames(video, f'fps=1,scale={FW}:{FH}', 'bgr24', (FH, FW, 3))
    sharp = {True: [], False: []}
    caps = []
    for s in range(len(fr)):
        gray = cv2.cvtColor(fr[s], cv2.COLOR_BGR2GRAY)
        lap = cv2.Laplacian(gray[int(0.08 * FH):int(0.58 * FH)], cv2.CV_64F).var()
        sharp[bool(moving[s]) if s < len(moving) else False].append(lap)
        band = fr[s][int(lo * FH):int(hi * FH)]
        hsv = cv2.cvtColor(band, cv2.COLOR_BGR2HSV)
        white = ((hsv[..., 2] > 235) & (hsv[..., 1] < 25)).astype(np.uint8)
        white = cv2.morphologyEx(white, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
        _, _, stats, _ = cv2.connectedComponentsWithStats(white, 8)
        boxes = [st for st in stats[1:] if st[4] > 150 and 25 < st[3] < 220 and st[2] < 400]
        if boxes:
            y0 = min(b[1] for b in boxes); y1 = max(b[1] + b[3] for b in boxes)
            x0 = min(b[0] for b in boxes); x1 = max(b[0] + b[2] for b in boxes)
            if (y1 - y0) < 240 and abs((x0 + x1) / 2 - FW / 2) < 160:
                caps.append((int(np.median([b[3] for b in boxes])), int(lo * FH) + (y0 + y1) // 2))
    out = {'sharp_moving': float(np.median(sharp[True])) if sharp[True] else None,
           'sharp_still': float(np.median(sharp[False])) if sharp[False] else None}
    if caps:
        c = np.array(caps)
        out['caption_letter_px'] = int(np.median(c[:, 0]))
        out['caption_y_pct'] = round(100 * float(np.median(c[:, 1])) / FH)
    return out


def clock(s):
    return '%d:%02d' % (s // 60, s % 60)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('video')
    ap.add_argument('--captions', nargs=2, type=float, default=[0.62, 0.84], metavar=('LO', 'HI'))
    ap.add_argument('--json')
    a = ap.parse_args()
    lo, hi = a.captions
    per_sec = motion(a.video, lo, hi)
    moving = [m >= MOVING for m in per_sec]
    rr = runs(moving)
    still = [(s, e) for s, e, m in rr if not m and e - s >= 4]
    rep = {'video': a.video, 'seconds': len(per_sec), 'moving_pct': round(100 * sum(moving) / max(1, len(moving))),
           'longest_still_s': max([e - s for s, e, m in rr if not m] or [0]),
           'still_stretches': [[clock(s), clock(e), e - s] for s, e in still], 'runs': rr, 'per_second': per_sec}
    rep.update(captions_and_sharpness(a.video, moving, lo, hi))
    print(f"{a.video}: {rep['seconds']} s")
    print(f"  moving in {rep['moving_pct']}% of the seconds; longest stretch without movement {rep['longest_still_s']} s")
    for s, e, n in rep['still_stretches']:
        print(f"    no movement {s}-{e} ({n} s)")
    if 'caption_letter_px' in rep:
        print(f"  caption letters about {rep['caption_letter_px']} px tall, centred {rep['caption_y_pct']}% down the frame")
    if rep['sharp_moving'] is not None and rep['sharp_still'] is not None:
        print(f"  sharpness: moving seconds {rep['sharp_moving']:.0f}, still seconds {rep['sharp_still']:.0f}")
    if a.json:
        json.dump(rep, open(a.json, 'w'))


if __name__ == '__main__':
    sys.exit(main())
