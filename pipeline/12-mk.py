# usage: python3 12-mk.py KEY [KEY ...]  -> JSON requests for generate_image_batch (indices 0..n-1, refs from REFS via 12-jobs.tsv)
# A key may carry a try suffix after a dot (ST0.B uses ST0's prompt and refs); refs resolve to the latest accepted job of each key.
import importlib.util, json, sys
spec = importlib.util.spec_from_file_location("p12", __file__.replace("12-mk.py", "12-prompts.py")); p12 = importlib.util.module_from_spec(spec); spec.loader.exec_module(p12)
J = {}
try:
    for l in open(__file__.replace("12-mk.py", "12-jobs.tsv")):
        if l.strip() and not l.startswith("#") and not l.startswith("key"):
            k, j = l.split("\t")[:2]; J[k] = j.strip()
except FileNotFoundError:
    pass
FOLDER = "25f62fea-3516-4722-a1d8-62520102b743"  # Higgsfield project "HBX – Why Some Manhole Covers Are Full of Holes"
out = []
for i, key in enumerate(sys.argv[1:]):
    k = key.split(".")[0]
    prm = {"model": "seedream_v5_pro", "resolution": "1k", "aspect_ratio": p12.AR.get(k, "9:16"), "folder_id": FOLDER, "prompt": p12.P[k]}
    refs = p12.REFS[k]
    if refs: prm["medias"] = [{"role": "image_references", "value": J[r]} for r in refs]
    out.append({"index": i, "params": prm})
print(json.dumps(out, ensure_ascii=False))
