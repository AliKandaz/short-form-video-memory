# Video 16, Gate D (21 Nov 2026): the two pilots as they will play in the edit, with the build format's overlays on them for
# the first time (the caption, a term label, the price counter), so the sizes in CLAUDE.md section 5 can be checked on a
# phone-sized sheet. No narration exists yet, so the word times are estimates (3.5 words a second) and the previews are silent.
# Run from the work dir: clips/C1.mp4, clips/C3.mp4 (the pilots), stills/FR6.png, stills/OU1.png, fonts/HBXCaption.ttf.
#   python3 16-gateD.py  ->  out/gateD_hook.mp4, out/gateD_flight.mp4, out/gateD_total.mp4,
#                            out/gateD_hook_frames.jpg (frames at 0, 0.5, 1 and 2 s: as rendered, and as the edit plays them),
#                            out/gateD_overlays.jpg (five frames at phone size with TikTok's covered areas marked)
# RAMP is new: the first seconds of the hook clip play faster and the rest slower, so the lit roof line lands earlier
# (kling lit the gable at 1.0 s and the whole roof edge at 1.8-2.0 s; at 1.4x that is 0.7 s and 1.4 s). PUSH as in 15-build.py.
import importlib.util, os, re, subprocess
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("ov", os.path.join(HERE, "16-overlays.py")); ov = importlib.util.module_from_spec(spec); spec.loader.exec_module(ov)
W, H, FPS = 1080, 1920, 30
CAP_Y, CAP_FS, MAXW = 1440, 114, 900
SHARP = "unsharp=5:5:0.6:5:5:0.0"
ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '16', '-pix_fmt', 'yuv420p', '-r', str(FPS), '-an']
for d in ('seg', 'out', 'tmp'): os.makedirs(d, exist_ok=True)
def run(args): subprocess.run(['ffmpeg', '-loglevel', 'error', '-y'] + args, check=True)
def dur(p): return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout)
ts = ov.ts

def est_words(text, a, b):
    """Word times spread over a..b by syllables, with a beat after punctuation (stands in for the narration's timings)."""
    toks = text.split(); wt = []
    for t in toks:
        syl = max(1, len(re.findall(r"[aeiouy]+", re.sub(r"e\b", "", t.lower()))) or 1)
        wt.append(syl + (0.9 if t[-1] in ",:." else 0.0))
    out = []; c = a; k = (b - a) / sum(wt)
    for t, w in zip(toks, wt):
        syl = w - (0.9 if t[-1] in ",:." else 0.0); out.append([round(c, 3), round(c + syl * k, 3), t]); c += w * k
    return out

CAPFONT = ImageFont.truetype('fonts/HBXCaption.ttf', round(CAP_FS * 1000 / 1219))
def cap(w): return re.sub(r"[^A-Za-z0-9'’\-]", "", w).upper()
def caption_events(words, t1):
    ev = []; prev_end = 0.0
    for i, (s, e, w) in enumerate(words):
        s = max(s, prev_end); nxt = words[i + 1][0] if i + 1 < len(words) else None
        end = nxt if (nxt is not None and nxt - e <= 0.35) else e + 0.18
        end = min(max(end, s + 0.12), t1); prev_end = end
        txt = cap(w); sc = min(100, int(100 * MAXW / max(CAPFONT.getlength(txt), 1)))
        ev.append(f"Dialogue: 2,{ts(s)},{ts(end)},Caption,,0,0,0,,{{\\an5\\pos(540,{CAP_Y})\\fscx{int(sc*0.92)}\\fscy{int(sc*0.92)}"
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
""" + ov.STYLES + """
[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

def zoom_xy(fx, fy):
    return (f"max(0,min(iw-iw/zoom,{fx/W}*iw-iw/zoom/2))", f"max(0,min(ih-ih/zoom,{fy/H}*ih-ih/zoom/2))")

def seg(name, src, L, ramp=None, push=None):
    """clips/<src> -> seg/<name>.mp4 at 1080x1920, L seconds. ramp=(t, speed): the clip's first t seconds play at that
    speed and the rest fills what is left of L. push=(focus x, focus y, zoom gained over the segment)."""
    c = dur(src)
    if ramp:
        a, s1 = ramp; s2 = (c - a) / (L - a / s1)
        pts = f"setpts='if(lt(T,{a}),T/{s1},{a / s1:.4f}+(T-{a})/{s2:.4f})/TB',"; note = f"first {a}s at {s1}x, rest at {s2:.2f}x"
    else:
        sp = c / L; pts = f"setpts=PTS/{sp:.4f},"; note = f"{sp:.3f}x"
    vf = (pts + f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},{SHARP},fps={FPS},"
          f"trim=duration={L:.3f},setpts=PTS-STARTPTS,setsar=1")
    run(['-i', src, '-vf', vf] + ENC + [f'seg/{name}.mp4'])
    if push:
        fx, fy, zz = push; n = max(2, round(L * FPS)); x, y = zoom_xy(fx, fy)
        run(['-i', f'seg/{name}.mp4', '-vf', f"scale={W*2}:{H*2},zoompan=z='1+{zz}*on/{n - 1}':x='{x}':y='{y}':d=1:s={W}x{H}:fps={FPS},setsar=1"]
            + ENC + [f'tmp/{name}_z.mp4'])
        os.replace(f'tmp/{name}_z.mp4', f'seg/{name}.mp4'); note += f", push-in to {1 + zz:.2f}x toward ({fx},{fy})"
    print(f"  {name}: {os.path.basename(src)} {c:.2f}s -> {L:.2f}s ({note})")

def still_seg(name, png, L, push):
    fx, fy, zz = push; n = round(L * FPS); x, y = zoom_xy(fx, fy)
    run(['-loop', '1', '-framerate', str(FPS), '-t', f'{L}', '-i', png, '-vf',   # 30 frames a second in, or zoompan runs short
         f"scale={W*2}:{H*2}:force_original_aspect_ratio=increase,crop={W*2}:{H*2},zoompan=z='1+{zz}*on/{n - 1}':x='{x}':y='{y}':d=1:s={W}x{H}:fps={FPS},setsar=1"]
        + ENC + [f'seg/{name}.mp4'])

def burn(name, events, out):
    open(f'tmp/{name}.ass', 'w').write(ASS_HEAD + "\n".join(events) + "\n")
    run(['-i', f'seg/{name}.mp4', '-vf', f'ass=tmp/{name}.ass:fontsdir=fonts', '-c:v', 'libx264', '-preset', 'medium', '-crf', '18',
         '-pix_fmt', 'yuv420p', '-r', str(FPS), '-an', '-movflags', '+faststart', out])

def frame(video, t, size=None):
    run(['-ss', f'{t:.3f}', '-i', video, '-frames:v', '1', 'tmp/_f.png']); im = Image.open('tmp/_f.png').convert('RGB')
    return im.resize(size, Image.LANCZOS) if size else im

# ---- the hook (C1): "If you clip one string of lights to your gutter, you have a Christmas light show." ----
L1 = 4.6
seg('C1', 'clips/C1.mp4', L1, ramp=(2.0, 1.4), push=(560, 900, 0.17))   # 3.7% a second: camera_path.py counts 3% and up as moving;
                                                                          # the focus keeps the dog above the caption
w1 = est_words("If you clip one string of lights to your gutter, you have a Christmas light show.", 0.0, L1 - 0.1)
burn('C1', caption_events(w1, L1) + ov.bill_events({'start': 3, 'steps': [], 'final': None, 'end': L1}, 0, L1), 'out/gateD_hook.mp4')

# ---- the flight (C3): "So you swap every bulb for an LED: the same glow, on about a tenth of the power." ----
L3 = 5.1
seg('C3', 'clips/C3.mp4', L3)
w3 = est_words("So you swap every bulb for an LED: the same glow, on about a tenth of the power.", 0.05, L3 - 0.1)
t_led = max(next(w[0] for w in w3 if w[2].startswith('LED')), 3.3)   # the label waits for its picture: the camera reaches
burn('C3', caption_events(w3, L3) + ov.label_events([("LED", t_led, w3[-1][1] + 0.1)], 0, L3)   # the bulb at ~3.3 s of the clip
     + ov.bill_events({'start': 3, 'steps': [(w3[0][0], 305)], 'final': None, 'end': L3}, 0, L3), 'out/gateD_flight.mp4')

# ---- the closing total, on the finished build's still (the clip isn't rendered yet) ----
L6 = 3.6
still_seg('FR6', 'stills/FR6.png', L6, (540, 900, 0.05))
w6 = est_words("That's your light show. The bill: about two thousand dollars,", 0.0, L6 - 0.1)
t_bill = next(w[0] for w in w6 if w[2] == 'The')
burn('FR6', caption_events(w6, L6) + ov.bill_events({'start': 2107, 'steps': [], 'final': t_bill, 'end': L6}, 0, L6), 'out/gateD_total.mp4')

# ---- the longest label, on the outlet's still ----
L4 = 2.0
still_seg('OU1', 'stills/OU1.png', L4, (540, 900, 0.03))
w4 = est_words("This is a ground-fault outlet.", 0.1, 1.6)
burn('OU1', caption_events(w4, L4) + ov.label_events([("GROUND-FAULT\\NOUTLET", 0.1, 1.9)], 0, L4)
     + ov.bill_events({'start': 308, 'steps': [], 'final': None, 'end': L4}, 0, L4), 'tmp/gateD_label2.mp4')

# ---- sheet 1: the hook's frames at 0, 0.5, 1 and 2 s ----
F = ImageFont.truetype('fonts/HBXCaption.ttf', 30); FS = ImageFont.truetype('fonts/HBXCaption.ttf', 22)
TW, TH = 432, 768; PAD, HEAD = 14, 64
sheet = Image.new('RGB', (4 * TW + 5 * PAD, 2 * (TH + HEAD) + PAD), (16, 26, 51)); d = ImageDraw.Draw(sheet)
rows = (("AS RENDERED (kling4_0, 4 s)", 'clips/C1.mp4'), ("AS THE EDIT PLAYS IT (first 2 s at 1.4x, slow push-in, overlays)", 'out/gateD_hook.mp4'))
for r, (title, vid) in enumerate(rows):
    y0 = r * (TH + HEAD) + PAD; d.text((PAD, y0 + 2), title, font=F, fill=(255, 214, 46))
    for i, t in enumerate((0.0, 0.5, 1.0, 2.0)):
        x0 = PAD + i * (TW + PAD); sheet.paste(frame(vid, t, (TW, TH)), (x0, y0 + HEAD - 14))
        d.rectangle([x0, y0 + HEAD - 14, x0 + 96, y0 + HEAD + 22], fill=(16, 26, 51)); d.text((x0 + 8, y0 + HEAD - 10), f"{t:.1f} s", font=FS, fill=(255, 255, 255))
sheet.save('out/gateD_hook_frames.jpg', quality=90)

# ---- sheet 2: the overlays at phone size, with the areas TikTok covers marked ----
def guides(im):
    o = Image.new('RGBA', im.size, (0, 0, 0, 0)); g = ImageDraw.Draw(o); sx = im.size[0] / W; sy = im.size[1] / H
    for box in ((0, 0, W, 0.09 * H), (0, 0.80 * H, W, H), (940, 950, W, 0.80 * H)):
        g.rectangle([box[0] * sx, box[1] * sy, box[2] * sx, box[3] * sy], fill=(255, 60, 60, 70), outline=(255, 90, 90, 200))
    return Image.alpha_composite(im.convert('RGBA'), o).convert('RGB')
shots = (("hook at 1.2 s", 'out/gateD_hook.mp4', 1.2), ("the price slides in", 'out/gateD_flight.mp4', w3[0][0] + 0.45),
         ("label + new total", 'out/gateD_flight.mp4', t_led + 1.0), ("longest label, 2 lines", 'tmp/gateD_label2.mp4', 1.2),
         ("the closing total", 'out/gateD_total.mp4', L6 - 0.4))
PW, PH = 405, 720
sheet = Image.new('RGB', (len(shots) * PW + (len(shots) + 1) * PAD, PH + HEAD + PAD + 40), (16, 26, 51)); d = ImageDraw.Draw(sheet)
for i, (title, vid, t) in enumerate(shots):
    x0 = PAD + i * (PW + PAD); d.text((x0, PAD + 6), title, font=FS, fill=(255, 214, 46))
    sheet.paste(guides(frame(vid, t, (PW, PH))), (x0, HEAD))
d.text((PAD, HEAD + PH + 8), "Red = covered by TikTok (tabs above 9%, caption and sound below 80%, buttons right of x 940). Each frame is shown at about phone size.",
       font=FS, fill=(255, 255, 255))
sheet.save('out/gateD_overlays.jpg', quality=90)
print("t_led", t_led, "t_bill", t_bill, "| done")
