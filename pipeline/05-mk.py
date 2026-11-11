# usage: python3 05-mk.py KEY [KEY ...]  -> JSON requests for generate_image_batch (indices 0..n-1, refs from REFS via 05-jobs.tsv)
import importlib.util, json, sys
spec = importlib.util.spec_from_file_location("p05", __file__.replace("05-mk.py", "05-prompts.py")); p05 = importlib.util.module_from_spec(spec); spec.loader.exec_module(p05)
J = {}
for l in open(__file__.replace("05-mk.py", "05-jobs.tsv")):
    if l.strip() and not l.startswith("#") and not l.startswith("key"):
        k, j = l.split("\t")[:2]; J[k] = j.strip()
FOLDER = "696a691c-e24b-415f-96a3-427d896b05e2"
out = []
for i, k in enumerate(sys.argv[1:]):
    prm = {"model": "seedream_v5_pro", "resolution": "1k", "aspect_ratio": p05.AR.get(k, "9:16"), "folder_id": FOLDER, "prompt": p05.P[k]}
    refs = p05.REFS[k]
    if refs: prm["medias"] = [{"role": "image_references", "value": J[r]} for r in refs]
    out.append({"index": i, "params": prm})
print(json.dumps(out, ensure_ascii=False))
