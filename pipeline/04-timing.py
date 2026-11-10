# Video 04 (H15 seawater). Runs in the Higgsfield sandbox (v04/). Needs audio/takeX.wav, audio/words_takeX.json (from 02-whisper.py) and script.txt.
# usage: python3 timing04.py A|B [SPEED<=1.1]   -> audio/narration_tight.wav, audio/words_tight.json, timeline.json (video 04, 27 beats)
# Tightens every pause to ~0.15 s, optionally applies a pitch-preserving atempo (never above 1.1x), maps Whisper word
# times through the cuts, and writes each beat's real start/end plus the clip length it needs (ceil, min 3 s; minimax needs 4).
import json, re, subprocess, difflib, sys, math
T = sys.argv[1]; SPEED = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0; assert SPEED <= 1.1; SRC = f'audio/take{T}.wav'
def silences(path, d):
    out = subprocess.run(['ffmpeg','-i',path,'-af',f'silencedetect=noise=-38dB:d={d}','-f','null','-'],capture_output=True,text=True).stderr
    return [float(x) for x in re.findall(r'silence_start: ([\d.]+)',out)], [float(x) for x in re.findall(r'silence_end: ([\d.]+)',out)]
dur = float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',SRC],capture_output=True,text=True).stdout)
st, en = silences(SRC, 0.25)
keep = 0.075; segs = []; cur = 0.0
for s, e in zip(st, en):
    if s < 0.05: cur = max(cur, e - 0.05); continue
    if e >= dur - 0.01: segs.append((cur, s + 0.15)); cur = None; break
    segs.append((cur, s + keep)); cur = e - keep
if cur is not None: segs.append((cur, dur))
offs = []; acc = 0.0
for a, b in segs: offs.append((a, b, acc)); acc += b - a
TIGHT = acc
def o2t(t):
    for a, b, o in offs:
        if t < a: return o
        if t <= b: return o + (t - a)
    return TIGHT
# render the tightened narration (5 ms fades at each cut to avoid clicks)
fc = ''.join(f"[0:a]atrim={a:.4f}:{b:.4f},asetpts=PTS-STARTPTS,afade=t=in:d=0.005,afade=t=out:st={max(0,b-a-0.005):.4f}:d=0.005[s{i}];" for i,(a,b) in enumerate(segs))
fc += ''.join(f'[s{i}]' for i in range(len(segs))) + f'concat=n={len(segs)}:v=0:a=1,atempo={SPEED}[out]'
subprocess.run(['ffmpeg','-loglevel','error','-y','-i',SRC,'-filter_complex',fc,'-map','[out]','-ar','44100','-ac','1','audio/narration_tight.wav'],check=True)
W = json.load(open(f'audio/words_take{T}.json'))
script = open('script.txt').read().split()
norm = lambda w: re.sub(r"[^a-z0-9']", "", w.lower().replace('’', "'"))
sm = difflib.SequenceMatcher(a=[norm(x) for x in script], b=[norm(w[2]) for w in W], autojunk=False)
T2 = [None]*len(script); matched = 0
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == 'equal' or (tag == 'replace' and i2-i1 == j2-j1):
        for k in range(i2-i1):
            T2[i1+k] = (W[j1+k][0], W[j1+k][1]); matched += 1
    elif tag == 'replace':   # e.g. "ten thousand" vs "10,000": spread the span over the script words by length
        a0, b0 = W[j1][0], W[j2-1][1]; L = [max(1, len(norm(x))) for x in script[i1:i2]]; c = a0
        for k, n in enumerate(L):
            d = (b0 - a0) * n / sum(L); T2[i1+k] = (c, c + d); c += d
        matched += i2 - i1
    if tag != 'equal': print('  diff', tag, script[i1:i2], [w[2] for w in W[j1:j2]])
for i in range(len(script)):
    if T2[i] is None:
        p = T2[i-1][1] if i > 0 and T2[i-1] else 0.0
        n = next((T2[j][0] for j in range(i+1, len(script)) if T2[j]), p + 0.3)
        T2[i] = (p, min(n, p + 0.3))
words = [[round(o2t(a)/SPEED,3), round(o2t(b)/SPEED,3), w] for (a,b), w in zip(T2, script)]
TIGHT = TIGHT / SPEED
json.dump(words, open('audio/words_tight.json','w'))
beats = [("B1","If"),("B2","But it's salt"),("B3","So you boil"),("B4","But boiling a"),("B5","So instead"),("B6","Giant pumps"),
 ("B7","That's about sixty"),("B8","This is reverse"),("B9","But the intake"),("B10","So you move"),("B11","The water slips"),
 ("B12","But sand and"),("B13","So you filter"),("B14","But those pumps"),("B15","So the leftover"),("B16","But the water is now"),
 ("B17","So you trickle"),("B18","That's right"),("B19","That's why bottled"),("B20","But worldwide"),("B21","It's heavier"),
 ("B22","So you spray"),("B23","But then the rain"),("B24","Rivers shrink"),("B25","But your taps"),("B26","Perth Australia"),
 ("B27","Pump it press")]
toks = [norm(x) for x in script]; starts = []
for b, ph in beats:
    p = [norm(x) for x in ph.split()]
    idx = next(i for i in range(len(toks)) if toks[i:i+len(p)] == p and (not starts or i > starts[-1][1]))
    starts.append((b, idx))
TAIL = 0.9; out = []
for k, (b, idx) in enumerate(starts):
    s = 0.0 if k == 0 else words[idx][0] - 0.08
    e = (words[starts[k+1][1]][0] - 0.08) if k+1 < len(starts) else TIGHT + TAIL
    out.append({"beat": b, "start": round(s,3), "end": round(e,3), "len": round(e-s,3), "first_word": idx, "clip_s": max(3, math.ceil(e-s))})
json.dump({"take": T, "speed": SPEED, "raw": round(dur,2), "total": round(TIGHT+TAIL,3), "beats": out}, open('timeline.json','w'), indent=1)
print(f'take {T} x{SPEED}: raw {dur:.2f}s -> tight {TIGHT:.2f}s ({len(script)/TIGHT:.2f} w/s), video {TIGHT+TAIL:.2f}s; whisper matched {matched}/{len(script)} words')
for x in out: print(f"{x['beat']:4} {x['start']:6.2f} -> {x['end']:6.2f}  ({x['len']:.2f}s)  clip {x['clip_s']}s")
print('clip seconds total', sum(x['clip_s'] for x in out))
