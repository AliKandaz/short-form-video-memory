# Video 12 (V1, "Why Some Manhole Covers Are Full of Holes"): motion prompts and request builder for the 14 clips.
# usage: python3 12-clips.py C1 C10 ...  (or C1:5 to override the length) -> JSON requests for generate_video_batch
# kling4_0 image-to-video 720p, 2.25 cr/s. Lengths from the real timings (12-plan.json: take B x1.03, 64 s of clips). Every clip
# flies the camera from one camera position to another, each a real still, except C2, C6 and C8, which have one position and a
# start still only (add PUSH in the edit if the camera stays still). C1, C5 and C13 pass a middle keyframe (image_references).
# STYLE is byte-identical to 12-prompts.py. Lessons carried over: every keyframe of a clip agrees on the state of things (the
# sensor light stays green in C12's end still, so it only blinks); say what must not change; FLOOR on every clip inside the
# concrete room; "No people, no characters" on every clip (the pigeon clips name it as the only animal); "Motion starts on frame 1".
import importlib.util, json, sys
spec = importlib.util.spec_from_file_location("p12", __file__.replace("12-clips.py", "12-prompts.py")); p12 = importlib.util.module_from_spec(spec); spec.loader.exec_module(p12)
STYLE = p12.STYLE
LIGHT = ("Bright soft winter daylight the whole time. The only water is grey-white slush and a few clear drips: there are no "
         "puddles and no pools.")
FLOOR = ("Inside the concrete room the floor and walls stay solid concrete and nothing in them is cut open: no soil, no pit, no "
         "steps.")
ONE = "One smooth, continuous camera move with no cuts."
NOBODY = "No people, no characters."
PIGEON = "No people; the grey pigeon is the only animal."
TAIL = "Motion starts on frame 1. No text, no captions, no letters."
VENTED = "the lid full of round holes"
C = {
 # clip: (start key, middle keys, end key or None, seconds, motion, who)
 "C1": ("ST0", ["ST1"], "H0", 4, "On the first frame the manhole lid bursts straight up off the road on a tall column of bright "
        "orange flame and thick grey smoke; slush sprays out in all directions and the grey pigeon flaps away. The camera rises fast "
        "after the tumbling lid, climbing high above the street, and tilts down to look at the open hole pouring grey smoke, with "
        f"the orange salt truck beside it throwing white rock salt. {ONE}", PIGEON),
 "C2": ("H0", [], None, 3, "The camera drifts slowly down toward the street the whole time. The iron lid tumbles past the camera "
        "and away; the open hole keeps pouring grey smoke; the salt truck's spinner keeps throwing white rock salt onto the slushy "
        "road.", NOBODY),
 "C3": ("V0", [], "W0", 6, "The camera glides slowly along the racks of thick black cables inside the dim, clean concrete room, "
        "then pulls back out through the room's open front and rises until the whole sliced-open street block is in view: the "
        "concrete room under the lid, and the orange salt truck rolling along the far lane above, its spinner throwing white rock "
        f"salt onto the slush. The lid stays shut on its hole with the grey pigeon standing on it, and there is no smoke. {FLOOR} "
        f"{ONE}", PIGEON),
 "C4": ("W0", [], "U0", 3, "The camera swoops down and forward into the concrete room through its open front and turns to look "
        "straight up the short round shaft at the underside of the dark lid, where clear drops of meltwater fall from the small "
        f"pick hole straight down past the camera. {FLOOR} {ONE}", NOBODY),
 "C5": ("U0", ["C0"], "C1", 6, "The camera drops down the shaft to the cable racks and pushes in close on one thick black cable: "
        "a clear drop of meltwater lands on its coat and beads; then a white crust of salt spreads along the coat and a thin crack "
        f"opens in the middle of it. The cable stays on its rack. {FLOOR} {ONE}", NOBODY),
 "C6": ("C1", [], None, 4, "The camera drifts slowly closer to the crack the whole time. A bright blue-white electric arc crackles "
        "and jumps across the crack in the cable's coat, flickering, throwing small sparks. The salt crust and the cable stay "
        f"where they are. {FLOOR}", NOBODY),
 "C7": ("C1", [], "V1", 4, "The camera pulls back from the cracked cable across the concrete room as grey smoke pours off the "
        "cracked coat and spreads until it fills the whole room; the cables and racks show only dimly through it. "
        f"{FLOOR} {ONE}", NOBODY),
 "C8": ("V1", [], None, 4, "The camera tilts slowly up the smoky shaft toward the lid. A spark flashes, the smoke ignites in a "
        "bright orange flash, and the lid at the top of the shaft lifts off and flies away; bright daylight floods down the shaft. "
        f"{FLOOR}", NOBODY),
 "C9": ("H0", [], "H1", 4, "The camera rises higher and further back above the street. The tumbling lid falls away and lands on the "
        "road beside the open hole, which keeps smoking in the near lane; further along the street two more manhole lids each "
        f"send up thin curls of grey smoke; the salt truck drives on along the far lane. {ONE}", NOBODY),
 "C10": ("H1", [], "U1", 5, "The camera swoops down from high above the street toward the near lane, down past the cut edge of the "
         "street block into the concrete room under the hole, and turns to look straight up the shaft at the underside of the "
         f"lid, which is now {VENTED}: bright daylight shines down through the holes in thin beams, and thin grey smoke streams "
         f"up out through them. {FLOOR} {ONE}", NOBODY),
 "C11": ("U1", [], "R0", 3, "The camera rises up the shaft, out past the cut edge of the street block, and comes to rest just "
         f"above the road looking at {VENTED} from the side, with thin wisps of grey smoke rising from its holes and slush round "
         f"its rim; the orange salt truck works the far lane behind. {ONE}", NOBODY),
 "C12": ("R0", [], "SEN", 6, f"The camera pushes in slowly on {VENTED}: grey-white slush on the road beside it melts and trickles "
         "into its holes. Then the camera dives down past the cut edge of the street block into the concrete room and comes to the "
         "small grey sensor box on the wall beside the cables; its small green light starts blinking. The lid stays in place. "
         f"{FLOOR} {ONE}", NOBODY),
 "C13": ("SEN", ["R2"], "R3", 7, f"The camera rises from the sensor box up past the cut edge of the street block to just above "
         f"the road beside {VENTED}. With a thump the lid lifts a finger's width straight up out of its frame on its four small "
         "steel latches, grey smoke puffs out all round its rim, and the lid settles back down into its frame; the smoke drifts "
         f"away. {ONE}", NOBODY),
 "C14": ("R3", [], "ST9", 6, "The camera pulls back and down to the level of the slush on the road, a short step from the lid. The "
         f"grey pigeon flutters down out of the sky, lands on {VENTED} and folds its wings, then pecks at the slush. There is no "
         f"smoke. The orange salt truck stays in the background with its amber lights on. {ONE}", PIGEON),
}
J = {}
for l in open(__file__.replace("12-clips.py", "12-jobs.tsv")):
    if l.strip() and not l.startswith("#") and not l.startswith("key"):
        k, j = l.split("\t")[:2]; J[k] = j.strip()
FOLDER = "25f62fea-3516-4722-a1d8-62520102b743"  # Higgsfield project "HBX – Why Some Manhole Covers Are Full of Holes"

def req(clip, secs=None):
    start, mids, end, s, motion, who = C[clip]
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
