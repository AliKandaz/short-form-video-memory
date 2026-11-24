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
# (clip, source from, source time of the landing, video time of the landing). Landings were read off each clip (the motion in
# work/check.json, the loudest moment of its sound, the sheets at 8 frames a second) and are set on, or just before, the word
# that names the step. A clip plays at its own speed from v0 = landing - (s_land - s_from) until the next clip starts (its
# still tail is cut) or to its last frame, which then holds.
def place_pilot():
    return [('HOOK', 0.00, 0.00, 0.00),                                   # pickets ring up from 0.13 s; the ring closes on "T-rex"
            ('FC1',  0.00, 1.20, at('steps') - 0.10),                     # his foot comes down, with its thud, on "steps"
            ('W1_1', 0.00, 1.10, at('holes') + 0.15),                     # the last holes open on "holes"
            ('W1_2', 0.20, 1.13, at('posts') + 0.13),                     # the last post drops in on "posts" (its still 0.2 s skipped)
            ('W1_3', 0.00, 1.00, at('concrete') + 0.23),                  # the collars are poured on "concrete"
            ('W1_4', 0.00, 1.00, at('cable', after=at('thick')) + 0.16)]  # the cables are strung tight on "cable"

CHECK = json.load(open('work/check.json'))
def nframes(k): return CHECK[k]['frames']
def timemap(place, end):
    seg = []
    starts = [vl - (sl - s0) for k, s0, sl, vl in place] + [end]
    for i, (k, s0, sl, vl) in enumerate(place):
        v0, v_next = starts[i], starts[i + 1]
        assert v0 >= (seg[-1][4] - 1e-6 if seg else 0.0), f'{k} starts before the clip before it has been shown'
        last = (nframes(k) - 1) / FPS; v1 = min(v0 + (last + 1 / FPS - s0), v_next)
        seg.append((k, s0, s0 + (v1 - v0), v0, v1))
        if v1 < v_next - 1e-6: seg.append((k, last, last, v1, v_next))            # rest on its last frame
    return seg

# ---- colour: each still's shift against S0, on the lawn and on the pale ground ----
GROUND = (0.05, 0.87, 0.40, 0.97)       # the pale ground under the block, left of the pool's shadow (x0, y0, x1, y1)
def lab_stats(img):
    lab = cv2.cvtColor(cv2.resize(img, (SW, SH), interpolation=cv2.INTER_AREA), cv2.COLOR_BGR2LAB).astype(np.float32)
    reg = lab[int(0.15 * SH):int(0.55 * SH)]; m = (reg[..., 1] < 124) & (reg[..., 2] > 138)     # lawn: green and yellowish
    x0, y0, x1, y1 = GROUND
    return np.median(reg[m], 0), lab[int(y0 * SH):int(y1 * SH), int(x0 * SW):int(x1 * SW)].reshape(-1, 3).mean(0)
_stats = {}
def still_shift(key):
    if key not in _stats: _stats[key] = lab_stats(cv2.imread(f'stills/{key}.png'))
    rl, rg = still_shift_ref(); sl, sg = _stats[key]; return rl - sl, rg - sg
_ref = []
def still_shift_ref():
    if not _ref: _ref.extend(lab_stats(cv2.imread('stills/S0.png')))
    return _ref
def progress(k):
    """How far the step has got at each frame of clip k, 0 to 1, from its frame-to-frame motion (check17.py)."""
    st = np.array(CHECK[k]['step'], np.float32); c = np.cumsum(st); return c / max(c[-1], 1e-6)
def colour_fix(f, dl, dg):
    lab = cv2.cvtColor(f, cv2.COLOR_BGR2LAB).astype(np.float32)
    wgt = np.clip((132.0 - cv2.GaussianBlur(lab[..., 1], (0, 0), 3)) / 10.0, 0, 1)[..., None]   # 1 on grass, 0 elsewhere
    lab += wgt * dl + (1 - wgt) * dg
    return cv2.cvtColor(np.clip(lab, 0, 255).astype(np.uint8), cv2.COLOR_LAB2BGR)

# ---- the push-in: about 0.8% a second through each loop, eased back over the beat before the next "But" ----
RATE, EASE, BASE = 0.008, 0.45, 1.004   # BASE: 720x1276 x 1.5 is 6 px short of 1920
FOCUS = (0.50, 0.42)                    # the middle of the lawn stays where it is
def zoom(t, acts):
    for a0, a1 in zip(acts, acts[1:]):
        if a0 <= t < a1:
            if t < a1 - EASE: return 1 + RATE * (t - a0)
            top = 1 + RATE * max(0.0, a1 - EASE - a0); p = (t - (a1 - EASE)) / EASE
            return top + (1 - top) * (0.5 - 0.5 * np.cos(np.pi * p))
    return 1.0

class Clip:
    """Reads a clip's frames in order (the time map only ever goes forward in a clip), keeping the last one read."""
    def __init__(self, k): self.cap = cv2.VideoCapture(f'clips/{k}.mp4'); self.i = -1; self.f = None
    def get(self, j):
        while self.i < j:
            ok, f = self.cap.read()
            if not ok: break
            self.i += 1; self.f = f
        return self.f

def render(seg, end, acts, out):
    n = int(round(end * FPS)); clips = {}; shifts = {}
    p = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}',
                          '-r', str(FPS), '-i', '-', '-vf', 'unsharp=5:5:0.6:5:5:0.0', '-c:v', 'libx264', '-crf', '16',
                          '-pix_fmt', 'yuv420p', out], stdin=subprocess.PIPE)
    used = []
    for i in range(n):
        t = i / FPS; k, s0, s1, v0, v1 = next((s for s in seg if s[3] <= t < s[4]), seg[-1])
        ts = s0 + (s1 - s0) * (t - v0) / max(v1 - v0, 1e-9)
        j = min(nframes(k) - 1, max(0, int(round(ts * FPS))))          # the nearest source frame, never a blend
        if k not in clips: clips[k] = Clip(k)
        f = clips[k].get(j)
        if f.shape[1] != SW: f = cv2.resize(f, (SW, SH), interpolation=cv2.INTER_AREA)
        if k not in shifts:
            a, b = pr.C[k][0], pr.C[k][1]; shifts[k] = (still_shift(a), still_shift(b), progress(k))
        (la, ga), (lb, gb), pg = shifts[k]; w = float(pg[min(j, len(pg) - 1)])
        f = colour_fix(f, la + w * (lb - la), ga + w * (gb - ga))
        z = BASE * zoom(t, acts); sc = (W / SW) * z; cx, cy = FOCUS[0] * SW, FOCUS[1] * SH
        M = np.float32([[sc, 0, W * FOCUS[0] - cx * sc], [0, sc, H * FOCUS[1] - cy * sc]])
        g = cv2.warpAffine(f, M, (W, H), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REPLICATE)
        p.stdin.write(g.tobytes()); used.append((round(t, 3), k, j))
    p.stdin.close(); p.wait()
    return used

# ---- overlays ----
CAP_Y, CAP_FS, MAXW = 1440, 114, 900
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
POST_GAIN, LIMIT = 0.6, 0.79
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
def mix(seg, fx, t1, out, voice_only=False):
    voice = 'audio/narr_tight.wav'; v_db = rms_db(voice)
    inputs = ['-i', voice]
    fc = [f"[0:a]aresample=48000,pan=stereo|c0=c0|c1=c0,apad=whole_dur={t1:.3f},atrim=0:{t1:.3f},asetpts=PTS-STARTPTS[v]"]
    parts = ['[v]']
    if not voice_only:
        bed = bed_loop(); g = v_db - BED_UNDER - rms_db(bed)
        inputs += ['-stream_loop', '-1', '-i', bed]
        fc.append(f"[1:a]aresample=48000,pan=stereo|c0=c0|c1=c0,atrim=0:{t1:.3f},asetpts=PTS-STARTPTS,volume={g:.2f}dB,"
                  f"afade=t=in:d=0.4,afade=t=out:st={max(0, t1 - 0.6):.3f}:d=0.6[bed]"); parts.append('[bed]')
        n = 2
        for k, s0, s1, v0, v1 in seg:                 # each clip's own sound where its picture is
            if s1 - s0 < 0.05: continue
            g = v_db - FX_UNDER - clip_level(k) + FX_OFF.get(k, 0.0); d = int(round(v0 * 1000)); L = s1 - s0
            inputs += ['-ss', f'{s0:.3f}', '-t', f'{L:.3f}', '-i', f'clips/{k}.mp4']
            fc.append(f"[{n}:a]aresample=48000,aformat=channel_layouts=stereo,afade=t=in:d=0.03,"
                      f"afade=t=out:st={max(0, L - 0.06):.3f}:d=0.06,volume={g:.2f}dB,adelay={d}|{d}[c{n}]")
            parts.append(f'[c{n}]'); n += 1
        g = v_db - FX_UNDER - rms_db('audio/tick.mp3') + TICK_OFF
        for lab, a, b, add in fx:                     # the counter's tick as the price drops into the pill
            d = int(round((a + ov.CHIP_IN + ov.CHIP_HOLD) * 1000))
            inputs += ['-i', 'audio/tick.mp3']
            fc.append(f"[{n}:a]aresample=48000,pan=stereo|c0=c0|c1=c0,atrim=0:0.12,volume={g:.2f}dB,adelay={d}|{d}[c{n}]")
            parts.append(f'[c{n}]'); n += 1
    fc.append(''.join(parts) + f"amix=inputs={len(parts)}:normalize=0:duration=first,atrim=0:{t1:.3f},"
              f"afade=t=out:st={max(0, t1 - 0.25):.3f}:d=0.25,"
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
    place = place_pilot(); seg = timemap(place, END); acts = [0.0] + [b for b in BUTS if b <= END]
    if acts[-1] < END - 1e-6: acts.append(END)
    print('time map (clip, source from, source to, video from, video to):')
    for s in seg: print(f'  {s[0]:5s} {s[1]:5.2f} {s[2]:5.2f}  {s[3]:6.2f} {s[4]:6.2f}' + ('  rest' if s[1] == s[2] else ''))
    for k, s0, sl, vl in place[1:]:
        print(f'  {k}: lands at {vl:.2f} s')
    used = render(seg, END, acts, 'work/pilot_raw.mp4')
    fx = ass_file(END, 'work/pilot.ass')
    mix(seg, fx, END, 'work/pilot_mix.wav'); mix(seg, fx, END, 'work/pilot_voice.wav', voice_only=True)
    run(['-i', 'work/pilot_raw.mp4', '-i', 'work/pilot_mix.wav', '-vf', 'ass=work/pilot.ass:fontsdir=fonts', '-c:v', 'libx264',
         '-crf', '18', '-pix_fmt', 'yuv420p', '-r', str(FPS), '-c:a', 'aac', '-b:a', '192k', '-shortest', 'work/pilot.mp4'])
    run(['-i', 'work/pilot_raw.mp4', '-i', 'work/pilot_voice.wav', '-vf', 'ass=work/pilot.ass:fontsdir=fonts', '-c:v', 'libx264',
         '-crf', '18', '-pix_fmt', 'yuv420p', '-r', str(FPS), '-c:a', 'aac', '-b:a', '192k', '-shortest', 'work/pilot_voiceonly.mp4'])
    natural([k for k, *_ in place], 'work/pilot_natural.mp4')
if MODE in ('pilot', 'pilot-sheets'):
    sheet('work/pilot.mp4', [(0.0, 'frame 0'), (0.5, ''), (1.0, ''), (2.0, '')], 'work/pilot_hook.jpg')
    marks = [(at('t-rex') + 0.3, '"T-REX"'), (at('steps') + 0.05, '"STEPS"'), (at('holes') + 0.2, '"HOLES"'),
             (at('posts') + 0.2, '"POSTS"'), (at('concrete') + 0.3, '"CONCRETE"'), (at('cable', after=at('thick')) + 0.25, '"CABLE"'),
             (fx[0][1] + 1.2, 'label, counter'), (END - 0.05, 'last frame')]
    sheet('work/pilot.mp4', marks, 'work/pilot_steps.jpg', cols=4)
    print('fixes:', [(lab, round(a, 2), round(b, 2), add) for lab, a, b, add in fx])
    print('loudness pilot (LUFS, true peak dBFS):', loudness('work/pilot.mp4'))
