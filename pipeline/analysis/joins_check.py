#!/usr/bin/env python3
"""Are the steps of a build-steps video crisp? A check of every join between clips on the finished picture.

    python3 joins_check.py <work dir> [picture.mp4] [map.json]

Written 24 Nov 2026 after the user's review of video 17 ("the animations are mushed together at times"; CLAUDE.md 1.10).
<work dir> holds clips/, work/check.json (steps-check.py: each clip's `settle` time) and the edit's time map, by default
work/full_map.json: {"segs": [{"k", "s0", "s1", "v0", "v1"[, "view"][, "whip"]}], "steps": [[clip, landing time, word, ...]]}.
The picture defaults to work/full_raw.mp4 (the clean picture, before captions).

For every join from one clip to the next it prints
- the biggest frame-to-frame change over the join, against a resting picture's (about 0.2-0.5): a clean join is under about
  2; video 17's bad joins measured 4-10;
- whether the outgoing clip was cut before it had settled (its source time at the cut against its `settle`), and whether the
  incoming clip starts on its first four frames (wan2_7's first frames fade from the still's tone: start at frame 4);
- and, from the landings, every pair of steps that land less than 1.6 s apart.
It measures; the eye still has to look at a strip of the worst joins (10 frames a second).
Needs: pip install numpy opencv-python-headless
"""
import json, os, sys
import numpy as np, cv2

D = sys.argv[1]
PIC = sys.argv[2] if len(sys.argv) > 2 else f'{D}/work/full_raw.mp4'
MAP = sys.argv[3] if len(sys.argv) > 3 else f'{D}/work/full_map.json'
FPS = 30
m = json.load(open(MAP)); segs = m['segs']
chk = json.load(open(f'{D}/work/check.json')) if os.path.exists(f'{D}/work/check.json') else {}

cap = cv2.VideoCapture(PIC); G = []
while True:
    ok, f = cap.read()
    if not ok: break
    G.append(cv2.GaussianBlur(cv2.cvtColor(cv2.resize(f, (270, 480), interpolation=cv2.INTER_AREA), cv2.COLOR_BGR2GRAY), (0, 0), 1.2).astype(np.float32))
step = np.array([0.0] + [float(np.abs(G[i] - G[i - 1]).mean()) for i in range(1, len(G))])
rest = float(np.percentile(step[1:], 20))
print(f'{len(G)} frames; a resting picture changes by about {rest:.2f} a frame')
print('  t(s)   join             kind      change   out clip cut at (settles at)        in clip starts at')
bad = 0
for a, b in zip(segs, segs[1:]):
    if a['k'] == b['k'] and abs(a['s1'] - b['s0']) < 0.05: continue
    kind = 'whip' if (a.get('whip') or b.get('whip')) else 'view cut' if a.get('view') != b.get('view') else 'join'
    i = int(round(a['v1'] * FPS)); ch = float(step[max(1, i - 1):i + 5].max()) if i < len(step) else 0.0
    st = chk.get(a['k'], {}).get('settle'); notes = []
    if kind == 'join':
        if st is not None and a['s1'] < st - 0.04: notes.append(f"CUT {st - a['s1']:.2f} s BEFORE IT SETTLED")
        if b['s0'] < 4 / FPS - 1e-3: notes.append('starts on frame 0-3 (tone pop)')
        if ch > 2.5: notes.append('JUMP')
        bad += bool(notes)
    print(f"{a['v1']:6.2f}  {a['k']:5s} -> {b['k']:5s}  {kind:8s} {ch:6.2f}   {a['s1']:4.2f} ({'%.2f' % st if st is not None else '  ? '})"
          f"                      {b['s0']:4.2f}   {'  '.join(notes)}")
print(f'{bad} joins to look at')
if m.get('steps'):
    st = sorted(m['steps'], key=lambda x: x[1]); print('landings closer than 1.6 s:')
    for p, q in zip(st, st[1:]):
        if q[1] - p[1] < 1.6: print(f'  {p[1]:6.2f} {p[0]:5s} "{p[2]}"  ->  {q[1]:6.2f} {q[0]:5s} "{q[2]}"   {q[1] - p[1]:.2f} s')
