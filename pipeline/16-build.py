# Video 16 (B3, the Christmas light show), the first build-format video. Assemble: 13 clips -> clean master -> sound (voice +
# bed + effects) -> overlays (pointers, the sign's frequency, term labels, the price counter, one-word captions) -> the street
# card. Runs locally (ffmpeg with libass, numpy, opencv, Pillow). Work dir: plan.json + timeline.json + audio/words_tight.json
# (16-timing.py), clips/<SEG>.mp4 (kling, 720p), fonts/HBXCaption.ttf, and, once the narration exists, audio/narration_tight.wav,
# audio/bed.mp3, audio/fx*.mp3.
# Usage: python3 16-build.py            -> out/final.mp4 (+ final_voiceonly.mp4, final_clean.mp4), or, with no narration in
#                                          audio/, out/preview_silent.mp4 (+ preview_silent_clean.mp4): picture and overlays only
#        python3 16-build.py C1 C10,C11 -> out/preview.mp4: each argument is a run of consecutive segments
#        REUSE=1 python3 16-build.py    -> keeps the segments in seg/ and redoes only the overlays, the card and the mix
# Made from 15-build.py. New for the build format (CLAUDE.md 5): LABELS and BILL (16-overlays.py), SIGN (words put on an
# object in the scene: its four corners are found in every frame and the words are warped onto it), STREET (the end card),
# RAMP (a clip's first seconds faster, the rest slower), EASE_FROM (a clip starts at the zoom the clip before it ended on)
# and HOLD_START (a clip's first frame held under that zoom-out). No loop: the last frame is the finished build.
import importlib.util, json, math, os, re, subprocess, sys
import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("ov", os.path.join(HERE, "16-overlays.py")); ov = importlib.util.module_from_spec(spec); spec.loader.exec_module(ov)
W, H, FPS = 1080, 1920, 30
CAP_Y, CAP_FS, MAXW = 1440, 114, 900   # 114 -> ~57 px letters with this font (08, measured); Rule 5
SHARP = "unsharp=5:5:0.6:5:5:0.0"       # 720p clips after the upscale
ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '16', '-pix_fmt', 'yuv420p', '-r', str(FPS), '-an']
PLAN = json.load(open('plan.json')); SEG = {s['seg']: s for s in PLAN['segments']}; ORDER = [s['seg'] for s in PLAN['segments']]
TOTAL = PLAN['total']; CARD = 1.5
SILENT = not os.path.exists('audio/narration_tight.wav')
for d in ('seg', 'out', 'tmp'): os.makedirs(d, exist_ok=True)
def run(args): subprocess.run(['ffmpeg', '-loglevel', 'error', '-y'] + args, check=True)
def dur(p): return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout)

# ---- fitting each clip to its line ----
FULLFIT = {"C10"}                 # a 3 s swoop over a ~2 s line plays whole and faster (up to 2x), never trimmed
LO = {"C13": 0.70}                # the closing shot may play slower than 0.8x: a slow push-in on a finished scene
# RAMP: the clip's first `a` seconds play at speed s1 and the rest fills what is left of the line.
#   C1: kling lit the gable at 1.0 s and the whole roof edge at 2.0 s; at 1.4x that is 0.7 s and 1.4 s (Gate D).
#   C8: the camera reaches the roof edge at 2.2 s and the far lights turn pink from 3.4 s, a beat after "white turns pink";
#       the swoop plays faster so the pink arrives while the line is still on it.
RAMP = {"C1": (2.0, 1.4), "C8": (2.6, 1.3)}

def speed_of(name, c, L):
    lo, hi = (0.8, 2.0) if name in FULLFIT else (LO.get(name, 0.8), 1.2)
    return min(max(c / L, lo), hi)

# PUSH adds a push-in to a clip whose camera came back still; PULL starts zoomed in and pulls back to 1.0.
#   C1 (the hook) and C2 (fifty strings, the blackout) are changes at one position: kling held the camera dead still in both.
#   C1 pushes in at 3.7% a second (camera_path.py counts 3% and up as moving) and C2 pulls back out from that zoom, so the two
#   read as one move in and out, and C2 ends on the still that C3's flight starts from. C9 (power injection) came back still too.
PUSH = {"C1": (560, 900, 0.17), "C9": (600, 760, 0.16)}        # (focus x, focus y, zoom gained over the segment)
PULL = {"C2": (560, 900, 0.17)}                                # (focus x, focus y, zoom at the start, back to 1.0 at the end)
EASE_AFTER = {"C10": "C9"}; EASE_S = 0.8                       # the clip after a PUSH starts at that zoom and eases back
# EASE_FROM: kling pushed in for real in C5 (start-only) and ended 2.75x closer than the still C6 starts on, so the cut would
# jump back. C6 starts at that zoom on the outlet and pulls out fast, like a whip zoom: (focus x, focus y, zoom gained,
# seconds), measured on gridded frames of the two segments (the outlet box is 563 px wide at C5's end and 210 px in C6's
# first frame; its red button sits at 520,1017 and 345,1083). HOLD_START holds C6's first frame for that long under the
# zoom-out, so the boxes snapping shut (0.1-0.4 s into the clip) are seen after it, not during it.
EASE_FROM = {"C6": (352, 1062, 1.75, 0.45)}
HOLD_START = {"C6": 0.3}
WHIP = {}                          # no far jumps: every cut joins two clips that share a still
EXTRA = {}
for (a_, b_), (wd_, _k) in WHIP.items(): EXTRA[a_] = EXTRA.get(a_, 0) + wd_ / 2; EXTRA[b_] = EXTRA.get(b_, 0) + wd_ / 2

def zoom_xy(fx, fy):
    return (f"max(0,min(iw-iw/zoom,{fx/W}*iw-iw/zoom/2))", f"max(0,min(ih-ih/zoom,{fy/H}*ih-ih/zoom/2))")

def post_zoom(name):
    if name not in PUSH and name not in EASE_AFTER and name not in PULL and name not in EASE_FROM: return
    n = max(2, round((SEG[name]['len'] + EXTRA.get(name, 0)) * FPS))
    if name in PUSH:
        fx, fy, zz = PUSH[name]; z = f"1+{zz}*on/{n - 1}"; note = f'push-in to {1+zz:.2f}x toward ({fx},{fy})'
    elif name in PULL:
        fx, fy, zz = PULL[name]; z = f"1+{zz}*(1-on/{n - 1})"; note = f'pulls back from {1+zz:.2f}x'
    else:
        if name in EASE_FROM: fx, fy, zz, es = EASE_FROM[name]
        else: fx, fy, zz = PUSH[EASE_AFTER[name]]; es = EASE_S
        N = round(es * FPS); note = f'eases back from {1+zz:.2f}x over {es}s'
        z = f"if(lt(on,{N}),1+{zz}*(1-(3*pow(on/{N},2)-2*pow(on/{N},3))),1)"
    x, y = zoom_xy(fx, fy)
    run(['-i', f'seg/{name}.mp4', '-vf', f"scale={W*2}:{H*2},zoompan=z='{z}':x='{x}':y='{y}':d=1:s={W}x{H}:fps={FPS},setsar=1"]
        + ENC + [f'tmp/{name}_z.mp4'])
    os.replace(f'tmp/{name}_z.mp4', f'seg/{name}.mp4'); print(f'  {name}: {note}')

def seg_clip(name):
    s = SEG[name]; L0 = s['len'] + EXTRA.get(name, 0); hold = HOLD_START.get(name, 0.0); L = L0 - hold
    p = f'clips/{name}.mp4'; c = dur(p)
    base = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},{SHARP},fps={FPS}"
    if name in RAMP:
        a, s1 = RAMP[name]; s2 = (c - a) / (L - a / s1)
        vf = f"setpts='if(lt(T,{a}),T/{s1},{a / s1:.4f}+(T-{a})/{s2:.4f})/TB',{base}"
        print(f'  {name}: clip {c:.2f}s -> {L:.2f}s, first {a}s at {s1}x, the rest at {s2:.2f}x')
    else:
        speed = speed_of(name, c, L); played = c / speed; pad = max(0.0, L - played)
        vf = f"setpts=PTS/{speed:.4f},{base}"
        if pad > 0.02:   # a clip that is too short for its line holds its last frame under a slow push-in (never planned)
            n = round(L * FPS)
            vf += (f",tpad=stop_mode=clone:stop_duration={pad+0.1:.3f},scale={W*2}:{H*2},"
                   f"zoompan=z='1+0.04*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS}")
        print(f'  {name}: clip {c:.2f}s -> {L:.2f}s at {speed:.3f}x' + (f', trims {played-L:.2f}s' if played > L + 0.02 else '')
              + (f', holds {pad:.2f}s' if pad > 0.02 else ''))
    if hold: vf += f",tpad=start_mode=clone:start_duration={hold:.3f}"
    run(['-i', p, '-vf', vf + f",trim=duration={L0:.3f},setpts=PTS-STARTPTS,setsar=1"] + ENC + [f'seg/{name}.mp4'])
    post_zoom(name)
    if name in SIGN: sign_pass(name)

def on(seg, t_clip):
    """Video time of a moment t_clip seconds into clips/<seg>.mp4, as seg_clip plays it."""
    sg = SEG[seg]; hold = HOLD_START.get(seg, 0.0); L = sg['len'] + EXTRA.get(seg, 0) - hold; c = dur(f'clips/{seg}.mp4')
    if seg in RAMP:
        a, s1 = RAMP[seg]; s2 = (c - a) / (L - a / s1); t = t_clip / s1 if t_clip < a else a / s1 + (t_clip - a) / s2
    else: t = t_clip / speed_of(seg, c, L)
    return sg['start'] + hold + t

# ---- the narration's words and beats ----
WORDS = json.load(open('audio/words_tight.json'))
NORM = [re.sub(r"[^a-z0-9']", "", w[2].lower()) for w in WORDS]
TL = json.load(open('timeline.json')); BT = {b['beat']: b for b in TL['beats']}
def at(beat, word=None, off=0.0):
    if word is None: return max(0.0, BT[beat]['start'] + off)
    i = next(j for j in range(BT[beat]['first_word'], len(NORM)) if NORM[j] == word); return WORDS[i][0] + off
def beat_end(beat): return BT[beat]['end']

# ---- pointer tracking (Rule 6), as in 15-build.py ----
TW, TH = 540, 960
def seg_frames(name, color=False):
    pf = 'bgr24' if color else 'gray'; ch = 3 if color else 1
    raw = subprocess.run(['ffmpeg','-v','error','-i',f'seg/{name}.mp4','-vf',f'scale={TW}:{TH}','-f','rawvideo','-pix_fmt',pf,'-'],
                         capture_output=True).stdout
    n = len(raw) // (TW * TH * ch); a = np.frombuffer(raw[:n*TW*TH*ch], np.uint8)
    return a.reshape(n, TH, TW, 3) if color else a.reshape(n, TH, TW)

def track(name, t_anchor, pts):
    """Similarity transforms from the anchor frame to every frame of seg/<name>.mp4, from points near the pointer."""
    fr = seg_frames(name); n = len(fr); fa = min(n - 1, max(0, round(t_anchor * FPS)))
    P = np.array(pts, np.float32) * (TW / W)
    T = {fa: np.array([[1, 0, 0], [0, 1, 0]], np.float64)}
    for step in (1, -1):
        i = fa; M = T[fa].copy()
        while 0 <= i + step < n:
            cur = (P @ M[:, :2].T + M[:, 2]).mean(0)
            mask = np.zeros((TH, TW), np.uint8); cv2.circle(mask, (int(cur[0]), int(cur[1])), 130, 255, -1)
            f0 = fr[i]; f1 = fr[i + step]
            p0 = cv2.goodFeaturesToTrack(f0, 300, 0.01, 4, mask=mask)
            if p0 is None or len(p0) < 12: p0 = cv2.goodFeaturesToTrack(f0, 400, 0.01, 5)
            S = None
            if p0 is not None and len(p0) >= 8:
                p1, st, _ = cv2.calcOpticalFlowPyrLK(f0, f1, p0, None, winSize=(21, 21), maxLevel=3)
                g = st.ravel() == 1
                if g.sum() >= 8: S, _ = cv2.estimateAffinePartial2D(p0[g], p1[g], method=cv2.RANSAC, ransacReprojThreshold=1.5)
            if S is None: S = np.array([[1, 0, 0], [0, 1, 0]], np.float64)
            M = np.vstack([S, [0, 0, 1]]) @ np.vstack([M, [0, 0, 1]]); M = M[:2]
            i += step; T[i] = M.copy()
    return T
def apply(M, p):
    q = np.array(p, np.float64) * (TW / W); r = M[:, :2] @ q + M[:, 2]; return r * (W / TW)
def mscale(M): return float(np.hypot(M[0, 0], M[1, 0]))

def arrow_path(ang, L=200, Hh=92):
    pts = [(0, 30), (125, 30), (125, 0), (L, Hh / 2), (125, Hh), (125, 62), (0, 62)]
    pts = [(x * L / 200, y * Hh / 92) for x, y in pts]
    pts = [(x - L / 2, y - Hh / 2) for x, y in pts]; a = math.radians(ang)
    rp = [(x * math.cos(a) - y * math.sin(a), x * math.sin(a) + y * math.cos(a)) for x, y in pts]
    mx = min(p[0] for p in rp); my = min(p[1] for p in rp); rp = [(x - mx, y - my) for x, y in rp]
    w = max(p[0] for p in rp); h = max(p[1] for p in rp)
    return 'm ' + ' l '.join(f'{x:.0f} {y:.0f}' for x, y in rp), w, h
def ring_path(r):
    k = 0.5523 * r
    return (f"m {r:.0f} 0 b {r+k:.0f} 0 {2*r:.0f} {r-k:.0f} {2*r:.0f} {r:.0f} b {2*r:.0f} {r+k:.0f} {r+k:.0f} {2*r:.0f} {r:.0f} {2*r:.0f} "
            f"b {r-k:.0f} {2*r:.0f} 0 {r+k:.0f} 0 {r:.0f} b 0 {r-k:.0f} {r-k:.0f} 0 {r:.0f} 0")
ts = ov.ts

# Pointers: positions measured on 100 px grids over frames of seg/<SEG>.mp4 (1080x1920) at t_anchor seconds into the
# segment. 'arrows': three solid arrows slide from p0 to p1; 'ring': one ring of radius r. Times are seconds into the segment.
POINTERS = [   # measured on gridded frames of seg/<SEG>.mp4 (22 Nov 2026)
    ("C9", "arrows", 0.9, 2.7, 1.5, {"p0": (620, 1650), "p1": (598, 1010), "size": 0.8}),    # B12 fresh power up the new wire
    ("C11", "arrows", 0.5, 2.3, 1.0, {"p0": (897, 770), "p1": (850, 1370), "size": 0.8}),    # B15 from the aerial to the car's radio
]   # no ring on the outlet's button (C5): the label GROUND-FAULT OUTLET is on then, and it is one device at a time

def pointer_events(t0, t1):
    ev = []
    for seg, kind, a_on, a_off, t_anchor, geo in POINTERS:
        s0 = SEG[seg]['start']
        if s0 + a_off <= t0 or s0 + a_on >= t1: continue
        pts = [geo['p0'], geo['p1']] if kind == 'arrows' else [geo['c']]
        T = track(seg, t_anchor, pts); nfr = max(T) + 1
        for f in range(max(0, round(a_on * FPS)), min(nfr, round(a_off * FPS))):
            M = T[f]; tt = s0 + f / FPS - t0; nxt = tt + 1 / FPS; sc = mscale(M)
            if tt < 0 or tt >= t1 - t0: continue
            fade = min(1.0, (f / FPS - a_on) / 0.2, (a_off - f / FPS) / 0.2)
            if kind == 'ring':
                c = apply(M, geo['c']); r = geo['r'] * sc; path = ring_path(r)
                al = int(255 * (1 - max(0.0, fade)))
                ev.append(f"Dialogue: 1,{ts(tt)},{ts(nxt)},Ring,,0,0,0,,{{\\an7\\pos({c[0]-r:.0f},{c[1]-r:.0f})\\alpha&H{al:02X}&"
                          f"\\1a&HFF&\\p1}}{path}{{\\p0}}")
            else:
                p0 = apply(M, geo['p0']); p1 = apply(M, geo['p1']); ang = round(math.degrees(math.atan2(p1[1]-p0[1], p1[0]-p0[0])))
                k_ = geo.get('size', 1.0); path, aw, ah = arrow_path(ang, L=200 * sc * k_, Hh=92 * sc * k_)
                for k in range(3):
                    ph = (f / FPS - a_on - 0.35 * k) % 1.05 if f / FPS - a_on - 0.35 * k >= 0 else None
                    if ph is None or ph > 1.0: continue
                    q = p0 + (p1 - p0) * ph; fa = min(1.0, ph / 0.18, (1.0 - ph) / 0.22, fade)
                    al = int(255 * (1 - max(0.0, fa)))
                    ev.append(f"Dialogue: 1,{ts(tt)},{ts(nxt)},Pointer,,0,0,0,,{{\\an7\\pos({q[0]-aw/2:.0f},{q[1]-ah/2:.0f})"
                              f"\\alpha&H{al:02X}&\\p1}}{path}{{\\p0}}")
    return ev

# ---- SIGN: words on the blank yard sign (CLAUDE.md 5, "Words inside the scene") ----
# The sign is a bright, colourless four-sided patch. Its corners are followed from an anchor frame where it is the biggest
# such patch (so the white garage door is never taken for it), smoothed, and the words are warped onto it in perspective and
# mixed into the picture. The words go on when the narrator posts the station (B16) and fade as the sign shrinks in the
# pull-back; in the last wide shots the sign is about 100 px wide and stays blank (it also sits under TikTok's buttons there).
SIGN_LINES = ("TUNE TO", "88.7 FM")
SIGN = {"C11": ("back", lambda: at("B16") - SEG["C11"]["start"]),     # (follow from the last or the first frame, the second
        "C12": ("fwd", lambda: -1.0)}                                   # into the segment the words go on; -1 = already on)
SIGN_MINW, SIGN_FADEW = 190, 70      # px at 1080: under MINW no words; full strength from MINW + FADEW

def _order(pts):
    pts = np.array(pts, np.float32); sm = pts.sum(1); d = pts[:, 0] - pts[:, 1]
    return np.array([pts[sm.argmin()], pts[d.argmax()], pts[sm.argmax()], pts[d.argmin()]], np.float32)   # TL, TR, BR, BL
def _quads(f):
    """Bright, colourless four-sided patches, at several brightness cuts: against a white wall the sign only separates at
    a high cut, and in a dim wide shot only at a low one."""
    hsv = cv2.cvtColor(f, cv2.COLOR_BGR2HSV); out = []
    for vmin in (165, 185, 200, 215):
        m = ((hsv[..., 2] > vmin) & (hsv[..., 1] < 50)).astype(np.uint8) * 255
        m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
        cs, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in cs:
            a = cv2.contourArea(c)
            if a < 250: continue
            hull = cv2.convexHull(c)
            if a / max(cv2.contourArea(hull), 1) < 0.9: continue
            q = _order(cv2.approxPolyN(hull, 4).reshape(4, 2))
            w = (np.linalg.norm(q[1] - q[0]) + np.linalg.norm(q[2] - q[3])) / 2; h = (np.linalg.norm(q[3] - q[0]) + np.linalg.norm(q[2] - q[1])) / 2
            if 0.55 < h / max(w, 1) < 1.25: out.append((a, q))
    return out
def sign_track(name, mode):
    """Per frame of seg/<name>.mp4, the sign's corners (TL, TR, BR, BL) in 1080x1920 px, or None where it is not followed.
    It starts from the biggest patch of the anchor frame and follows the patch nearest the last one; up to 10 frames in a
    row may miss (the corners are filled in between), after which the sign counts as lost."""
    fr = seg_frames(name, color=True); n = len(fr); order = list(range(n - 1, -1, -1) if mode == "back" else range(n))
    Q = [None] * n; prev = None; miss = 0
    for i in order:
        cand = _quads(fr[i])
        if prev is None: pick = max(cand, key=lambda x: x[0])[1] if cand else None
        else:
            pc = prev.mean(0); pw = np.linalg.norm(prev[1] - prev[0]); tol = (0.35 + 0.08 * miss) * pw + 20
            near = [q for a, q in cand if np.linalg.norm(q.mean(0) - pc) < tol and 0.75 ** (1 + miss / 3) < np.linalg.norm(q[1] - q[0]) / pw < 1.33 ** (1 + miss / 3)]
            pick = min(near, key=lambda q: np.linalg.norm(q.mean(0) - pc)) if near else None
        if pick is None:
            miss += 1
            if prev is None or miss > 10: break
            continue
        Q[i] = pick; prev = pick; miss = 0
    known = [i for i in range(n) if Q[i] is not None]
    for a_, b_ in zip(known, known[1:]):                      # fill the short gaps between two found frames
        for j in range(a_ + 1, b_): Q[j] = Q[a_] + (Q[b_] - Q[a_]) * ((j - a_) / (b_ - a_))
    k = 2; S = [None] * n
    for i in range(n):
        v = [Q[j] for j in range(max(0, i - k), min(n, i + k + 1)) if Q[j] is not None]
        if Q[i] is not None: S[i] = np.mean(v, axis=0) * (W / TW)
    return S

def sign_canvas():
    cw, ch = 1000, 870; im = Image.new('L', (cw, ch), 0); d = ImageDraw.Draw(im)
    f1 = ImageFont.truetype('fonts/HBXCaption.ttf', 150); f2 = ImageFont.truetype('fonts/HBXCaption.ttf', 235)
    d.text((cw // 2, 285), SIGN_LINES[0], font=f1, fill=255, anchor='mm'); d.text((cw // 2, 545), SIGN_LINES[1], font=f2, fill=255, anchor='mm')
    return np.array(im, np.float32) / 255.0

def sign_pass(name):
    mode, t_on = SIGN[name]; t_on = t_on(); Q = sign_track(name, mode); n = len(Q); canvas = sign_canvas(); ch, cw = canvas.shape
    src = np.float32([[0, 0], [cw, 0], [cw, ch], [0, ch]]); ink = np.array([51, 26, 16], np.float32)   # #101A33 as BGR
    rd = subprocess.Popen(['ffmpeg','-v','error','-i',f'seg/{name}.mp4','-f','rawvideo','-pix_fmt','bgr24','-'], stdout=subprocess.PIPE)
    wr = subprocess.Popen(['ffmpeg','-loglevel','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r',str(FPS),'-i','-'] + ENC
                          + [f'tmp/{name}_s.mp4'], stdin=subprocess.PIPE)
    done = 0
    for i in range(n):
        buf = rd.stdout.read(W * H * 3)
        if len(buf) < W * H * 3: break
        q = Q[i]; t = i / FPS
        if q is not None and t >= t_on:
            w = (np.linalg.norm(q[1] - q[0]) + np.linalg.norm(q[2] - q[3])) / 2
            a = min(1.0, (t - t_on) / 0.4) * min(1.0, max(0.0, (w - SIGN_MINW) / SIGN_FADEW))
            if a > 0.01:
                f = np.frombuffer(buf, np.uint8).reshape(H, W, 3).astype(np.float32)
                x0, y0 = np.floor(q.min(0)).astype(int) - 4; x1, y1 = np.ceil(q.max(0)).astype(int) + 4
                x0, y0, x1, y1 = max(0, x0), max(0, y0), min(W, x1), min(H, y1)
                M = cv2.getPerspectiveTransform(src, (q - [x0, y0]).astype(np.float32))
                m = cv2.warpPerspective(canvas, M, (x1 - x0, y1 - y0), flags=cv2.INTER_AREA)
                m = cv2.GaussianBlur(m, (0, 0), 0.9)[..., None] * (0.92 * a)
                f[y0:y1, x0:x1] = f[y0:y1, x0:x1] * (1 - m) + ink * m
                buf = np.clip(f, 0, 255).astype(np.uint8).tobytes(); done += 1
        wr.stdin.write(buf)
    wr.stdin.close(); wr.wait(); rd.stdout.close(); rd.wait()
    os.replace(f'tmp/{name}_s.mp4', f'seg/{name}.mp4'); print(f'  {name}: the sign carries "{" ".join(SIGN_LINES)}" in {done} frames')

# ---- LABELS and BILL (16-overlays.py); every time comes from the narration's words ----
def labels():
    led_on = max(at("B3", "led"), on("C3", 3.3))          # the label waits for its picture: the camera reaches the bulb
    return [("LED", led_on, beat_end("B3") - 0.1),
            ("GROUND-FAULT\\NOUTLET", at("B6"), beat_end("B6") - 0.05),
            ("PIXELS", at("B10"), beat_end("B10") + 0.25),
            ("POWER\\NINJECTION", at("B13"), beat_end("B13") - 0.05),
            ("FM\\NTRANSMITTER", at("B15", "transmitter", -0.1), at("B15", "transmitter", 1.7))]
def bill():
    steps = [(at("B3", "so"), 305), (at("B7", "so"), 120), (at("B9", "so"), 715), (at("B12", "so"), 52), (at("B15", "so"), 140),
             (at("B17", "add"), 772)]
    return {'start': 3, 'steps': steps, 'final': at("B19", "the"), 'end': TOTAL}

# ---- captions (ASS) ----
CAPFONT = ImageFont.truetype('fonts/HBXCaption.ttf', round(CAP_FS * 1000 / 1219))
CAPMAP = {}
MERGE = []
CAP_Y_AT = [("B18", 1500)]     # from this beat on the caption sits here (78% down, still inside the safe box): in the closing
                               # shot kling's push-in brings the dog down onto the usual line, and he is the last shot's payoff
def cap(w):
    t = re.sub(r"[^A-Za-z0-9'’\-]", "", w).upper(); return CAPMAP.get(t, t)
def caption_events(t0, t1):
    ev = []; words = [list(w) for w in WORDS if t0 - 0.01 <= w[0] < t1]; prev_end = t0
    nm = [re.sub(r"[^a-z0-9'\-]", "", w[2].lower()) for w in words]
    i = 0; merged = []
    while i < len(words):
        hit = next(((seq, txt) for seq, txt in MERGE if tuple(nm[i:i + len(seq)]) == seq), None)
        if hit: merged.append([words[i][0], words[i + len(hit[0]) - 1][1], hit[1]]); i += len(hit[0])
        else: merged.append(words[i]); i += 1
    for i, (s, e, w) in enumerate(merged):
        s = max(s, prev_end); nxt = merged[i + 1][0] if i + 1 < len(merged) else None
        end = nxt if (nxt is not None and nxt - e <= 0.35) else e + 0.18
        end = min(max(end, s + 0.12), t1); prev_end = end
        txt = cap(w); wpx = CAPFONT.getlength(txt); sc = min(100, int(100 * MAXW / max(wpx, 1)))
        cy = next((y for b, y in reversed(CAP_Y_AT) if s >= BT[b]['start'] - 0.01), CAP_Y)
        ev.append(f"Dialogue: 2,{ts(s-t0)},{ts(end-t0)},Caption,,0,0,0,,{{\\an5\\pos(540,{cy})\\fscx{int(sc*0.92)}\\fscy{int(sc*0.92)}"
                  f"\\t(0,70,\\fscx{sc}\\fscy{sc})}}{txt}")
    return ev

ASS_HEAD = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
ScaledBorderAndShadow: yes
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Caption,HBX Caption,114,&H00FFFFFF,&H00FFFFFF,&H00000000,&H8C000000,0,0,0,0,100,100,0,0,1,7,5,5,60,60,0,1
Style: Pointer,HBX Caption,20,&H00FFFFFF,&H00FFFFFF,&H00FFFFFF,&H90000000,0,0,0,0,100,100,0,0,1,0,6,7,0,0,0,1
Style: Ring,HBX Caption,20,&HFF000000,&H00FFFFFF,&H00FFFFFF,&H90000000,0,0,0,0,100,100,0,0,1,8,5,7,0,0,0,1
""" + ov.STYLES + """
[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

# ---- STREET: the end card (CLAUDE.md 4.5). Every build so far is a tile (its last frame); the new one drops into its lot ----
INK, YEL = (16, 26, 51), (255, 214, 46)
def street_card(last_frame_png, out, built=1, lots=6):
    """1.5 s, 1080x1920: ink ground, a row-by-row grid of lots; tile `built` (this video) drops in; the rest are empty."""
    os.makedirs('tmp/street', exist_ok=True)
    F1 = ImageFont.truetype('fonts/HBXCaption.ttf', 76); F2 = ImageFont.truetype('fonts/HBXCaption.ttf', 58)
    cols = 3; tw, th, gap = 270, 480, 36; rows = -(-lots // cols)
    gx = (W - cols * tw - (cols - 1) * gap) // 2; gy = 430
    tile = Image.open(last_frame_png).convert('RGB').resize((tw, th), Image.LANCZOS)
    prev = [Image.open(f'{HERE}/street/{n:02d}.jpg').convert('RGB').resize((tw, th), Image.LANCZOS) for n in STREET_BEFORE]
    n = round(CARD * FPS)
    for i in range(n):
        t = i / FPS; im = Image.new('RGB', (W, H), INK); d = ImageDraw.Draw(im)
        for x in range(0, W, 90): d.line([(x, 0), (x, H)], fill=(22, 34, 64), width=1)      # a faint grid, as on the banner
        for y in range(0, H, 90): d.line([(0, y), (W, y)], fill=(22, 34, 64), width=1)
        d.text((W // 2, 300), "OUR STREET", font=F1, fill=(255, 255, 255), anchor='mm')
        for k in range(lots):
            x0 = gx + (k % cols) * (tw + gap); y0 = gy + (k // cols) * (th + gap)
            if k < len(prev):
                im.paste(prev[k], (x0, y0)); d.rectangle([x0 - 4, y0 - 4, x0 + tw + 3, y0 + th + 3], outline=YEL, width=5)
            elif k == built - 1:
                p = min(1.0, max(0.0, (t - 0.15) / 0.35)); e = 1 - (1 - p) ** 3          # drops in from above, 0.15-0.5 s
                d.rectangle([x0, y0, x0 + tw, y0 + th], outline=(60, 78, 120), width=3)
                if p > 0:
                    yy = int(y0 - 90 * (1 - e)); im.paste(tile, (x0, yy)); d.rectangle([x0 - 4, yy - 4, x0 + tw + 3, yy + th + 3], outline=YEL, width=6)
            else:
                step = 26                                                              # an empty lot: a dashed outline
                for xx in range(x0, x0 + tw, step):
                    d.line([(xx, y0), (min(xx + 13, x0 + tw), y0)], fill=(90, 110, 160), width=3)
                    d.line([(xx, y0 + th), (min(xx + 13, x0 + tw), y0 + th)], fill=(90, 110, 160), width=3)
                for yy in range(y0, y0 + th, step):
                    d.line([(x0, yy), (x0, min(yy + 13, y0 + th))], fill=(90, 110, 160), width=3)
                    d.line([(x0 + tw, yy), (x0 + tw, min(yy + 13, y0 + th))], fill=(90, 110, 160), width=3)
                d.text((x0 + tw // 2, y0 + th // 2), "?", font=F1, fill=(60, 78, 120), anchor='mm')
        d.text((W // 2, gy + rows * (th + gap) + 40), "WHAT DO WE BUILD NEXT?", font=F2, fill=YEL, anchor='mm')
        im.save(f'tmp/street/{i:03d}.png')
    run(['-framerate', str(FPS), '-i', 'tmp/street/%03d.png', '-vf', f'fade=t=in:st=0:d=0.12,setsar=1'] + ENC + [out])
STREET_BEFORE = []     # the numbers of the build videos already on the street (their tiles are pipeline/street/NN.jpg)

# ---- sound: voice + bed + effects (as 15-build.py; runs once audio/ holds the narration, the bed and the effects) ----
def rms_db(path):
    ch = int(subprocess.run(['ffprobe','-v','error','-select_streams','a:0','-show_entries','stream=channels','-of','csv=p=0',path],
                            capture_output=True, text=True).stdout.strip())
    a = np.frombuffer(subprocess.run(['ffmpeg','-loglevel','error','-i',path,'-ar','22050','-f','f32le','-'],
                                     capture_output=True).stdout, np.float32)
    a = a[:len(a) // ch * ch].reshape(-1, ch).mean(1)
    fr = a[:len(a)//1102*1102].reshape(-1, 1102); e = np.sqrt((fr**2).mean(1) + 1e-12)
    act = e[e > e.max() * 0.1]
    return 20 * np.log10(np.sqrt((act**2).mean()))
def fx_list():
    """(file stem in audio/, start time, optional cut length, optional level offset dB, optional low-pass Hz). Event times
    read off the clips (16-jobs.tsv). fx1 bulbs ticking on, fx2 the breaker's clunk, fx3 rain, fx4 a sharp click, fx5 the
    pixels' shimmer, fx6 a muffled thump and a howl, fx7 a car radio tuning in, fx8 the till."""
    b = bill(); ticks = [("fx4", t + ov.CHIP_IN + ov.CHIP_HOLD, 0.35, -5) for t, _ in b['steps']]     # the counter's tick, quieter
    return [("fx1", on("C1", 0.6)), ("fx2", on("C2", 2.95)), ("fx3", on("C4", 0.4), 6.5), ("fx4", on("C5", 3.9)),
            ("fx4", on("C6", 0.15), 0.6, -3), ("fx5", on("C7", 2.1)), ("fx4", on("C9", 1.0), 0.6, -2), ("fx6", on("C10", 1.4)),
            ("fx7", on("C11", 0.6)), ("fx8", b['final'] + 0.15)] + ticks
BED, BED_UNDER, FX_UNDER = 'bed', 17.0, 11.0     # dB under the voice by active RMS; then set by under_the_voice.py (18-22 dB)

def mix(t0, t1, out, voice_only=False):
    voice = 'audio/narration_tight.wav'; v_db = rms_db(voice); T = t1 - t0
    inputs = ['-i', voice]; fc = [f"[0:a]aresample=48000,pan=stereo|c0=c0|c1=c0,apad=whole_dur={TOTAL + CARD:.3f},atrim={t0:.3f}:{t1:.3f},"
                                  f"asetpts=PTS-STARTPTS[v]"]
    parts = ['[v]']
    if not voice_only:
        g = v_db - BED_UNDER - rms_db(f'audio/{BED}.mp3')
        inputs += ['-stream_loop', '-1', '-i', f'audio/{BED}.mp3']
        fc.append(f"[1:a]aresample=48000,aformat=channel_layouts=stereo,atrim={t0:.3f}:{t0+T:.3f},asetpts=PTS-STARTPTS,volume={g:.2f}dB,"
                  f"afade=t=in:d=0.6,afade=t=out:st={max(0,T-0.8):.3f}:d=0.8[bed]"); parts.append('[bed]')
        k = 2
        for name, t, *opt in fx_list():
            if not (t0 - 0.5 <= t < t1): continue
            cut = opt[0] if len(opt) > 0 else None; off = opt[1] if len(opt) > 1 else 0.0; lp = opt[2] if len(opt) > 2 else None
            g = v_db - FX_UNDER - rms_db(f'audio/{name}.mp3') + off; d_ms = int(max(0, t - t0) * 1000)
            trim = f"atrim=0:{cut:.2f},afade=t=out:st={max(0, cut-0.3):.2f}:d={min(0.3, cut):.2f}," if cut else ""
            if lp: trim += f"lowpass=f={lp},"
            inputs += ['-i', f'audio/{name}.mp3']
            fc.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=stereo,{trim}volume={g:.2f}dB,adelay={d_ms}|{d_ms}[f{k}]")
            parts.append(f'[f{k}]'); k += 1
    fc.append(''.join(parts) + f"amix=inputs={len(parts)}:normalize=0:duration=first,atrim=0:{T:.3f},"
              f"loudnorm=I=-14:TP=-1.5:LRA=11,volume=2.6dB,alimiter=limit=0.84:level=false,aresample=48000[a]")
    run(inputs + ['-filter_complex', ';'.join(fc), '-map', '[a]', '-ac', '2', '-c:a', 'pcm_s16le', out])

def render(run_segs, tag, card=False):
    t0 = SEG[run_segs[0]]['start']; t1 = SEG[run_segs[-1]]['end']
    print(f'{tag}: {"+".join(run_segs)}  {t0:.2f}-{t1:.2f}s' + ('  (silent: no narration in audio/)' if SILENT else ''))
    for name in run_segs:
        if os.environ.get('REUSE') and os.path.exists(f'seg/{name}.mp4'): continue     # REUSE=1: only the overlays are redone
        seg_clip(name)
    with open(f'tmp/{tag}_list.txt', 'w') as f:
        for name in run_segs: f.write(f"file '../seg/{name}.mp4'\n")
    run(['-f','concat','-safe','0','-i',f'tmp/{tag}_list.txt','-c','copy',f'tmp/{tag}_clean.mp4'])
    ev = pointer_events(t0, t1) + ov.label_events(labels(), t0, t1) + ov.bill_events(bill(), t0, t1) + caption_events(t0, t1)
    open(f'tmp/{tag}.ass', 'w').write(ASS_HEAD + "\n".join(ev) + "\n")
    venc = ['-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-r',str(FPS)]
    run(['-i',f'tmp/{tag}_clean.mp4','-vf',f'ass=tmp/{tag}.ass:fontsdir=fonts'] + venc + ['-an', f'tmp/{tag}_burn.mp4'])
    pic, clean = f'tmp/{tag}_burn.mp4', f'tmp/{tag}_clean.mp4'
    if card:   # the street card after the last word, on both the captioned and the clean picture
        run(['-sseof', '-0.1', '-i', clean, '-update', '1', '-frames:v', '1', 'tmp/last_clean.png'])
        Image.open('tmp/last_clean.png').convert('RGB').save('out/street_tile.jpg', quality=92)
        street_card('tmp/last_clean.png', 'tmp/card.mp4', built=len(STREET_BEFORE) + 1)
        for src, dst in ((pic, f'tmp/{tag}_burn_card.mp4'), (clean, f'tmp/{tag}_clean_card.mp4')):
            with open('tmp/cardlist.txt', 'w') as f: f.write(f"file '{os.path.basename(src)}'\nfile 'card.mp4'\n")
            run(['-f','concat','-safe','0','-i','tmp/cardlist.txt'] + venc + ['-an', dst])
        pic, clean = f'tmp/{tag}_burn_card.mp4', f'tmp/{tag}_clean_card.mp4'; t1 += CARD
    if SILENT:
        os.replace(pic, f'tmp/{tag}.mp4'); os.replace(clean, f'tmp/{tag}_cleanmaster.mp4')
        return f'tmp/{tag}.mp4', None, f'tmp/{tag}_cleanmaster.mp4'
    mix(t0, t1, f'tmp/{tag}_mix.wav'); mix(t0, t1, f'tmp/{tag}_voice.wav', voice_only=True)
    aenc = ['-c:v','copy','-c:a','aac','-b:a','192k','-movflags','+faststart','-shortest']
    run(['-i', pic, '-i', f'tmp/{tag}_mix.wav'] + aenc + [f'tmp/{tag}.mp4'])
    run(['-i', pic, '-i', f'tmp/{tag}_voice.wav'] + aenc + [f'tmp/{tag}_voiceonly.mp4'])
    run(['-i', clean, '-i', f'tmp/{tag}_mix.wav'] + aenc + [f'tmp/{tag}_cleanmaster.mp4'])
    return f'tmp/{tag}.mp4', f'tmp/{tag}_voiceonly.mp4', f'tmp/{tag}_cleanmaster.mp4'

if __name__ == '__main__':
    args = [a for a in sys.argv[1:]]
    runs = [a.split(',') for a in args] or [ORDER]
    outs = [render(r, f'part{i}', card=not args) for i, r in enumerate(runs)]
    name = ('preview_silent' if SILENT else 'final') if not args else 'preview'
    if len(outs) == 1:
        for src, suf in zip(outs[0], ('', '_voiceonly', '_clean')):
            if src: os.replace(src, f'out/{name}{suf}.mp4')
    else:
        with open('tmp/join.txt','w') as f:
            for o, _, _ in outs: f.write(f"file '{os.path.basename(o)}'\n")
        run(['-f','concat','-safe','0','-i','tmp/join.txt','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p',
             '-movflags','+faststart'] + (['-an'] if SILENT else ['-c:a','aac','-b:a','192k']) + [f'out/{name}.mp4'])
    print('done:', name, round(dur(f'out/{name}.mp4'), 2), 's')
