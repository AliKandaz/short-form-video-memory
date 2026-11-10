# usage: python3 04-mk.py KEY [KEY ...]  -> JSON requests for generate_image_batch (indices 0..n-1, refs from REFS via 04-jobs.tsv)
import importlib.util, json, sys
spec = importlib.util.spec_from_file_location("p04", __file__.replace("04-mk.py", "04-prompts.py")); p04 = importlib.util.module_from_spec(spec); spec.loader.exec_module(p04)
J = {}
for l in open(__file__.replace("04-mk.py", "04-jobs.tsv")):
    if l.strip() and not l.startswith("#") and not l.startswith("key"):
        k, j = l.split("\t")[:2]; J[k] = j.strip()
FOLDER = "95b78d03-a34b-4999-b679-1c8f5371f9de"
out = []
for i, k in enumerate(sys.argv[1:]):
    prm = {"model": "seedream_v5_pro", "resolution": "1k", "aspect_ratio": "9:16", "folder_id": FOLDER, "prompt": p04.P[k]}
    refs = p04.REFS[k]
    if refs: prm["medias"] = [{"role": "image_references", "value": J[r]} for r in refs]
    out.append({"index": i, "params": prm})
print(json.dumps(out, ensure_ascii=False))
