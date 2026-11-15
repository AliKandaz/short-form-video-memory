# Video 08 (C1 sewer trap, the first Cutaway video): motion prompts and request builder for the 11 animated clips.
# usage: python3 08-clips.py P1 C11 ...  -> JSON requests for generate_video_batch (index = order given)
# kling4_0 image-to-video 720p, 2.25 cr/s. Durations come from the real timings (plan.json, take B x1.0); a clip up to ~4% shorter
# than its segment plays slightly slower, a longer one is trimmed. Every clip has start and end keyframes (Rule 3: the camera or the
# set changes inside the clip, never by a fade); P1 and C12 also pass a middle keyframe (image_references, ordered middle frames).
# STYLE is byte-identical to 08-prompts.py. Lessons carried over: say the camera stays still on every main-view clip (3.4h), say what
# must not change (3.4e), "No people, no characters" on every clip (3.4d).
import importlib.util, json, sys
spec = importlib.util.spec_from_file_location("p08", __file__.replace("08-clips.py", "08-prompts.py")); p08 = importlib.util.module_from_spec(spec); spec.loader.exec_module(p08)
STYLE = p08.STYLE
FIXED = "The camera stays completely still, looking straight at the same sliced-open house; no zoom and no camera movement."
HAZE = "a faint, translucent yellow-green haze of sewer gas, soft and see-through like thin mist, not smoke and not fire"
NOBODY = "No people, no characters."
RATONLY = "The rat is the only animal; no people, no characters."
TAIL = "Motion starts on frame 1. No text, no captions, no letters."
C = {
 # clip: (segment in plan.json, start key, middle keys, end key, seconds, motion)
 "P1": ("P1", "S0", ["S0H"], "S1", 12, f"{FIXED} The kitchen tap turns on by itself and clear cyan water runs into the steel sink and "
        f"drops straight down the plain grey drain pipe into the big sewer pipe under the street. Then {HAZE} rises from the sewer "
        f"pipe, up the straight drain pipe, and drifts out of the kitchen sink into the kitchen. Then the straight drain pipe under the "
        f"kitchen sink bends into a U shape, clean cyan water settles in the bottom of the U, and the haze sinks back below the water "
        f"and fades away. The bathroom upstairs and every other pipe do not change. {NOBODY}"),
 "C3": ("C3", "S1", [], "S1D", 7, f"{FIXED} Upstairs the toilet flushes: the water swirls out of the bowl and a rush of cyan water "
        f"falls down inside the grey main pipe. As it rushes past, it sucks the water out of the U-bend under the kitchen sink, and "
        f"the U is left empty; then {HAZE} rises up out of the empty U and out of the kitchen sink. The toilet bowl fills up again. "
        f"Nothing else changes. {NOBODY}"),
# After Gate D (the user kept P1): the main-view clips get camera moves from free crop keyframes (08-jobs.tsv: S2_roof,
 # S2R_bath, S2HK_bath, S3NS_sewer), because the fixed-camera hook barely registered as motion (0.1-0.7% of the picture changing
 # each second). C3 and C7 keep a still camera for their flow arrows.
 "C4": ("C4", "S1D", [], "S2_roof", 4, f"The camera rises slowly toward the roof while a grey pipe grows straight up from the top of "
        f"the main pipe, through the attic and out through the roof tiles. Fresh air flows down the new pipe, the haze in the kitchen "
        f"fades away, and the U-bend under the kitchen sink fills with clean cyan water again. Nothing else changes. {NOBODY}"),
 "C5": ("C5", "S2_roof", [], "S2X_dn", 9, f"The camera slowly pulls back from the roof until the whole sliced-open house is in view "
        f"again, while a time-lapse of many days plays: sunlight and shadows sweep across the house again and again while the house "
        f"itself stays exactly the same. Upstairs in the bathroom, the water slowly sinks out of the U-bend under the bathroom sink and "
        f"out of the floor drain's U-shaped pipe, and the toilet water sinks lower; {HAZE} creeps up into the bathroom and slowly fills "
        f"it. The kitchen does not change. {NOBODY}"),
 "C6": ("C6", "S2X_dn", [], "S2R_bath", 3, f"The camera pushes in toward the upstairs bathroom while the bathroom sink tap turns on by "
        f"itself for a moment: clear water runs into the sink and fills its U-bend with cyan water, the toilet bowl fills up, and the "
        f"haze in the bathroom clears away. The floor drain stays dry. {NOBODY}"),
 "C7": ("C7", "S2R_bath", [], "S2HK_bath", 12, f"The camera stays completely still on the same view of the bathroom; no zoom and no "
        f"camera movement. A thin wisp of {HAZE} curls up out of the dry floor drain in the bathroom floor. More haze rises out of it, "
        f"and then the round exhaust fan in the bathroom ceiling starts spinning and pulls the haze up across the room into the fan in "
        f"a steady stream. Nothing else changes. {NOBODY}"),
 "C8": ("C8", "S2HK_bath", [], "S3", 5, f"The camera slowly pulls back until the whole sliced-open house is in view, while a thin copper "
        f"water pipe appears and runs to the floor drain's U-shaped pipe; a trickle of clean water flows through it and fills the "
        f"floor drain's U with cyan water. The fan stops and the haze clears away completely. Nothing else changes. {NOBODY}"),
 "C9": ("C9", "S3", [], "S3NS_sewer", 8, f"Day turns to night: the sky darkens to deep blue with a few stars and cool moonlight falls "
        f"over the house; the water keeps the same cyan colour and nothing glows. The camera glides slowly down toward the big sewer "
        f"pipe under the street, where a small brown rat swims into view inside its see-through window, paddling through the cyan "
        f"water toward the house pipe. {RATONLY}"),
 "C10": ("C10", "S3NS_sewer", [], "S3NT", 3, f"It is night. The rat in the sewer pipe darts into the house pipe and disappears while the "
         f"camera pulls back and up to show the whole house, and its head and front paws pop up out of the water in the toilet bowl "
         f"upstairs. {RATONLY}"),
 "C11": ("C11", "S3NT", [], "S4NZ", 6, f"It is night. The rat in the toilet ducks back down under the water and is gone. Then the "
         f"camera glides smoothly down from the house, past the kitchen and the lawn, into the ground, and comes in close to the spot "
         f"where the sloping house pipe joins the big sewer pipe. There a small round steel flap hangs inside the house pipe: water "
         f"flows down the pipe and swings the flap open, then the flap drops shut again. One smooth, continuous camera move with no "
         f"cuts. {NOBODY}"),
 "C12": ("C12", "S4NZ", ["S4NZR"], "S3", 7, f"It is night, close up on the junction of the pipes under the lawn. A small brown rat "
         f"swims up the big sewer pipe to the closed steel flap, bumps its nose against it, and turns back. Then the camera pulls "
         f"smoothly back and up out of the ground until the whole sliced-open house is in view, while dawn breaks and the sky turns to "
         f"bright morning daylight. One smooth, continuous camera move with no cuts. {RATONLY}"),
}
J = {}
for l in open(__file__.replace("08-clips.py", "08-jobs.tsv")):
    if l.strip() and not l.startswith("#") and not l.startswith("key"):
        k, j = l.split("\t")[:2]; J[k] = j.strip()
FOLDER = "69c0772c-01fe-4bd4-a2cc-54828fa84bca"  # Higgsfield project "HBX – Why Your House Doesn't Smell Like the Sewer"

def req(clip, secs=None):
    seg, start, mids, end, s, motion = C[clip]
    prm = {"model": "kling4_0", "mode": "image-to-video", "resolution": "720p", "aspect_ratio": "9:16", "duration": secs or s,
           "folder_id": FOLDER, "prompt": f"{STYLE} {motion} {TAIL}",
           "medias": [{"role": "start_image", "value": J[start]}] + [{"role": "image_references", "value": J[m]} for m in mids]
                     + [{"role": "end_image", "value": J[end]}]}
    return prm

if __name__ == "__main__":
    out = []
    for i, a in enumerate(sys.argv[1:]):
        clip, _, secs = a.partition(":")
        out.append({"index": i, "params": req(clip, int(secs) if secs else None)})
    print(json.dumps(out, ensure_ascii=False))
