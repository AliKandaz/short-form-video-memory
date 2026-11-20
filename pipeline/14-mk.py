# usage: python3 14-mk.py KEY [KEY ...]  -> JSON requests for generate_image_batch (indices 0..n-1, refs from REFS via 14-jobs.tsv)
# A key may carry a try suffix after a dot (ST0.B uses ST0's prompt and refs); refs resolve to the latest accepted job of each key.
import importlib.util, json, sys
spec = importlib.util.spec_from_file_location("p14", __file__.replace("14-mk.py", "14-prompts.py")); p14 = importlib.util.module_from_spec(spec); spec.loader.exec_module(p14)
J = {}
try:
    for l in open(__file__.replace("14-mk.py", "14-jobs.tsv")):
        if l.strip() and not l.startswith("#") and not l.startswith("key"):
            k, j = l.split("\t")[:2]; J[k] = j.strip()
except FileNotFoundError:
    pass
FOLDER = "0bef4887-0b2b-4935-aa7d-409e5caab067"  # Higgsfield project "HBX – Why It Rains Inside a Nuclear Cooling Tower"
out = []
for i, key in enumerate(sys.argv[1:]):
    k = key if key in p14.P else key.split(".")[0]
    prm = {"model": "seedream_v5_pro", "resolution": "1k", "aspect_ratio": p14.AR.get(k, "9:16"), "folder_id": FOLDER, "prompt": p14.P[k]}
    refs = p14.REFS[k]
    if refs: prm["medias"] = [{"role": "image_references", "value": J[r]} for r in refs]
    out.append({"index": i, "params": prm})
print(json.dumps(out, ensure_ascii=False))
