# s2-01 (style 2): assemble cut B (the fast-cut story) and cut A (the one-take time-lapse) from the wan2_7 clips.
# usage: python3 s2-01-build.py <work dir> [B] [A]      (default both)
# The work dir holds clips/C1.mp4 ... clips/C17.mp4: the accepted takes (wan2_7, 720x1276, 30 fps, each with its own sound).
# Writes <work dir>/out/s2-01-cutB.mp4 and s2-01-cutA.mp4: 1080x1920, 30 fps, H.264, AAC, about -14 LUFS.
# What it does: every shot is a window of a clip (in, out, speed), scaled to fill 1080x1920 (720x1276 is 0.3% wider than 9:16,
# so it is scaled to 1920 tall and the sides cropped), lightly sharpened (the 720p clips, CLAUDE.md 7.5), and carries the same
# window of its clip's own sound, with 15 ms fades so the hard cuts don't click. Quiet clips are lifted toward a floor (Wan made
# the dusk clips near-silent: C14 -54 dB, C17 -52 dB) and loud ones trimmed toward a ceiling, at most 14 dB either way; then the
# whole mix is normalised to -14 LUFS (two-pass loudnorm). Cut A joins its chain clips where they share a still (the clips
# start and end on the stills, 0 px shift, Gate D), with a 3-frame dissolve to hide the small change of tone between takes.
import json, os, subprocess, sys
import numpy as np

D = sys.argv[1]; WHICH = [a for a in sys.argv[2:] if a in ("A", "B")] or ["B", "A"]
CLIPS = os.path.join(D, "clips"); OUT = os.path.join(D, "out"); TMP = os.path.join(D, "tmp")
os.makedirs(OUT, exist_ok=True); os.makedirs(TMP, exist_ok=True)
FPS = 30
VF = "scale=-2:1920:flags=lanczos,crop=1080:1920,unsharp=5:5:0.6:5:5:0.0,setsar=1,fps=30"
ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "17", "-pix_fmt", "yuv420p", "-r", str(FPS)]
AENC = ["-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2"]
FLOOR, CEIL, MAXG = -30.0, -18.0, 14.0   # per-shot RMS band (dB) and the largest gain change

# Ambiences laid under shots whose own sound came back empty (C2 after 0.8 s, C14, C17: -50 to -60 dB). ElevenLabs sfx
# (flow pvtHhV6Ln05XmrgRuOEP, 21 Nov 2026): audio/ambA.mp3 a frosty morning yard (4 s), audio/ambB.mp3 a calm winter dusk (8 s).
# (file, shot index where it starts (1-based) or a time in s, offset into the file, length, low-pass Hz or 0, RMS target dB)
# ambB is muffled under the indoor shots (29-31) and opens up when the cut goes outside to the payoff (32).
OVER_B = [("ambA", 11, 2.0, 1.35, 0, -30.0), ("ambB", 29, 0.0, 4.7, 1600, -31.0), ("ambB", 32, 4.7, 3.0, 0, -30.0)]
OVER_A = [("ambB", 32.0, 0.0, 5.0, 1600, -31.0), ("ambB", 37.0, 5.0, 3.0, 0, -30.0)]
XO = 0.2   # fade in and out of each ambience piece, so the muffled and open pieces of ambB cross over

# Usable windows found at the clip check (21 Nov 2026): C1 freezes the hens mid-flap after ~2.3 s (its end still has them so);
# C8 loses the hands at 2.8 s; C11 is done at 2.5 s; C14 is still after ~2.4 s; C15 wanders between 0.8 and 1.6 s; C16 doubles
# the window and shows a forest from 2.6 s.
CUT_B = [  # (clip, in s, out s, speed). Neighbouring chain clips share a still and join seamlessly, so a plain run of them plays
           # as one long take (the first build had an 11 s inside take); each time-lapse is cut in two with a small jump in time
           # instead (the reference's hard cut about every 1.4 s), and the demolition intercuts inside and out.
    ("C1", 0.0, 1.6, 1.0),   # 1 frame 0; the roof gives way, dust, hens flap off by 1.0 s
    ("C2", 0.3, 1.5, 1.0),   # 2 the wife laughing behind her mug
    ("C1", 1.6, 2.3, 1.0),   # 3 dust, his hand on his head
    ("C9", 0.0, 1.3, 1.0),   # 4 INSIDE: under the broken roof, the guts coming out
    ("C9", 1.7, 3.0, 1.0),   # 5 gutted, open to the sky
    ("C3", 0.0, 1.2, 1.0),   # 6 OUTSIDE: the wreck being cleared
    ("C8", 0.3, 1.2, 1.0),   # 7 close: the screw into the rafter
    ("C3", 1.6, 3.0, 1.0),   # 8 the frame on new posts, the hens' new house
    ("C4", 0.3, 1.5, 1.0),   # 9 rafters going up
    ("C4", 1.8, 3.0, 1.0),   # 10 the metal roof, sheathing
    ("C2", 1.8, 3.0, 1.0),   # 11 the wife: her grin gone, mug lowered (a hen clucks: ambA)
    ("C5", 0.0, 1.3, 1.0),   # 12 the window going in
    ("C5", 1.7, 3.0, 1.0),   # 13 the glazed door, cladding
    ("C8", 1.4, 2.3, 1.0),   # 14 close: the screw seats
    ("C6", 0.0, 1.3, 1.0),   # 15 paint going on
    ("C6", 1.7, 3.0, 1.0),   # 16 the porch; the hen house painted to match
    ("C7", 0.3, 1.5, 1.0),   # 17 lantern, planter, doormat
    ("C7", 1.8, 3.0, 1.0),   # 18 finished
    ("C10", 0.0, 1.3, 1.0),  # 19 INSIDE: a new roof, studs
    ("C15", 0.0, 0.8, 1.0),  # 20 close: a pine board pressed in, a nail
    ("C10", 1.7, 3.0, 1.0),  # 21 insulation, subfloor
    ("C11", 0.3, 1.4, 1.0),  # 22 pine going up
    ("C11", 1.6, 2.5, 1.0),  # 23 pine walls and ceiling, plank floor
    ("C15", 1.8, 2.7, 1.0),  # 24 close: the next board (its second nail-gun shot is at 2.5 s)
    ("C12", 0.0, 1.3, 1.0),  # 25 the bed coming in
    ("C12", 1.7, 3.0, 1.0),  # 26 bed, desk, shelves
    ("C13", 0.3, 1.5, 1.0),  # 27 the quilt going on
    ("C13", 1.8, 3.0, 1.0),  # 28 rug, books, plant, lamp
    ("C14", 0.0, 1.2, 1.0),  # 29 the daylight going
    ("C14", 1.4, 2.4, 1.0),  # 30 dusk, snow outside
    ("C16", 0.0, 2.5, 1.0),  # 31 the last touch: the lamp on, the pillow plumped
    ("C17", 0.0, 3.0, 1.0),  # 32 payoff: dusk, snow, the glowing cabin, the wife staring
]
CUT_A = [  # takes: each a list of clips joined where they share a still
    [("C1", 0.0, 2.3, 1.0)],
    [("C9", 0.0, 3.0, 1.0)],
    [("C3", 0.0, 3.0, 1.0), ("C4", 0.0, 3.0, 1.0), ("C5", 0.0, 3.0, 1.0), ("C6", 0.0, 3.0, 1.0), ("C7", 0.0, 3.0, 1.0)],
    [("C10", 0.0, 3.0, 1.0), ("C11", 0.0, 3.0, 1.0), ("C12", 0.0, 3.0, 1.0), ("C13", 0.0, 3.0, 1.0), ("C14", 0.0, 3.0, 1.0)],
    [("C16", 0.0, 2.5, 1.0)],
    [("C17", 0.0, 3.0, 1.0)],
]
XF = 3 / FPS   # cut A's dissolve inside a take

def run(args): subprocess.run(["ffmpeg", "-loglevel", "error", "-y"] + args, check=True)

def rms_db(clip, t0, t1):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t0), "-t", str(t1 - t0), "-i", os.path.join(CLIPS, clip + ".mp4"),
                          "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True).stdout
    a = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
    return 20 * np.log10(np.sqrt(np.mean(a ** 2)) + 1e-9) if len(a) else -90.0

def shot(i, clip, t0, t1, sp, tag):
    """One shot as its own file: the clip window, scaled and sharpened, with its own sound levelled and faded."""
    out = os.path.join(TMP, f"{tag}{i:02d}_{clip}.mp4"); dur = (t1 - t0) / sp
    r = rms_db(clip, t0, t1); g = 0.0
    if r < FLOOR: g = min(MAXG, FLOOR - r)
    elif r > CEIL: g = max(-MAXG, CEIL - r)
    vf = VF + (f",setpts=PTS/{sp}" if sp != 1.0 else "")
    af = (f"atempo={sp}," if sp != 1.0 else "") + f"volume={g:.1f}dB,afade=t=in:d=0.015,afade=t=out:st={max(0, dur - 0.015):.3f}:d=0.015"
    run(["-ss", f"{t0:.3f}", "-i", os.path.join(CLIPS, clip + ".mp4"), "-t", f"{(t1 - t0):.3f}", "-vf", vf, "-af", af,
         "-t", f"{dur:.3f}"] + ENC + AENC + [out])
    return out, dur, r, g

def concat(files, out):
    lst = out + ".txt"
    with open(lst, "w") as f:
        for p in files: f.write(f"file '{p}'\n")
    run(["-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", out])

def file_rms(path, t0, dur, lp):
    af = (["-af", f"lowpass=f={lp}"] if lp else [])
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t0), "-t", str(dur), "-i", path] + af + ["-ac", "1", "-ar", "16000",
                          "-f", "s16le", "-"], capture_output=True).stdout
    a = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
    return 20 * np.log10(np.sqrt(np.mean(a ** 2)) + 1e-9)

def overlay(src, overs, starts, out):
    """Mix the ambience pieces onto the cut's sound at their places, each levelled to its RMS target by measurement."""
    inputs = ["-i", src]; fc = []; labels = ["[0:a]"]
    for k, (name, at, off, dur, lp, target) in enumerate(overs, 1):
        path = os.path.join(D, "audio", name + ".mp3"); inputs += ["-i", path]
        t = starts[at - 1] if isinstance(at, int) else at
        g = target - file_rms(path, off, dur, lp)
        chain = f"[{k}:a]atrim=start={off}:duration={dur + XO},asetpts=PTS-STARTPTS" + (f",lowpass=f={lp}" if lp else "")
        chain += (f",volume={g:.1f}dB,afade=t=in:d={XO},afade=t=out:st={dur - XO / 2:.3f}:d={XO},aformat=sample_rates=48000:"
                  f"channel_layouts=stereo,adelay={int(round((t - XO / 2) * 1000))}:all=1[o{k}]")
        fc.append(chain); labels.append(f"[o{k}]")
        print(f"  overlay {name} at {t:.2f} s for {dur:.2f} s, gain {g:+.1f} dB" + (f", low-pass {lp} Hz" if lp else ""))
    fc.append("".join(labels) + f"amix=inputs={len(labels)}:duration=first:normalize=0[a]")
    run(inputs + ["-filter_complex", ";".join(fc), "-map", "0:v", "-map", "[a]", "-c:v", "copy"] + AENC + [out])

# Loudness (21 Nov 2026): the build sounds are percussive (a crash, nail-gun shots, fast hammering), so plain gain or loudnorm
# stopped at -15.5 to -16 LUFS with true peaks near 0 dBFS. A gentle compressor and a -9 dBFS limiter first (LRA about 7.6 LU),
# then the gain to -14 LUFS measured twice (the last limiter takes back about a dB), then a -3 dBFS limiter for the true peaks.
PRE = "acompressor=threshold=0.04:ratio=3:attack=8:release=120:makeup=1,alimiter=limit=0.35:attack=2:release=60:level=0"
TPL = "alimiter=limit=0.708:attack=1:release=40:level=0"
def integrated(src, af):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", src, "-af", af + ",ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    return float([l for l in r.splitlines() if l.strip().startswith("I:")][-1].split()[1])

def loudnorm(src, out):
    g = -14.0 - integrated(src, PRE)
    g += -14.0 - integrated(src, f"{PRE},volume={g:.2f}dB,{TPL}")
    run(["-i", src, "-c:v", "copy", "-af", f"{PRE},volume={g:.2f}dB,{TPL}"] + AENC + [out])
    print(f"  loudness: gain {g:+.1f} dB after the compressor and limiter")

def take(files_durs, tag):
    """Join the clips of one cut-A take with a short dissolve (video and sound)."""
    if len(files_durs) == 1: return files_durs[0][0]
    out = os.path.join(TMP, f"{tag}.mp4"); inputs = []; fc = []; t = 0.0
    for p, _ in files_durs: inputs += ["-i", p]
    v, a = "[0:v]", "[0:a]"
    for k in range(1, len(files_durs)):
        t += files_durs[k - 1][1] - XF
        fc.append(f"{v}[{k}:v]xfade=transition=fade:duration={XF:.4f}:offset={t:.4f}[v{k}]")
        fc.append(f"{a}[{k}:a]acrossfade=d={XF:.4f}[a{k}]")
        v, a = f"[v{k}]", f"[a{k}]"
    run(inputs + ["-filter_complex", ";".join(fc), "-map", v, "-map", a] + ENC + AENC + [out])
    return out

if "B" in WHICH:
    parts = []; log = []
    for i, (c, t0, t1, sp) in enumerate(CUT_B, 1):
        p, d, r, g = shot(i, c, t0, t1, sp, "B"); parts.append(p); log.append((i, c, t0, t1, d, r, g))
    raw = os.path.join(TMP, "cutB_raw.mp4"); concat(parts, raw)
    durs = [x[4] for x in log]; starts = list(np.cumsum([0] + durs[:-1]))
    mixed = os.path.join(TMP, "cutB_mix.mp4"); overlay(raw, OVER_B, starts, mixed); loudnorm(mixed, os.path.join(OUT, "s2-01-cutB.mp4"))
    print(f"cut B: {len(log)} shots, {sum(durs):.2f} s, median {np.median(durs):.2f} s, longest {max(durs):.2f} s")
    for i, c, t0, t1, d, r, g in log: print(f"  {i:2d} {c:4s} {t0:.1f}-{t1:.1f}  {d:.2f} s  sound {r:6.1f} dB  gain {g:+.1f}")
if "A" in WHICH:
    tfiles = []
    for ti, tk in enumerate(CUT_A, 1):
        fd = [shot(j, c, t0, t1, sp, f"A{ti}_")[:2] for j, (c, t0, t1, sp) in enumerate(tk, 1)]
        tfiles.append(take(fd, f"A_take{ti}"))
    raw = os.path.join(TMP, "cutA_raw.mp4"); concat(tfiles, raw)
    mixed = os.path.join(TMP, "cutA_mix.mp4"); overlay(raw, OVER_A, [], mixed); loudnorm(mixed, os.path.join(OUT, "s2-01-cutA.mp4"))
    d = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                              os.path.join(OUT, "s2-01-cutA.mp4")], capture_output=True, text=True).stdout)
    print(f"cut A: {len(CUT_A)} takes, {d:.2f} s")
