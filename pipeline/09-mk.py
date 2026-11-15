# usage: python3 09-mk.py KEY [KEY ...]  -> JSON requests for generate_image_batch (indices 0..n-1, refs from REFS via 09-jobs.tsv)
import importlib.util, json, sys
spec = importlib.util.spec_from_file_location("p09", __file__.replace("09-mk.py", "09-prompts.py")); p09 = importlib.util.module_from_spec(spec); spec.loader.exec_module(p09)
J = {}
try:
    for l in open(__file__.replace("09-mk.py", "09-jobs.tsv")):
        if l.strip() and not l.startswith("#") and not l.startswith("key"):
            k, j = l.split("\t")[:2]; J[k] = j.strip()
except FileNotFoundError:
    pass
FOLDER = "783ef666-4a82-436a-90f9-36e3983264a4"  # Higgsfield project "HBX – What Lightning Does Inside Your House"
out = []
for i, k in enumerate(sys.argv[1:]):
    prm = {"model": "seedream_v5_pro", "resolution": "1k", "aspect_ratio": p09.AR.get(k, "9:16"), "folder_id": FOLDER, "prompt": p09.P[k]}
    refs = p09.REFS[k]
    if refs: prm["medias"] = [{"role": "image_references", "value": J[r]} for r in refs]
    out.append({"index": i, "params": prm})
print(json.dumps(out, ensure_ascii=False))
