# usage: python3 13-mk.py KEY [KEY ...]  -> JSON requests for generate_image_batch (indices 0..n-1, refs from REFS via 13-jobs.tsv)
# A key may carry a try suffix after a dot (ST0.B uses ST0's prompt and refs); refs resolve to the latest accepted job of each key.
import importlib.util, json, sys
spec = importlib.util.spec_from_file_location("p13", __file__.replace("13-mk.py", "13-prompts.py")); p13 = importlib.util.module_from_spec(spec); spec.loader.exec_module(p13)
J = {}
try:
    for l in open(__file__.replace("13-mk.py", "13-jobs.tsv")):
        if l.strip() and not l.startswith("#") and not l.startswith("key"):
            k, j = l.split("\t")[:2]; J[k] = j.strip()
except FileNotFoundError:
    pass
FOLDER = "7377ac71-fa47-499b-b891-0d4c57eccc6d"  # Higgsfield project "HBX – Why Firefighters Drop Frozen Turkeys Into Fryers"
out = []
for i, key in enumerate(sys.argv[1:]):
    k = key.split(".")[0]
    prm = {"model": "seedream_v5_pro", "resolution": "1k", "aspect_ratio": p13.AR.get(k, "9:16"), "folder_id": FOLDER, "prompt": p13.P[k]}
    refs = p13.REFS[k]
    if refs: prm["medias"] = [{"role": "image_references", "value": J[r]} for r in refs]
    out.append({"index": i, "params": prm})
print(json.dumps(out, ensure_ascii=False))
