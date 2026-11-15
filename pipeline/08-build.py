# Video 08 (C1 sewer trap), the first Cutaway video under the 15 Nov 2026 rules (3.4). Assemble: clip segments and holds -> clean
# master -> sound (voice + bed + effects) -> pointers and one-word captions. Runs locally (ffmpeg with libass, numpy, Pillow).
# Work dir: plan.json + timeline.json (08-timing.py), audio/narration_tight.wav, audio/words_tight.json, audio/bed.mp3,
# audio/fx_*.mp3, clips/<SEG>.mp4 (kling, 720p), fonts/HBXCaption.ttf (Montserrat 800, family renamed "HBX Caption").
# Usage: python3 08-build.py              -> out/final.mp4 (+ out/final_voiceonly.mp4, out/final_clean.mp4)
#        python3 08-build.py P1,H1 C11,H3 -> out/preview.mp4: each argument is a run of consecutive segments, rendered with its own
#                                          slice of the sound and captions, joined by 0.4 s of black.
# Rules carried in code: a clip plays at 0.8x-1.15x to fit its segment (a 3 s clip over a ~2 s line plays whole, up to 2x), then is
# trimmed at the end (or holds its last frame with a slow push-in); a hold is the last frame of the clip before, 3 s at most, with a
# slow push-in toward a point, and the clip after it eases back out from that zoom; no cross-fades between different pictures;
# clips are sharpened after the 720p upscale (unsharp 5:5:0.6, 7.5); captions ALL CAPS ~57 px at y 1440.
import json, math, os, re, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw
W, H, FPS = 1080, 1920, 30
CAP_Y, CAP_FS, MAXW = 1440, 114, 900   # 130 measured 65 px letters with this font; 114 -> ~57 px (Rule 5)
SHARP = "unsharp=5:5:0.6:5:5:0.0"
ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '16', '-pix_fmt', 'yuv420p', '-r', str(FPS), '-an']
PLAN = json.load(open('plan.json')); SEG = {s['seg']: s for s in PLAN['segments']}; ORDER = [s['seg'] for s in PLAN['segments']]
TOTAL = PLAN['total']
for d in ('seg', 'out', 'tmp'): os.makedirs(d, exist_ok=True)
def run(args): subprocess.run(['ffmpeg', '-loglevel', 'error', '-y'] + args, check=True)
def dur(p): return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout)

# Holds: (focus x, focus y in 1080x1920 frame, zoom gain over the hold, ring (x, y, r) or None)
HOLDS = {"H1": (480, 672, 0.18, (480, 672, 78)),      # B5 "The water in your toilet bowl is one too": the toilet's water seal
         "H2": (506, 359, 0.20, None),                # B9 "That's the pipe sticking out of your roof": the vent, in C4's roof framing
         "H3": (550, 810, 0.10, (550, 810, 105))}      # B22 "This is a rat blocker": the flap in the close-up
# Clips whose end frame matters (a keyframe the next segment continues from): fit by speed, never trim the end
KEEP_END = {"P1", "C3", "C4", "C5", "C7", "C8", "C9", "C11", "C12"}
# A 3 s clip over a ~2 s line: play the whole clip faster (C6 1.46x, C10 1.69x). Trimming its start instead (the first cut of this
# video) made a visible jump from the end of the clip before, because the first frames are where the camera move begins.
FULLFIT = {"C6", "C10"}
# The clip after a hold starts at the hold's last zoom and focus and eases back to its own framing over EASE_S, so the camera
# pulls back instead of snapping back (the first cut had a jump at each of the three).
EASE_AFTER = {"C3": "H1", "C5": "H2", "C12": "H3"}
EASE_S = 0.8

def zoom_xy(fx, fy):
    return (f"max(0,min(iw-iw/zoom,{fx/W}*iw-iw/zoom/2))", f"max(0,min(ih-ih/zoom,{fy/H}*ih-ih/zoom/2))")

def seg_clip(name):
    s = SEG[name]; L = s['len']; p = f'clips/{name}.mp4'; c = dur(p); r = c / L
    lo, hi = (0.8, 2.0) if name in FULLFIT else (0.8, 1.15) if name in KEEP_END else (0.8, 1.25)
    speed = min(max(r, lo), hi); played = c / speed
    vf = f"setpts=PTS/{speed:.4f},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},{SHARP},fps={FPS}"
    if name in EASE_AFTER:   # smoothstep from the hold's final zoom back to 1.0
        h = EASE_AFTER[name]; fx, fy, zz, _ = HOLDS[h]; nh = max(1, round(SEG[h]['len'] * FPS)); z0 = 1 + zz * (nh - 1) / nh
        N = round(EASE_S * FPS); x, y = zoom_xy(fx, fy)
        vf += (f",zoompan=z='if(lt(on,{N}),1+{z0-1:.5f}*(1-(3*pow(on/{N},2)-2*pow(on/{N},3))),1)'"
               f":x='{x}':y='{y}':d=1:s={W}x{H}:fps={FPS}")
    pad = max(0.0, L - played)
    if pad > 0.02:   # hold the last frame with a slow push-in so it never looks frozen
        n = round(L * FPS)
        vf += (f",tpad=stop_mode=clone:stop_duration={pad+0.1:.3f},scale={W*2}:{H*2},"
               f"zoompan=z='1+0.04*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS}")
    vf += f",trim=duration={L:.3f},setpts=PTS-STARTPTS,setsar=1"
    print(f'  {name}: clip {c:.2f}s -> {L:.2f}s at {speed:.3f}x' + (f', trims {played-L:.2f}s' if played > L + 0.02 else '')
          + (f', holds {pad:.2f}s' if pad > 0.02 else ''))
    run(['-i', p, '-vf', vf] + ENC + [f'seg/{name}.mp4'])

def last_frame(name):
    p = f'tmp/last_{name}.png'
    run(['-sseof', '-0.08', '-i', f'seg/{name}.mp4', '-frames:v', '1', '-update', '1', p]); return p

def ring_png(src, x, y, r, out):
    im = Image.open(src).convert('RGB'); d = ImageDraw.Draw(im, 'RGBA')
    for k, a in ((10, 70), (6, 110)):   # soft dark shadow under the ring
        d.ellipse([x - r - k + 4, y - r - k + 6, x + r + k + 4, y + r + k + 6], outline=(0, 0, 0, a), width=16 + 2 * k)
    d.ellipse([x - r, y - r, x + r, y + r], outline=(255, 255, 255, 255), width=16)
    im.save(out); return out

def seg_hold(name, prev):
    s = SEG[name]; L = s['len']; fx, fy, zz, ring = HOLDS[name]; base = last_frame(prev); n = max(1, round(L * FPS))
    z = f"1.0+{zz}*on/{n}"; x, y = zoom_xy(fx, fy)
    zp = f"scale={W*2}:{H*2},zoompan=z='{z}':x='{x}':y='{y}':d=1:s={W}x{H}:fps={FPS},trim=duration={L:.3f},setsar=1"
    if ring:   # the same picture with the ring fades in over 0.25 s (not a fade between two pictures), then the push-in
        rp = ring_png(base, *ring, f'tmp/ring_{name}.png')
        run(['-loop','1','-framerate',str(FPS),'-t',f'{L+0.3:.3f}','-i',base,'-loop','1','-framerate',str(FPS),'-t',f'{L+0.3:.3f}',
             '-i',rp,'-filter_complex',f"[0:v][1:v]xfade=transition=fade:duration=0.25:offset=0.15,{zp}[v]",'-map','[v]'] + ENC
            + [f'seg/{name}.mp4'])
    else:
        run(['-loop','1','-framerate',str(FPS),'-t',f'{L+0.3:.3f}','-i',base,'-vf',zp] + ENC + [f'seg/{name}.mp4'])
    print(f'  {name}: hold {L:.2f}s on the last frame of {prev}' + (' + ring' if ring else ''))

# ---- sound: voice + bed + effects (3.4 "Sound under the voice"; 3.3 Step 9) ----
def rms_db(path):
    # Level of the mono fold-down (L+R)/2: what one phone speaker plays and what under_the_voice.py measures. A stereo bed is up to
    # 3 dB quieter here than in each channel, so levels set this way read as set in that check.
    ch = int(subprocess.run(['ffprobe','-v','error','-select_streams','a:0','-show_entries','stream=channels','-of','csv=p=0',path],
                            capture_output=True, text=True).stdout.strip())
    a = np.frombuffer(subprocess.run(['ffmpeg','-loglevel','error','-i',path,'-ar','22050','-f','f32le','-'],
                                     capture_output=True).stdout, np.float32)
    a = a[:len(a) // ch * ch].reshape(-1, ch).mean(1)
    fr = a[:len(a)//1102*1102].reshape(-1, 1102); e = np.sqrt((fr**2).mean(1) + 1e-12)
    act = e[e > e.max() * 0.1]   # loud frames only (ignores silence before and after a sound)
    return 20 * np.log10(np.sqrt((act**2).mean()))
WORDS = json.load(open('audio/words_tight.json'))
NORM = [re.sub(r"[^a-z0-9']", "", w[2].lower()) for w in WORDS]
TL = json.load(open('timeline.json')); BT = {b['beat']: b for b in TL['beats']}
def at(beat, word=None, off=0.0):
    if word is None: return max(0.0, BT[beat]['start'] + off)
    i = next(j for j in range(BT[beat]['first_word'], len(NORM)) if NORM[j] == word); return WORDS[i][0] + off
FX = [("fx_tap", at("B1", off=0.05)), ("fx_flush", at("B6", "flushes", -0.25)), ("fx_gurgle", at("B7", "sucks", -0.05)),
      ("fx_tap", at("B13", "run", -0.1)), ("fx_fan", at("B16", "fans", -0.1)), ("fx_rat", at("B19", "swims", 0.0)),
      ("fx_rat", at("B20", "pops", -0.05)), ("fx_flap", at("B21", "drops", 0.05)), ("fx_flap", at("B23", "hits", 0.0))]
BED_UNDER, FX_UNDER = 19.0, 11.0      # dB under the voice (approved starting points, 3.4)

def mix(t0, t1, out, voice_only=False):
    voice = 'audio/narration_tight.wav'; v_db = rms_db(voice); T = t1 - t0
    # The voice is mono; copy it to both channels so the mix stays stereo and the bed and effects keep their width (the first cut
    # mixed down to mono because amix followed the voice's layout).
    inputs = ['-i', voice]; fc = [f"[0:a]aresample=48000,pan=stereo|c0=c0|c1=c0,apad=whole_dur={TOTAL:.3f},atrim={t0:.3f}:{t1:.3f},"
                                  f"asetpts=PTS-STARTPTS[v]"]
    parts = ['[v]']
    if not voice_only:
        g = v_db - BED_UNDER - rms_db('audio/bed.mp3')
        inputs += ['-stream_loop', '-1', '-i', 'audio/bed.mp3']
        fc.append(f"[1:a]aresample=48000,aformat=channel_layouts=stereo,atrim={t0:.3f}:{t0+T:.3f},asetpts=PTS-STARTPTS,volume={g:.2f}dB,"
                  f"afade=t=in:d=0.6,afade=t=out:st={max(0,T-0.8):.3f}:d=0.8[bed]"); parts.append('[bed]')
        k = 2
        for name, t in FX:
            if not (t0 - 0.5 <= t < t1): continue
            g = v_db - FX_UNDER - rms_db(f'audio/{name}.mp3'); d_ms = int(max(0, t - t0) * 1000)
            inputs += ['-i', f'audio/{name}.mp3']
            fc.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=stereo,volume={g:.2f}dB,adelay={d_ms}|{d_ms}[f{k}]")
            parts.append(f'[f{k}]'); k += 1
    fc.append(''.join(parts) + f"amix=inputs={len(parts)}:normalize=0:duration=first,atrim=0:{T:.3f},"
              f"loudnorm=I=-14:TP=-1.5:LRA=11,volume=2.6dB,alimiter=limit=0.84:level=false,aresample=48000[a]")
    run(inputs + ['-filter_complex', ';'.join(fc), '-map', '[a]', '-ac', '2', '-c:a', 'pcm_s16le', out])

# ---- captions and pointers (ASS) ----
from PIL import ImageFont
CAPFONT = ImageFont.truetype('fonts/HBXCaption.ttf', round(CAP_FS * 1000 / 1219))   # libass Fontsize -> em for Montserrat
def ts(t):
    t = max(0, t); h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"
def cap(w): return re.sub(r"[^A-Za-z0-9'’\-]", "", w).upper()
def arrow_path(ang, L=200, Hh=92):
    # solid arrow pointing at angle ang (degrees, 0 = right, 90 = down), rotated in Python and shifted to positive coordinates
    pts = [(0, 30), (125, 30), (125, 0), (L, Hh / 2), (125, Hh), (125, 62), (0, 62)]
    pts = [(x - L / 2, y - Hh / 2) for x, y in pts]; a = math.radians(ang)
    rp = [(x * math.cos(a) - y * math.sin(a), x * math.sin(a) + y * math.cos(a)) for x, y in pts]
    mx = min(p[0] for p in rp); my = min(p[1] for p in rp); rp = [(x - mx, y - my) for x, y in rp]
    w = max(p[0] for p in rp); h = max(p[1] for p in rp)
    d = 'm ' + ' l '.join(f'{x:.0f} {y:.0f}' for x, y in rp)
    return d, w, h
# Arrows on clips that keep the camera still: (beat, from (x,y), to (x,y), angle). Three arrows slide along the flow, 0.35 s apart.
ARROWS = [("B7", (340, 430), (340, 930), 90), ("B16", (300, 950), (515, 660), -53)]   # B16 in C7's 1.35x bathroom framing: floor drain -> fan

def events(t0, t1):
    ev = []
    words = [w for w in WORDS if t0 - 0.01 <= w[0] < t1]; prev_end = t0
    for i, (s, e, w) in enumerate(words):
        s = max(s, prev_end); nxt = words[i + 1][0] if i + 1 < len(words) else None
        end = nxt if (nxt is not None and nxt - e <= 0.35) else e + 0.18
        end = min(max(end, s + 0.12), t1); prev_end = end
        txt = cap(w); wpx = CAPFONT.getlength(txt); sc = min(100, int(100 * MAXW / max(wpx, 1)))
        ev.append(f"Dialogue: 2,{ts(s-t0)},{ts(end-t0)},Caption,,0,0,0,,{{\\an5\\pos(540,{CAP_Y})\\fscx{int(sc*0.92)}\\fscy{int(sc*0.92)}"
                  f"\\t(0,70,\\fscx{sc}\\fscy{sc})}}{txt}")
    for beat, (x0, y0), (x1, y1), ang in ARROWS:
        b0, b1 = BT[beat]['start'] + 0.15, BT[beat]['end'] - 0.1
        if b1 <= t0 or b0 >= t1: continue
        path, aw, ah = arrow_path(ang); k = 0; t = b0
        while t + 0.9 <= b1:
            a0 = t - t0; a1 = a0 + 1.0
            ev.append(f"Dialogue: 1,{ts(a0)},{ts(a1)},Pointer,,0,0,0,,{{\\an7\\move({x0-aw/2:.0f},{y0-ah/2:.0f},{x1-aw/2:.0f},{y1-ah/2:.0f})"
                      f"\\fad(180,220)\\p1}}{path}{{\\p0}}")
            k += 1; t = b0 + 0.35 * k
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

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

def render(run_segs, tag):
    t0 = SEG[run_segs[0]]['start']; t1 = SEG[run_segs[-1]]['end']
    print(f'{tag}: {"+".join(run_segs)}  {t0:.2f}-{t1:.2f}s')
    prev = ORDER[ORDER.index(run_segs[0]) - 1] if ORDER.index(run_segs[0]) > 0 else None
    for name in run_segs:
        if name.startswith('H'):
            assert prev and os.path.exists(f'seg/{prev}.mp4'), f'{name} needs seg/{prev}.mp4'
            seg_hold(name, prev)
        else: seg_clip(name)
        prev = name
    with open(f'tmp/{tag}_list.txt', 'w') as f:
        for name in run_segs: f.write(f"file '../seg/{name}.mp4'\n")
    run(['-f','concat','-safe','0','-i',f'tmp/{tag}_list.txt','-c','copy',f'tmp/{tag}_clean.mp4'])
    mix(t0, t1, f'tmp/{tag}_mix.wav'); mix(t0, t1, f'tmp/{tag}_voice.wav', voice_only=True)
    open(f'tmp/{tag}.ass', 'w').write(ASS_HEAD + "\n".join(events(t0, t1)) + "\n")
    for audio, suffix in ((f'tmp/{tag}_mix.wav', ''), (f'tmp/{tag}_voice.wav', '_voiceonly')):
        run(['-i',f'tmp/{tag}_clean.mp4','-i',audio,'-vf',f'ass=tmp/{tag}.ass:fontsdir=fonts','-c:v','libx264','-preset','medium',
             '-crf','18','-pix_fmt','yuv420p','-r',str(FPS),'-c:a','aac','-b:a','192k','-movflags','+faststart','-shortest',
             f'tmp/{tag}{suffix}.mp4'])
    run(['-i',f'tmp/{tag}_clean.mp4','-i',f'tmp/{tag}_mix.wav','-c:v','copy','-c:a','aac','-b:a','192k','-shortest',
         f'tmp/{tag}_cleanmaster.mp4'])   # the clean master (no text) carries the full sound, for re-captioning elsewhere
    return f'tmp/{tag}.mp4', f'tmp/{tag}_voiceonly.mp4', f'tmp/{tag}_cleanmaster.mp4'

if __name__ == '__main__':
    runs = [a.split(',') for a in sys.argv[1:]] or [ORDER]
    outs = [render(r, f'part{i}') for i, r in enumerate(runs)]
    name = 'final' if not sys.argv[1:] else 'preview'
    if len(outs) == 1:
        for src, suf in zip(outs[0], ('', '_voiceonly', '_clean')): os.replace(src, f'out/{name}{suf}.mp4')
    else:   # join previews with 0.4 s of black
        run(['-f','lavfi','-i',f'color=black:s={W}x{H}:r={FPS}:d=0.4','-f','lavfi','-i','anullsrc=r=48000:cl=stereo','-t','0.4',
             '-c:v','libx264','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-shortest','tmp/black.mp4'])
        with open('tmp/join.txt','w') as f:
            for i, (o, _, _) in enumerate(outs):
                if i: f.write("file 'black.mp4'\n")
                f.write(f"file '{os.path.basename(o)}'\n")
        run(['-f','concat','-safe','0','-i','tmp/join.txt','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p',
             '-c:a','aac','-b:a','192k','-movflags','+faststart',f'out/{name}.mp4'])
    print('done:', name, round(dur(f'out/{name}.mp4'), 2), 's')
