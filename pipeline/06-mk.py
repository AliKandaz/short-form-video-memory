# usage: python3 06-mk.py KEY [KEY ...]  -> JSON requests for generate_image_batch (indices 0..n-1, refs from REFS via 06-jobs.tsv)
import importlib.util, json, sys
spec = importlib.util.spec_from_file_location("p06", __file__.replace("06-mk.py", "06-prompts.py")); p06 = importlib.util.module_from_spec(spec); spec.loader.exec_module(p06)
J = {}
for l in open(__file__.replace("06-mk.py", "06-jobs.tsv")):
    if l.strip() and not l.startswith("#") and not l.startswith("key"):
        k, j = l.split("\t")[:2]; J[k] = j.strip()
FOLDER = "452e85a7-bd8f-4644-bdab-cb74b076b356"  # Higgsfield project "HBX – Hidden City of Petra"
out = []
for i, k in enumerate(sys.argv[1:]):
    prm = {"model": "seedream_v5_pro", "resolution": "1k", "aspect_ratio": p06.AR.get(k, "9:16"), "folder_id": FOLDER, "prompt": p06.P[k]}
    refs = p06.REFS[k]
    if refs: prm["medias"] = [{"role": "image_references", "value": J[r]} for r in refs]
    out.append({"index": i, "params": prm})
print(json.dumps(out, ensure_ascii=False))
