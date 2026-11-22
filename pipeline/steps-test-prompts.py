# Build-steps test (22 Nov 2026, approved by the user: about 42 credits with the reserve). Not a video: one fix built in four
# visible steps in our Cutaway look, in daylight, from one locked view, to see whether our AI tools can follow the helipad
# video's "build it out step by step" staging. The subject is a neutral test build (a garden shed), not a video idea.
#   python3 steps-test-prompts.py still KEY [KEY ...]   -> requests for generate_image_batch (seedream_v5_pro, 1k, 9:16)
#   python3 steps-test-prompts.py clip  KEY [KEY ...]   -> requests for generate_video_batch
# Two ways of making the steps are compared:
#   W1..W4  one short wan2_7 clip a step, between two neighbouring stage stills (2 s and 3 s; 1.50 a second)
#   K1      all four steps inside one kling4_0 clip of 5 s, with the three middle stages as ordered keyframes (12.50)
# Job ids are read from steps-test-jobs.tsv (key <tab> job id; a key with a try suffix, S2.B, replaces S2 when it is listed later).
import json, sys
STYLE = ("Photoreal 3D cutaway render: the ground is sliced open like a cake toward the camera, showing clean layers and what is "
"buried in them. Bright soft daylight, warm tones, soft shadows, mild depth of field, clean realistic materials, tidy and "
"uncluttered. No text, no letters, no numbers, no captions, no logos, no watermark.")
NOWATER = "There is no water anywhere."
WIDE = ("Vertical 9:16 composition: the subject sits in the upper 60% of the frame, and the lower 40% is plain, calm, low-detail "
"ground.")
SET = ("a suburban back yard on a bright summer afternoon, shown as a cutaway model: a neat, freshly mown green lawn with faint "
"mowing stripes; at the back, the rear wall of a two-storey house with pale blue-grey siding, white window frames and a dark "
"grey shingle roof, with a low green hedge along the foot of the wall; a plain wooden fence along the left side. The yard "
"stands on a deep block of ground cut straight down like a slice of cake toward the camera, so the cut face shows dark topsoil "
"over even layers of brown earth")
CAMERA = ("Camera: from the front and high up, looking down at about 35 degrees over the cut face and across the lawn toward the "
"back of the house, which faces the camera. The house fills the top quarter of the frame. The lawn fills the middle of the "
"frame, and its front edge runs straight across the frame about 62% down from the top. Below that the block of ground is cut "
"straight down all the way to the bottom edge of the frame: deep, even layers of dark topsoil and brown earth with nothing in "
"them. There is no ground in front of the block")
SPOT = ("The middle of the lawn is a wide, empty, flat patch of grass with nothing on it: no shed, no slab, no furniture, no "
"tools, no people and no animals anywhere in the yard")
LOCK = ("Same scene as the reference image. Keep exactly the same camera position, zoom and framing as that image: the house, "
"the hedge, the fence, the lawn and the cut face of the ground stay exactly where they are and the same size.")
KEEP = "Everything else identical."
WHOLE = ("The lawn stays whole around it: no hole, pit or trench is dug anywhere, and the cut face of the ground at the front "
"does not change.")
NOPE = "No people. No animals."
SLAB = ("a rectangular slab of smooth pale grey concrete lies flat on the lawn in the middle of the frame, about 45% of the "
"frame wide, its near edge about 57% down from the top; it is a hand's width thick and sits on top of the grass")
WALLS = ("on the concrete slab stand the four walls of a garden shed with no roof: plain pale unpainted timber boards, as tall "
"as a person, with an empty doorway in the front wall facing the camera and a small empty square window opening beside it; "
"looking down from the camera, the bare concrete floor shows inside the four walls")
ROOF = ("the shed now has a pitched roof of dark grey shingles sitting on its four walls, its ridge running left to right; the "
"walls are still plain pale unpainted timber, and the doorway and the window opening are still empty")
DONE = ("the shed is finished: its timber walls are now painted barn red with white corner trim, a white door hangs closed in "
"the doorway, and there is glass in the small window; the dark grey shingle roof and the concrete slab stay as they are")

P = {
 "S0": f"{STYLE} {NOWATER} {WIDE} Scene: {SET}. {CAMERA}. {SPOT}.",
 "S1": f"{STYLE} {NOWATER} {LOCK} Change only this: {SLAB}. {WHOLE} {KEEP} {NOPE}",
 "S2": f"{STYLE} {NOWATER} {LOCK} The concrete slab stays exactly where it is. Change only this: {WALLS}. {WHOLE} {KEEP} {NOPE}",
 "S3": f"{STYLE} {NOWATER} {LOCK} The concrete slab and the shed's four walls stay exactly where they are. Change only this: "
       f"{ROOF}. {WHOLE} {KEEP} {NOPE}",
 "S4": f"{STYLE} {NOWATER} {LOCK} The shed stays exactly where it is, the same size and shape. Change only this: {DONE}. {WHOLE} "
       f"{KEEP} {NOPE}",
}
# S0 try A came back from head height (the lawn a shallow band, on which a slab would be a thin sliver). S0.B moves the camera
# up, so the lawn is seen from above like a stage; the stages are then edits of S0.B.
POS = ("The same back yard, house, hedge, fence, lawn and block of ground as the reference image, with the same parts, colours, "
"materials and light.")
P["S0.B"] = (f"{STYLE} {NOWATER} {POS} New camera position: much higher and a little closer, as if from a drone at the height of "
"the house's roof edge, looking down at about 45 degrees. The house's roof and upper floor are cut off by the top of the "
"frame: only its ground floor, the hedge and the back door show, in the top fifth of the frame. The lawn is seen from above "
"and fills the frame from about 20% to 64% down, wide and open, with its mowing stripes. Its front edge runs straight across "
"the frame about 64% down; below it the cut face of the block of ground, dark topsoil over layers of brown earth with nothing "
"in them, runs down to about 84%, and under that is the same plain pale ground. Nothing in view changes: the lawn is empty, "
"with no shed, no slab, no furniture, no tools, no people and no animals.")
REFS = {"S0": [], "S0.B": ["S0"], "S1": ["S0"], "S2": ["S1"], "S3": ["S2"], "S4": ["S3"]}

# ---- clips ----
CLOCK = "The camera is locked and never moves."
STAY = ("The house, the hedge, the fence, the lawn and the cut face of the ground stay exactly as they are: no hole, pit or "
"trench opens anywhere, and no soil appears on the lawn.")
SELF = "Nobody is there: the parts move by themselves."
TAIL = "Real speed. Motion starts on frame 1. No people, no characters. No animals. No text, no captions, no letters."
C = {
 # key: (model, start, [middle keyframes], end, seconds, prompt, sound line for wan2_7)
 "W1": ("wan2_7", "S0", [], "S1", 2,
        f"A thick slab of pale grey concrete drops straight down out of the sky and lands flat on the middle of the lawn with a "
        f"heavy thud: it bounces once, very slightly, and a small ring of dust puffs out from under its edges. {SELF} {CLOCK} "
        f"{STAY} {TAIL}",
        "Sound: one heavy stone slab thudding onto grass, a low short rumble, then quiet birdsong."),
 "W2": ("wan2_7", "S1", [], "S2", 3,
        f"Four timber walls shoot up out of the edges of the concrete slab one after another, the back wall first, then the left, "
        f"the right and the front: each slides straight up fast and stops with a small shake, until a roofless shed of pale "
        f"timber stands on the slab. {SELF} {CLOCK} {STAY} {TAIL}",
        "Sound: four quick wooden thunks one after another, boards knocking into place, quiet birdsong."),
 "W3": ("wan2_7", "S2", [], "S3", 3,
        f"A pitched roof of dark grey shingles drops straight down out of the sky onto the shed's four walls, lands with a "
        f"thump, bounces once a little and settles; a little dust puffs out from under the eaves. The walls stay standing and do "
        f"not move. {SELF} {CLOCK} {STAY} {TAIL}",
        "Sound: a heavy wooden roof thumping down onto timber walls, a short creak, quiet birdsong."),
 "W4": ("wan2_7", "S3", [], "S4", 2,
        f"A wave of barn-red paint sweeps across the shed's timber walls from left to right, leaving them red with white trim, "
        f"and a white door swings into the empty doorway and clicks shut. The roof and the slab do not change. {SELF} {CLOCK} "
        f"{STAY} {TAIL}",
        "Sound: a quick wet swoosh of paint, then a wooden door clicking shut, quiet birdsong."),
 "K1": ("kling4_0", "S0", ["S1", "S2", "S3"], "S4", 5,
        f"{STYLE} A garden shed builds itself on the lawn in four quick steps of about one second each. First, a thick slab of "
        f"pale grey concrete drops out of the sky and lands flat on the middle of the lawn with a small puff of dust. Second, "
        f"four timber walls shoot up out of the slab's edges one after another. Third, a pitched roof of dark grey shingles "
        f"drops onto the walls and settles. Fourth, a wave of barn-red paint sweeps across the walls and a white door swings shut "
        f"in the doorway. {SELF} {CLOCK} {STAY} {TAIL}",
        None),
}

def jobs():
    J = {}
    try:
        for l in open(__file__.replace("steps-test-prompts.py", "steps-test-jobs.tsv")):
            if l.startswith("# Higgsfield folder "): J["FOLDER"] = l.split()[3]
            if l.strip() and not l.startswith("#") and not l.startswith("key"):
                k, j = l.split("\t")[:2]; J[k.split(".")[0]] = j.strip()
    except FileNotFoundError:
        pass
    return J

if __name__ == "__main__":
    kind, keys = sys.argv[1], sys.argv[2:]; J = jobs(); out = []
    for i, key in enumerate(keys):
        k = key.split(".")[0]
        if kind == "still":
            prm = {"model": "seedream_v5_pro", "resolution": "1k", "aspect_ratio": "9:16", "prompt": P[key] if key in P else P[k]}
            refs = REFS[key] if key in REFS else REFS[k]
            if refs: prm["medias"] = [{"role": "image_references", "value": J[r]} for r in refs]
        else:
            model, start, mids, end, secs, prompt, sound = C[key] if key in C else C[k]
            medias = [{"role": "start_image", "value": J[start]}] + [{"role": "image_references", "value": J[m]} for m in mids]
            medias.append({"role": "end_image", "value": J[end]})
            prm = {"model": model, "resolution": "720p", "aspect_ratio": "9:16", "duration": secs, "medias": medias,
                   "prompt": prompt + (" " + sound if sound else "")}
            if model == "kling4_0": prm["mode"] = "image-to-video"
        if "FOLDER" in J: prm["folder_id"] = J["FOLDER"]
        out.append({"index": i, "params": prm})
    print(json.dumps(out, ensure_ascii=False))
