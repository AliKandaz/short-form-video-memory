# usage: python3 10-mk.py KEY [KEY ...]  -> JSON requests for generate_image_batch (indices 0..n-1, refs from REFS via 10-jobs.tsv)
import importlib.util, json, sys
spec = importlib.util.spec_from_file_location("p10", __file__.replace("10-mk.py", "10-prompts.py")); p10 = importlib.util.module_from_spec(spec); spec.loader.exec_module(p10)
J = {}
try:
    for l in open(__file__.replace("10-mk.py", "10-jobs.tsv")):
        if l.strip() and not l.startswith("#") and not l.startswith("key"):
            k, j = l.split("\t")[:2]; J[k] = j.strip()
except FileNotFoundError:
    pass
FOLDER = "dc9cd687-a9ef-4334-a7db-29df6b684c68"  # Higgsfield project "HBX – Why These People Are Frozen Upside Down"
out = []
for i, k in enumerate(sys.argv[1:]):
    prm = {"model": "seedream_v5_pro", "resolution": "1k", "aspect_ratio": p10.AR.get(k, "9:16"), "folder_id": FOLDER, "prompt": p10.P[k]}
    refs = p10.REFS[k]
    if refs: prm["medias"] = [{"role": "image_references", "value": J[r]} for r in refs]
    out.append({"index": i, "params": prm})
print(json.dumps(out, ensure_ascii=False))
