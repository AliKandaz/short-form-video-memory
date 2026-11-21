# Video 16 (B3, the Christmas light show). Runs locally in the work dir (clips/, audio/, fonts/). Made from 15-timing.py.
# usage: python3 16-timing.py A|B [SPEED<=1.1]  needs audio/takeX.wav and audio/words_takeX.json (word times of that take)
#        python3 16-timing.py EST               no narration yet: word times estimated at 3.5 words a second from the script,
#                                               for a silent preview of the picture and the overlays (21 Nov 2026: ElevenLabs
#                                               had no credits when the clips were ready)
# -> audio/narration_tight.wav (not in EST), audio/words_tight.json, timeline.json (19 beats), plan.json (13 clips)
# Tightens every pause to ~0.15 s, optionally applies a pitch-preserving atempo (never above 1.1x), maps the word times through
# the cuts, and writes each beat's real start and end. The 13 clips were rendered at the beat sheet's lengths before the
# narration existed (Gate B's plan), so plan.json reports the speed each clip must play at; outside 0.8-1.2x means the line
# needs a cut, a hold or FULLFIT in the build.
import json, re, subprocess, difflib, sys, math, os
HERE = os.path.dirname(os.path.abspath(__file__))
T = sys.argv[1]; SPEED = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0; assert SPEED <= 1.1
raw = open(os.path.join(HERE, '16-script.txt')).read()
script = raw[raw.index('If you clip'):].split()          # the spoken words only (the file has a header)
norm = lambda w: re.sub(r"[^a-z0-9']", "", w.lower().replace('’', "'"))
os.makedirs('audio', exist_ok=True)

if T == 'EST':
    WPS = 3.5; dur = None
    wt = []
    for t in script:
        syl = max(1, len(re.findall(r"[aeiouy]+", re.sub(r"e\b", "", t.lower()))))
        wt.append((syl, 0.55 if t[-1] in ",:" else (0.9 if t[-1] == "." else 0.0)))
    TIGHT = len(script) / WPS; k = TIGHT / sum(a + b for a, b in wt); c = 0.0; words = []
    for t, (syl, gap) in zip(script, wt):
        words.append([round(c, 3), round(c + syl * k, 3), t]); c += (syl + gap) * k
    matched = len(script)
else:
    SRC = f'audio/take{T}.wav'
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
    fc = ''.join(f"[0:a]atrim={a:.4f}:{b:.4f},asetpts=PTS-STARTPTS,afade=t=in:d=0.005,afade=t=out:st={max(0,b-a-0.005):.4f}:d=0.005[s{i}];" for i,(a,b) in enumerate(segs))
    fc += ''.join(f'[s{i}]' for i in range(len(segs))) + f'concat=n={len(segs)}:v=0:a=1,atempo={SPEED}[out]'
    subprocess.run(['ffmpeg','-loglevel','error','-y','-i',SRC,'-filter_complex',fc,'-map','[out]','-ar','44100','-ac','1','audio/narration_tight.wav'],check=True)
    W = json.load(open(f'audio/words_take{T}.json'))
    sm = difflib.SequenceMatcher(a=[norm(x) for x in script], b=[norm(w[2]) for w in W], autojunk=False)
    T2 = [None]*len(script); matched = 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal' or (tag == 'replace' and i2-i1 == j2-j1):
            for k in range(i2-i1):
                T2[i1+k] = (W[j1+k][0], W[j1+k][1]); matched += 1
        elif tag == 'replace':   # e.g. "two thousand" heard as "2,000": spread the span over the script words by length
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

beats = [("B1","If you clip"),("B2","But you plug"),("B3","So you swap"),("B4","But the first"),("B5","The outlet felt"),
 ("B6","This is a ground-fault"),("B7","So every plug"),("B8","But all your"),("B9","So every bulb"),("B10","These are pixels"),
 ("B11","But halfway along"),("B12","So you feed"),("B13","This is power"),("B14","But the music"),("B15","So you send"),
 ("B16","That's why light-show"),("B17","Add a tree"),("B18","That's your light"),("B19","The bill")]
toks = [norm(x) for x in script]; starts = []
for b, ph in beats:
    p = [norm(x) for x in ph.split()]
    idx = next(i for i in range(len(toks)) if toks[i:i+len(p)] == p and (not starts or i > starts[-1][1]))
    starts.append((b, idx))
TAIL = 0.9; out = []   # the picture runs 0.9 s past the last word; the street card (1.5 s) comes after it, in the build
for k, (b, idx) in enumerate(starts):
    s = 0.0 if k == 0 else words[idx][0] - 0.08
    e = (words[starts[k+1][1]][0] - 0.08) if k+1 < len(starts) else TIGHT + TAIL
    out.append({"beat": b, "start": round(s,3), "end": round(e,3), "len": round(e-s,3), "first_word": idx})
json.dump({"take": T, "speed": SPEED, "raw": dur and round(dur,2), "total": round(TIGHT+TAIL,3), "beats": out}, open('timeline.json','w'), indent=1)
print(f'take {T} x{SPEED}: ' + (f'raw {dur:.2f}s -> ' if dur else 'estimated, ') + f'tight {TIGHT:.2f}s ({len(script)/TIGHT:.2f} w/s), '
      f'video {TIGHT+TAIL:.2f}s + the card; matched {matched}/{len(script)} words')
for x in out: print(f"{x['beat']:4} {x['start']:6.2f} -> {x['end']:6.2f}  ({x['len']:.2f}s)  {' '.join(script[x['first_word']:x['first_word']+4])}")

# The clip plan: one clip per segment, rendered at these lengths (16-beat-sheet.md) before the narration existed.
SEG = [("C1",["B1"]),("C2",["B2"]),("C3",["B3"]),("C4",["B4"]),("C5",["B5","B6"]),("C6",["B7","B8"]),("C7",["B9","B10"]),
       ("C8",["B11"]),("C9",["B12","B13"]),("C10",["B14"]),("C11",["B15","B16"]),("C12",["B17"]),("C13",["B18","B19"])]
CLIP_S = {"C1": 4, "C2": 5, "C3": 5, "C4": 4, "C5": 5, "C6": 4, "C7": 6, "C8": 4, "C9": 4, "C10": 3, "C11": 8, "C12": 4, "C13": 5}
BB = {x["beat"]: x for x in out}; plan = []
for name, bs in SEG:
    s = BB[bs[0]]["start"]; e = BB[bs[-1]]["end"]; L = e - s; c = CLIP_S[name]
    plan.append({"seg": name, "beats": bs, "start": round(s,3), "end": round(e,3), "len": round(L,3), "clip_s": c, "rate": round(c / L, 3)})
json.dump({"take": T, "speed": SPEED, "total": round(TIGHT+TAIL,3), "segments": plan}, open('plan.json','w'), indent=1)
print('\nsegments:')
for p in plan:
    flag = '' if 0.8 <= p['rate'] <= 1.2 else '   <- outside 0.8-1.2x'
    print(f"{p['seg']:4} {'+'.join(p['beats']):9} {p['start']:6.2f}-{p['end']:6.2f} ({p['len']:.2f}s)  clip {p['clip_s']}s  speed x{p['rate']}{flag}")
print(f"clip seconds {sum(CLIP_S.values())} for {TIGHT+TAIL:.2f}s of video")
