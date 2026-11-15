# Video 09 (C3 lightning). Runs locally (v09/ work dir). Needs audio/takeX.wav, audio/words_takeX.json (from 09-whisper.py)
# and script.txt. usage: python3 08-timing.py A|B [SPEED<=1.1] -> audio/narration_tight.wav, audio/words_tight.json, timeline.json (24 beats), plan.json (16 clips)
# Tightens every pause to ~0.15 s, optionally applies a pitch-preserving atempo (never above 1.1x), maps Whisper word
# times through the cuts, and writes each beat's real start/end plus the clip length it needs (ceil, min 3 s).
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
beats = [("B1","Everyone's heard"),("B2","Here's what"),("B3","It hits your roof"),("B4","The wires in"),("B5","So you give"),
 ("B6","a thick cable"),("B7","This is a lightning"),("B8","But thirty"),("B9","Just inside"),("B10","This is a side"),
 ("B11","So you clamp"),("B12","This is bonding"),("B13","But the bolt"),("B14","It hits the pole"),("B15","Every outlet"),
 ("B16","So you fit"),("B17","But the pipes"),("B18","And about a third"),("B19","That's why your mom"),("B20","So when it thunders"),
 ("B21","Then the big"),("B22","It slams"),("B23","Upstairs the pipes"),("B24","Catch it high")]
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

# Clip plan (beat sheet): one clip per segment, no holds (3.4 Rule 1).
SEG = [("C1",["B1","B2"]),("C2",["B3","B4"]),("C3",["B5"]),("C4",["B6"]),("C5",["B7"]),("C6",["B8"]),("C7",["B9","B10"]),
       ("C8",["B11","B12"]),("C9",["B13"]),("C10",["B14","B15"]),("C11",["B16"]),("C12",["B17","B18"]),("C13",["B19"]),
       ("C14",["B20"]),("C15",["B21","B22"]),("C16",["B23","B24"])]
BB = {x["beat"]: x for x in out}; plan = []; tot_clip = 0
for name, bs in SEG:
    s = BB[bs[0]]["start"]; e = BB[bs[-1]]["end"]; L = e - s
    if name.startswith("H"):
        plan.append({"seg": name, "beats": bs, "start": round(s,3), "end": round(e,3), "len": round(L,3), "clip_s": 0}); continue
    c = max(3, math.ceil(L - 0.06))
    if c - 1 >= 3 and L / (c - 1) <= 1.04: c -= 1      # up to ~4% short: play the clip slightly slower instead
    tot_clip += c
    plan.append({"seg": name, "beats": bs, "start": round(s,3), "end": round(e,3), "len": round(L,3), "clip_s": c, "rate": round(c / L, 3)})
json.dump({"take": T, "speed": SPEED, "total": round(TIGHT+TAIL,3), "segments": plan}, open('plan.json','w'), indent=1)
print('\nsegments:')
for p in plan: print(f"{p['seg']:4} {'+'.join(p['beats']):14} {p['start']:6.2f}-{p['end']:6.2f} ({p['len']:.2f}s)  clip {p['clip_s']}s" + (f"  speed x{p['rate']}" if p['clip_s'] else '  hold'))
holds = sum(p['len'] for p in plan if not p['clip_s'])
print(f'clip seconds {tot_clip}; holds {holds:.2f}s of {TIGHT+TAIL:.2f}s ({holds/(TIGHT+TAIL):.0%}); 720p cost {tot_clip*2.25:.2f}')
