# usage: python3 15-mk.py KEY [KEY ...]  -> JSON requests for generate_image_batch (indices 0..n-1, refs from REFS via 15-jobs.tsv)
# A key may carry a try suffix after a dot (SIDE0.B uses SIDE0's prompt and refs); refs resolve to the latest accepted job of each key.
import importlib.util, json, sys
spec = importlib.util.spec_from_file_location("p15", __file__.replace("15-mk.py", "15-prompts.py")); p15 = importlib.util.module_from_spec(spec); spec.loader.exec_module(p15)
J = {}
try:
    for l in open(__file__.replace("15-mk.py", "15-jobs.tsv")):
        if l.strip() and not l.startswith("#") and not l.startswith("key"):
            k, j = l.split("\t")[:2]; J[k] = j.strip()
except FileNotFoundError:
    pass
FOLDER = "7537e99d-691b-4212-8723-c068ec0f29ba"  # Higgsfield project "HBX – Why This NFL Field Is Sitting on 546 Wheels"
out = []
for i, key in enumerate(sys.argv[1:]):
    k = key if key in p15.P else key.split(".")[0]
    prm = {"model": "seedream_v5_pro", "resolution": "1k", "aspect_ratio": p15.AR.get(k, "9:16"), "folder_id": FOLDER, "prompt": p15.P[k]}
    refs = p15.REFS[k]
    if refs: prm["medias"] = [{"role": "image_references", "value": J[r]} for r in refs]
    out.append({"index": i, "params": prm})
print(json.dumps(out, ensure_ascii=False))
