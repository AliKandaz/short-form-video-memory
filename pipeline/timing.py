import json, re, subprocess, difflib
def silences(path, d):
    out=subprocess.run(['ffmpeg','-i',path,'-af',f'silencedetect=noise=-38dB:d={d}','-f','null','-'],capture_output=True,text=True).stderr
    return [float(x) for x in re.findall(r'silence_start: ([\d.]+)',out)],[float(x) for x in re.findall(r'silence_end: ([\d.]+)',out)]
dur=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0','audio/take1.wav'],capture_output=True,text=True).stdout)
st,en=silences('audio/take1.wav',0.25)
keep=0.075; segs=[]; cur=0.0
for s,e in zip(st,en):
    if s<0.05: cur=max(cur,e-0.05); continue
    if e>=dur-0.01: segs.append((cur,s+0.15)); cur=None; break
    segs.append((cur,s+keep)); cur=e-keep
if cur is not None: segs.append((cur,dur))
offs=[];acc=0.0
for a,b in segs: offs.append((a,b,acc)); acc+=b-a
TIGHT=acc
def o2t(t):
    for a,b,o in offs:
        if t<a: return o
        if t<=b: return o+(t-a)
    return TIGHT
W=json.load(open('audio/words_take1.json'))
script=open('script.txt').read().split()
norm=lambda w: re.sub(r"[^a-z0-9']","",w.lower())
sm=difflib.SequenceMatcher(a=[norm(x) for x in script],b=[norm(w[2]) for w in W],autojunk=False)
T=[None]*len(script)
for tag,i1,i2,j1,j2 in sm.get_opcodes():
    if tag in('equal','replace'):
        for k in range(min(i2-i1,j2-j1)): T[i1+k]=(W[j1+k][0],W[j1+k][1])
for i in range(len(script)):           # fill any gaps by interpolation
    if T[i] is None:
        p=T[i-1][1] if i>0 and T[i-1] else 0.0
        n=next((T[j][0] for j in range(i+1,len(script)) if T[j]),p+0.3)
        T[i]=(p,min(n,p+0.3))
words=[[round(o2t(a),3),round(o2t(b),3),w] for (a,b),w in zip(T,script)]
json.dump(words,open('audio/words_tight.json','w'))
beats=[("B1","If"),("B2","But by noon"),("B3","So you mix"),("B4","But wet bricks"),("B5","But thin walls"),("B6","The heat takes"),
 ("B7","But at night"),("B8","But a flat"),("B9","But the deadliest"),("B10a","So you tilt"),("B10b","And you set"),("B11","Then you paint"),
 ("B12","Then the storm"),("B13","But yours"),("B14","Add a clay")]
toks=[norm(x) for x in script]; starts=[]
for b,ph in beats:
    p=[norm(x) for x in ph.split()]
    idx=next(i for i in range(len(toks)) if toks[i:i+len(p)]==p and (not starts or i>starts[-1][1]))
    starts.append((b,idx))
TAIL=0.9
out=[]
for k,(b,idx) in enumerate(starts):
    s=0.0 if k==0 else words[idx][0]-0.08
    e=(words[starts[k+1][1]][0]-0.08) if k+1<len(starts) else TIGHT+TAIL
    out.append({"beat":b,"start":round(s,3),"end":round(e,3),"len":round(e-s,3),"first_word":idx})
json.dump({"total":round(TIGHT+TAIL,3),"beats":out},open('timeline.json','w'),indent=1)
print('narration',round(TIGHT,2),'s; video',round(TIGHT+TAIL,2),'s')
for x in out: print(f"{x['beat']:5} {x['start']:6.2f} -> {x['end']:6.2f}  ({x['len']:.2f}s)")
