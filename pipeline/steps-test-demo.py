# Build-steps test: the demo edit. Each version is re-timed so that every build step lands on the word that names it, with our
# one-word captions (estimated word times: there is no narration), a slow push-in on the locked view, and the stage-to-stage
# colour drift of the stills taken out. Silent. A second file plays both versions at natural speed with the models' own sound.
#   python3 steps-test-demo.py <dir with stills/ clips/ work/> <fonts dir with HBXCaption.ttf>
#   -> work/demo_timed.mp4 (A then B), work/demo_natural_sound.mp4 (A then B), work/demo_sheet.jpg
import subprocess, sys
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont
D, FONTS = sys.argv[1], sys.argv[2]
W, H, FPS = 1080, 1920, 30
SENT = "So you drop in a slab, stand up four walls, lower on a roof, and paint it red."
def word_times(sent, comma=0.20):
    t, out = 0.0, []
    for w in sent.split():
        letters = sum(ch.isalpha() for ch in w); d = 0.10 + 0.055 * letters
        out.append((w.strip(",.").upper(), t, t + d)); t += d + (comma if w.endswith(",") else 0.0)
    return out
WORDS = word_times(SENT); WT = {w: (a, b) for w, a, b in WORDS}
END = 6.8
# (clip, source from, source to, video from, video to): each step lands on its word ("SLAB" 1.16 s, "WALLS" 2.59-2.96, "ROOF" 3.90,
# "PAINT IT RED" 4.69-5.54). Source times were read off the clips (steps-test-check.py and its sheets).
A = [("W1", 0.00, 0.23, 0.00, 0.89), ("W1", 0.23, 0.50, 0.89, 1.16), ("W1", 0.50, 1.90, 1.16, 1.72),
     ("W2", 0.15, 2.05, 1.72, 2.96), ("W2", 2.05, 2.30, 2.96, 3.20),
     ("W3", 0.00, 0.37, 3.20, 3.57), ("W3", 0.37, 0.80, 3.57, 3.95), ("W3", 0.80, 2.00, 3.95, 4.55),
     ("W4", 0.00, 0.10, 4.55, 4.685), ("W4", 0.10, 0.80, 4.685, 5.40), ("W4", 0.80, 1.40, 5.40, 6.00), ("W4", 1.40, 1.97, 6.00, END)]
B = [("K1", 0.00, 0.25, 0.00, 0.69), ("K1", 0.25, 0.75, 0.69, 1.19), ("K1", 0.75, 1.36, 1.19, 2.40),
     ("K1", 1.36, 1.90, 2.40, 2.94), ("K1", 1.90, 2.38, 2.94, 3.55), ("K1", 2.38, 2.80, 3.55, 3.97),
     ("K1", 2.80, 3.22, 3.97, 4.685), ("K1", 3.22, 3.66, 4.685, 5.27), ("K1", 3.66, 4.15, 5.27, 5.76), ("K1", 4.15, 5.00, 5.76, END)]
def load(key):
    cap = cv2.VideoCapture(f"{D}/clips/{key}.mp4"); fps = cap.get(cv2.CAP_PROP_FPS); F = []
    while True:
        ok, f = cap.read()
        if not ok: break
        F.append(f)
    return fps, F
CL = {k: load(k) for k in ("W1", "W2", "W3", "W4", "K1")}
# colour: every edit of a still came back a little lighter and less yellow (lawn L 173 -> 189, b 160 -> 139 over four edits), so
# each frame is shifted back to the first still's lawn (on green pixels) and pale ground (elsewhere), read from two patches the
# build never covers
LAWN, GROUND = (0.03, 0.28, 0.13, 0.45), (0.10, 0.90, 0.90, 0.98)
def patch(lab, box):
    h, w = lab.shape[:2]; x0, y0, x1, y1 = box
    return lab[int(y0 * h):int(y1 * h), int(x0 * w):int(x1 * w)].reshape(-1, 3).mean(0)
REF = cv2.cvtColor(cv2.resize(cv2.imread(f"{D}/stills/S0B.png"), (720, 1276), interpolation=cv2.INTER_AREA), cv2.COLOR_BGR2LAB).astype(np.float32)
RL, RG = patch(REF, LAWN), patch(REF, GROUND)
def fix(f):
    lab = cv2.cvtColor(f, cv2.COLOR_BGR2LAB).astype(np.float32)
    sl, sg = RL - patch(lab, LAWN), RG - patch(lab, GROUND)
    wgt = np.clip((132.0 - cv2.GaussianBlur(lab[..., 1], (0, 0), 3)) / 10.0, 0, 1)[..., None]      # 1 on grass and hedge, 0 elsewhere
    lab += wgt * sl + (1 - wgt) * sg
    return cv2.cvtColor(np.clip(lab, 0, 255).astype(np.uint8), cv2.COLOR_LAB2BGR)
def render(segs, out, zoom=0.07, focus=(0.5, 0.50)):
    n = int(round(END * FPS)); p = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}",
        "-r", str(FPS), "-i", "-", "-vf", "unsharp=5:5:0.6:5:5:0.0", "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
    keep = []
    for i in range(n):
        t = i / FPS; seg = next((s for s in segs if s[3] <= t < s[4]), segs[-1]); key, s0, s1, v0, v1 = seg
        fps, F = CL[key]; ts = s0 + (s1 - s0) * (t - v0) / (v1 - v0); j = min(len(F) - 1, max(0, int(round(ts * fps))))
        f = F[j]            # the nearest source frame, never a blend of two: a blend doubles a part that is moving fast
        f = fix(cv2.resize(f, (720, 1276), interpolation=cv2.INTER_AREA))
        z = 1 + zoom * t / END; cx, cy = focus[0] * 720, focus[1] * 1276; sc = (W / 720) * z
        M = np.float32([[sc, 0, W / 2 - cx * sc + (cx * W / 720 - W / 2) * 0.0], [0, sc, H / 2 - cy * sc]])
        M[0, 2] = W * focus[0] - cx * sc; M[1, 2] = H * focus[1] - cy * sc                                     # keep the focus point where it is
        g = cv2.warpAffine(f, M, (W, H), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REPLICATE)
        p.stdin.write(g.tobytes()); keep.append(g if i % 3 == 0 else None)
    p.stdin.close(); p.wait(); return keep
def ts(t):
    return f"{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}"
def ass(tag, path):
    font = ImageFont.truetype(f"{FONTS}/HBXCaption.ttf", 114); ev = []
    for i, (w, a, b) in enumerate(WORDS):
        e = WORDS[i + 1][1] if i + 1 < len(WORDS) else b + 0.5
        sc = min(100, int(100 * 900 / max(font.getlength(w) * 1000 / 1219 * 114 / 114, 1)))
        ev.append(f"Dialogue: 1,{ts(a)},{ts(e)},Caption,,0,0,0,,{{\\an5\\pos(540,1440)\\fscx{sc}\\fscy{sc}}}{w}")
    ev.append(f"Dialogue: 0,{ts(0)},{ts(END)},Tag,,0,0,0,,{{\\an8\\pos(540,196)}}{tag}")
    open(path, "w").write("[Script Info]\nScriptType: v4.00+\nPlayResX: 1080\nPlayResY: 1920\nWrapStyle: 2\n\n[V4+ Styles]\n"
        "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, "
        "ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n"
        "Style: Caption,HBX Caption,114,&H00FFFFFF,&H00FFFFFF,&H00000000,&H8C000000,0,0,0,0,100,100,0,0,1,7,5,5,60,60,0,1\n"
        "Style: Tag,HBX Caption,46,&H002ED6FF,&H002ED6FF,&H00000000,&H8C000000,0,0,0,0,100,100,0,0,1,4,2,8,40,40,0,1\n\n[Events]\n"
        "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n" + "\n".join(ev) + "\n")
def burn(src, sub, out):
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", src, "-vf", f"ass={sub}:fontsdir={FONTS}", "-c:v", "libx264", "-crf", "20",
                    "-pix_fmt", "yuv420p", "-r", str(FPS), out], check=True)
ka = render(A, f"{D}/work/a_raw.mp4"); kb = render(B, f"{D}/work/b_raw.mp4")
ass("A: ONE SHORT CLIP A STEP", f"{D}/work/a.ass"); ass("B: ALL FOUR STEPS IN ONE CLIP", f"{D}/work/b.ass")
burn(f"{D}/work/a_raw.mp4", f"{D}/work/a.ass", f"{D}/work/a.mp4"); burn(f"{D}/work/b_raw.mp4", f"{D}/work/b.ass", f"{D}/work/b.mp4")
open(f"{D}/work/cat.txt", "w").write(f"file '{D}/work/a.mp4'\nfile '{D}/work/b.mp4'\n")
subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{D}/work/cat.txt", "-c", "copy", f"{D}/work/demo_timed.mp4"], check=True)
# natural speed, the models' own sound: the four wan clips in a row, then the kling clip
ins, fc = [], []
for i, k in enumerate(("W1", "W2", "W3", "W4", "K1")):
    ins += ["-i", f"{D}/clips/{k}.mp4"]
    tag = "A: ONE SHORT CLIP A STEP (AS IT CAME, ITS OWN SOUND)" if k != "K1" else "B: ALL FOUR STEPS IN ONE CLIP (AS IT CAME, ITS OWN SOUND)"
    fc.append(f"[{i}:v]fps={FPS},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,"
              f"drawtext=fontfile={FONTS}/HBXCaption.ttf:text='{tag}':fontsize=30:fontcolor=0xFFD62E:borderw=3:bordercolor=black:x=(w-text_w)/2:y=190[v{i}];"
              f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo[a{i}]")
fc.append("".join(f"[v{i}][a{i}]" for i in range(5)) + "concat=n=5:v=1:a=1[v][a]")
subprocess.run(["ffmpeg", "-loglevel", "error", "-y"] + ins + ["-filter_complex", ";".join(fc), "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "21",
                "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", f"{D}/work/demo_natural_sound.mp4"], check=True)
# a sheet for the chat: both versions at the same moments
marks = [0.6, 1.0, 1.2, 2.2, 2.9, 3.8, 4.0, 5.0, 5.6, 6.5]; tw, th = 180, 320
sheet = Image.new("RGB", (len(marks) * tw, 2 * th + 2 * 30), (16, 26, 51)); dr = ImageDraw.Draw(sheet); f2 = ImageFont.truetype(f"{FONTS}/HBXCaption.ttf", 20)
for r, (name, src) in enumerate((("A: one short clip a step (wan2_7, 4 clips, 15.00 credits)", "a.mp4"), ("B: all four steps in one clip (kling4_0, 1 clip, 12.50 credits)", "b.mp4"))):
    cap = cv2.VideoCapture(f"{D}/work/{src}"); y = r * (th + 30); dr.text((8, y + 4), name, font=f2, fill=(255, 214, 46))
    for c, t in enumerate(marks):
        cap.set(cv2.CAP_PROP_POS_MSEC, t * 1000); ok, f = cap.read()
        sheet.paste(Image.fromarray(cv2.cvtColor(cv2.resize(f, (tw, th), interpolation=cv2.INTER_AREA), cv2.COLOR_BGR2RGB)), (c * tw, y + 30))
        dr.rectangle((c * tw, y + 30, c * tw + 50, y + 48), fill=(0, 0, 0)); dr.text((c * tw + 4, y + 32), f"{t:.1f}s", fill=(255, 255, 255))
sheet.save(f"{D}/work/demo_sheet.jpg", quality=90)
print("words", [(w, round(a, 2)) for w, a, b in WORDS]); print("done")
