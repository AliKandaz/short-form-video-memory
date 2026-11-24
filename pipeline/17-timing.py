# Video 17: tighten the narration and give every script word its time (CLAUDE.md 6.2 Step 6; written 24 Nov 2026).
# Like 16-timing.py, with the beats of the build-steps style (4.3): every pause is tightened to 0.15 s, except the pause
# before each "But" (the first one is also the beat after the premise), which is set to BEAT seconds once sped up. Pauses
# shorter than the beat are padded with silence. Then the take is sped up to TEMPO (never past 1.1, 7.5).
#
#   python3 17-timing.py <work dir>
#     reads  <work>/audio/narr_A.mp3, <work>/audio/words_takeA.json (Whisper's words: [start, end, text] in the raw take),
#            17-script.txt (next to this file; the captions take their text from it)
#     writes <work>/audio/narr_tight.wav (mono, 44.1 kHz) and <work>/audio/words_tight.json:
#            [{"w": script word, "a": start, "b": end}] in the tightened take's time, and prints the timeline.
import json, os, re, subprocess, sys, difflib
import numpy as np

WORK = sys.argv[1] if len(sys.argv) > 1 else '.'
HERE = os.path.dirname(os.path.abspath(__file__))
SR, TEMPO = 44100, 1.1
KEEP = 0.075            # kept at each side of a tightened pause: 0.15 s raw, 0.136 s after the speed-up
BEAT = 0.50             # the beat before each "But", after the speed-up
LEAD, TAIL = 0.03, 0.20  # silence kept before the first word and after the last
SIL_DB, SIL_D = -38, 0.25

def run(cmd): return subprocess.run(cmd, check=True, capture_output=True, text=True)

def script_words():
    txt = open(os.path.join(HERE, '17-script.txt')).read().split('\n')
    body = [l for l in txt[9:] if l.strip()]                         # the spoken text starts on line 10
    words = ' '.join(body)
    words = re.sub(r'\s*\[[^\]]*\]', '', words)                      # drop the [landing] marks
    return words.split()

def norm(w): return re.sub(r'[^a-z0-9$]', '', w.lower())

def main():
    raw = os.path.join(WORK, 'audio/narr_A.mp3'); wav = os.path.join(WORK, 'audio/narr_A.wav')
    run(['ffmpeg', '-y', '-v', 'error', '-i', raw, '-ac', '1', '-ar', str(SR), wav])
    x = np.frombuffer(run(['ffmpeg', '-v', 'error', '-i', wav, '-f', 's16le', '-ac', '1', '-ar', str(SR), '-']).stdout
                      if False else open(wav, 'rb').read()[44:], dtype='<i2').astype(np.float32) / 32768
    dur = len(x) / SR
    log = run(['ffmpeg', '-v', 'info', '-i', wav, '-af', f'silencedetect=noise={SIL_DB}dB:d={SIL_D}', '-f', 'null', '-']).stderr
    st = [float(v) for v in re.findall(r'silence_start: ([\d.]+)', log)]
    en = [float(v) for v in re.findall(r'silence_end: ([\d.]+)', log)]
    sil = list(zip(st, en + [dur] * (len(st) - len(en))))
    ww = json.load(open(os.path.join(WORK, 'audio/words_takeA.json')))
    # Whisper splits "T-rex", "ha-ha" and "$180,000": join a piece that starts with "-" or "," to the word before it
    wh = []
    for a, b, w in ww:
        if wh and w[:1] in '-,': wh[-1] = [wh[-1][0], b, wh[-1][2] + w]
        else: wh.append([a, b, w])
    # a word Whisper stretched back over a pause (it starts in the silence) starts where the silence ends
    for v in wh:
        for s, e in sil:
            if v[0] - 0.05 <= s < v[0] + 0.25 and e < v[1] - 0.05: v[0] = e
    buts = [a for a, b, w in wh if norm(w) == 'but']
    first, last = wh[0][0], wh[-1][1]
    # the pieces of the raw take to keep, and the silence to insert before each piece
    pieces = []; t = max(0.0, first - LEAD); gaps = []
    for s, e in sil:
        if e <= first or s >= last: continue
        is_beat = any(abs(e - b) < 0.35 for b in buts)
        pieces.append((t, s + KEEP))
        pad = max(0.0, BEAT * TEMPO - 2 * KEEP) if is_beat else 0.0
        gaps.append((s, e, is_beat, pad))
        t = e - KEEP
    pieces.append((t, min(dur, last + TAIL)))
    pads = [0.0] + [g[3] for g in gaps]
    # build the tightened take: each piece with 5 ms fades, the pads as silence
    out = []; fade = int(0.005 * SR); seg_map = []; pos = 0.0
    for (a, b), pad in zip(pieces, pads):
        if pad: out.append(np.zeros(int(round(pad * SR)), np.float32)); pos += pad
        y = x[int(a * SR):int(b * SR)].copy()
        if len(y) > 2 * fade:
            y[:fade] *= np.linspace(0, 1, fade); y[-fade:] *= np.linspace(1, 0, fade)
        seg_map.append((a, b, pos)); out.append(y); pos += len(y) / SR
    y = np.concatenate(out)
    tmp = os.path.join(WORK, 'audio/narr_tight_1x.wav')
    import wave
    with wave.open(tmp, 'wb') as f:
        f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR)
        f.writeframes((np.clip(y, -1, 1) * 32767).astype('<i2').tobytes())
    dst = os.path.join(WORK, 'audio/narr_tight.wav')
    run(['ffmpeg', '-y', '-v', 'error', '-i', tmp, '-af', f'atempo={TEMPO}', '-ar', str(SR), '-ac', '1', dst])
    def mapt(t):
        for a, b, p in seg_map:
            if t < a: return p / TEMPO                    # inside a cut pause: snap to the next piece
            if t <= b: return (p + t - a) / TEMPO
        a, b, p = seg_map[-1]; return (p + b - a) / TEMPO
    # script words get Whisper's times (difflib; a replaced span is spread evenly, as in 16-timing.py)
    sw = script_words(); A = [norm(w) for w in sw]; B = [norm(w) for w in (v[2] for v in wh)]
    times = [None] * len(sw)
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, A, B, autojunk=False).get_opcodes():
        if op == 'equal':
            for k in range(i2 - i1): times[i1 + k] = (wh[j1 + k][0], wh[j1 + k][1])
        elif op == 'replace' or (op == 'delete' and j1 > 0):
            a = wh[j1][0] if j2 > j1 else wh[j1 - 1][1]; b = wh[j2 - 1][1] if j2 > j1 else a
            n = i2 - i1
            for k in range(n): times[i1 + k] = (a + (b - a) * k / n, a + (b - a) * (k + 1) / n)
            if op == 'replace': print(f'  spread: {" ".join(sw[i1:i2])!r} over {" ".join(v[2] for v in wh[j1:j2])!r}')
        elif op == 'insert':
            print(f'  Whisper only: {" ".join(v[2] for v in wh[j1:j2])!r}')
    res = [{'w': w, 'a': round(mapt(a), 3), 'b': round(mapt(b), 3)} for w, (a, b) in zip(sw, times)]
    json.dump(res, open(os.path.join(WORK, 'audio/words_tight.json'), 'w'), indent=0)
    total = float(run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', dst]).stdout)
    print(f'raw {dur:.2f} s -> tightened {pos:.2f} s -> x{TEMPO} {total:.2f} s; {len(gaps)} pauses, '
          f'{sum(g[2] for g in gaps)} beats; {len(sw)} script words, {len(wh)} Whisper words')
    for s, e, b, pad in gaps:
        print(f'  pause {s:6.2f}-{e:6.2f} ({e - s:.2f} s) -> {(2 * KEEP + pad) / TEMPO:.2f} s{"  BEAT" if b else ""}')
    line = []
    for r in res:
        line.append(f"{r['w']}@{r['a']:.2f}")
        if r['w'].endswith(('.', '?')): print('  ' + ' '.join(line)); line = []
    if line: print('  ' + ' '.join(line))

if __name__ == '__main__':
    main()
