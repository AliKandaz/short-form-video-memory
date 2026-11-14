# usage: python3 07-mk.py KEY [KEY ...]  -> JSON requests for generate_image_batch (indices 0..n-1, refs from REFS via 07-jobs.tsv)
import importlib.util, json, sys
spec = importlib.util.spec_from_file_location("p07", __file__.replace("07-mk.py", "07-prompts.py")); p07 = importlib.util.module_from_spec(spec); spec.loader.exec_module(p07)
J = {}
for l in open(__file__.replace("07-mk.py", "07-jobs.tsv")):
    if l.strip() and not l.startswith("#") and not l.startswith("key"):
        k, j = l.split("\t")[:2]; J[k] = j.strip()
FOLDER = "f5ea6596-e005-46f2-a7b0-cd016a6cf293"  # Higgsfield project "HBX – 1959 Car vs 2009 Car"
out = []
for i, k in enumerate(sys.argv[1:]):
    prm = {"model": "seedream_v5_pro", "resolution": "1k", "aspect_ratio": p07.AR.get(k, "9:16"), "folder_id": FOLDER, "prompt": p07.P[k]}
    refs = p07.REFS[k]
    if refs: prm["medias"] = [{"role": "image_references", "value": J[r]} for r in refs]
    out.append({"index": i, "params": prm})
print(json.dumps(out, ensure_ascii=False))
