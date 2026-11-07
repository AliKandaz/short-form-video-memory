# usage: python3 mk.py IDX:KEY:REF1,REF2[:AR] ...  (refs are keys from jobs.tsv) -> prints JSON requests
import sys, json, prompts
J=dict(l.split('\t') for l in open('jobs.tsv').read().split('\n') if l.strip())
out=[]
for a in sys.argv[1:]:
    parts=a.split(':'); i,k,refs=parts[0],parts[1],parts[2]; ar=parts[3] if len(parts)>3 else "9:16"
    out.append({"index":int(i),"params":{"model":"seedream_v5_pro","resolution":"1k","aspect_ratio":ar,"prompt":prompts.P[k],
      "medias":[{"role":"image_references","value":J[r].strip()} for r in refs.split(',')]}})
print(json.dumps(out))
