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
- from the landings, every pair of steps that land less than 1.6 s apart;
- and every stretch of 2 s or more in which nothing moves but the push-in (video 17 stood still from 46.2 to 51.4 s
  but for a label and a shake).
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
def own_motion(k, s0, n=6):
    """The incoming clip's own frame-to-frame change over its first n frames shown, measured the same way (26 Nov 2026):
    a clip whose step starts at once (video 18's W3_1 and W3_L) moves by 3-4 a frame there, and that is its step, not a
    jump at the join. None if the clip file is not in <work dir>/clips."""
    p = f'{D}/clips/{k}.mp4'
    if not os.path.exists(p): return None
    c = cv2.VideoCapture(p); j0 = int(round(s0 * FPS)); out, prev, j = [], None, 0
    while j <= j0 + n:
        ok, f = c.read()
        if not ok: break
        if j >= j0 - 1:
            g = cv2.GaussianBlur(cv2.cvtColor(cv2.resize(f, (270, 480), interpolation=cv2.INTER_AREA), cv2.COLOR_BGR2GRAY), (0, 0), 1.2).astype(np.float32)
            if prev is not None: out.append(float(np.abs(g - prev).mean()))
            prev = g
        j += 1
    return max(out) if out else None
print('  t(s)   join             kind      change  (in clip\'s own)  out clip cut at (settles at)   in clip starts at')
bad = 0
for a, b in zip(segs, segs[1:]):
    if a['k'] == b['k'] and abs(a['s1'] - b['s0']) < 0.05: continue
    kind = 'whip' if (a.get('whip') or b.get('whip')) else 'view cut' if a.get('view') != b.get('view') else 'join'
    i = int(round(a['v1'] * FPS)); ch = float(step[max(1, i - 1):i + 5].max()) if i < len(step) else 0.0
    st = chk.get(a['k'], {}).get('settle'); notes = []; own = own_motion(b['k'], b['s0']) if kind == 'join' else None
    if kind == 'join':
        if st is not None and a['s1'] < st - 0.04: notes.append(f"CUT {st - a['s1']:.2f} s BEFORE IT SETTLED")
        if b['s0'] < 4 / FPS - 1e-3: notes.append('starts on frame 0-3 (tone pop)')
        if ch > 2.5:
            if own is not None and ch <= own + 1.0: notes.append('its step moves from the first frame shown (look at the strip)')
            else: notes.append('JUMP')
        bad += bool(notes)
    ch = f'{ch:6.2f}' + (f'  ({own:5.2f})       ' if own is not None else '                 ')
    print(f"{a['v1']:6.2f}  {a['k']:5s} -> {b['k']:5s}  {kind:8s} {ch}  {a['s1']:4.2f} ({'%.2f' % st if st is not None else '  ? '})"
          f"                {b['s0']:4.2f}   {'  '.join(notes)}")
print(f'{bad} joins to look at')
if m.get('steps'):
    st = sorted(m['steps'], key=lambda x: x[1]); print('landings closer than 1.6 s:')
    for p, q in zip(st, st[1:]):
        if q[1] - p[1] < 1.6: print(f'  {p[1]:6.2f} {p[0]:5s} "{p[2]}"  ->  {q[1]:6.2f} {q[0]:5s} "{q[2]}"   {q[1] - p[1]:.2f} s')
still = step < max(0.6, 2.2 * rest); i = 1; print('the picture stands still (nothing moves but the push-in) for 2 s or more:')
while i < len(step):
    j = i
    while j < len(step) and still[j]: j += 1
    if (j - i) / FPS >= 2.0: print(f'  {i / FPS:6.2f} - {j / FPS:6.2f} s   {(j - i) / FPS:.1f} s')
    i = j + 1
