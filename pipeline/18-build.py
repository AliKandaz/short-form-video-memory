# Video 18 (B20, "How to Launch a Ship From Your Back Yard"): the edit (CLAUDE.md 6.2 Steps 7, 9 and 10; written 26 Nov 2026).
# The first video edited under the rules of 25 Nov 2026 (CLAUDE.md 7.4), on 17-build.py's machinery:
# - place2(): every clip plays at its own speed with its landing on the word that names it, plays until it has settled, and
#   the finished step rests for a beat (STEP_BEAT) before the next clip starts. No clip is cut while its part is moving;
# - every clip is joined at its fifth frame or later (MINSTART) with three frames mixed (XFADE): wan2_7's first frames fade
#   from the still's tone into the clip's own;
# - the nearest source frame, never a blend; the colour shift back to S0's; the 720p frames upscaled to 1080x1920 with a light
#   sharpen; a slow push-in (0.6% a second) that is never snapped back; no whip and no blur;
# - captions, the term label and the counter are 16-overlays.py's ASS events; each clip's own sound is placed where its
#   picture is, never raised by more than 3 dB (MAXBOOST), left out if nearly silent (QUIET) or if a recogniser hears a
#   word in it (MUTE: none of the pilot's six).
#
#   python3 18-build.py <work dir> pilot      (pilot-map: the time map and the beats only)
#     the Gate D pilot: the opening (frame 0 to the first "But") and loop 3, the hardest fix (its "But" to the next "But"),
#     as the edit will play them. -> work/pilot.mp4 (voice, bed, the clips' own sounds, the tick), work/pilot_voiceonly.mp4,
#     work/pilot_natural.mp4 (the six clips as they came, with their own sound), work/pilot_hook.jpg (0, 0.5, 1 and 2 s),
#     work/pilot_steps.jpg (each step on its word), work/pilot_B_raw.mp4 + work/pilot_B_map.json (analysis/joins_check.py).
# The work dir holds stills/<key>.png, clips/<key>.mp4, work/check.json (steps-check.py), audio/ (narr_gateC.wav and
# words_gateC.json: the narration as the user heard it at Gate C; bed.mp3, tick.mp3, till.mp3) and fonts/HBXCaption.ttf.
import importlib.util, json, os, re, subprocess, sys
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
WORK, MODE = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else 'pilot')
os.chdir(WORK); os.makedirs('work', exist_ok=True)
def _imp(name, f):
    s = importlib.util.spec_from_file_location(name, os.path.join(HERE, f)); m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m); return m
ov = _imp('ov', '16-overlays.py'); pr = _imp('pr', '18-prompts.py')
W, H, FPS = ov.W, ov.H, ov.FPS
SW, SH = 720, 1276                       # wan2_7's 720p frame

def run(args): subprocess.run(['ffmpeg', '-loglevel', 'error', '-y'] + args, check=True)

# ---- the words: the narration as heard at Gate C (steps-timing.py: beats and step beats kept) ----
NARR = 'audio/narr_gateC.wav'
WORDS = [(d['a'], d['b'], d['w']) for d in json.load(open('audio/words_gateC.json'))]
def norm(w): return re.sub(r"[^a-z0-9'\-]", '', w.lower())
def at(word, after=0.0, end=False):
    """The start (or end) of the first `word` that starts at or after `after`."""
    for a, b, w in WORDS:
        if a >= after - 1e-6 and norm(w) == word: return b if end else a
    raise KeyError(word)
BUTS = [a for a, b, w in WORDS if norm(w) == 'but']

# ---- the clips: when each step lands and when it has settled ----
# Read on 26 Nov 2026 off each clip's sheet at 8 frames a second, close strips and the motion inside its part's own box
# (the heaps are 0.5% of the frame: steps-check.py's whole-frame `settle` sees only the first frames' fade, so check.json
# carries the boxes' reading for W3_2 and W3_3).
CHECK = json.load(open('work/check.json'))
def nframes(k): return CHECK[k]['frames']
def lastf(k): return (nframes(k) - 1) / FPS
def seg(k, s0, s1, v0, v1, **kw): return dict(k=k, s0=s0, s1=s1, v0=v0, v1=v1, **kw)
READ = {  # clip: (source time of the landing, what lands)
    'FC3':  (1.07, 'the hook opens at 0.15 s and the boat rolls; it hits the dock at 1.07 s; the splash peaks at 1.3-1.5 s'),
    'W3_1': (1.60, 'the cradle surfaces under the boat at 0.25 s; boat and cradle stop at the top of the rails at 1.6 s'),
    'W3_2': (0.60, 'two heaps fly out from the hull ends from 0.2 s and land at 0.6 s, with dust'),
    'W3_3': (0.60, 'two more heaps, further down, land at 0.6 s, with dust'),
    'W3_L': (1.73, 'the hook opens at 0.3 s; the boat rolls down dragging the heaps; in the water at 1.5 s; afloat at 1.73 s'),
}

MINSTART, STEP_BEAT, XFADE = 4 / FPS, 0.20, 3
XMASK = 8.0                              # grey levels a frame: more than this, the incoming clip is moving there (not mixed)
def place2(items, end):
    """17-build.py's: items are dicts with k, land (source time of the landing), at (video time the landing falls on),
    settle, and optionally s0 (first source time shown; at least MINSTART), speed and to (last source time shown). Each clip
    plays from at - (land - s0) / speed to `to`, or until the next clip starts, then rests on its last frame shown.
    Returns (segments, report); report rows are (clip, starts, lands, settled at, next starts, beat on the finished step)."""
    out, rep = [], []
    it = [{'s0': MINSTART, 'speed': 1.0, **x} for x in items]
    for x in it: x['s0'] = max(x['s0'], MINSTART); x['v0'] = x['at'] - (x['land'] - x['s0']) / x['speed']
    for i, x in enumerate(it):
        vn = it[i + 1]['v0'] if i + 1 < len(it) else end
        to = x.get('to', x['settle']); v_done = x['v0'] + (to - x['s0']) / x['speed']
        v_settled = x['v0'] + (x['settle'] - x['s0']) / x['speed']
        v1 = min(v_done, vn); out.append(seg(x['k'], x['s0'], x['s0'] + (v1 - x['v0']) * x['speed'], x['v0'], v1))
        if v1 < vn - 1e-6: out.append(seg(x['k'], x['s0'] + (v1 - x['v0']) * x['speed'], x['s0'] + (v1 - x['v0']) * x['speed'], v1, vn))
        rep.append((x['k'], x['v0'], x['at'], v_settled, vn, vn - v_settled))
    return out, rep
def item(k, at_, to=None):
    land = READ[k][0]
    return dict(k=k, land=land, settle=CHECK[k]['settle'], at=at_, to=lastf(k) if to is None else to)

# ---- colour: each still's shift against S0 on its sunlit lawn and (lightness only) on its pale ground (17-build.py) ----
GROUND = (0.10, 0.90, 0.90, 0.98)       # the pale ground under the block
LAWN_K, GROUND_K, NOFIX = 0.7, 0.5, set()
def lawn_mask(lab):
    a = cv2.GaussianBlur(lab[..., 1], (0, 0), 3); b = cv2.GaussianBlur(lab[..., 2], (0, 0), 3)
    return np.clip((130.0 - a) / 8.0, 0, 1) * np.clip((b - 136.0) / 8.0, 0, 1)
def lab_stats(img):
    lab = cv2.cvtColor(cv2.resize(img, (SW, SH), interpolation=cv2.INTER_AREA), cv2.COLOR_BGR2LAB).astype(np.float32)
    y0, y1 = int(0.12 * SH), int(0.52 * SH)
    reg = lab[y0:y1].reshape(-1, 3); m = lawn_mask(lab)[y0:y1].reshape(-1) > 0.9
    px = reg[m]; lit = px[px[:, 0] >= np.percentile(px[:, 0], 50)]
    x0, g0, x1, g1 = GROUND
    return np.median(lit, 0), lab[int(g0 * SH):int(g1 * SH), int(x0 * SW):int(x1 * SW)].reshape(-1, 3).mean(0)
_stats, _ref = {}, []
def still_shift(key):
    if not _ref: _ref.extend(lab_stats(cv2.imread('stills/S0.png')))
    if key not in _stats: _stats[key] = lab_stats(cv2.imread(f'stills/{key}.png'))
    (rl, rg), (sl, sg) = _ref, _stats[key]
    return LAWN_K * (rl - sl), np.array([float(np.clip(GROUND_K * (rg[0] - sg[0]), -6, 6)), 0.0, 0.0], np.float32)
def progress(k):
    st = np.array(CHECK[k]['step'], np.float32); c = np.cumsum(st); return c / max(c[-1], 1e-6)
def colour_fix(f, dl, dg):
    lab = cv2.cvtColor(f, cv2.COLOR_BGR2LAB).astype(np.float32)
    wgt = lawn_mask(lab)[..., None]
    lab += wgt * dl + (1 - wgt) * dg
    return cv2.cvtColor(np.clip(lab, 0, 255).astype(np.uint8), cv2.COLOR_LAB2BGR)

# ---- the camera in the edit: a slow push-in through a loop, never snapped back (5 Rule 5) ----
RATE, BASE = 0.006, 1.004               # BASE: 720x1276 x 1.5 is 6 px short of 1920
FOCUS = (0.50, 0.46)                    # the lawn's foot, where the hull goes in: it stays where it is
def zoom(t, acts):
    for a0, a1, mode in acts:
        if a0 <= t < a1 + 1e-6 and mode == 'push': return 1 + RATE * (t - a0)
    return 1.0

def M_at(t, acts):
    """The affine map from a 720p clip frame to the edit's 1080x1920 frame at video time t: the upscale and the push-in."""
    z = BASE * zoom(t, acts); sc = (W / SW) * z; cx, cy = FOCUS[0] * SW, FOCUS[1] * SH
    return np.float32([[sc, 0, W * FOCUS[0] - cx * sc], [0, sc, H * FOCUS[1] - cy * sc]])

class Clip:
    """Reads a clip's frames in order (the time map only ever goes forward in a clip), keeping the last one read."""
    def __init__(self, k): self.cap = cv2.VideoCapture(f'clips/{k}.mp4'); self.i = -1; self.f = None
    def get(self, j):
        while self.i < j:
            ok, f = self.cap.read()
            if not ok: break
            self.i += 1; self.f = f
        return self.f

def render(segs, t0, t1, acts, out):
    """The clean picture from video time t0 to t1."""
    n = int(round((t1 - t0) * FPS)); clips = {}; shifts = {}
    p = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}',
                          '-r', str(FPS), '-i', '-', '-vf', 'unsharp=5:5:0.6:5:5:0.0', '-c:v', 'libx264', '-crf', '16',
                          '-pix_fmt', 'yuv420p', out], stdin=subprocess.PIPE)
    def picture(k, ts, t):
        j = min(nframes(k) - 1, max(0, int(round(ts * FPS))))            # the nearest source frame, never a blend
        if k not in clips or clips[k].i > j: clips[k] = Clip(k)
        f = clips[k].get(j)
        if f.shape[1] != SW: f = cv2.resize(f, (SW, SH), interpolation=cv2.INTER_AREA)
        if k not in NOFIX:
            if k not in shifts: a, b = pr.C[k][0], pr.C[k][1]; shifts[k] = (still_shift(a), still_shift(b), progress(k))
            (la, ga), (lb, gb), pg = shifts[k]; w = float(pg[min(j, len(pg) - 1)])
            f = colour_fix(f, la + w * (lb - la), ga + w * (gb - ga))
        return cv2.warpAffine(f, M_at(t, acts), (W, H), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REPLICATE)
    def moving(k, j0, t):
        """Where the incoming clip moves over the frames to be mixed (its source frames j0 .. j0 + XFADE + 1, all past
        wan2_7's four fade-in frames), as a soft mask in the edit's frame."""
        c = cv2.VideoCapture(f'clips/{k}.mp4'); fr = []; j = 0
        while j <= j0 + XFADE + 1:
            ok, f = c.read()
            if not ok: break
            if j >= j0: fr.append(cv2.GaussianBlur(f, (0, 0), 1.5).astype(np.float32))
            j += 1
        mv = np.zeros(fr[0].shape[:2], np.float32)
        for a_, b_ in zip(fr, fr[1:]): mv = np.maximum(mv, np.abs(a_ - b_).mean(2))
        m = cv2.GaussianBlur(cv2.dilate(np.clip((mv - XMASK) / XMASK, 0, 1), np.ones((21, 21), np.uint8)), (0, 0), 4)
        return cv2.warpAffine(m, M_at(t, acts), (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    prev, last, hold, xf, mask = None, None, None, 0, None
    for i in range(n):
        t = t0 + i / FPS; s = next((x for x in segs if x['v0'] <= t + 1e-9 < x['v1']), segs[-1])
        ts = s['s0'] + (s['s1'] - s['s0']) * (t - s['v0']) / max(s['v1'] - s['v0'], 1e-9)
        g = picture(s['k'], ts, t)
        # a join into another clip of the same view: two renderings of one picture differ in their fine texture and
        # shading, so the first XFADE frames are mixed with the last frame shown (the step before has settled). The mix is
        # masked by the incoming clip's own motion over those frames (26 Nov 2026): where its part moves (W3_1's cradle
        # and W3_L's hull start at once) the incoming frame is taken whole, so no part is shown twice; everywhere else, the
        # hull at rest included, the two renderings are mixed. A plain mix showed the hull twice for two frames (the
        # pilot's first build, joins at 31.99 and 38.19 s); a mask on the difference between the two frames, or on motion
        # that took in wan2_7's fade-in frames, switched the floating hull's shading in one frame (31.99 s).
        if XFADE and prev is not None and s['k'] != prev['k'] and s.get('view') == prev.get('view'):
            hold, xf = last, XFADE; mask = moving(s['k'], min(nframes(s['k']) - 1, int(round(ts * FPS))), t)
        if xf and hold is not None:
            w = (XFADE - xf + 1) / (XFADE + 1); a = (w + (1 - w) * np.clip(mask, 0, 1))[..., None]
            g = np.clip(hold.astype(np.float32) * (1 - a) + g.astype(np.float32) * a, 0, 255).astype(np.uint8); xf -= 1
        prev, last = s, g
        p.stdin.write(g.tobytes())
    p.stdin.close(); p.wait()

# ---- overlays (17-build.py's) ----
CAP_Y, CAP_FS, MAXW = 1440, 114, 900
CAPFONT = ImageFont.truetype('fonts/HBXCaption.ttf', round(ov.em(CAP_FS)))
MERGE = [(('four', 'hundred', 'thousand', 'dollars'), '$400,000')]   # a long spoken number shows as digits (7.4)
def cap(w): return re.sub(r"[^A-Za-z0-9'\-]", '', w).upper()
def caption_events(t0, t1):
    ev = []; words = [list(w) for w in WORDS if t0 - 0.01 <= w[0] < t1]; prev_end = t0
    nm = [norm(w[2]) for w in words]; i = 0; merged = []
    while i < len(words):
        hit = next(((sq, txt) for sq, txt in MERGE if tuple(nm[i:i + len(sq)]) == sq), None)
        if hit: merged.append([words[i][0], words[i + len(hit[0]) - 1][1], hit[1]]); i += len(hit[0])
        else: merged.append([words[i][0], words[i][1], cap(words[i][2])]); i += 1
    for i, (s, e, txt) in enumerate(merged):
        s = max(s, prev_end); nxt = merged[i + 1][0] if i + 1 < len(merged) else None
        end = nxt if (nxt is not None and nxt - e <= 0.35) else e + 0.18
        end = min(max(end, s + 0.12), t1); prev_end = end
        sc = min(100, int(100 * MAXW / max(CAPFONT.getlength(txt), 1)))
        ev.append(f"Dialogue: 2,{ov.ts(s - t0)},{ov.ts(end - t0)},Caption,,0,0,0,,{{\\an5\\pos(540,{CAP_Y})"
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
# the bill (18-bill.md): $50 (a tow rope) at frame 0, then one jump per fix as its name is said ("This is a ...", "These
# are ..."); the total $397,150. A term wider than 940 px goes on two lines (5).
BILL = [('SLIPWAY', 'slipway', 37900), ('LAUNCHING\\NTRIGGER', 'trigger', 3000), ('DRAG CHAINS', 'chains', 2700),
        ('BALLAST', 'ballast', 2500), ('BOAT HOIST', 'hoist', 351000)]
START_PRICE = 50
def fixes(t1):
    """(label, start of "This"/"These", end of the sentence, price) for each fix whose sentence starts before t1."""
    out = []; t = 0.0
    for lab, last, add in BILL:
        starts = []
        for w in ('this', 'these'):
            try: starts.append(at(w, after=t))
            except KeyError: pass
        if not starts: break
        a = min(starts)
        if a >= t1: break
        b = at(last, after=a, end=True); out.append((lab, a, b, add)); t = b
    return out
def ass_file(t0, t1, path, final=None):
    fx = fixes(t1); ev = caption_events(t0, t1)
    ev += ov.label_events([(lab, a, b + 0.35) for lab, a, b, add in fx], t0, t1)
    ev += ov.bill_events({'start': START_PRICE, 'steps': [(a, add) for lab, a, b, add in fx], 'final': final, 'end': t1}, t0, t1)
    open(path, 'w').write(ASS_HEAD + '\n'.join(ev) + '\n')
    return fx

# ---- sound ----
BED_UNDER, FX_UNDER, TICK_OFF = 15.0, 11.0, -6.0    # dB under the voice by active RMS (measure the result)
POST_GAIN, LIMIT = 0.0, 0.79
MAXBOOST, QUIET, MUTE, FX_OFF = 3.0, -35.0, set(), {}
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
LEFT_OUT = {}
def mix(segs, fx, t0, t1, out, voice_only=False, final=None, tail=0.0):
    """The voice from t0; the bed; each clip's own sound where its picture is; the counter's tick at each jump; the till as
    the final bill grows. The window is t0..t1 (+ `tail` seconds of picture after the narration, e.g. the street card)."""
    T = t1 - t0 + tail; v_db = rms_db(NARR)
    inputs = ['-ss', f'{t0:.3f}', '-t', f'{t1 - t0:.3f}', '-i', NARR]
    fc = [f"[0:a]aresample=48000,pan=stereo|c0=c0|c1=c0,afade=t=out:st={max(0, t1 - t0 - 0.04):.3f}:d=0.04,"
          f"apad=whole_dur={T:.3f},atrim=0:{T:.3f},asetpts=PTS-STARTPTS[v]"]
    parts = ['[v]']
    if not voice_only:
        bed = bed_loop(); g = v_db - BED_UNDER - rms_db(bed)
        inputs += ['-stream_loop', '-1', '-i', bed]
        fc.append(f"[1:a]aresample=48000,highpass=f=70,pan=stereo|c0=c0|c1=c0,atrim=0:{T:.3f},asetpts=PTS-STARTPTS,"
                  f"volume={g:.2f}dB,afade=t=in:d=0.3,afade=t=out:st={max(0, T - 0.5):.3f}:d=0.5[bed]"); parts.append('[bed]')
        n = 2; lv = {}
        for x in segs:
            k, s0, s1, v0, v1 = x['k'], x['s0'], x['s1'], x['v0'], x['v1']
            if s1 - s0 < 0.05 or v1 <= t0 or v0 >= t1: continue
            if v0 < t0: s0 += (t0 - v0) * (s1 - s0) / (v1 - v0); v0 = t0
            if v1 > t1: s1 -= (v1 - t1) * (s1 - s0) / (v1 - v0); v1 = t1
            if k not in lv: lv[k] = rms_db(f'clips/{k}.mp4')
            if k in MUTE or lv[k] < QUIET: LEFT_OUT[k] = round(lv[k], 1); continue
            g = min(v_db - FX_UNDER - lv[k], MAXBOOST) + FX_OFF.get(k, 0.0)
            d = int(round((v0 - t0) * 1000)); L = s1 - s0; sp = L / (v1 - v0)
            tempo = f"atempo={sp:.4f}," if abs(sp - 1) > 0.01 else ""
            inputs += ['-ss', f'{s0:.3f}', '-t', f'{L:.3f}', '-i', f'clips/{k}.mp4']
            fc.append(f"[{n}:a]aresample=48000,aformat=channel_layouts=stereo,{tempo}afade=t=in:d=0.03,"
                      f"afade=t=out:st={max(0, v1 - v0 - 0.06):.3f}:d=0.06,volume={g:.2f}dB,adelay={d}|{d}[c{n}]")
            parts.append(f'[c{n}]'); n += 1
        g = v_db - FX_UNDER - rms_db('audio/tick.mp3') + TICK_OFF
        for lab, a, b, add in fx:                     # the counter's tick as the price drops into the pill
            tt = a + ov.CHIP_IN + ov.CHIP_HOLD
            if not (t0 <= tt < t1): continue
            d = int(round((tt - t0) * 1000)); inputs += ['-i', 'audio/tick.mp3']
            fc.append(f"[{n}:a]aresample=48000,pan=stereo|c0=c0|c1=c0,atrim=0:0.12,volume={g:.2f}dB,adelay={d}|{d}[c{n}]")
            parts.append(f'[c{n}]'); n += 1
        if final is not None and t0 <= final < t1:   # the till (keys, then the bell) as the total grows
            g = v_db - FX_UNDER - rms_db('audio/till.mp3'); d = int(round((final + 0.15 - t0) * 1000))
            inputs += ['-i', 'audio/till.mp3']
            fc.append(f"[{n}:a]aresample=48000,pan=stereo|c0=c0|c1=c0,afade=t=out:st=1.7:d=0.3,volume={g:.2f}dB,adelay={d}|{d}[c{n}]")
            parts.append(f'[c{n}]'); n += 1
    fc.append(''.join(parts) + f"amix=inputs={len(parts)}:normalize=0:duration=first,atrim=0:{T:.3f},"
              f"afade=t=out:st={max(0, T - 0.25):.3f}:d=0.25,"
              f"loudnorm=I=-14:TP=-1.5:LRA=11,volume={POST_GAIN}dB,alimiter=limit={LIMIT}:level=false,aresample=48000[a]")
    run(inputs + ['-filter_complex', ';'.join(fc), '-map', '[a]', '-ac', '2', '-c:a', 'pcm_s16le', out])

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
                  f"drawtext=fontfile=fonts/HBXCaption.ttf:text='{k.replace('_', ' ')}  (AS IT CAME, ITS OWN SOUND)':fontsize=34:"
                  f"fontcolor=0xFFD62E:borderw=3:bordercolor=black:x=(w-text_w)/2:y=200[v{i}];"
                  f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo[a{i}]")
    fc.append(''.join(f'[v{i}][a{i}]' for i in range(len(keys))) + f'concat=n={len(keys)}:v=1:a=1[v][a]')
    run(ins + ['-filter_complex', ';'.join(fc), '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-crf', '20',
               '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', out])

TAG = ("drawtext=fontfile=fonts/HBXCaption.ttf:text='{}':fontsize=40:fontcolor=0xFFD62E:borderw=4:bordercolor=black:"
       "x=(w-text_w)/2:y=110")
def window(name, segs, t0, t1, acts, tag):
    """One stretch of the video as the edit will play it: work/<name>_raw.mp4 (clean), work/<name>.mp4 (captions, label,
    counter, the full mix), work/<name>_voice.mp4 (the same with the voice only)."""
    render(segs, t0, t1, acts, f'work/{name}_raw.mp4')
    fx = ass_file(t0, t1, f'work/{name}.ass')
    mix(segs, fx, t0, t1, f'work/{name}_mix.wav'); mix(segs, fx, t0, t1, f'work/{name}_vo.wav', voice_only=True)
    for wav, out in ((f'work/{name}_mix.wav', f'work/{name}.mp4'), (f'work/{name}_vo.wav', f'work/{name}_voice.mp4')):
        run(['-i', f'work/{name}_raw.mp4', '-i', wav, '-vf', f'ass=work/{name}.ass:fontsdir=fonts,' + TAG.format(tag),
             '-c:v', 'libx264', '-crf', '18', '-pix_fmt', 'yuv420p', '-r', str(FPS), '-c:a', 'aac', '-b:a', '192k',
             '-ar', '48000', '-shortest', out])
    return fx
def concat(parts, out):
    ins = sum((['-i', p] for p in parts), [])
    fc = ''.join(f'[{i}:v]setsar=1[v{i}];[{i}:a]aresample=48000[a{i}];' for i in range(len(parts)))
    fc += ''.join(f'[v{i}][a{i}]' for i in range(len(parts))) + f'concat=n={len(parts)}:v=1:a=1[v][a]'
    run(ins + ['-filter_complex', fc, '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-crf', '18', '-pix_fmt', 'yuv420p',
               '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', out])

if MODE in ('pilot', 'pilot-map'):              # pilot-map: only the time map and the beats, nothing rendered
    # A: the opening. The hook plays from its fifth frame at frame 0 (no join before it) to the first "But".
    A0, A1 = 0.0, BUTS[0] - 0.02
    segA = [seg('HOOK', MINSTART, MINSTART + (A1 - A0), A0, A1)]
    # B: loop 3, from 0.3 s before its "But" to the next "But". Each step on the word that names it:
    B0, B1 = BUTS[2] - 0.30, BUTS[3] - 0.02
    items = [item('FC3', at('rams', after=BUTS[2])),                                # "set free" opens the hook; it hits the dock on "rams"
             item('W3_1', at('rails', after=BUTS[2]) + 0.10),                       # back at the top on "rails"
             item('W3_2', at('chain', after=BUTS[2]) + 0.10),                       # the first heaps land on "chain"
             item('W3_3', at('heaps', after=at('more', after=BUTS[2])) + 0.10),     # the second pair on "heaps"
             item('W3_L', at('chains', after=BUTS[2], end=True) + 0.25)]            # rolls from "These", afloat after "chains"
    segB, rep = place2(items, B1)
    segB = [seg('FC3', MINSTART, MINSTART, B0, segB[0]['v0'])] + segB          # the hull at rest on its trigger before "But"
    print('loop 3, each clip (video time):  starts  lands   settled  next starts  beat on the finished step')
    for k, v0, vl, vs, vn, beat in rep:
        print(f'  {k:5s}  {v0:6.2f}  {vl:6.2f}  {vs:6.2f}   {vn:6.2f}      {beat:+5.2f} s' + ('   << the next clip cuts in' if beat < STEP_BEAT - 0.01 else ''))
    print('time map (clip, source from, source to, video from, video to):')
    for x in segA + segB:
        print(f"  {x['k']:5s} {x['s0']:5.2f} {x['s1']:5.2f}  {x['v0']:6.2f} {x['v1']:6.2f}" + ('  rest' if x['s1'] == x['s0'] else ''))
if MODE == 'pilot':
    fxA = window('pilot_A', segA, A0, A1, [(A0, A1, 'push')], 'THE OPENING')
    fxB = window('pilot_B', segB, B0, B1, [(B0, B1, 'push')], f'LOOP 3, FROM {B0:.1f} S')
    concat(['work/pilot_A.mp4', 'work/pilot_B.mp4'], 'work/pilot.mp4')
    concat(['work/pilot_A_voice.mp4', 'work/pilot_B_voice.mp4'], 'work/pilot_voiceonly.mp4')
    natural(['HOOK', 'FC3', 'W3_1', 'W3_2', 'W3_3', 'W3_L'], 'work/pilot_natural.mp4')
    # for analysis/joins_check.py: loop 3's map in its own picture's time
    steps = [[x['k'], x['at'] - B0, w] for x, w in zip(items, ('rams', 'rails', 'chain', 'heaps', 'chains'))]
    json.dump(dict(segs=[{**x, 'v0': x['v0'] - B0, 'v1': x['v1'] - B0} for x in segB], end=B1 - B0, steps=steps),
              open('work/pilot_B_map.json', 'w'), indent=0)
    sheet('work/pilot_A.mp4', [(0.0, 'frame 0'), (0.5, ''), (1.0, ''), (2.0, '')], 'work/pilot_hook.jpg')
    lab = [f for f in fxB if f[1] >= B0]
    marks = [(x['at'] - B0 + 0.05, f'{x["k"]}: "{w.upper()}"') for x, w in zip(items, ('rams', 'rails', 'chain', 'heaps', 'chains'))]
    marks += [(lab[0][1] - B0 + 1.0, 'label, counter'), (B1 - B0 - 0.05, 'last frame')] if lab else []
    sheet('work/pilot_B.mp4', marks, 'work/pilot_steps.jpg', cols=4)
    print('fixes in loop 3:', [(l, round(a, 2), round(b, 2), add) for l, a, b, add in lab])
    print('clip sounds left out (active level, dB):', LEFT_OUT or 'none')
    print('loudness pilot (LUFS, true peak dBFS):', loudness('work/pilot.mp4'))
