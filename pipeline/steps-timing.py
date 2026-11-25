# The narration's timing for a build-steps video (CLAUDE.md 6.2 Step 6; written 24 Nov 2026 after video 17's review).
# 17-timing.py with step beats: video 17 tightened every pause inside a "So" sentence, so steps landed 0.9-1.3 s apart
# and their clips had to be cut into each other ("mushed together"). Here:
# - every pause is tightened to 0.15 s, except
# - the beat before each "But" (and after the premise): BEAT seconds once sped up, and
# - the step beats: inside a sentence, two landing words (the words in [brackets] in the script) are kept at least
#   STEP_GAP seconds apart, by adding silence after the first one's phrase (at most MAXPAD; a gap that is still short is
#   printed as a script problem: lengthen the phrase, or give the step its own sentence).
# Then the take is sped up to TEMPO (never past 1.1).
#
#   python3 steps-timing.py <work dir> <script.txt> [--gap 1.6] [--gaps gaps.json] [--out tight]
#     reads  <work>/audio/narr_A.mp3 and <work>/audio/words_takeA.json (Whisper's words: [start, end, text], raw take)
#     writes <work>/audio/narr_<out>.wav and <work>/audio/words_<out>.json: [{"w", "a", "b", "land": true if a landing word}]
#     --gaps: {"<n>": seconds} the gap wanted after landing number n (0-based, counted through the script), where a clip
#             needs longer to finish than STEP_GAP; the edit (17-build.py, place2) prints what each clip needs.
import json, os, re, subprocess, sys, difflib, wave
import numpy as np

A = sys.argv[1:]
def opt(name, default):
    return A[A.index(name) + 1] if name in A else default
WORK, SCRIPT = A[0], A[1]
STEP_GAP, OUT = float(opt('--gap', 1.6)), opt('--out', 'tight')
GAPS = {int(k): float(v) for k, v in json.load(open(opt('--gaps', ''))).items()} if '--gaps' in A else {}
SR, TEMPO = 44100, 1.1
KEEP = 0.075             # kept at each side of a tightened pause: 0.15 s raw, 0.136 s after the speed-up
BEAT = 0.50              # the beat before each "But", after the speed-up
MAXPAD = 0.60            # the most silence added after one step's phrase; more than that sounds like a stall
LEAD, TAIL = 0.03, 0.20
SIL_DB, SIL_D = -38, 0.25

def run(cmd): return subprocess.run(cmd, check=True, capture_output=True, text=True)
def norm(w): return re.sub(r'[^a-z0-9$]', '', w.lower())

def script_words():
    """The spoken words, and for each whether it is a landing word (followed by its [mark] in the script)."""
    txt = open(SCRIPT).read().split('\n')
    start = next(i for i, l in enumerate(txt) if l.startswith('If '))            # the spoken text starts at the premise
    toks = ' '.join(l for l in txt[start:] if l.strip()).split()
    words, land = [], []
    for t in toks:
        if t.startswith('['):
            if words: land[-1] = True
            continue
        words.append(t); land.append(False)
    return words, land

def main():
    raw = os.path.join(WORK, 'audio/narr_A.mp3'); wav = os.path.join(WORK, 'audio/narr_A.wav')
    run(['ffmpeg', '-y', '-v', 'error', '-i', raw, '-ac', '1', '-ar', str(SR), wav])
    with wave.open(wav, 'rb') as f: x = np.frombuffer(f.readframes(f.getnframes()), dtype='<i2').astype(np.float32) / 32768
    dur = len(x) / SR
    log = run(['ffmpeg', '-v', 'info', '-i', wav, '-af', f'silencedetect=noise={SIL_DB}dB:d={SIL_D}', '-f', 'null', '-']).stderr
    st = [float(v) for v in re.findall(r'silence_start: ([\d.]+)', log)]
    en = [float(v) for v in re.findall(r'silence_end: ([\d.]+)', log)]
    sil = list(zip(st, en + [dur] * (len(st) - len(en))))
    wh = []
    for a, b, w in json.load(open(os.path.join(WORK, 'audio/words_takeA.json'))):
        if wh and w[:1] in '-,': wh[-1] = [wh[-1][0], b, wh[-1][2] + w]         # "T", "-rex," -> "T-rex,"
        else: wh.append([a, b, w])
    for v in wh:                                                                 # a word stretched back over a pause
        for s, e in sil:
            if v[0] - 0.05 <= s < v[0] + 0.25 and e < v[1] - 0.05: v[0] = e
    # script words get Whisper's raw times
    sw, land = script_words(); SA = [norm(w) for w in sw]; SB = [norm(v[2]) for v in wh]
    times = [None] * len(sw)
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, SA, SB, autojunk=False).get_opcodes():
        if op == 'equal':
            for k in range(i2 - i1): times[i1 + k] = (wh[j1 + k][0], wh[j1 + k][1])
        elif op == 'replace' or (op == 'delete' and j1 > 0):
            a = wh[j1][0] if j2 > j1 else wh[j1 - 1][1]; b = wh[j2 - 1][1] if j2 > j1 else a; n = i2 - i1
            for k in range(n): times[i1 + k] = (a + (b - a) * k / n, a + (b - a) * (k + 1) / n)
            if op == 'replace': print(f'  spread: {" ".join(sw[i1:i2])!r} over {" ".join(v[2] for v in wh[j1:j2])!r}')
        elif op == 'insert':
            print(f'  Whisper only: {" ".join(v[2] for v in wh[j1:j2])!r}')
    buts = [a for a, b, w in wh if norm(w) == 'but']
    first, last = wh[0][0], wh[-1][1]

    def build(extra):
        """extra: [(raw time to split at, seconds of silence to add there)]. Returns the pieces [(a, b, pad before)]."""
        pieces = []; t = max(0.0, first - LEAD); notes = []
        for s, e in sil:
            if e <= first or s >= last: continue
            is_beat = any(abs(e - b) < 0.35 for b in buts)
            pieces.append([t, s + KEEP, 0.0]); t = e - KEEP
            notes.append((s, e, is_beat, max(0.0, BEAT * TEMPO - 2 * KEEP) if is_beat else 0.0))
        pieces.append([t, min(dur, last + TAIL), 0.0])
        for i, n in enumerate(notes): pieces[i + 1][2] = n[3]
        for ts, pad in sorted(extra):
            for i, (a, b, p) in enumerate(pieces):
                if a < ts < b:                                                   # split this piece at ts
                    pieces[i:i + 1] = [[a, ts, p], [ts, b, pad]]; break
                if i + 1 < len(pieces) and b <= ts <= pieces[i + 1][0]:          # ts is in a pause already cut here
                    pieces[i + 1][2] += pad; break
        return pieces, notes
    def mapper(pieces):
        seg = []; pos = 0.0
        for a, b, pad in pieces: pos += pad; seg.append((a, b, pos)); pos += b - a
        def mapt(t):
            for a, b, p in seg:
                if t < a: return p / TEMPO
                if t <= b: return (p + t - a) / TEMPO
            a, b, p = seg[-1]; return (p + b - a) / TEMPO
        return mapt, pos
    # pass 1: no step beats; measure the gaps between landings inside each sentence
    pieces, notes = build([]); mapt, _ = mapper(pieces)
    lands = [i for i, f in enumerate(land) if f]; extra = []; report = []
    def quietest(a, b):
        """The quietest 20 ms between raw times a and b: where a silence can be let in without cutting a word."""
        a, b = max(0.0, a - 0.04), min(dur, b + 0.04); n = int(0.02 * SR); best = (1e9, (a + b) / 2)
        for s0 in range(int(a * SR), max(int(a * SR) + 1, int(b * SR) - n), n // 4):
            e = float(np.sqrt(np.mean(x[s0:s0 + n] ** 2)))
            if e < best[0]: best = (e, (s0 + n / 2) / SR)
        return best[1]
    for n, (i, j) in enumerate(zip(lands, lands[1:])):
        if any(sw[k].rstrip('"').endswith(('.', '?', '!', ':')) for k in range(i, j)): continue     # not the same sentence
        gap = mapt(times[j][0]) - mapt(times[i][0]); want = GAPS.get(n, STEP_GAP)
        pad = min(max(0.0, want - gap), MAXPAD)
        if pad > 0.02: extra.append((quietest(times[i][1], times[i + 1][0]), pad * TEMPO))
        report.append((n, sw[i], sw[j], gap, want, pad))
    pieces, notes = build(extra); mapt, pos = mapper(pieces)
    out = []; fade = int(0.005 * SR)
    for a, b, pad in pieces:
        if pad: out.append(np.zeros(int(round(pad * SR)), np.float32))
        y = x[int(a * SR):int(b * SR)].copy()
        if len(y) > 2 * fade: y[:fade] *= np.linspace(0, 1, fade); y[-fade:] *= np.linspace(1, 0, fade)
        out.append(y)
    tmp = os.path.join(WORK, f'audio/narr_{OUT}_1x.wav')
    with wave.open(tmp, 'wb') as f:
        f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR)
        f.writeframes((np.clip(np.concatenate(out), -1, 1) * 32767).astype('<i2').tobytes())
    dst = os.path.join(WORK, f'audio/narr_{OUT}.wav')
    run(['ffmpeg', '-y', '-v', 'error', '-i', tmp, '-af', f'atempo={TEMPO}', '-ar', str(SR), '-ac', '1', dst])
    res = [{'w': w, 'a': round(mapt(a), 3), 'b': round(mapt(b), 3), **({'land': True} if f else {})}
           for w, (a, b), f in zip(sw, times, land)]
    json.dump(res, open(os.path.join(WORK, f'audio/words_{OUT}.json'), 'w'), indent=0)
    total = float(run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', dst]).stdout)
    print(f'raw {dur:.2f} s -> x{TEMPO} {total:.2f} s; {len(notes)} pauses tightened, {sum(n[2] for n in notes)} beats, '
          f'{len(extra)} step beats; {len(sw)} script words, {sum(land)} landing words')
    print('step beats (landing -> next landing: gap before, wanted, silence added, gap after):')
    for n, a, b, gap, want, pad in report:
        flag = '   << STILL SHORT: lengthen this phrase in the script' if gap + pad < want - 0.02 else ''
        print(f'  {n:2d} {a:12s} -> {b:12s} {gap:4.2f}  want {want:4.2f}  +{pad:4.2f}  = {gap + pad:4.2f}{flag}')
    line = []
    for r in res:
        line.append(f"{r['w']}@{r['a']:.2f}" + ('*' if r.get('land') else ''))
        if r['w'].endswith(('.', '?')): print('  ' + ' '.join(line)); line = []
    if line: print('  ' + ' '.join(line))

if __name__ == '__main__':
    main()
