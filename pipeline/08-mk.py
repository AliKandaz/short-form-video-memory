# usage: python3 08-mk.py KEY [KEY ...]  -> JSON requests for generate_image_batch (indices 0..n-1, refs from REFS via 08-jobs.tsv)
import importlib.util, json, sys
spec = importlib.util.spec_from_file_location("p08", __file__.replace("08-mk.py", "08-prompts.py")); p08 = importlib.util.module_from_spec(spec); spec.loader.exec_module(p08)
J = {}
try:
    for l in open(__file__.replace("08-mk.py", "08-jobs.tsv")):
        if l.strip() and not l.startswith("#") and not l.startswith("key"):
            k, j = l.split("\t")[:2]; J[k] = j.strip()
except FileNotFoundError:
    pass
FOLDER = "69c0772c-01fe-4bd4-a2cc-54828fa84bca"  # Higgsfield project "HBX – Why Your House Doesn't Smell Like the Sewer"
out = []
for i, k in enumerate(sys.argv[1:]):
    prm = {"model": "seedream_v5_pro", "resolution": "1k", "aspect_ratio": p08.AR.get(k, "9:16"), "folder_id": FOLDER, "prompt": p08.P[k]}
    refs = p08.REFS[k]
    if refs: prm["medias"] = [{"role": "image_references", "value": J[r]} for r in refs]
    out.append({"index": i, "params": prm})
print(json.dumps(out, ensure_ascii=False))
