# usage: python3 s2-01-mk.py KEY [KEY ...]  -> JSON requests for generate_image_batch (indices 0..n-1, refs from REFS via s2-01-jobs.tsv)
# A key may carry a try suffix after a dot (O1.B uses O1's prompt and refs); refs resolve to the latest accepted job of each key.
import importlib.util, json, sys
spec = importlib.util.spec_from_file_location("ps2", __file__.replace("s2-01-mk.py", "s2-01-prompts.py")); ps2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(ps2)
J = {}
try:
    for l in open(__file__.replace("s2-01-mk.py", "s2-01-jobs.tsv")):
        if l.strip() and not l.startswith("#") and not l.startswith("key"):
            k, j = l.split("\t")[:2]; J[k] = j.strip()
except FileNotFoundError:
    pass
FOLDER = "44326d13-708b-4085-89e4-eaab34db660b"  # Higgsfield project "S2 – The chicken coop that became a guest cabin"
out = []
for i, key in enumerate(sys.argv[1:]):
    k = key if key in ps2.P else key.split(".")[0]
    prm = {"model": "seedream_v5_pro", "resolution": "1k", "aspect_ratio": ps2.AR.get(k, "9:16"), "folder_id": FOLDER, "prompt": ps2.P[k]}
    refs = ps2.REFS[k]
    if refs: prm["medias"] = [{"role": "image_references", "value": J[r]} for r in refs]
    out.append({"index": i, "params": prm})
print(json.dumps(out, ensure_ascii=False))
