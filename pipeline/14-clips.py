# Video 14 (V3, "Why It Rains Inside a Nuclear Cooling Tower"): motion prompts and request builder for the 15 clips.
# usage: python3 14-clips.py C1 C15 ...  (or C1:5 to override the length) -> JSON requests for generate_video_batch
# kling4_0 image-to-video 720p, 2.25 cr/s. Lengths from the real timings (14-plan.json: take A x1.1, 64 s of clips for a 63.90 s
# video). Every clip flies the camera from one camera position to another, each a real still, except C5 (the sprays) and C10
# (the 1965 storm), which have one position and a start still only (add PUSH in the edit if the camera stays still). C14 and C15
# pass a middle keyframe (image_references). STYLE is byte-identical to 14-prompts.py. Lessons carried over (7.2): every
# keyframe of a clip agrees on the state of things; say what must not change; OPEN on every clip that shows the cut-open tower
# (a flight into or out of a cut-open structure can close its wall or fill it with earth, video 13); EMPTYK where the camera is
# in the hollow; GROUND inside the tower; "No people, no characters" on every clip (the duck named as the only animal where it
# shows); "Motion starts on frame 1". C1 opens the tower and C15 closes it again: the only clips where the near half moves.
import importlib.util, json, sys
spec = importlib.util.spec_from_file_location("p14", __file__.replace("14-clips.py", "14-prompts.py")); p14 = importlib.util.module_from_spec(spec); spec.loader.exec_module(p14)
STYLE = p14.STYLE
LIGHT = "Bright, soft, cool daylight the whole time."
STORMLIGHT = "Dim, grey storm light the whole time."
RAIN = "Rain pours down from the underside of the stacked white sheets into the cyan pond the whole time."
OPEN = ("The near half of the tower stays cut away for the whole move: the tower never closes up and no wall appears across the "
        "opening.")
EMPTYK = ("Above the grey zigzag baffles the tower stays completely empty: nothing appears in the hollow but faint white mist: no "
          "floors, no beams, no pipes, no machines.")
GROUND = "No soil, no pit and no hole appears inside the tower or in the floor of the pond."
ONE = "One smooth, continuous camera move with no cuts."
NOBODY = "No people, no characters."
DUCKONLY = "No people, no characters; the only animal is one mallard duck on the pond."
TAIL = "Motion starts on frame 1. No text, no captions, no letters."
INSIDE = ("the inside: rain pouring down from a layer of stacked white plastic sheets into a cyan pond, a big pipe in the middle "
          "with water surging up it, spray pipes and grey zigzag baffles above the sheets, and above them a completely empty "
          "hollow rising to the bright mouth")
C = {
 # clip: (start key, middle keys, end key or None, seconds, motion, who)
 "C1": ("ST0", [], "ST1", 4, "On the first frame a straight cut runs down the middle of the tower from its mouth to the ground, "
        "and the near half of the concrete shell drops smoothly straight down into the ground and is gone, cleanly, with no dust "
        f"and no debris, revealing {INSIDE}. The thick white cloud keeps rolling out of the top the whole time. Once the wall is "
        f"gone the camera pushes in slowly. {GROUND} {ONE}", NOBODY),
 "C2": ("ST1", [], "SH0", 3, "The camera flies forward through the cut-open front of the tower, over the rain and past the "
        "spray pipes, and tilts up as it rises above the grey zigzag baffles to look up the empty hollow: the smooth curved inner "
        f"face of the concrete shell rising to the bright round mouth, with faint mist drifting up. {RAIN} {OPEN} {EMPTYK} "
        f"{GROUND} {ONE}", NOBODY),
 "C3": ("SH0", [], "BA0", 5, "The camera tilts down and dives down along the open cut face of the tower, past the edges of the "
        "grey baffles, the spray pipes and the white sheets, into the falling rain, and comes to rest just above the cyan pond, "
        "facing the big round pipe in the middle: cyan water surges up inside its cut-open side faster and faster, with wisps of "
        f"steam rising off it; rain pours all round into the pond; a mallard duck floats small at the right. {OPEN} {GROUND} "
        f"{ONE}", DUCKONLY),
 "C4": ("BA0", [], "FI0", 4, "The camera rises up from the pond beside the big pipe, through the falling rain, past the "
        "underside of the white sheets, to the grid of spray pipes just above them, where every nozzle bursts into a cone of "
        f"spray onto the stacked white sheets; the grey zigzag baffles span the tower above. {OPEN} {GROUND} {ONE}", DUCKONLY),
 "C5": ("FI0", [], None, 6, "The camera drifts slowly along the spray pipes and pushes in. The nozzles keep spraying onto the "
        "stacked white sheets; thin films of water run down between the sheets and drip off below; faint white mist lifts off "
        "the wet sheets and rises; then the mist slowly thickens into a dense white fog that hangs still around the sprays and "
        f"under the baffles. {OPEN} {GROUND} {ONE}", NOBODY),
 "C6": ("FI0", [], "SH0", 3, "The camera rises up out of the mist, past the grey zigzag baffles, and tilts up as it climbs "
        "into the empty hollow of the tower: the smooth curved inner face of the concrete shell rising to the bright round "
        f"mouth. {OPEN} {EMPTYK} {ONE}", NOBODY),
 "C7": ("SH0", [], "ST1", 5, "The camera pulls back and down out of the hollow and back out through the cut-open front of the "
        "tower, until the whole cut-open tower fills the frame from its legs to its mouth: white mist streams steadily up the "
        f"middle of the empty hollow and out of the mouth as a thick white cloud. {RAIN} {OPEN} {EMPTYK} {GROUND} {ONE}",
        NOBODY),
 "C8": ("ST1", [], "RO0", 3, "The camera rises fast and swings round to the side, climbing high above the river beside the "
        "tower, until it looks along the row of three whole cooling towers standing along the river, each with a white cloud "
        f"rising from its mouth; the clouds lean in a strong wind and clouds race across the sky. {OPEN} {ONE}", NOBODY),
 "C9": ("RO0", [], "ED0", 4, "The camera swoops back toward the cut-open tower and down to its narrow waist, coming in close to "
        "the cut edge of the concrete shell: a thin band of pale grey concrete with steel bars showing in it, curving in to the "
        f"waist and out again; the empty inside of the tower on one side, the sky and the river far below on the other. {OPEN} "
        f"{ONE}", NOBODY),
 "C10": ("RO1", [], None, 4, "In a violent storm under a black sky, heavy rain drives sideways and a gale tears the clouds "
         "away from the towers' mouths. One after another, the three whole cooling towers shudder, crack and collapse, each "
         "folding down into itself in a cloud of grey dust and rubble that the wind sweeps sideways. The camera drifts slowly. "
         "No fire, no lightning, no explosions.", NOBODY),
 "C11": ("ED0", [], "FI0", 7, "The camera holds close on the cut edge of the concrete shell at the waist for a moment, then "
         "dives down inside the empty hollow along the curved inner face, all the way down to the grey zigzag baffles just above "
         "the spray pipes, and comes to rest at the sprays: fine drops of water carried up by the rising air drift up off the "
         f"sprays into the baffles, where they are caught and run back down. {OPEN} {EMPTYK} {GROUND} {ONE}", NOBODY),
 "C12": ("FI0", [], "TO0", 4, "The camera rises fast straight up from the sprays through the empty hollow of the tower, past "
         "the narrow waist, and out of the round mouth into the thick white cloud billowing up out of it, coming to rest just "
         "above the half ring of the cut-open rim, looking across and down past it, with the river, the plain grey building and "
         f"the row of towers far below through gaps in the cloud. {OPEN} {EMPTYK} {ONE}", NOBODY),
 "C13": ("TO0", [], "W0", 5, "The camera pulls back and down from the rim through the cloud until the whole sliced-open set is "
         "in view: the cut-open tower with rain pouring inside it and its cloud drifting over the river, the plain grey "
         f"building, the row of three towers, and the cut face of the ground with the buried pipe below. {OPEN} {ONE}", NOBODY),
 "C14": ("W0", ["BA0"], "DU0", 3, "The camera swoops down and forward through the cut-open front of the tower into the rain at "
         "its base and comes down to the surface of the cyan pond, close to a mallard duck floating happily under the pouring "
         f"rain, raindrops splashing round it. {OPEN} {GROUND} {ONE}", DUCKONLY),
 "C15": ("DU0", ["ST1"], "ST0", 4, "The camera pulls back from the duck, rising up from the pond and back out through the "
         "cut-open front of the tower to the front view, where the whole tower fills the frame; then the near half of the "
         "concrete shell rises smoothly straight back up out of the ground into place and the tower closes up: one smooth pale "
         "grey concrete wall from the legs to the mouth, with the thick white cloud still rolling out of the top. "
         f"{GROUND} {ONE}", DUCKONLY),
}
J = {}
for l in open(__file__.replace("14-clips.py", "14-jobs.tsv")):
    if l.strip() and not l.startswith("#") and not l.startswith("key"):
        k, j = l.split("\t")[:2]; J[k] = j.strip()
FOLDER = "0bef4887-0b2b-4935-aa7d-409e5caab067"  # Higgsfield project "HBX – Why It Rains Inside a Nuclear Cooling Tower"

try:  # clip lengths from the real timings (14-timing.py writes plan.json; a copy is kept as 14-plan.json)
    PLAN = {x["seg"]: x["clip_s"] for x in json.load(open(__file__.replace("14-clips.py", "14-plan.json")))["segments"]}
except FileNotFoundError:
    PLAN = {}

def req(clip, secs=None):
    start, mids, end, s, motion, who = C[clip]
    s = PLAN.get(clip, s)
    light = STORMLIGHT if clip == "C10" else LIGHT
    medias = [{"role": "start_image", "value": J[start]}] + [{"role": "image_references", "value": J[m]} for m in mids]
    if end: medias.append({"role": "end_image", "value": J[end]})
    return {"model": "kling4_0", "mode": "image-to-video", "resolution": "720p", "aspect_ratio": "9:16", "duration": secs or s,
            "folder_id": FOLDER, "prompt": f"{STYLE} {light} {motion} {who} {TAIL}", "medias": medias}

if __name__ == "__main__":
    out = []
    for i, a in enumerate(sys.argv[1:]):
        clip, _, secs = a.partition(":")
        out.append({"index": i, "params": req(clip, int(secs) if secs else None)})
    print(json.dumps(out, ensure_ascii=False))
