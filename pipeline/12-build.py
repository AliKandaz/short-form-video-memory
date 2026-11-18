# Video 12 (V1 manhole covers), travelling camera (section 5 Rules 0-7). Assemble: 14 clips -> clean master -> sound (voice +
# street bed + effects) -> pointers pinned to the picture and one-word captions. Runs locally (ffmpeg with libass, numpy, opencv,
# Pillow). Work dir: plan.json + timeline.json (12-timing.py, take B x1.03), audio/narration_tight.wav, audio/words_tight.json,
# audio/bed_street.mp3, audio/fx*.mp3, clips/<SEG>.mp4 (kling, 720p), fonts/HBXCaption.ttf (Montserrat 800 renamed "HBX Caption").
# Usage: python3 12-build.py               -> out/final.mp4 (+ out/final_voiceonly.mp4, out/final_clean.mp4)
#        python3 12-build.py C1 C10        -> out/preview.mp4: each argument is a run of consecutive segments (comma-separated),
#                                            rendered with its own slice of the sound and captions, joined by 0.4 s of black.
# Made from 10-build.py. What changed: WHIP takes a direction, so the two far jumps slide vertically with vertical motion blur
# (C2 -> C3 dives from the smoking street down to the vault before the blast; C8 -> C9 flies from the blast up to HIGH); the sound
# list and the bed are this video's; no LIGHTS, no SPLICE yet. PUSH, PULL, FULLFIT and POINTERS are set from the rendered clips.
import json, math, os, re, subprocess, sys
import numpy as np
import cv2
from PIL import ImageFont
W, H, FPS = 1080, 1920, 30
CAP_Y, CAP_FS, MAXW = 1440, 114, 900   # 114 -> ~57 px letters with this font (08, measured); Rule 5
SHARP = "unsharp=5:5:0.6:5:5:0.0"       # 720p clips after the upscale (7.5); the user chose 720p with the light sharpen
ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '16', '-pix_fmt', 'yuv420p', '-r', str(FPS), '-an']
PLAN = json.load(open('plan.json')); SEG = {s['seg']: s for s in PLAN['segments']}; ORDER = [s['seg'] for s in PLAN['segments']]
TOTAL = PLAN['total']
for d in ('seg', 'out', 'tmp'): os.makedirs(d, exist_ok=True)
def run(args): subprocess.run(['ffmpeg', '-loglevel', 'error', '-y'] + args, check=True)
def dur(p): return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout)

# A 3 s clip over a ~2 s line plays whole and faster (C2 1.32x), never trimmed (08: trimming made jumps).
FULLFIT = {"C2"}

# A clip whose middle went wrong is played as its clean start and clean end, joined by a fast whip down with motion blur
# (Rule 3 allows a whip in the edit), both parts slowed to fill the line. C8: both renders scrolled a second copy of the house
# up from under the ground between ~1.3 s and ~3.5 s; the first render (C8A, 7 s) has the longer clean ending.
# Video 10, C3 (the ice): from ~2.2 s to ~3.4 s of the render the counter behind the tub and the tub's side turned to soil (the
# cutaway leaking in again). The camera is still in that clip, so its clean start and end are joined by a short dissolve inside
# the one shot ("fade": it reads as the fog clearing), not a whip; the push-in from PUSH runs over the whole segment.
SPLICE = {}   # (source, clean parts, join s, whip|fade)

def seg_splice(name):
    s = SEG[name]; L = s['len']; src, parts, wd = SPLICE[name][:3]; kind = (SPLICE[name][3:] or ('whip',))[0]
    speed = sum(b - a for a, b in parts) / (L + wd * (len(parts) - 1))   # the join overlaps the two parts
    base = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},{SHARP},fps={FPS},setsar=1"
    for i, (a, b) in enumerate(parts):
        run(['-ss', f'{a:.3f}', '-to', f'{b:.3f}', '-i', src, '-vf', f"setpts=(PTS-STARTPTS)/{speed:.4f},{base}"] + ENC
            + [f'tmp/{name}_p{i}.mp4'])
    d0 = dur(f'tmp/{name}_p0.mp4')
    if kind == 'fade':
        fc = (f"[0:v][1:v]xfade=transition=fade:duration={wd}:offset={d0 - wd:.3f},"
              f"trim=duration={L:.3f},setpts=PTS-STARTPTS[v]")
    else:   # a whip down; fillborders hides xfade's junk edge on the first frame of the slide (see whip_join)
        win = f"between(t,{d0 - wd - 0.001:.3f},{d0:.3f})"
        fc = (f"[0:v][1:v]xfade=transition=slideup:duration={wd}:offset={d0 - wd:.3f},"
              f"fillborders=top=48:bottom=48:mode=smear:enable='{win}',"
              f"gblur=sigma=1:sigmaV=28:enable='between(t,{d0 - wd:.3f},{d0:.3f})',trim=duration={L:.3f},setpts=PTS-STARTPTS[v]")
    run(['-i', f'tmp/{name}_p0.mp4', '-i', f'tmp/{name}_p1.mp4', '-filter_complex', fc, '-map', '[v]'] + ENC + [f'seg/{name}.mp4'])
    print(f'  {name}: spliced {parts} of {src} at {speed:.3f}x with a {wd}s {kind} -> {L:.2f}s (got {dur(f"seg/{name}.mp4"):.2f}s)')

# Kling held the camera dead still in C7 (the side flash, 5 s; the prompt asked for a slow drift), so the edit adds the drift: a
# slow push-in toward the arc, and the clip after it starts at that zoom and eases back out (no jump at the cut; 08's EASE_AFTER).
# Kling held the camera still in C3 (the ice), C5 (the strawberry) and C17 (the crack), so the edit adds a slow push-in toward
# the change, and the clip after each starts at that zoom and eases back out. C19 (the closing wide) also came back still: PULL
# starts it zoomed in and pulls back to exactly the first frame's framing, so the loop lands on W0.
PUSH = {}        # (focus x, focus y, zoom gained): set for any clip Kling leaves with a still camera
PULL = {}        # (focus x, focus y, zoom at the start, back to 1.0 at the end)
EASE_AFTER = {}; EASE_S = 0.8

def zoom_xy(fx, fy):
    return (f"max(0,min(iw-iw/zoom,{fx/W}*iw-iw/zoom/2))", f"max(0,min(ih-ih/zoom,{fy/H}*ih-ih/zoom/2))")

def post_zoom(name):
    if name not in PUSH and name not in EASE_AFTER and name not in PULL: return
    n = max(2, round((SEG[name]['len'] + EXTRA.get(name, 0)) * FPS))
    if name in PUSH:
        fx, fy, zz = PUSH[name]; z = f"1+{zz}*on/{n - 1}"
    elif name in PULL:
        fx, fy, zz = PULL[name]; z = f"1+{zz}*(1-on/{n - 1})"
    else:
        fx, fy, zz = PUSH[EASE_AFTER[name]]; N = round(EASE_S * FPS)
        z = f"if(lt(on,{N}),1+{zz}*(1-(3*pow(on/{N},2)-2*pow(on/{N},3))),1)"
    x, y = zoom_xy(fx, fy)
    run(['-i', f'seg/{name}.mp4', '-vf', f"scale={W*2}:{H*2},zoompan=z='{z}':x='{x}':y='{y}':d=1:s={W}x{H}:fps={FPS},setsar=1"]
        + ENC + [f'tmp/{name}_z.mp4'])
    os.replace(f'tmp/{name}_z.mp4', f'seg/{name}.mp4')
    print(f'  {name}: ' + (f'push-in to {1+zz:.2f}x toward ({fx},{fy})' if name in PUSH else (f'pulls back from {1+zz:.2f}x' if name in PULL else f'eases back from {1+zz:.2f}x over {EASE_S}s')))

# Far jumps made in the edit (Rule 3): (seconds, xfade transition). slideup = the camera dives down; slidedown = it flies up.
WHIP = {("C2", "C3"): (0.3, "slideup"), ("C8", "C9"): (0.3, "slidedown")}
EXTRA = {}
for (a_, b_), (wd_, _k) in WHIP.items(): EXTRA[a_] = EXTRA.get(a_, 0) + wd_ / 2; EXTRA[b_] = EXTRA.get(b_, 0) + wd_ / 2
LIGHTS = {}

def lights(name):
    if name not in LIGHTS: return
    a, b = LIGHTS[name]
    d = f"between(t,{a:.2f},{b:.2f})+between(t,{b+0.08:.2f},{b+0.14:.2f})"
    run(['-i', f'seg/{name}.mp4', '-vf', f"eq=brightness='-0.30*({d})':saturation='1-0.45*({d})':gamma='1-0.25*({d})':eval=frame"]
        + ENC + [f'tmp/{name}_l.mp4'])
    os.replace(f'tmp/{name}_l.mp4', f'seg/{name}.mp4'); print(f'  {name}: lights off {a:.2f}-{b:.2f}s, flicker back on')

def seg_clip(name):
    seg_clip_raw(name); post_zoom(name); lights(name)

def whip_join(a, b, wd, out, kind="slideleft"):
    # xfade's slide transitions draw junk into the edge rows/columns on the first frame of the transition (a green strip in
    # video 10): fillborders smears the edges during the whip, where the motion blur hides it. The blur runs along the slide.
    d0 = dur(f'seg/{a}.mp4'); win = f"between(t,{d0 - wd - 0.001:.3f},{d0:.3f})"
    horiz = kind in ("slideleft", "slideright")
    fb = "fillborders=left=48:right=48:mode=smear" if horiz else "fillborders=top=48:bottom=48:mode=smear"
    blur = "gblur=sigma=30:sigmaV=1" if horiz else "gblur=sigma=1:sigmaV=30"
    fc = (f"[0:v][1:v]xfade=transition={kind}:duration={wd}:offset={d0 - wd:.3f},{fb}:enable='{win}',"
          f"{blur}:enable='between(t,{d0 - wd:.3f},{d0:.3f})'[v]")
    run(['-i', f'seg/{a}.mp4', '-i', f'seg/{b}.mp4', '-filter_complex', fc, '-map', '[v]'] + ENC + [out])
    print(f'  whip {a} -> {b}: {wd}s {kind}, joined {dur(out):.2f}s')

def seg_clip_raw(name):
    if name in SPLICE: return seg_splice(name)
    s = SEG[name]; L = s['len'] + EXTRA.get(name, 0); p = f'clips/{name}.mp4'; c = dur(p); r = c / L
    lo, hi = (0.8, 2.0) if name in FULLFIT else (0.8, 1.2)
    speed = min(max(r, lo), hi); played = c / speed
    vf = f"setpts=PTS/{speed:.4f},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},{SHARP},fps={FPS}"
    pad = max(0.0, L - played)
    if pad > 0.02:   # only if a clip came back short: hold its last frame with a slow push-in (never seen planned)
        n = round(L * FPS)
        vf += (f",tpad=stop_mode=clone:stop_duration={pad+0.1:.3f},scale={W*2}:{H*2},"
               f"zoompan=z='1+0.04*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS}")
    vf += f",trim=duration={L:.3f},setpts=PTS-STARTPTS,setsar=1"
    print(f'  {name}: clip {c:.2f}s -> {L:.2f}s at {speed:.3f}x' + (f', trims {played-L:.2f}s' if played > L + 0.02 else '')
          + (f', holds {pad:.2f}s' if pad > 0.02 else ''))
    run(['-i', p, '-vf', vf] + ENC + [f'seg/{name}.mp4'])

# ---- pointer tracking (Rule 6) ----
TW, TH = 540, 960   # tracking resolution (half size)
def seg_frames(name):
    raw = subprocess.run(['ffmpeg','-v','error','-i',f'seg/{name}.mp4','-vf',f'scale={TW}:{TH}','-f','rawvideo','-pix_fmt','gray','-'],
                         capture_output=True).stdout
    n = len(raw) // (TW * TH); return np.frombuffer(raw[:n*TW*TH], np.uint8).reshape(n, TH, TW)

def track(name, t_anchor, pts):
    """Similarity transforms from the anchor frame to every frame of seg/<name>.mp4, from points near the pointer (local
    tracking, so a near object keeps its pointer even when the background moves differently). Returns {frame: 2x3 matrix}."""
    fr = seg_frames(name); n = len(fr); fa = min(n - 1, max(0, round(t_anchor * FPS)))
    P = np.array(pts, np.float32) * (TW / W)
    T = {fa: np.array([[1, 0, 0], [0, 1, 0]], np.float64)}
    for step in (1, -1):
        i = fa; M = T[fa].copy()
        while 0 <= i + step < n:
            cur = (P @ M[:, :2].T + M[:, 2]).mean(0)
            mask = np.zeros((TH, TW), np.uint8); cv2.circle(mask, (int(cur[0]), int(cur[1])), 130, 255, -1)
            mask[int(0.70 * TH):int(0.80 * TH), :] = 0          # the caption band changes every word
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
    # solid arrow pointing at angle ang (degrees, 0 = right, 90 = down), rotated in Python and shifted to positive coordinates
    pts = [(0, 30), (125, 30), (125, 0), (L, Hh / 2), (125, Hh), (125, 62), (0, 62)]
    pts = [(x - L / 2, y - Hh / 2) for x, y in pts]; a = math.radians(ang)
    rp = [(x * math.cos(a) - y * math.sin(a), x * math.sin(a) + y * math.cos(a)) for x, y in pts]
    mx = min(p[0] for p in rp); my = min(p[1] for p in rp); rp = [(x - mx, y - my) for x, y in rp]
    w = max(p[0] for p in rp); h = max(p[1] for p in rp)
    return 'm ' + ' l '.join(f'{x:.0f} {y:.0f}' for x, y in rp), w, h

def ring_path(r):
    k = 0.5523 * r   # four bezier quarter circles, drawn from a top-left origin (\an7)
    return (f"m {r:.0f} 0 b {r+k:.0f} 0 {2*r:.0f} {r-k:.0f} {2*r:.0f} {r:.0f} b {2*r:.0f} {r+k:.0f} {r+k:.0f} {2*r:.0f} {r:.0f} {2*r:.0f} "
            f"b {r-k:.0f} {2*r:.0f} 0 {r+k:.0f} 0 {r:.0f} b 0 {r-k:.0f} {r-k:.0f} 0 {r:.0f} 0")

# Pointers, positions measured on a 100 px grid over a frame of the segment (seg/<SEG>.mp4 at 1080x1920), at t_anchor seconds
# into the segment, when the camera has arrived. kind 'arrows': three solid arrows slide from p0 to p1, 0.35 s apart;
# kind 'ring': one ring of radius r. (segment, kind, t_on, t_off, t_anchor, geometry) - times in seconds into the segment.
POINTERS = [   # measured on 100 px grids over seg/<SEG>.mp4 (18 Nov 2026); times in seconds into the segment
    ("C4", "arrows", 1.6, 3.0, 2.4, {"p0": (560, 770), "p1": (560, 1040)}),   # B5 "drips ... onto the cables": down the drips
    ("C5", "ring", 3.6, 5.6, 4.6, {"c": (485, 1005), "r": 130}),               # B7 "salt water eats into it": the crust and crack
    ("C10", "arrows", 3.6, 5.4, 4.2, {"p0": (540, 880), "p1": (540, 600)}),    # B12 "the gas gets out": up through the holes
    ("C13", "ring", 3.3, 5.8, 4.5, {"c": (935, 1045), "r": 85}),               # B17 "latches": the right-hand latch
]

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
                path, aw, ah = arrow_path(ang, L=200 * sc, Hh=92 * sc)
                for k in range(8):
                    ph = (f / FPS - a_on - 0.35 * k) % 1.05 if f / FPS - a_on - 0.35 * k >= 0 else None
                    if ph is None or ph > 1.0 or k > 2: continue
                    q = p0 + (p1 - p0) * ph; fa = min(1.0, ph / 0.18, (1.0 - ph) / 0.22, fade)
                    al = int(255 * (1 - max(0.0, fa)))
                    ev.append(f"Dialogue: 1,{ts(tt)},{ts(nxt)},Pointer,,0,0,0,,{{\\an7\\pos({q[0]-aw/2:.0f},{q[1]-ah/2:.0f})"
                              f"\\alpha&H{al:02X}&\\p1}}{path}{{\\p0}}")
    return ev

# ---- sound: voice + bed + effects (3.4 "Sound under the voice"; 3.3 Steps 6b and 9) ----
def rms_db(path):
    # Level of the mono fold-down (L+R)/2, what one phone speaker plays and what under_the_voice.py measures (3.4k).
    ch = int(subprocess.run(['ffprobe','-v','error','-select_streams','a:0','-show_entries','stream=channels','-of','csv=p=0',path],
                            capture_output=True, text=True).stdout.strip())
    a = np.frombuffer(subprocess.run(['ffmpeg','-loglevel','error','-i',path,'-ar','22050','-f','f32le','-'],
                                     capture_output=True).stdout, np.float32)
    a = a[:len(a) // ch * ch].reshape(-1, ch).mean(1)
    fr = a[:len(a)//1102*1102].reshape(-1, 1102); e = np.sqrt((fr**2).mean(1) + 1e-12)
    act = e[e > e.max() * 0.1]
    return 20 * np.log10(np.sqrt((act**2).mean()))
WORDS = json.load(open('audio/words_tight.json'))
NORM = [re.sub(r"[^a-z0-9']", "", w[2].lower()) for w in WORDS]
TL = json.load(open('timeline.json')); BT = {b['beat']: b for b in TL['beats']}
def at(beat, word=None, off=0.0):
    if word is None: return max(0.0, BT[beat]['start'] + off)
    i = next(j for j in range(BT[beat]['first_word'], len(NORM)) if NORM[j] == word); return WORDS[i][0] + off
# (file stem in audio/, start time, optional cut length). Measured on the files (18 Nov 2026): fx1 is loud from its start (the
# whump) to the clang at 2.1 s; fx2's wings peak 0.33 s in; fx3's salt rattles 0.0-2.1 s; fx4's drips plink 0.46-1.13 s; fx5's arc
# cracks at 0.31 s; fx6's three beeps start at once; fx7's lid lifts with a hiss and clanks back at 1.52 s. The blast times are set
# from the pilots: in C1 the pigeon takes off at ~0.45 s and the lid leaves the road on flame at ~0.58 s (measured
# 18 Nov 2026), so the wings start at 0.12 s (peak 0.33 s in) and the blast at 0.5 s; C8's flash is set once it is rendered.
FX = [("fx1_blast", at("B1", None, 0.5)), ("fx2_wings", at("B1", None, 0.12), 1.2), ("fx3_salt", at("B4", "trucks", -0.3)),
      ("fx4_drips", at("B5", "drips", -0.5)), ("fx5_arc", at("B8", "jumps", -0.25)), ("fx1_blast", at("B10", "lights", -0.1)),
      ("fx4_drips", at("B14", "let", -0.4)), ("fx6_beeps", at("B15", "raise", -0.05)), ("fx7_latch", at("B17", "lift", -1.0)),
      ("fx2_wings", at("B18", "pigeon", 0.1), 1.2)]
BED, BED_UNDER, FX_UNDER = 'bed_street', 19.0, 11.0      # dB under the voice (approved starting points, 3.4)

def mix(t0, t1, out, voice_only=False):
    voice = 'audio/narration_tight.wav'; v_db = rms_db(voice); T = t1 - t0
    inputs = ['-i', voice]; fc = [f"[0:a]aresample=48000,pan=stereo|c0=c0|c1=c0,apad=whole_dur={TOTAL:.3f},atrim={t0:.3f}:{t1:.3f},"
                                  f"asetpts=PTS-STARTPTS[v]"]
    parts = ['[v]']
    if not voice_only:
        g = v_db - BED_UNDER - rms_db(f'audio/{BED}.mp3')
        inputs += ['-stream_loop', '-1', '-i', f'audio/{BED}.mp3']
        fc.append(f"[1:a]aresample=48000,aformat=channel_layouts=stereo,atrim={t0:.3f}:{t0+T:.3f},asetpts=PTS-STARTPTS,volume={g:.2f}dB,"
                  f"afade=t=in:d=0.6,afade=t=out:st={max(0,T-0.8):.3f}:d=0.8[bed]"); parts.append('[bed]')
        k = 2
        for name, t, *cut in FX:
            if not (t0 - 0.5 <= t < t1): continue
            g = v_db - FX_UNDER - rms_db(f'audio/{name}.mp3'); d_ms = int(max(0, t - t0) * 1000)
            trim = f"atrim=0:{cut[0]:.2f},afade=t=out:st={cut[0]-0.3:.2f}:d=0.3," if cut else ""
            inputs += ['-i', f'audio/{name}.mp3']
            fc.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=stereo,{trim}volume={g:.2f}dB,adelay={d_ms}|{d_ms}[f{k}]")
            parts.append(f'[f{k}]'); k += 1
    fc.append(''.join(parts) + f"amix=inputs={len(parts)}:normalize=0:duration=first,atrim=0:{T:.3f},"
              f"loudnorm=I=-14:TP=-1.5:LRA=11,volume=2.6dB,alimiter=limit=0.84:level=false,aresample=48000[a]")
    run(inputs + ['-filter_complex', ';'.join(fc), '-map', '[a]', '-ac', '2', '-c:a', 'pcm_s16le', out])

# ---- captions (ASS) ----
CAPFONT = ImageFont.truetype('fonts/HBXCaption.ttf', round(CAP_FS * 1000 / 1219))   # libass Fontsize -> em for Montserrat
def ts(t):
    t = max(0, t); h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"
def cap(w): return re.sub(r"[^A-Za-z0-9'’\-]", "", w).upper()

def caption_events(t0, t1):
    ev = []; words = [w for w in WORDS if t0 - 0.01 <= w[0] < t1]; prev_end = t0
    for i, (s, e, w) in enumerate(words):
        s = max(s, prev_end); nxt = words[i + 1][0] if i + 1 < len(words) else None
        end = nxt if (nxt is not None and nxt - e <= 0.35) else e + 0.18
        end = min(max(end, s + 0.12), t1); prev_end = end
        txt = cap(w); wpx = CAPFONT.getlength(txt); sc = min(100, int(100 * MAXW / max(wpx, 1)))
        ev.append(f"Dialogue: 2,{ts(s-t0)},{ts(end-t0)},Caption,,0,0,0,,{{\\an5\\pos(540,{CAP_Y})\\fscx{int(sc*0.92)}\\fscy{int(sc*0.92)}"
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

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

def render(run_segs, tag):
    t0 = SEG[run_segs[0]]['start']; t1 = SEG[run_segs[-1]]['end']
    print(f'{tag}: {"+".join(run_segs)}  {t0:.2f}-{t1:.2f}s')
    for name in run_segs: seg_clip(name)
    files = []; i = 0
    while i < len(run_segs):
        name = run_segs[i]; nxt = run_segs[i + 1] if i + 1 < len(run_segs) else None
        if nxt and (name, nxt) in WHIP:
            out = f'tmp/whip_{name}_{nxt}.mp4'; whip_join(name, nxt, *WHIP[(name, nxt)][:1], out, WHIP[(name, nxt)][1]); files.append(f'../{out}'); i += 2
        else:
            files.append(f'../seg/{name}.mp4'); i += 1
    with open(f'tmp/{tag}_list.txt', 'w') as f:
        for fn in files: f.write(f"file '{fn}'\n")
    run(['-f','concat','-safe','0','-i',f'tmp/{tag}_list.txt','-c','copy',f'tmp/{tag}_clean.mp4'])
    mix(t0, t1, f'tmp/{tag}_mix.wav'); mix(t0, t1, f'tmp/{tag}_voice.wav', voice_only=True)
    open(f'tmp/{tag}.ass', 'w').write(ASS_HEAD + "\n".join(pointer_events(t0, t1) + caption_events(t0, t1)) + "\n")
    for audio, suffix in ((f'tmp/{tag}_mix.wav', ''), (f'tmp/{tag}_voice.wav', '_voiceonly')):
        run(['-i',f'tmp/{tag}_clean.mp4','-i',audio,'-vf',f'ass=tmp/{tag}.ass:fontsdir=fonts','-c:v','libx264','-preset','medium',
             '-crf','18','-pix_fmt','yuv420p','-r',str(FPS),'-c:a','aac','-b:a','192k','-movflags','+faststart','-shortest',
             f'tmp/{tag}{suffix}.mp4'])
    run(['-i',f'tmp/{tag}_clean.mp4','-i',f'tmp/{tag}_mix.wav','-c:v','copy','-c:a','aac','-b:a','192k','-shortest',
         f'tmp/{tag}_cleanmaster.mp4'])
    return f'tmp/{tag}.mp4', f'tmp/{tag}_voiceonly.mp4', f'tmp/{tag}_cleanmaster.mp4'

if __name__ == '__main__':
    runs = [a.split(',') for a in sys.argv[1:]] or [ORDER]
    outs = [render(r, f'part{i}') for i, r in enumerate(runs)]
    name = 'final' if not sys.argv[1:] else 'preview'
    if len(outs) == 1:
        for src, suf in zip(outs[0], ('', '_voiceonly', '_clean')): os.replace(src, f'out/{name}{suf}.mp4')
    else:
        run(['-f','lavfi','-i',f'color=black:s={W}x{H}:r={FPS}:d=0.4','-f','lavfi','-i','anullsrc=r=48000:cl=stereo','-t','0.4',
             '-c:v','libx264','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-shortest','tmp/black.mp4'])
        with open('tmp/join.txt','w') as f:
            for i, (o, _, _) in enumerate(outs):
                if i: f.write("file 'black.mp4'\n")
                f.write(f"file '{os.path.basename(o)}'\n")
        run(['-f','concat','-safe','0','-i','tmp/join.txt','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p',
             '-c:a','aac','-b:a','192k','-movflags','+faststart',f'out/{name}.mp4'])
    print('done:', name, round(dur(f'out/{name}.mp4'), 2), 's')
