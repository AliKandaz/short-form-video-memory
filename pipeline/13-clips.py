# Video 13 (V2, "Why Firefighters Drop Frozen Turkeys Into Fryers"): motion prompts and request builder for the 14 clips.
# usage: python3 13-clips.py C1 C14 ...  (or C1:5 to override the length) -> JSON requests for generate_video_batch
# kling4_0 image-to-video 720p, 2.25 cr/s. Lengths from the real timings (13-plan.json: take B x1.0, 64 s of clips for a 64.06 s
# video). Every clip flies the camera from one camera position to another, each a real still, except C2, which has one position
# and a start still only (add PUSH in the edit if the camera stays still). C1 passes a middle keyframe (image_references).
# STYLE is byte-identical to 13-prompts.py. Lessons carried over: every keyframe of a clip agrees on the state of things; say
# what must not change; LAWN on every clip at the fryer and INDOOR on every clip inside the house (the STYLE line's cut ground
# leaked a pit into two stills here, 7.1); "No people, no characters" on every clip (C13 names the TV's two tiny firefighters as
# the only figures); "Motion starts on frame 1".
import importlib.util, json, sys
spec = importlib.util.spec_from_file_location("p13", __file__.replace("13-clips.py", "13-prompts.py")); p13 = importlib.util.module_from_spec(spec); spec.loader.exec_module(p13)
STYLE = p13.STYLE
LIGHT = "Soft, warm late-afternoon daylight the whole time."
OIL = "The pot holds golden-yellow cooking oil, not water."
WATER = "The pot holds clear water, not oil."
LAWN = ("The grass under and around the fryer stays whole: no soil, no pit, no hole and no cut face of ground appears anywhere "
        "near the fryer.")
INDOOR = "Inside the house the floors and walls stay solid and nothing in them is cut open: no soil, no pit, no steps."
ONE = "One smooth, continuous camera move with no cuts."
NOBODY = "No people, no characters."
TVFIG = "No people, no characters; the only figures are the two tiny firefighters on the TV screen."
TAIL = "Motion starts on frame 1. No text, no captions, no letters."
FROZEN = "a whole frozen turkey, frosted white with chunks of clear ice in its open cavity,"
C = {
 # clip: (start key, middle keys, end key or None, seconds, motion, who)
 "C1": ("ST0", ["ST1"], "H1", 6, f"On the first frame {FROZEN} drops off its hook straight down into the hot oil. At once the oil "
        "boils over violently: a churning mass of pale foam surges up through the cut-open pot and over the rim, golden oil pours "
        "down the outside onto the burner, and orange flames leap up around the pot. The camera rises fast and pulls back as a "
        "huge rolling ball of orange fire bursts up out of the pot, climbing high above the lawn and tilting down to look at the "
        f"fryer engulfed in fire and black smoke, with the deck and the house far behind. {OIL} {LAWN} {ONE}", NOBODY),
 "C2": ("IN0", [], None, 3, "The camera pushes in slowly through the cut-open front of the pot toward the frozen turkey sinking "
        "into the golden oil: chunks of clear ice glint in its open cavity, thin streams of tiny bubbles rise off the ice, and "
        f"clear drops of water start to fall from the cavity down through the oil. {OIL} {LAWN}", NOBODY),
 "C3": ("IN0", [], "IN1", 8, "The camera drifts slowly down along the cut-open front of the pot, following clear drops of water "
        "as they fall from the turkey's cavity down through the golden oil to the hot steel bottom. There the drops burst into big "
        "round bubbles of steam that swell and burst upward, faster and faster, until the oil churns and surges up. The burner's "
        f"blue flames glow under the pot the whole time. {OIL} {LAWN} {ONE}", NOBODY),
 "C4": ("IN1", [], "ST1", 4, "The camera rises up along the cut-open front of the pot with the surging oil, past the turkey to "
        "the rim, as a churning mass of pale foam surges up and spills over the rim and golden oil runs down the outside of the "
        f"pot; the first orange flames lick up from the burner around the base. {OIL} {LAWN} {ONE}", NOBODY),
 "C5": ("ST1", [], "BU0", 5, "The camera follows the golden oil down the outside of the pot to the burner at the bottom: the oil "
        "streams onto the ring of blue flames and bursts into bright orange fire that flares up the side of the pot. "
        f"{OIL} {LAWN} {ONE}", NOBODY),
 "C6": ("K0", [], "K1", 4, "Inside the cut-open kitchen the camera drifts slowly in toward the open white fridge. The white frost "
        "on the turkey lying on its tray melts away and the ice in its cavity disappears, leaving plain pale golden-pink skin, "
        "patted dry, with crumpled white paper towels on the tray beside it. The fridge light glows the whole time. "
        f"{INDOOR} {ONE}", NOBODY),
 "C7": ("K1", [], "R0", 3, "The camera pulls back out of the open fridge, out through the cut-away back wall of the house and "
        "over the wooden deck, and flies low across the lawn to the turkey fryer, coming to rest level with the rim of its pot, "
        "which is filled with clear water with the thawed turkey sitting under it on its rack. The burner under the pot is off, "
        f"with no flames. {INDOOR} {LAWN} {ONE}", NOBODY),
 "C8": ("R0", [], "R1", 5, "The thawed turkey rises slowly up out of the clear water on its steel hook and hangs just above the "
        "rim, dripping; as it comes out, the water level in the pot drops a few inches, and a strip of bright blue tape appears "
        "along the inside wall of the pot at the new waterline. The camera drifts slowly round the pot. The burner stays off, "
        f"with no flames. {WATER} {LAWN} {ONE}", NOBODY),
 "C9": ("BU1", [], "PT2", 5, "A few thin drips of golden oil run down the outside of the pot toward the burner's ring of blue "
        "flames; then the blue flames shrink and go out. The camera rises up the side of the pot to the rim, where the thawed "
        "turkey on its hook slides slowly down into the calm golden oil, which rises a little but stays well below the rim. There "
        f"is no orange fire at any time. {OIL} {LAWN} {ONE}", NOBODY),
 "C10": ("PT2", [], "D0", 3, "The camera rises up from the fryer and swoops across the lawn toward the back of the house, "
         "coming down onto the wooden deck, which is joined to the house, beside its empty folding lawn chair; the cut-open "
         f"kitchen and living room glow warmly behind it. {LAWN} {ONE}", NOBODY),
 "C11": ("D0", [], "H0", 3, "The camera pulls back from the house and rises high above the lawn, tilting down, until the turkey "
         "fryer comes into view standing far out on the grass with a thin wisp of steam rising from its pot, a long stretch of "
         f"empty lawn between it and the deck. {LAWN} {ONE}", NOBODY),
 "C12": ("H0", [], "W0", 5, "The camera pulls back further and comes down in front of the yard until the whole sliced-open back "
         "yard is in view: the house with its cut-open kitchen, where steam rises from the pots on the stove, the deck with its "
         "empty lawn chair, the lawn with the fryer far out on it, and the cut face of the ground below. A few dry leaves drift "
         f"down. {OIL} {ONE}", NOBODY),
 "C13": ("W0", [], "TV0", 4, "The camera flies forward over the lawn and the deck into the cut-open living room of the house and "
         "comes to rest facing the flat TV on the wall, whose screen shows a turkey fryer erupting in a huge orange fireball in a "
         f"parking lot, a red fire engine with no lettering and two tiny firefighters standing well back. {INDOOR} {ONE}", TVFIG),
 "C14": ("TV0", [], "ST0", 6, "The camera pulls back from the TV, out of the living room through the cut-away back wall, over the "
         "deck and across the lawn, and comes down to the turkey fryer, settling close in front of its cut-open pot, where "
         f"{FROZEN} hangs on the hook just above the calm, shimmering golden oil, with blue flames burning under the pot. "
         f"{INDOOR} {OIL} {LAWN} {ONE}", NOBODY),
}
J = {}
for l in open(__file__.replace("13-clips.py", "13-jobs.tsv")):
    if l.strip() and not l.startswith("#") and not l.startswith("key"):
        k, j = l.split("\t")[:2]; J[k] = j.strip()
FOLDER = "7377ac71-fa47-499b-b891-0d4c57eccc6d"  # Higgsfield project "HBX – Why Firefighters Drop Frozen Turkeys Into Fryers"

try:  # clip lengths from the real timings (13-timing.py writes plan.json; a copy is kept as 13-plan.json)
    PLAN = {x["seg"]: x["clip_s"] for x in json.load(open(__file__.replace("13-clips.py", "13-plan.json")))["segments"]}
except FileNotFoundError:
    PLAN = {}

def req(clip, secs=None):
    start, mids, end, s, motion, who = C[clip]
    s = PLAN.get(clip, s)
    medias = [{"role": "start_image", "value": J[start]}] + [{"role": "image_references", "value": J[m]} for m in mids]
    if end: medias.append({"role": "end_image", "value": J[end]})
    return {"model": "kling4_0", "mode": "image-to-video", "resolution": "720p", "aspect_ratio": "9:16", "duration": secs or s,
            "folder_id": FOLDER, "prompt": f"{STYLE} {LIGHT} {motion} {who} {TAIL}", "medias": medias}

if __name__ == "__main__":
    out = []
    for i, a in enumerate(sys.argv[1:]):
        clip, _, secs = a.partition(":")
        out.append({"index": i, "params": req(clip, int(secs) if secs else None)})
    print(json.dumps(out, ensure_ascii=False))
