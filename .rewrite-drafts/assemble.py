"""Assemble the new CLAUDE.md from parts and check internal section references. Usage: assemble.py <parts_dir> <out>"""
import re, sys, os
d, out = sys.argv[1], sys.argv[2]
order = ['00-start','01-what-works','02-plan','03-ideas','04-script','05-look','06-runbook','07-lessons','08-posting',
         '09-results','10-money','11-prompts','12-reading','13-parked']
parts = []
for p in order:
    fn = os.path.join(d, p + '.md')
    if not os.path.exists(fn):
        print('MISSING PART', p); continue
    parts.append(open(fn, encoding='utf-8').read().rstrip('\n') + '\n')
text = '\n'.join(parts)
open(out, 'w', encoding='utf-8').write(text)
heads = set()
for m in re.finditer(r'^(#{2,3}) (\d+)(?:\.(\d+))?\.? ', text, re.M):
    heads.add(m.group(2) + ('.' + m.group(3) if m.group(3) else ''))
# references like (6.1), (4.2, 6.2 Gate D), "section 3", "in 9.2", "13.1)"
refs = set()
for m in re.finditer(r'(?<![\d.,$×x])\b(\d{1,2})\.(\d{1,2})\b(?![\d.%]| ?(?:s\b|px|words|w/s|dB|M\b|K\b|×|x\b|cr|credits|LUFS|km|m\b|ft|in\b|°|million|times))', text):
    refs.add(f'{m.group(1)}.{m.group(2)}')
for m in re.finditer(r'\bsections? (\d{1,2})\b', text):
    refs.add(m.group(1))
bad = sorted(r for r in refs if r not in heads and r.split('.')[0] in {str(i) for i in range(0, 14)})
print('lines', text.count('\n'), 'chars', len(text))
print('headings', sorted(heads, key=lambda x: [int(i) for i in x.split('.')]))
print('refs not found as headings (check by hand; many are numbers, not refs):', bad)
