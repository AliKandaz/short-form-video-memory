# The narration check (CLAUDE.md 6.2 Step 6; written 24 Nov 2026 after the user's review of video 17).
# Runs in the Higgsfield sandbox, where faster-whisper is installed and its models can be fetched (free):
#   python3 narration-check.py <take.mp3 or its https result URL> <script.txt> [out.json]
#
# Why: video 17's check gave Whisper the script's rare words in `initial_prompt`, and Whisper duly "heard" them. The take
# said "This is a ha-ha" exactly as written and passed word for word, but to a listener it is a laugh ("this is a ahah", the
# user). So the recogniser is told NOTHING here, and three things are reported:
#   1. the script against what was heard, with no prompt (a word that differs is a slip of the voice, or a word that does
#      not survive being heard);
#   2. every word the recogniser was unsure of (probability under 0.6; "ha" scored 0.25-0.37), and any "!" or "?" it heard
#      that the script does not have (it heard "This is a ha ha!");
#   3. each naming sentence of the script ("This is a ...") cut out of the take and heard ALONE by two models, word for
#      word, as a viewer who missed the caption would hear it.
# A flagged term fails the ear test (CLAUDE.md 4.3): change the term, don't respell it. Everything flagged is listed for the
# user with its time, and the user hears the whole take at Gate C. The words it writes ([start, end, text], no prompt) are
# the ones steps-timing.py reads.
import difflib, json, re, subprocess, sys
from faster_whisper import WhisperModel

src, script = sys.argv[1], sys.argv[2]
out = sys.argv[3] if len(sys.argv) > 3 else 'narration-check.json'
if src.startswith('http'):
    subprocess.run(['curl', '-sfL', '-o', 'take.mp3', src], check=True); src = 'take.mp3'

def norm(w): return re.sub(r"[^a-z0-9$]", '', w.lower())
def spoken(path):
    txt = open(path).read().split('\n'); start = next(i for i, l in enumerate(txt) if l.startswith('If '))
    return re.sub(r'\s*\[[^\]]*\]', '', ' '.join(l for l in txt[start:] if l.strip())).split()
def hear(m, path):
    segs, info = m.transcribe(path, word_timestamps=True, beam_size=5, language='en', condition_on_previous_text=False)
    return [[round(w.start, 2), round(w.end, 2), w.word.strip(), round(float(w.probability), 2)] for s in segs for w in s.words]

small = WhisperModel('small.en', device='cpu', compute_type='int8')
W = hear(small, src)
J = []                                                   # "T", "-rex," -> "T-rex,"
for a, b, w, p in W:
    if J and w[:1] in '-,': J[-1] = [J[-1][0], b, J[-1][2] + w, min(J[-1][3], p)]
    else: J.append([a, b, w, p])
sw = spoken(script); A = [norm(w) for w in sw]; B = [norm(w[2]) for w in J]
flags = []
print('1. THE SCRIPT AGAINST WHAT WAS HEARD (no prompt):')
same = True
for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, A, B, autojunk=False).get_opcodes():
    if op == 'equal': continue
    said, heard = ' '.join(sw[i1:i2]), ' '.join(w[2] for w in J[j1:j2])
    if re.sub(r'[^a-z0-9]', '', said.lower()) and heard.replace(',', '').replace('$', '').replace('.', '').isdigit(): continue   # a number said in words
    t = J[min(j1, len(J) - 1)][0]; same = False
    print(f'   at {t:6.2f} s  script "{said}"  heard "{heard}"'); flags.append(dict(t=t, kind='differs', script=said, heard=heard))
print('   word for word' if same else '   ^ these differ')
print('2. WORDS THE RECOGNISER WAS UNSURE OF (p < 0.6), AND MARKS THE SCRIPT DOES NOT HAVE:')
text = ' '.join(sw)
for a, b, w, p in J:
    if p < 0.6:
        print(f'   at {a:6.2f} s  "{w}"  p {p}'); flags.append(dict(t=a, kind='unsure', heard=w, p=p))
    if w[-1:] in '!?' and (norm(w) + w[-1]) not in re.sub(r"[^a-z0-9$!?]", '', text.lower()):
        print(f'   at {a:6.2f} s  heard "{w}": a "{w[-1]}" the script does not have'); flags.append(dict(t=a, kind='mark', heard=w))
print('3. EACH NAMING SENTENCE HEARD ALONE, BY TWO MODELS:')
def joined(h):                                           # the same joining as above: "ha", "-ha!" -> "ha-ha!"
    out = []
    for a, b, w, p in h:
        if out and w[:1] in '-,': out[-1] = [out[-1][0], b, out[-1][2] + w, min(out[-1][3], p)]
        else: out.append([a, b, w, p])
    return out
models = [('small.en', small)]
try: models.append(('medium.en', WhisperModel('medium.en', device='cpu', compute_type='int8')))
except Exception as e: print('   (medium.en could not be loaded:', repr(e)[:120], ')')
where = {}                                               # script word -> the heard words it was matched to
for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, A, B, autojunk=False).get_opcodes():
    if op == 'equal':
        for k in range(i2 - i1): where[i1 + k] = (j1 + k, j1 + k)
    elif op == 'replace':
        for k in range(i1, i2): where[k] = (j1, j2 - 1)
i = 0
while i < len(sw):                                       # the sentences are taken from the SCRIPT, not from what was heard
    if norm(sw[i]) == 'this' and i + 1 < len(sw) and norm(sw[i + 1]) == 'is' and (i == 0 or sw[i - 1][-1:] in '.!?:'):
        j = i
        while j < len(sw) - 1 and sw[j][-1:] not in '.!?': j += 1
        want = ' '.join(sw[i:j + 1]); ks = [where[k] for k in range(i, j + 1) if k in where]
        if not ks:
            print(f'   "{want}": not found in the take   << LOOK'); flags.append(dict(kind='alone', sentence=want, heard=None)); i = j + 1; continue
        a, b = max(0, J[min(k[0] for k in ks)][0] - 0.25), J[max(k[1] for k in ks)][1] + 0.35
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-ss', f'{a:.2f}', '-t', f'{b - a:.2f}', '-i', src, '-ac', '1', '-ar', '16000', 'one.wav'], check=True)
        for name, m in models:
            h = joined(hear(m, 'one.wav')); got = ' '.join(x[2] for x in h)
            k = next((n for n, x in enumerate(h) if norm(x[2]) == 'this'), 0); t = h[k:]      # a scrap of the word before is ignored
            low = [x[2] for x in t if x[3] < 0.6]
            ok = [norm(x[2]) for x in t] == [norm(w) for w in sw[i:j + 1]] and not low and not any(x[2][-1:] in '!?' for x in t)
            print(f'   {a:6.2f} s  "{want}"  {name}: "{got}"' + ('' if ok else f'   << LOOK: unsure of {low}' if low else '   << LOOK'))
            if not ok: flags.append(dict(t=a, kind='alone', sentence=want, model=name, heard=got, unsure=low))
        i = j
    i += 1
json.dump(dict(words=[[a, b, w] for a, b, w, p in W], probs=[p for a, b, w, p in W], flags=flags), open(out, 'w'))
print(f'{len(W)} words; last ends {W[-1][1]} s; {len(flags)} flags; wrote {out}')
