# usage: python3 16-mk.py KEY [KEY ...]  -> JSON requests for generate_image_batch (indices 0..n-1, refs from REFS via 16-jobs.tsv)
# A key may carry a try suffix after a dot (F0.B uses F0's prompt and refs unless 16-prompts.py has its own "F0.B"); refs resolve
# to the latest accepted job of each key. Nothing is generated before Gate B is approved.
import importlib.util, json, sys
spec = importlib.util.spec_from_file_location("p16", __file__.replace("16-mk.py", "16-prompts.py")); p16 = importlib.util.module_from_spec(spec); spec.loader.exec_module(p16)
J = {}
FOLDER = None  # set from the "# Higgsfield project <id>" line of 16-jobs.tsv once the project exists (Step 4)
try:
    for l in open(__file__.replace("16-mk.py", "16-jobs.tsv")):
        if l.startswith("# Higgsfield project "):
            FOLDER = l.split()[3]
        if l.strip() and not l.startswith("#") and not l.startswith("key"):
            k, j = l.split("\t")[:2]; J[k] = j.strip()
except FileNotFoundError:
    pass
out = []
for i, key in enumerate(sys.argv[1:]):
    k = key if key in p16.P else key.split(".")[0]
    prm = {"model": "seedream_v5_pro", "resolution": "1k", "aspect_ratio": p16.AR.get(k, "9:16"), "prompt": p16.P[k]}
    if FOLDER: prm["folder_id"] = FOLDER
    refs = p16.REFS[k]
    if refs: prm["medias"] = [{"role": "image_references", "value": J[r]} for r in refs]
    out.append({"index": i, "params": prm})
print(json.dumps(out, ensure_ascii=False))
