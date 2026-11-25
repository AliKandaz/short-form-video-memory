# Video 17 (B12, "How to Keep a T-Rex in Your Back Yard"): the edit (CLAUDE.md 6.2 Steps 7, 9 and 10; written 24 Nov 2026).
# The build-steps edit, joining steps-test-demo.py (the time map, the nearest frame, the colour shift, the push-in) with video
# 16's overlays and mix (16-overlays.py, 16-build.py):
# - every wan2_7 clip plays at its own speed, placed so that its step lands on the word that names it; between clips the
#   picture rests on the finished step. The nearest source frame is taken, never a blend (7.4);
# - every frame's colours are shifted back to S0's (7.4): the shift of each still against S0 is measured on its lawn (green
#   pixels) and its pale ground, and inside a clip it moves from the start still's to the end still's as the step happens;
# - a slow push-in runs through each loop and eases back in the beat before the next "But" (5 Rule 5);
# - the 720p frames are upscaled to 1080x1920 with a light sharpen;
# - captions, the term label and the counter are ASS events; the clips' own sounds are placed where their pictures are, under
#   the voice with the bed and the counter's tick.
#
#   python3 17-build.py <work dir> pilot
#     the Gate D pilot, the hook and loop 1 up to the second "But":
#     work/pilot.mp4 (as the edit will play it), work/pilot_natural.mp4 (the six clips as they came, with their own sound),
#     work/pilot_hook.jpg (the hook at 0, 0.5, 1 and 2 s), work/pilot_steps.jpg (each step on its word)
# The work dir holds stills/<key>.png, clips/<key>.mp4, work/check.json (check17.py: each clip's motion, frame by frame),
# audio/ (narr_tight.wav and words_tight.json from 17-timing.py, bed.mp3, tick.mp3) and fonts/HBXCaption.ttf.
import importlib.util, json, os, re, subprocess, sys
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
WORK, MODE = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else 'pilot')
os.chdir(WORK); os.makedirs('work', exist_ok=True)
def _imp(name, f):
    s = importlib.util.spec_from_file_location(name, os.path.join(HERE, f)); m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m); return m
ov = _imp('ov', '16-overlays.py'); pr = _imp('pr', '17-prompts.py')
W, H, FPS = ov.W, ov.H, ov.FPS
SW, SH = 720, 1276                       # wan2_7's 720p frame

def run(args): subprocess.run(['ffmpeg', '-loglevel', 'error', '-y'] + args, check=True)

# ---- the words (17-timing.py) ----
WORDS = [(d['a'], d['b'], d['w']) for d in json.load(open('audio/words_tight.json'))]
def norm(w): return re.sub(r"[^a-z0-9'\-]", '', w.lower())
def at(word, after=0.0, end=False):
    """The start (or end) of the first `word` that starts at or after `after`."""
    for a, b, w in WORDS:
        if a >= after - 1e-6 and norm(w) == word: return b if end else a
    raise KeyError(word)
BUTS = [a for a, b, w in WORDS if norm(w) == 'but']

# ---- the time map ----
# Segments: dict(k=clip, s0, s1 = source times, v0, v1 = video times[, view='close'][, whip=True]). s0 == s1 is a rest on one
# frame; s1 - s0 != v1 - v0 plays the clip faster or slower (nearest frames). Landings were read off each clip (its motion in
# work/check.json, the loudest moment of its sound, the sheets at 8 frames a second) and set on, or just before, the word
# that names the step.
CHECK = json.load(open('work/check.json'))
def nframes(k): return CHECK[k]['frames']
def lastf(k): return (nframes(k) - 1) / FPS
def seg(k, s0, s1, v0, v1, **kw): return dict(k=k, s0=s0, s1=s1, v0=v0, v1=v1, **kw)
LAND = []              # (clip, video time of its landing), for the report: each step against its word
def place(items, end, after=0.0):
    """items: (clip, source from, source time of the landing, video time of the landing[, source to]). Each clip plays at its
    own speed from v0 = landing - (s_land - s_from) until the next one starts (its still tail is cut) or to its last frame
    (or `source to`), which then holds until the next one starts."""
    out = []; starts = [it[3] - (it[2] - it[1]) for it in items] + [end]
    LAND.extend((it[0], it[3]) for it in items if it[2] > it[1])
    for i, it in enumerate(items):
        k, s0 = it[0], it[1]; stop = it[4] if len(it) > 4 else lastf(k) + 1 / FPS
        v0, vn = starts[i], starts[i + 1]
        assert v0 >= (out[-1]['v1'] if out else after) - 1e-6, f'{k} starts at {v0:.2f}, before the clip before it has been shown'
        v1 = min(v0 + (stop - s0), vn); out.append(seg(k, s0, s0 + (v1 - v0), v0, v1))
        if v1 < vn - 1e-6: hold = min(stop, lastf(k)); out.append(seg(k, hold, hold, v1, vn))
    return out

def items_loop1():
    return [('HOOK', 0.00, 0.00, 0.00),                                   # pickets ring up from 0.13 s; the ring closes on "T-rex"
            ('FC1',  0.00, 1.20, at('steps') - 0.10),                     # his foot comes down, with its thud, on "steps"
            ('W1_1', 0.00, 1.10, at('holes') + 0.15),                     # the last holes open on "holes"
            ('W1_2', 0.20, 1.13, at('posts') + 0.13),                     # the last post drops in on "posts" (its still 0.2 s skipped)
            ('W1_3', 0.00, 1.00, at('concrete') + 0.23),                  # the collars are poured on "concrete"
            ('W1_4', 0.00, 1.00, at('cable', after=at('thick')) + 0.16)]  # the cables are strung tight on "cable"

WHIP = 0.30            # W4_4 jumps to a smaller night house in one frame (1.50 -> 1.60 s): a whip pan hides the jump (5 Rule 5)
FC4_SLOW = 1.10 / 1.32 # the mower's run across the lawn (FC4 0.7-1.8 s) at 0.83x, so that he eats it on "eats": the mower is
                       # small, the T-rex still, so the repeated frames don't show
W44_SLOW = 0.5         # W4_4's tail (the mower mowing a stripe) at half speed through "This is a night house. But he's lonely"
SHAKE_A, SHAKE_D = 9.0, 1.3   # FC5 came back with the roar in its sound but nothing shaking: a camera shake in the edit (px, s)
def map_full():
    B = BUTS
    snap = at('eats') - 0.10; v18 = snap - 0.30; v07 = v18 - 1.10 / FC4_SLOW; fc4 = v07 - 0.70
    T = place(items_loop1() + [
        ('FC2a', 0.00, 0.00, B[1] + 0.06),                                # he leans out over the cables from "But"
        ('FC2b', 0.00, 1.00, at('dry') + 0.15),                           # the pool is empty on "dry"
        ('W2_1', 0.00, 1.10, at('ditch') + 0.20),                         # the ditch has opened on "ditch"
        ('W2_2', 0.15, 0.90, at('drain') + 0.14),                         # the pipe thunks into the ditch on "drain"
        ('W2_3', 0.00, 0.65, at('concrete', after=B[1]) + 0.13),          # the wall rises on "concrete"
        ('W2_4', 0.00, 1.20, at('turf') + 0.14),                          # the turf is down on "turf"
        ('FC3',  0.00, 1.05, at('swats') + 0.04),                         # his tail smashes the shed on "swats"
        ('W3_1', 0.00, 0.95, at('hollow') + 0.15),                        # the hollow has sunk on "hollow"
        ('W3_2', 0.00, 1.10, at('clay') + 0.13),                          # lined on "clay"
        ('W3_3', 0.00, 0.95, at('boulders') + 0.21),                      # the boulders roll in from "roll" and settle on "boulders"
        ('W3_4', 0.00, 1.10, at('water') + 0.11)], end=fc4)               # the water is in on "water"; he drinks under "wallow"
    T += [seg('FC4', 0.00, 0.70, fc4, v07), seg('FC4', 0.70, 1.80, v07, v18)]   # the mower rolls in from "mower"
    shut = at('shut') + 0.15
    T += place([('FC4', 1.80, 2.10, snap),                                # he snaps it up on "eats"
                ('W4_1', 0.00, 1.10, at('slab') + 0.16),                  # the slab has spread on "slab"
                ('W4_2', 0.35, 1.30, at('walls') + 0.06),                 # back, left, right (on "walls"), front
                ('W4_3', 0.00, 0.60, at('roof') + 0.10),                  # the roof drops from "drop" and lands on "roof"
                ('W4_4', 0.35, 1.47, shut, 1.47)], end=shut, after=T[-1]['v1'])   # he ducks in; the door slides shut on "shut"
    w1 = shut + WHIP; w2 = w1 + (lastf('W4_4') - 1.63) / W44_SLOW; fc5 = at('roars') - 0.05
    T += [seg('W4_4', 1.47, 1.63, shut, w1, whip=True),                  # "This is a night house." on the shut building
          seg('W4_4', 1.63, lastf('W4_4'), w1, w2), seg('W4_4', lastf('W4_4'), lastf('W4_4'), w2, fc5)]
    cut1 = at('this', after=at('bed'))                                    # "This is laminated glass." in the close view
    T += place([('FC5',  0.00, 0.00, fc5),                                # the roar on "roars", with the shake
                ('W5_1', 0.00, 0.85, at('hole') + 0.09),                  # the panel clangs flat on "hole"
                ('W5_2', 0.00, 0.85, at('frame') + 0.17),                 # the frame clanks in on "frame"
                ('W5_3', 0.00, 1.00, at('glass') + 0.20),                 # the glass comes down through "lower in glass"
                ('W5_4', 0.00, 1.40, at('bed') + 0.14)], end=cut1, after=T[-1]['v1'])   # the bed, with the dog on it, on "bed"
    cut2 = at("that's"); cut3 = at('the', after=cut2) - 0.08; end = WORDS[-1][1] + 0.25
    c1 = cut2 - cut1; w54 = T[-1]['s1']; w54e = min(lastf('W5_4'), w54 + (cut3 - cut2))
    T += [seg('CLOSE', 0.0, c1, cut1, cut2, view='close'),                # nose to nose through the glass; the dog yawns
          seg('W5_4', w54, w54e, cut2, cut2 + (w54e - w54)),               # "That's your pet dinosaur." over the whole yard
          seg('W5_4', w54e, w54e, cut2 + (w54e - w54), cut3)]
    c2 = min(lastf('CLOSE'), c1 + (end - cut3))
    T += [seg('CLOSE', c1, c2, cut3, cut3 + (c2 - c1), view='close'),     # the bill: both fall asleep against the glass
          seg('CLOSE', c2, c2, cut3 + (c2 - c1), end, view='close')]
    acts = [(0.0, B[0], 'push_ease')] + [(B[i], B[i + 1], 'push_ease') for i in range(4)] + \
           [(B[4], cut1, 'push'), (cut1, cut2, 'push'), (cut2, cut3, 'pull'), (cut3, end, 'push')]
    return T, acts, end, dict(fc5=fc5, cut1=cut1, cut2=cut2, cut3=cut3, final=at('the', after=cut2))

# ---- colour: each still's shift against S0, on its sunlit lawn and (lightness only) on its pale ground ----
# From loop 3 on the stills came back darker and duller (the lawn's median L 142 -> 117 by S5_4). The shift is measured on
# the sunlit half of the lawn's green-and-yellow pixels (not the house's mint siding, not the water) and applied, at LAWN_K
# of its size, to those pixels only; everything else gets GROUND_K of the pale ground's change in lightness, no hue change.
# Tested on S2_4-S5_4 (24 Nov 2026): the full shift turned the siding lime and the ground yellow.
GROUND = (0.05, 0.87, 0.40, 0.97)       # the pale ground under the block, left of the pool's shadow (x0, y0, x1, y1)
LAWN_K, GROUND_K, NOFIX = 0.7, 0.5, {'CLOSE'}     # the close view has no pale ground and is its own picture: no shift
def lawn_mask(lab):
    a = cv2.GaussianBlur(lab[..., 1], (0, 0), 3); b = cv2.GaussianBlur(lab[..., 2], (0, 0), 3)
    return np.clip((130.0 - a) / 8.0, 0, 1) * np.clip((b - 136.0) / 8.0, 0, 1)
def lab_stats(img):
    lab = cv2.cvtColor(cv2.resize(img, (SW, SH), interpolation=cv2.INTER_AREA), cv2.COLOR_BGR2LAB).astype(np.float32)
    reg = lab[int(0.15 * SH):int(0.60 * SH)].reshape(-1, 3); m = lawn_mask(lab)[int(0.15 * SH):int(0.60 * SH)].reshape(-1) > 0.9
    px = reg[m]; lit = px[px[:, 0] >= np.percentile(px[:, 0], 50)]
    x0, y0, x1, y1 = GROUND
    return np.median(lit, 0), lab[int(y0 * SH):int(y1 * SH), int(x0 * SW):int(x1 * SW)].reshape(-1, 3).mean(0)
_stats, _ref = {}, []
def still_shift(key):
    if not _ref: _ref.extend(lab_stats(cv2.imread('stills/S0.png')))
    if key not in _stats: _stats[key] = lab_stats(cv2.imread(f'stills/{key}.png'))
    (rl, rg), (sl, sg) = _ref, _stats[key]
    return LAWN_K * (rl - sl), np.array([float(np.clip(GROUND_K * (rg[0] - sg[0]), -6, 6)), 0.0, 0.0], np.float32)
def progress(k):
    """How far the step has got at each frame of clip k, 0 to 1, from its frame-to-frame motion (17-check.py)."""
    st = np.array(CHECK[k]['step'], np.float32); c = np.cumsum(st); return c / max(c[-1], 1e-6)
def colour_fix(f, dl, dg):
    lab = cv2.cvtColor(f, cv2.COLOR_BGR2LAB).astype(np.float32)
    wgt = lawn_mask(lab)[..., None]
    lab += wgt * dl + (1 - wgt) * dg
    return cv2.cvtColor(np.clip(lab, 0, 255).astype(np.uint8), cv2.COLOR_LAB2BGR)

# ---- the camera in the edit: a push-in of about 0.8% a second through each loop, eased back over the beat before the next
# "But"; a fresh push after each cut; a slow pull back over the whole yard on "That's your pet dinosaur." (5 Rule 5) ----
RATE, EASE, BASE, PULL = 0.008, 0.45, 1.004, 0.05   # BASE: 720x1276 x 1.5 is 6 px short of 1920
FOCUS = (0.50, 0.42)                    # the middle of the lawn stays where it is
def zoom(t, acts):
    for a0, a1, mode in acts:
        if a0 <= t < a1:
            if mode == 'pull': p = (t - a0) / (a1 - a0); return 1 + PULL * (1 - (1 - (1 - p) ** 2))
            if mode == 'push' or t < a1 - EASE: return 1 + RATE * (t - a0)
            top = 1 + RATE * max(0.0, a1 - EASE - a0); p = (t - (a1 - EASE)) / EASE
            return top + (1 - top) * (0.5 - 0.5 * np.cos(np.pi * p))
    return 1.0
def shake(t, t0):
    """FC5's roar: the frame jolts and settles (px offsets) under a little extra zoom so no edge shows."""
    if t0 is None: return 0.0, 0.0, 1.0
    u = t - t0
    if u < 0 or u > SHAKE_D: return 0.0, 0.0, 1.0
    a = SHAKE_A * np.exp(-u / 0.45) * min(1.0, u / 0.05)
    return (a * np.sin(2 * np.pi * 9.3 * u + 0.7), 0.8 * a * np.sin(2 * np.pi * 12.1 * u + 2.1),
            1 + 0.018 * min(1.0, u / 0.1) * (1 - u / SHAKE_D))
def whip_frame(g, p, n):
    """p in [0, 1): the picture flies off to the left, then the next one comes in from the right, blurred along the move."""
    def d(q): return -0.9 * W * (q / 0.5) ** 2 if q < 0.5 else 0.9 * W * (1 - (q - 0.5) / 0.5) ** 2
    x = d(p); L = int(min(420, abs(d(min(p + 1 / n, 0.999)) - x))) | 1
    g = cv2.warpAffine(g, np.float32([[1, 0, x], [0, 1, 0]]), (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    return cv2.blur(g, (L, 1)) if L > 1 else g

XFADE = 0                               # frames of cross-fade at a join (0 here: 'full' reproduces video 17 as delivered)
class Clip:
    """Reads a clip's frames in order (the time map only ever goes forward in a clip), keeping the last one read."""
    def __init__(self, k): self.cap = cv2.VideoCapture(f'clips/{k}.mp4'); self.i = -1; self.f = None
    def get(self, j):
        while self.i < j:
            ok, f = self.cap.read()
            if not ok: break
            self.i += 1; self.f = f
        return self.f

def render(segs, end, acts, out, shake_t=None):
    n = int(round(end * FPS)); clips = {}; shifts = {}
    p = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}',
                          '-r', str(FPS), '-i', '-', '-vf', 'unsharp=5:5:0.6:5:5:0.0', '-c:v', 'libx264', '-crf', '16',
                          '-pix_fmt', 'yuv420p', out], stdin=subprocess.PIPE)
    def picture(k, ts, t):
        j = min(nframes(k) - 1, max(0, int(round(ts * FPS))))            # the nearest source frame, never a blend
        if k not in clips: clips[k] = Clip(k)
        f = clips[k].get(j)
        if f.shape[1] != SW: f = cv2.resize(f, (SW, SH), interpolation=cv2.INTER_AREA)
        if k not in NOFIX:
            if k not in shifts: a, b = pr.C[k][0], pr.C[k][1]; shifts[k] = (still_shift(a), still_shift(b), progress(k))
            (la, ga), (lb, gb), pg = shifts[k]; w = float(pg[min(j, len(pg) - 1)])
            f = colour_fix(f, la + w * (lb - la), ga + w * (gb - ga))
        dx, dy, zs = shake(t, shake_t)
        z = BASE * zoom(t, acts) * zs; sc = (W / SW) * z; cx, cy = FOCUS[0] * SW, FOCUS[1] * SH
        M = np.float32([[sc, 0, W * FOCUS[0] - cx * sc + dx], [0, sc, H * FOCUS[1] - cy * sc + dy]])
        return cv2.warpAffine(f, M, (W, H), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REPLICATE)
    prev, hold, xf = None, None, 0
    for i in range(n):
        t = i / FPS; s = next((x for x in segs if x['v0'] <= t < x['v1']), segs[-1])
        if s.get('whip'):
            q = (t - s['v0']) / (s['v1'] - s['v0']); g = picture(s['k'], s['s0'] if q < 0.5 else s['s1'], t)
            g = whip_frame(g, q, max(1, round((s['v1'] - s['v0']) * FPS)))
        else:
            g = picture(s['k'], s['s0'] + (s['s1'] - s['s0']) * (t - s['v0']) / max(s['v1'] - s['v0'], 1e-9), t)
        # a join from one clip's resting frame into the next clip (same view): two renderings of one picture differ in
        # their fine texture, so the first XFADE frames are mixed with the resting frame (nothing is moving yet)
        if XFADE and prev is not None and s['k'] != prev['k'] and not s.get('whip') and not prev.get('whip') \
                and s.get('view') == prev.get('view'):
            hold, xf = last, XFADE
        if xf and hold is not None:
            w = (XFADE - xf + 1) / (XFADE + 1); g = cv2.addWeighted(hold, 1 - w, g, w, 0); xf -= 1
        prev, last = s, g
        p.stdin.write(g.tobytes())
    p.stdin.close(); p.wait()

# ---- overlays ----
CAP_Y, CAP_FS, MAXW = 1440, 114, 900
CAP_Y_CLOSE = 1500                      # in the close view the dog sits on the 75% line; 78% is on his bed's rim (5 Rule 7)
SEGS = []                               # the time map being rendered (caption_events reads which view a word falls in)
def cap_y(t): return CAP_Y_CLOSE if any(x.get('view') == 'close' and x['v0'] <= t < x['v1'] for x in SEGS) else CAP_Y
CAPFONT = ImageFont.truetype('fonts/HBXCaption.ttf', round(ov.em(CAP_FS)))
MERGE = [(('a', 'hundred', 'and', 'eighty', 'thousand', 'dollars'), '$180,000')]   # a long spoken number shows as digits (7.4)
def cap(w): return re.sub(r"[^A-Za-z0-9'\-]", '', w).upper()
def caption_events(t0, t1):
    ev = []; words = [list(w) for w in WORDS if t0 - 0.01 <= w[0] < t1]; prev_end = t0
    nm = [norm(w[2]) for w in words]; i = 0; merged = []
    while i < len(words):
        hit = next(((seq, txt) for seq, txt in MERGE if tuple(nm[i:i + len(seq)]) == seq), None)
        if hit: merged.append([words[i][0], words[i + len(hit[0]) - 1][1], hit[1]]); i += len(hit[0])
        else: merged.append([words[i][0], words[i][1], cap(words[i][2])]); i += 1
    for i, (s, e, txt) in enumerate(merged):
        s = max(s, prev_end); nxt = merged[i + 1][0] if i + 1 < len(merged) else None
        end = nxt if (nxt is not None and nxt - e <= 0.35) else e + 0.18
        end = min(max(end, s + 0.12), t1); prev_end = end
        sc = min(100, int(100 * MAXW / max(CAPFONT.getlength(txt), 1)))
        ev.append(f"Dialogue: 2,{ov.ts(s - t0)},{ov.ts(end - t0)},Caption,,0,0,0,,{{\\an5\\pos(540,{cap_y(s + 0.01)})"
                  f"\\fscx{int(sc * 0.92)}\\fscy{int(sc * 0.92)}\\t(0,70,\\fscx{sc}\\fscy{sc})}}{txt}")
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
""" + ov.STYLES + """
[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
# the bill (17-bill.md): $148 at frame 0, then one jump per fix as its name is said ("This is a ...")
BILL = [('CABLE FENCE', 'fence', 33822), ('HA-HA', 'ha-ha', 34401), ('WALLOW', 'wallow', 13500),
        ('NIGHT HOUSE', 'house', 87500), ('LAMINATED GLASS', 'glass', 10200)]
START_PRICE = 148
def fixes(t1):
    """(label, start of "This", end of the sentence, price) for each fix whose "This is a ..." starts before t1."""
    out = []; t = 0.0
    for lab, last, add in BILL:
        try: a = at('this', after=t); b = at(last, after=a, end=True)
        except KeyError: break
        if a >= t1: break
        out.append((lab, a, b, add)); t = b
    return out
def ass_file(t1, path, final=None):
    fx = fixes(t1); ev = caption_events(0, t1)
    ev += ov.label_events([(lab, a, min(b + 0.35, t1)) for lab, a, b, add in fx], 0, t1)
    ev += ov.bill_events({'start': START_PRICE, 'steps': [(a, add) for lab, a, b, add in fx], 'final': final, 'end': t1}, 0, t1)
    open(path, 'w').write(ASS_HEAD + '\n'.join(ev) + '\n')
    return fx

# ---- sound ----
BED_UNDER, FX_UNDER, TICK_OFF = 15.0, 11.0, -6.0    # dB under the voice by active RMS (16-build.py; measure the result)
POST_GAIN, LIMIT = 0.0, 0.79                       # 0.6 (video 16's) gave -13.4 LUFS on video 17's full mix; 0.0 gives about -14
def rms_db(path, ss=None, t=None):
    a = np.frombuffer(subprocess.run(['ffmpeg', '-loglevel', 'error'] + (['-ss', f'{ss:.3f}'] if ss is not None else []) +
                                     ['-i', path] + (['-t', f'{t:.3f}'] if t is not None else []) +
                                     ['-ac', '1', '-ar', '22050', '-f', 'f32le', '-'], capture_output=True).stdout, np.float32)
    fr = a[:len(a) // 1102 * 1102].reshape(-1, 1102); e = np.sqrt((fr ** 2).mean(1) + 1e-12)
    act = e[e > e.max() * 0.1]
    return 20 * np.log10(np.sqrt((act ** 2).mean()))
def bed_loop():
    """bed.mp3 made into a seamless loop: its last second crossfaded into its first."""
    out = 'audio/bed_loop.wav'
    if os.path.exists(out): return out
    x = np.frombuffer(subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', 'audio/bed.mp3', '-ac', '1', '-ar', '48000', '-f',
                                      'f32le', '-'], capture_output=True).stdout, np.float32).copy()
    F = 48000; y = x[:len(x) - F].copy(); p = np.linspace(0, np.pi / 2, F)
    y[:F] = x[:F] * np.sin(p) + x[len(x) - F:] * np.cos(p)
    import wave
    with wave.open(out, 'wb') as f:
        f.setnchannels(1); f.setsampwidth(2); f.setframerate(48000); f.writeframes((np.clip(y, -1, 1) * 32767).astype('<i2').tobytes())
    return out
def clip_level(k):
    return rms_db(f'clips/{k}.mp4')
FX_OFF = {}                                          # per-clip level offsets in dB, if the user's ear asks for them
TILL_OFF = 0.0
# Since 24 Nov 2026 (the review of video 17): setting every clip's sound to one level turned the T-rex's footfall down 24 dB
# and turned three nearly silent clips up 8-12 dB. A new video sets MAXBOOST = 3 (never raise a clip's sound by more than
# 3 dB), QUIET = -35 (leave out a clip whose active level is below this) and MUTE (clips whose sound a recogniser heard a
# word in, or the user's ear turned down). They are off here so that 'full' still reproduces video 17 as delivered.
MAXBOOST, QUIET, MUTE = None, None, set()
def mix(segs, fx, t1, out, voice_only=False, final=None):
    """The voice; the bed; each clip's own sound where its picture is (at the speed it plays); the counter's tick at each jump
    and the till as the final bill grows. t1 includes the street card."""
    voice = 'audio/narr_tight.wav'; v_db = rms_db(voice)
    inputs = ['-i', voice]
    fc = [f"[0:a]aresample=48000,pan=stereo|c0=c0|c1=c0,apad=whole_dur={t1:.3f},atrim=0:{t1:.3f},asetpts=PTS-STARTPTS[v]"]
    parts = ['[v]']
    if not voice_only:
        bed = bed_loop(); g = v_db - BED_UNDER - rms_db(bed)
        inputs += ['-stream_loop', '-1', '-i', bed]
        fc.append(f"[1:a]aresample=48000,pan=stereo|c0=c0|c1=c0,atrim=0:{t1:.3f},asetpts=PTS-STARTPTS,volume={g:.2f}dB,"
                  f"afade=t=in:d=0.4,afade=t=out:st={max(0, t1 - 0.8):.3f}:d=0.8[bed]"); parts.append('[bed]')
        n = 2; lv = {}
        for x in segs:
            k, s0, s1, v0, v1 = x['k'], x['s0'], x['s1'], x['v0'], x['v1']
            if s1 - s0 < 0.05 or x.get('whip'): continue
            if k not in lv: lv[k] = clip_level(k)
            if k in MUTE or (QUIET is not None and lv[k] < QUIET): continue
            g = v_db - FX_UNDER - lv[k]
            if MAXBOOST is not None: g = min(g, MAXBOOST)
            g += FX_OFF.get(k, 0.0); d = int(round(v0 * 1000)); L = s1 - s0; sp = L / (v1 - v0)
            tempo = f"atempo={sp:.4f}," if abs(sp - 1) > 0.01 else ""
            inputs += ['-ss', f'{s0:.3f}', '-t', f'{L:.3f}', '-i', f'clips/{k}.mp4']
            fc.append(f"[{n}:a]aresample=48000,aformat=channel_layouts=stereo,{tempo}afade=t=in:d=0.03,"
                      f"afade=t=out:st={max(0, v1 - v0 - 0.06):.3f}:d=0.06,volume={g:.2f}dB,adelay={d}|{d}[c{n}]")
            parts.append(f'[c{n}]'); n += 1
        g = v_db - FX_UNDER - rms_db('audio/tick.mp3') + TICK_OFF
        for lab, a, b, add in fx:                     # the counter's tick as the price drops into the pill
            d = int(round((a + ov.CHIP_IN + ov.CHIP_HOLD) * 1000))
            inputs += ['-i', 'audio/tick.mp3']
            fc.append(f"[{n}:a]aresample=48000,pan=stereo|c0=c0|c1=c0,atrim=0:0.12,volume={g:.2f}dB,adelay={d}|{d}[c{n}]")
            parts.append(f'[c{n}]'); n += 1
        if final is not None:                         # the till (keys, then the bell) as the total grows
            g = v_db - FX_UNDER - rms_db('audio/till.mp3') + TILL_OFF; d = int(round((final + 0.15) * 1000))
            inputs += ['-i', 'audio/till.mp3']
            fc.append(f"[{n}:a]aresample=48000,pan=stereo|c0=c0|c1=c0,afade=t=out:st=1.7:d=0.3,volume={g:.2f}dB,adelay={d}|{d}[c{n}]")
            parts.append(f'[c{n}]'); n += 1
    fc.append(''.join(parts) + f"amix=inputs={len(parts)}:normalize=0:duration=first,atrim=0:{t1:.3f},"
              f"afade=t=out:st={max(0, t1 - 0.25):.3f}:d=0.25,"
              f"loudnorm=I=-14:TP=-1.5:LRA=11,volume={POST_GAIN}dB,alimiter=limit={LIMIT}:level=false,aresample=48000[a]")
    run(inputs + ['-filter_complex', ';'.join(fc), '-map', '[a]', '-ac', '2', '-c:a', 'pcm_s16le', out])

# ---- the street card (CLAUDE.md 4.5; 16-build.py's): every build so far as a tile, this one dropping into its lot ----
CARD, INK, YEL = 1.5, (16, 26, 51), (255, 214, 46)
STREET_BEFORE = [16]   # the build videos already on the street (pipeline/street/NN.jpg): video 16, the Christmas light show,
                       # was posted on 22 Nov 2026 (read from TikTok on 24 Nov), so 17 drops into the second lot
def street_card(tile_png, out, built=1, lots=6):
    os.makedirs('work/street', exist_ok=True)
    F1 = ImageFont.truetype('fonts/HBXCaption.ttf', 76); F2 = ImageFont.truetype('fonts/HBXCaption.ttf', 58)
    cols = 3; tw, th, gap = 270, 480, 36; rows = -(-lots // cols)
    gx = (W - cols * tw - (cols - 1) * gap) // 2; gy = 430
    tile = Image.open(tile_png).convert('RGB').resize((tw, th), Image.LANCZOS)
    prev = [Image.open(f'{HERE}/street/{n:02d}.jpg').convert('RGB').resize((tw, th), Image.LANCZOS) for n in STREET_BEFORE]
    n = round(CARD * FPS)
    for i in range(n):
        t = i / FPS; im = Image.new('RGB', (W, H), INK); d = ImageDraw.Draw(im)
        for x in range(0, W, 90): d.line([(x, 0), (x, H)], fill=(22, 34, 64), width=1)
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
                step = 26
                for xx in range(x0, x0 + tw, step):
                    d.line([(xx, y0), (min(xx + 13, x0 + tw), y0)], fill=(90, 110, 160), width=3)
                    d.line([(xx, y0 + th), (min(xx + 13, x0 + tw), y0 + th)], fill=(90, 110, 160), width=3)
                for yy in range(y0, y0 + th, step):
                    d.line([(x0, yy), (x0, min(yy + 13, y0 + th))], fill=(90, 110, 160), width=3)
                    d.line([(x0 + tw, yy), (x0 + tw, min(yy + 13, y0 + th))], fill=(90, 110, 160), width=3)
                d.text((x0 + tw // 2, y0 + th // 2), "?", font=F1, fill=(60, 78, 120), anchor='mm')
        d.text((W // 2, gy + rows * (th + gap) + 40), "WHAT DO WE BUILD NEXT?", font=F2, fill=YEL, anchor='mm')
        im.save(f'work/street/{i:03d}.png')
    run(['-framerate', str(FPS), '-i', 'work/street/%03d.png', '-vf', 'fade=t=in:st=0:d=0.12,setsar=1', '-c:v', 'libx264',
         '-crf', '16', '-pix_fmt', 'yuv420p', '-r', str(FPS), out])

def loudness(path):
    log = subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-i', path, '-af', 'ebur128=peak=true', '-f', 'null', '-'],
                         capture_output=True, text=True).stderr
    i = re.findall(r'I:\s+(-?[\d.]+) LUFS', log); tp = re.findall(r'Peak:\s+(-?[\d.]+) dBFS', log)
    return (float(i[-1]) if i else None), (float(tp[-1]) if tp else None)

def sheet(video, marks, out, cols=None, tw=270, th=480):
    cols = cols or len(marks); rows = (len(marks) + cols - 1) // cols
    img = Image.new('RGB', (cols * tw, rows * (th + 34)), (16, 26, 51)); dr = ImageDraw.Draw(img)
    f2 = ImageFont.truetype('fonts/HBXCaption.ttf', 20); cap_ = cv2.VideoCapture(video)
    for i, (t, txt) in enumerate(marks):
        cap_.set(cv2.CAP_PROP_POS_FRAMES, int(round(t * FPS))); ok, f = cap_.read()
        x, y = (i % cols) * tw, (i // cols) * (th + 34)
        img.paste(Image.fromarray(cv2.cvtColor(cv2.resize(f, (tw, th), interpolation=cv2.INTER_AREA), cv2.COLOR_BGR2RGB)), (x, y + 34))
        dr.text((x + 6, y + 6), f'{t:.2f} s  {txt}', font=f2, fill=(255, 214, 46))
    img.save(out, quality=90)

def natural(keys, out):
    """The clips one after another as they came, with their own sound, each named at the top."""
    ins, fc = [], []
    for i, k in enumerate(keys):
        ins += ['-i', f'clips/{k}.mp4']
        fc.append(f"[{i}:v]fps={FPS},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,"
                  f"drawtext=fontfile=fonts/HBXCaption.ttf:text='{k}  (AS IT CAME, ITS OWN SOUND)':fontsize=34:"
                  f"fontcolor=0xFFD62E:borderw=3:bordercolor=black:x=(w-text_w)/2:y=200[v{i}];"
                  f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo[a{i}]")
    fc.append(''.join(f'[v{i}][a{i}]' for i in range(len(keys))) + f'concat=n={len(keys)}:v=1:a=1[v][a]')
    run(ins + ['-filter_complex', ';'.join(fc), '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-crf', '20',
               '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', out])

if MODE == 'pilot-sheets':                         # only the two sheets again, from work/pilot.mp4
    fx = fixes(BUTS[1]); END = BUTS[1]
if MODE == 'pilot':
    END = BUTS[1]                                    # the pilot stops where loop 2's "But" would start
    place_ = items_loop1(); seg_ = place(place_, END); SEGS[:] = seg_
    acts = [(0.0, BUTS[0], 'push_ease'), (BUTS[0], END, 'push_ease')]
    render(seg_, END, acts, 'work/pilot_raw.mp4')
    fx = ass_file(END, 'work/pilot.ass')
    mix(seg_, fx, END, 'work/pilot_mix.wav'); mix(seg_, fx, END, 'work/pilot_voice.wav', voice_only=True)
    run(['-i', 'work/pilot_raw.mp4', '-i', 'work/pilot_mix.wav', '-vf', 'ass=work/pilot.ass:fontsdir=fonts', '-c:v', 'libx264',
         '-crf', '18', '-pix_fmt', 'yuv420p', '-r', str(FPS), '-c:a', 'aac', '-b:a', '192k', '-shortest', 'work/pilot.mp4'])
    run(['-i', 'work/pilot_raw.mp4', '-i', 'work/pilot_voice.wav', '-vf', 'ass=work/pilot.ass:fontsdir=fonts', '-c:v', 'libx264',
         '-crf', '18', '-pix_fmt', 'yuv420p', '-r', str(FPS), '-c:a', 'aac', '-b:a', '192k', '-shortest', 'work/pilot_voiceonly.mp4'])
    natural([k for k, *_ in place_], 'work/pilot_natural.mp4')
if MODE in ('pilot', 'pilot-sheets'):
    sheet('work/pilot.mp4', [(0.0, 'frame 0'), (0.5, ''), (1.0, ''), (2.0, '')], 'work/pilot_hook.jpg')
    marks = [(at('t-rex') + 0.3, '"T-REX"'), (at('steps') + 0.05, '"STEPS"'), (at('holes') + 0.2, '"HOLES"'),
             (at('posts') + 0.2, '"POSTS"'), (at('concrete') + 0.3, '"CONCRETE"'), (at('cable', after=at('thick')) + 0.25, '"CABLE"'),
             (fx[0][1] + 1.2, 'label, counter'), (END - 0.05, 'last frame')]
    sheet('work/pilot.mp4', marks, 'work/pilot_steps.jpg', cols=4)
    print('fixes:', [(lab, round(a, 2), round(b, 2), add) for lab, a, b, add in fx])
    print('loudness pilot (LUFS, true peak dBFS):', loudness('work/pilot.mp4'))

INTENT = {'FC1': 'steps', 'W1_1': 'holes', 'W1_2': 'posts', 'W1_3': 'concrete', 'W1_4': 'cable', 'FC2b': 'dry', 'W2_1': 'ditch',
          'W2_2': 'drain', 'W2_3': 'concrete', 'W2_4': 'turf', 'FC3': 'swats', 'W3_1': 'hollow', 'W3_2': 'clay', 'W3_3': 'boulders',
          'W3_4': 'water', 'FC4': 'eats', 'W4_1': 'slab', 'W4_2': 'walls', 'W4_3': 'roof', 'W4_4': 'shut', 'FC5': 'roars',
          'W5_1': 'hole', 'W5_2': 'frame', 'W5_3': 'glass', 'W5_4': 'bed'}
def steps_report(extra=()):
    """Each landing against the word it was placed on (the nearest occurrence of that word)."""
    rows = []
    for k, vl in list(LAND) + list(extra):
        word = INTENT.get(k); hits = [x for x in WORDS if norm(x[2]) == word]
        a, b, w = min(hits, key=lambda x: abs(x[0] - vl))
        rows.append((k, vl, w.strip('.,?:'), a, vl - a))
    return rows

if MODE in ('full', 'full-reuse'):
    segs, acts, END, mk = map_full(); SEGS[:] = segs; TOTAL = END + CARD
    print('time map (clip, source from, source to, video from, video to):')
    for x in segs:
        sp = (x['s1'] - x['s0']) / (x['v1'] - x['v0']) if x['s1'] != x['s0'] else 0
        print(f"  {x['k']:5s} {x['s0']:5.2f} {x['s1']:5.2f}  {x['v0']:6.2f} {x['v1']:6.2f}" + ('  rest' if x['s1'] == x['s0'] else
              '  whip' if x.get('whip') else f'  x{sp:.2f}' if abs(sp - 1) > 0.01 else '') + ('  close view' if x.get('view') else ''))
    rows = steps_report([('FC5', mk['fc5'] + 0.05)])
    print('each step against its word:'); [print(f'  {k:22s} lands {vl:6.2f}  "{w}" {a:6.2f}  ({d:+.2f} s)') for k, vl, w, a, d in rows]
    json.dump(dict(segs=segs, acts=acts, end=END, marks=mk, steps=rows), open('work/full_map.json', 'w'), indent=0)
    if MODE == 'full' or not os.path.exists('work/full_raw.mp4'):
        render(segs, END, acts, 'work/full_raw.mp4', shake_t=mk['fc5'])
    fx = ass_file(END, 'work/full.ass', final=mk['final'])
    run(['-sseof', '-0.1', '-i', 'work/full_raw.mp4', '-update', '1', '-frames:v', '1', 'work/last_clean.png'])
    street_card('work/last_clean.png', 'work/card.mp4', built=len(STREET_BEFORE) + 1)
    venc = ['-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', '-r', str(FPS)]
    run(['-i', 'work/full_raw.mp4', '-i', 'work/card.mp4', '-filter_complex',
         '[0:v]ass=work/full.ass:fontsdir=fonts,setsar=1[a];[1:v]setsar=1[b];[a][b]concat=n=2:v=1:a=0[v]', '-map', '[v]'] + venc +
        ['work/full_burn_card.mp4'])
    run(['-i', 'work/full_raw.mp4', '-i', 'work/card.mp4', '-filter_complex',
         '[0:v]setsar=1[a];[1:v]setsar=1[b];[a][b]concat=n=2:v=1:a=0[v]', '-map', '[v]'] + venc + ['work/full_clean_card.mp4'])
    mix(segs, fx, TOTAL, 'work/full_mix.wav', final=mk['final']); mix(segs, fx, TOTAL, 'work/full_voice.wav', voice_only=True)
    aenc = ['-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', '-shortest']
    run(['-i', 'work/full_burn_card.mp4', '-i', 'work/full_mix.wav'] + aenc + ['work/17-final.mp4'])
    run(['-i', 'work/full_burn_card.mp4', '-i', 'work/full_voice.wav'] + aenc + ['work/17-final-voiceonly.mp4'])
    run(['-i', 'work/full_clean_card.mp4', '-i', 'work/full_mix.wav'] + aenc + ['work/17-final-clean.mp4'])
    sheet('work/17-final.mp4', [(0.0, 'frame 0'), (0.5, ''), (1.0, ''), (2.0, '')], 'work/final_hook.jpg')
    sheet('work/17-final.mp4', [(vl + 0.05, f'{k}: "{w.upper()}"') for k, vl, w, a, d in rows], 'work/final_steps.jpg', cols=6, tw=180, th=320)
    print('fixes:', [(lab, round(a, 2), round(b, 2), add) for lab, a, b, add in fx])
    dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', 'work/17-final.mp4'],
                               capture_output=True, text=True).stdout)
    print(f'final {dur:.2f} s; loudness (LUFS, true peak dBFS):', loudness('work/17-final.mp4'))

if MODE == 'full-remix':                             # the audio only, onto the finished pictures (7.5)
    segs, acts, END, mk = map_full(); SEGS[:] = segs; TOTAL = END + CARD; fx = fixes(END)
    mix(segs, fx, TOTAL, 'work/full_mix.wav', final=mk['final']); mix(segs, fx, TOTAL, 'work/full_voice.wav', voice_only=True)
    aenc = ['-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', '-shortest']
    run(['-i', 'work/full_burn_card.mp4', '-i', 'work/full_mix.wav'] + aenc + ['work/17-final.mp4'])
    run(['-i', 'work/full_burn_card.mp4', '-i', 'work/full_voice.wav'] + aenc + ['work/17-final-voiceonly.mp4'])
    run(['-i', 'work/full_clean_card.mp4', '-i', 'work/full_mix.wav'] + aenc + ['work/17-final-clean.mp4'])
    print('loudness final, voice only (LUFS, true peak dBFS):', loudness('work/17-final.mp4'), loudness('work/17-final-voiceonly.mp4'))

# ---- since 24 Nov 2026 (the review of video 17, CLAUDE.md 7.4): the edit rules that keep the steps crisp ----
# 1. A clip is never cut before its step has settled, and the finished step is shown still for a beat before the next clip
#    starts. If the words leave no room, the narration gets a step beat (steps-timing.py --gaps) or the clip plays faster
#    (frames are dropped; a moving part is never slowed and never cut off).
# 2. Every clip starts at its fifth frame or later (MINSTART). wan2_7's first frames fade from the start picture's tone and
#    texture into the clip's own (about 6 levels darker): a join into frame 0 jumps by about 5 grey levels in the parts of
#    the picture where nothing moves; into frame 4 by about 1.3 (measured on video 17's 26 joins).
# 3. No whip and no blur to hide a jump, and no fast zoom: the push-in is slow and is never snapped back.
MINSTART, STEP_BEAT = 4 / FPS, 0.20      # and XFADE = 3 (set where a video is built: see 'recut4')
def place2(items, end):
    """items: dicts with k (clip), land (source time of the landing), at (video time the landing must fall on), settle
    (source time by which the step is finished and still) and optionally s0 (first source time shown; at least MINSTART),
    speed (1.0; more plays the clip faster) and to (last source time shown; default: settle). Each clip plays from
    at - (land - s0) / speed to `to`, then rests on that frame until the next clip starts. Returns (segments, report);
    report rows are (clip, starts, lands, settled at, next starts, beat): a beat under STEP_BEAT means the next clip would
    cut into this step, and STEP_BEAT - beat is the silence to add after this step's phrase (steps-timing.py --gaps)."""
    out, rep = [], []
    it = [{'s0': MINSTART, 'speed': 1.0, **x} for x in items]
    for x in it: x['s0'] = max(x['s0'], MINSTART); x['v0'] = x['at'] - (x['land'] - x['s0']) / x['speed']
    for i, x in enumerate(it):
        vn = it[i + 1]['v0'] if i + 1 < len(it) else end
        to = x.get('to', x['settle']); v_done = x['v0'] + (to - x['s0']) / x['speed']
        v_settled = x['v0'] + (x['settle'] - x['s0']) / x['speed']
        v1 = min(v_done, vn); out.append(seg(x['k'], x['s0'], x['s0'] + (v1 - x['v0']) * x['speed'], x['v0'], v1))
        if v1 < vn - 1e-6: out.append(seg(x['k'], to, to, v1, vn))
        rep.append((x['k'], x['v0'], x['at'], v_settled, vn, vn - v_settled))
    return out, rep

if MODE == 'recut4':
    # A test of the rules above on loop 4 of video 17 (the night house: slab, walls, roof, door), where the delivered
    # edit cut every clip into the next. Same clips; the narration re-timed with step beats (steps-timing.py --out steps).
    # -> work/recut4.mp4: the loop as delivered, then the loop under the new rules.
    WORDS = [(d['a'], d['b'], d['w']) for d in json.load(open('audio/words_steps.json'))]
    BUTS = [a for a, b, w in WORDS if norm(w) == 'but']
    so = at('so', after=BUTS[3]); T0 = so - 0.30; T1 = at('house', after=so, end=True) + 0.60
    items = [dict(k='W4_1', land=1.10, settle=1.30, at=at('slab', after=so) + 0.16),
             dict(k='W4_2', s0=0.35, land=1.30, settle=2.40, speed=1.25, at=at('walls', after=so) + 0.06),   # four walls, one by one
             dict(k='W4_3', land=0.75, settle=1.30, at=at('roof', after=so) + 0.10),
             dict(k='W4_4', s0=0.35, land=1.47, settle=1.47, at=at('shut', after=so) + 0.15)]   # 1.47: before the building jumps
    segs, rep = place2(items, T1)
    head = segs[0]['v0'] - T0                       # before the slab: the end of FC4, to its last frame
    segs = [seg('FC4', lastf('FC4') - head, lastf('FC4'), T0, segs[0]['v0'])] + segs
    print('clip   starts  lands   settled  next starts  beat on the finished step')
    for k, v0, vl, vs, vn, beat in rep:
        print(f'  {k:5s} {v0 - T0:6.2f} {vl - T0:6.2f}  {vs - T0:6.2f}   {vn - T0:6.2f}      {beat:+5.2f} s' + ('   << the next clip cuts in' if beat < STEP_BEAT - 0.01 else ''))
    for x in segs: x['v0'] -= T0; x['v1'] -= T0
    END = T1 - T0; SEGS[:] = segs
    json.dump(dict(segs=segs, end=END, steps=[[x['k'], x['at'] - T0, w] for x, w in zip(items, ('slab', 'walls', 'roof', 'shut'))]),
              open('work/recut4_map.json', 'w'), indent=0)        # for analysis/joins_check.py
    WORDS = [(a - T0, b - T0, w) for a, b, w in WORDS if T0 - 0.01 <= a < T1]
    RATE = 0.006                                    # a slow push-in, never snapped back
    XFADE = 3
    render(segs, END, [(0.0, END + 1, 'push')], 'work/recut4_raw.mp4')
    this = at('this'); ev = caption_events(0, END)
    ev += ov.label_events([('NIGHT HOUSE', this, min(at('house', end=True) + 0.35, END))], 0, END)
    ev += ov.bill_events({'start': 81871, 'steps': [(this, 87500)], 'final': None, 'end': END}, 0, END)
    open('work/recut4.ass', 'w').write(ASS_HEAD + '\n'.join(ev) + '\n')
    # the sound: the voice from T0, the bed, each clip's own sound where its picture is, never boosted by more than 3 dB
    MAXBOOST, QUIET = 3.0, -35.0
    run(['-ss', f'{T0:.3f}', '-t', f'{END:.3f}', '-i', 'audio/narr_steps.wav', 'work/recut4_voice_in.wav'])
    _mix_voice = 'work/recut4_voice_in.wav'
    v_db = rms_db('audio/narr_steps.wav'); bed = bed_loop(); inputs = ['-i', _mix_voice, '-stream_loop', '-1', '-i', bed]
    fc = [f"[0:a]aresample=48000,pan=stereo|c0=c0|c1=c0,apad=whole_dur={END:.3f},atrim=0:{END:.3f}[v]",
          f"[1:a]aresample=48000,pan=stereo|c0=c0|c1=c0,atrim=0:{END:.3f},volume={v_db - BED_UNDER - rms_db(bed):.2f}dB,afade=t=in:d=0.3,afade=t=out:st={END - 0.5:.3f}:d=0.5[bed]"]
    parts = ['[v]', '[bed]']; n = 2
    for x in segs:
        if x['s1'] - x['s0'] < 0.05: continue
        lvl = clip_level(x['k'])
        if lvl < QUIET: print(f"  {x['k']}: its own sound is left out (active level {lvl:.0f} dB)"); continue
        g = min(v_db - FX_UNDER - lvl, MAXBOOST); L = x['s1'] - x['s0']; sp = L / (x['v1'] - x['v0']); d = int(round(x['v0'] * 1000))
        tempo = f"atempo={sp:.4f}," if abs(sp - 1) > 0.01 else ""
        inputs += ['-ss', f"{x['s0']:.3f}", '-t', f'{L:.3f}', '-i', f"clips/{x['k']}.mp4"]
        fc.append(f"[{n}:a]aresample=48000,aformat=channel_layouts=stereo,{tempo}afade=t=in:d=0.03,afade=t=out:st={max(0, x['v1'] - x['v0'] - 0.06):.3f}:d=0.06,volume={g:.2f}dB,adelay={d}|{d}[c{n}]")
        parts.append(f'[c{n}]'); n += 1
    d = int(round((this + ov.CHIP_IN + ov.CHIP_HOLD) * 1000)); inputs += ['-i', 'audio/tick.mp3']
    fc.append(f"[{n}:a]aresample=48000,pan=stereo|c0=c0|c1=c0,atrim=0:0.12,volume={v_db - FX_UNDER - rms_db('audio/tick.mp3') + TICK_OFF:.2f}dB,adelay={d}|{d}[c{n}]"); parts.append(f'[c{n}]')
    fc.append(''.join(parts) + f"amix=inputs={len(parts)}:normalize=0:duration=first,atrim=0:{END:.3f},loudnorm=I=-14:TP=-1.5:LRA=11,alimiter=limit={LIMIT}:level=false,aresample=48000[a]")
    run(inputs + ['-filter_complex', ';'.join(fc), '-map', '[a]', '-ac', '2', '-c:a', 'pcm_s16le', 'work/recut4_mix.wav'])
    tag = "drawtext=fontfile=fonts/HBXCaption.ttf:text='{}':fontsize=46:fontcolor=0xFFD62E:borderw=5:bordercolor=black:x=(w-text_w)/2:y=112"
    run(['-i', 'work/recut4_raw.mp4', '-i', 'work/recut4_mix.wav', '-vf', 'ass=work/recut4.ass:fontsdir=fonts,' + tag.format('SAME CLIPS, NEW EDIT RULES'),
         '-c:v', 'libx264', '-crf', '18', '-pix_fmt', 'yuv420p', '-r', str(FPS), '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-shortest', 'work/recut4_new.mp4'])
    # the same words as delivered (video 17's own timing), cut from the final
    WT = [(d['a'], d['b'], d['w']) for d in json.load(open('audio/words_tight.json'))]
    o_so = [a for a, b, w in WT if norm(w) == 'so'][3]; o_end = [b for a, b, w in WT if norm(w) == 'house.' or w == 'house.'][0]
    run(['-ss', f'{o_so - 0.30:.3f}', '-t', f'{o_end + 0.60 - (o_so - 0.30):.3f}', '-i', 'work/17-final.mp4', '-vf', tag.format('LOOP 4 AS IT IS IN VIDEO 17'),
         '-c:v', 'libx264', '-crf', '18', '-pix_fmt', 'yuv420p', '-r', str(FPS), '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', 'work/recut4_old.mp4'])
    run(['-i', 'work/recut4_old.mp4', '-i', 'work/recut4_new.mp4', '-filter_complex',
         '[0:v]setsar=1[a];[1:v]setsar=1[b];[0:a]aresample=48000[x];[1:a]aresample=48000[y];[a][x][b][y]concat=n=2:v=1:a=1[v][o]',
         '-map', '[v]', '-map', '[o]', '-c:v', 'libx264', '-crf', '20', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', 'work/recut4.mp4'])
    print('recut4: old', round(o_end + 0.60 - (o_so - 0.30), 2), 's, new', round(END, 2), 's; loudness of the new half:', loudness('work/recut4_new.mp4'))
