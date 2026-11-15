#!/usr/bin/env python3
"""How the camera moves in a video: pushing in, pulling out, panning, and flying through the scene in 3D.

    python3 camera_path.py <video.mp4> [--captions LO HI] [--json out.json] [--seconds]

Use it next to check_video.py on every pilot (Gate D) and on the final (CLAUDE.md 3.4 Rule 7). check_video.py takes the
camera move out and measures what moves inside the picture; this script measures the camera move itself.

How it works: points are tracked between frames (15 fps, 270x480) and a 2D move (zoom, pan, turn) is fitted to them.
- zoom: how much closer (+) or farther (-) the camera gets in a second.
- pan: how far the picture slides in a second, as a share of the frame width.
- parallax: the flow the 2D fit cannot explain (75th percentile, px a frame at 270 wide). A zoom or pan across a flat
  picture has none; a camera flying through a 3D scene has plenty, because near things slide faster than far things.
- a second "moves" when it zooms or pans more than 3% or has parallax over 0.6 px; a "big move" zooms or pans 25% or more.

It prints the share of seconds in which the camera moves, the median speeds, the big moves, the longest stretch with a
still camera, and how often the camera turns from pushing in to pulling out. --seconds also prints every second.

Reference values, measured 15 Nov 2026 (CLAUDE.md 7.7)
                                        camera   zoom   pan    parallax  big-move seconds   longest still  in / out / turns
                                        moving   %/s    %/s    px        (longest gap)      camera
  @1hidden_by_design power lines (88 s)  66%     5.5    4.1    0.46      22 (15 s)          5 s            31 / 17 / 14
  ours, video 08 sewer trap (80 s)       45%     0.9    0.7    0.03       7 (42 s)          13 s           19 / 17 / 9
  ours, video 09 lightning (76 s)        78%     6.4    6.5    0.44      23 (9 s)            3 s           26 / 27 / 13
Targets for our videos (3.4 Rule 7): camera moving in 65% or more of the seconds; median parallax 0.3 px or more; big moves
in at least one second in eight on average (10 or more in an 80 s video; the reference has 22 in 88 s), with no gap longer
than 15 s; and no still-camera stretch longer than 5 s.

Needs ffmpeg on PATH and: pip install numpy opencv-python-headless
"""
import argparse
import json
import subprocess

import cv2
import numpy as np

FPS, W, H = 15, 270, 480
MOVE_PCT, MOVE_PAR, BIG_PCT = 3.0, 0.6, 25.0


def frames(video):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', video, '-vf', f'fps={FPS},scale={W}:{H}', '-f', 'rawvideo',
                          '-pix_fmt', 'gray', '-'], capture_output=True).stdout
    n = len(raw) // (W * H)
    return np.frombuffer(raw[:n * W * H], np.uint8).reshape(n, H, W)


def per_frame(fr, lo, hi):
    mask = np.full((H, W), 255, np.uint8)
    mask[int(lo * H):int(hi * H), :] = 0           # captions change every word: leave them out
    mask[:8] = 0; mask[-8:] = 0
    rows = []
    for i in range(1, len(fr)):
        a, b = fr[i - 1], fr[i]
        z = tx = ty = par = 0.0
        pts = cv2.goodFeaturesToTrack(a, 500, 0.01, 5, mask=mask)
        if pts is not None and len(pts) >= 15:
            nxt, st, _ = cv2.calcOpticalFlowPyrLK(a, b, pts, None, winSize=(21, 21), maxLevel=3)
            g = st.ravel() == 1
            if g.sum() >= 15:
                M, _ = cv2.estimateAffinePartial2D(pts[g], nxt[g], method=cv2.RANSAC, ransacReprojThreshold=1.5)
                if M is not None:
                    z = float(np.log(np.hypot(M[0, 0], M[1, 0])))
                    c = np.array([W / 2, H / 2]); c2 = M[:, :2] @ c + M[:, 2]; tx, ty = c2 - c
                    pred = pts[g].reshape(-1, 2) @ M[:, :2].T + M[:, 2]
                    par = float(np.percentile(np.linalg.norm(nxt[g].reshape(-1, 2) - pred, axis=1), 75))
        rows.append((z, float(tx), float(ty), par))
    return rows


def per_second(rows):
    out = []
    for s in range(int(np.ceil(len(rows) / FPS))):
        r = rows[s * FPS:(s + 1) * FPS]
        if not r:
            continue
        zoom = 100 * (np.exp(sum(x[0] for x in r)) - 1)                  # + in, - out
        zabs = 100 * (np.exp(sum(abs(x[0]) for x in r)) - 1)
        pan = 100 * sum(np.hypot(x[1], x[2]) for x in r) / W
        par = float(np.median([x[3] for x in r]))
        out.append(dict(s=s, zoom_pct=round(zoom, 2), zoom_abs_pct=round(zabs, 2), pan_pct=round(pan, 2),
                        parallax_px=round(par, 3), moving=bool(zabs > MOVE_PCT or pan > MOVE_PCT or par > MOVE_PAR),
                        big=bool(zabs >= BIG_PCT or pan >= BIG_PCT)))
    return out


def summary(secs):
    n = len(secs)
    still, run = 0, 0
    for x in secs:
        run = 0 if x['moving'] else run + 1; still = max(still, run)
    big = [x['s'] for x in secs if x['big']]
    seq = ['I' if x['zoom_pct'] > MOVE_PCT else 'O' if x['zoom_pct'] < -MOVE_PCT else '' for x in secs]
    seq = [c for c in seq if c]
    return dict(seconds=n, camera_moving_pct=round(100 * sum(x['moving'] for x in secs) / n),
                median_zoom_pct=round(float(np.median([x['zoom_abs_pct'] for x in secs])), 1),
                median_pan_pct=round(float(np.median([x['pan_pct'] for x in secs])), 1),
                median_parallax_px=round(float(np.median([x['parallax_px'] for x in secs])), 2),
                big_move_seconds=len(big), longest_gap_between_big_moves_s=max(np.diff([0] + big + [n])) if n else 0,
                longest_still_camera_s=still, push_in_s=seq.count('I'), pull_out_s=seq.count('O'),
                in_out_turns=sum(1 for a, b in zip(seq, seq[1:]) if a != b))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('video')
    ap.add_argument('--captions', nargs=2, type=float, default=[0.62, 0.84], metavar=('LO', 'HI'))
    ap.add_argument('--json')
    ap.add_argument('--seconds', action='store_true')
    a = ap.parse_args()
    secs = per_second(per_frame(frames(a.video), *a.captions))
    s = summary(secs)
    print(f"{a.video}: {s['seconds']} s")
    print(f"  camera moving in {s['camera_moving_pct']}% of the seconds; longest still-camera stretch {s['longest_still_camera_s']} s")
    print(f"  median zoom {s['median_zoom_pct']}%/s, pan {s['median_pan_pct']}% of the width/s, parallax {s['median_parallax_px']} px")
    print(f"  big moves in {s['big_move_seconds']} seconds (longest gap {s['longest_gap_between_big_moves_s']} s); "
          f"pushing in {s['push_in_s']} s, pulling out {s['pull_out_s']} s, {s['in_out_turns']} turns between them")
    if a.seconds:
        for x in secs:
            tag = 'IN ' if x['zoom_pct'] > MOVE_PCT else 'OUT' if x['zoom_pct'] < -MOVE_PCT else '   '
            print(f"  {x['s']:3d}s {tag} zoom {x['zoom_pct']:+6.1f}%  pan {x['pan_pct']:5.1f}%  parallax {x['parallax_px']:5.2f}"
                  + ('  BIG' if x['big'] else '') + ('' if x['moving'] else '  still'))
    if a.json:
        json.dump(dict(video=a.video, summary=s, seconds=secs), open(a.json, 'w'), indent=1, default=int)


if __name__ == '__main__':
    main()
