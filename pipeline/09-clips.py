# Video 09 (C3 lightning, the first video with the travelling camera): motion prompts and request builder for the 16 clips.
# usage: python3 09-clips.py C1 C15 ...  (or C1:6 to override the length) -> JSON requests for generate_video_batch
# kling4_0 image-to-video 720p, 2.25 cr/s. Lengths from the real timings (plan.json, take A x1.0). Every clip flies the camera
# from one camera position to another (3.4 Rules 2 and 3), each a real still; C2, C4, C10 and C15 pass a middle keyframe
# (image_references) so one clip can pass through three positions (C2 lost its attic keyframe A at Gate C: both tries mixed the attic with soil). STYLE is byte-identical to 09-prompts.py; STORMV keeps the
# storm grade (the STYLE line says daylight). Lessons carried over: say what must not change (3.4e), "No people, no characters"
# on every clip (3.4d), "Motion starts on frame 1" (3.5). No FIXED camera anywhere (Rule 3).
import importlib.util, json, sys
spec = importlib.util.spec_from_file_location("p09", __file__.replace("09-clips.py", "09-prompts.py")); p09 = importlib.util.module_from_spec(spec); spec.loader.exec_module(p09)
STYLE = p09.STYLE
STORMV = ("It is a thunderstorm the whole time: dark blue-grey storm light outside, rain falling, warm lamps lit inside the house; "
          "the water keeps its translucent cyan colour.")
ONE = "One smooth, continuous camera move with no cuts."
NOBODY = "No people, no characters."
TAIL = "Motion starts on frame 1. No text, no captions, no letters."
BOLT = "a jagged white-blue lightning bolt"
C = {
 # clip: (start key, middle keys, end key, seconds, motion)
 "C1": ("W", [], "R0B", 5, f"The camera glides smoothly down and forward from the wide view of the whole sliced-open house, rising "
        f"and swinging to the right, to a high, close view over the front peak of the roof, rain streaking past, while the shower "
        f"keeps running in the upstairs bathroom. As the camera arrives, {BOLT} strikes the peak of the roof with a bright flash. {ONE}"),
 "C2": ("R0B", [], "Bg", 8, f"The lightning flash fades and a bright white-blue glow of electric current spreads from the struck "
        f"peak of the roof into the attic. The camera dives down through the cut-open roof into the attic, following the glow as it races along "
        f"the white cable on the rafters and down into the walls, then keeps descending to the upstairs bathroom, where the copper "
        f"water pipe in the wall glows white-blue all the way up to the running shower. {ONE}"),
 "C3": ("Bg", [], "R1", 3, f"The glow in the copper pipe fades away. The camera pulls back and rises up and away from the bathroom, "
        f"past the attic, to a high, close view over the front peak of the roof, while a short pointed metal rod rises up out of "
        f"the peak and a thick braided copper cable runs from its foot down the right-hand edge of the roof. {ONE}"),
 "C4": ("R1", ["D"], "G", 5, f"The camera flies down along the outside of the right-hand wall, following the thick braided copper "
        f"cable down the corner of the house, past the windows, to the lawn, and keeps going down into the cut face of the soil, "
        f"where a long copper rod drives straight down into the ground and the cable clamps onto its top. {ONE}"),
 "C5": ("G", [], "W1B", 5, f"The camera pulls back and rises out of the soil until the whole sliced-open house is in view again. "
        f"{BOLT[0].upper() + BOLT[1:]} comes down from the clouds and strikes the metal rod on the peak of the roof, and the bright glow races "
        f"down the copper cable on the corner of the house into the copper rod in the soil. Nothing inside the house glows. {ONE}"),
 "C6": ("W1B", [], "S", 3, f"The glow fades. The camera swoops in fast toward the right-hand wall at the height of the bathroom "
        f"floor, where the copper cable on the outside of the wall runs past the copper water pipe just inside it. {ONE}"),
 "C7": ("S", [], "Sa", 6, f"The camera drifts slowly closer to the wall the whole time. Bright white-blue current runs down the copper "
        f"cable, and a jagged electric arc jumps across the gap from the cable to the copper water pipe inside the wall, flickering "
        f"with small sparks."),
 # C8A (1ec6d1bd, 7 s): Kling scrolled a second copy of the house up from under the ground for ~2 s; C8 says it is one house.
 "C8": ("Sa", [], "K", 6, f"The arc dies away. The camera pulls back and moves down along the outside of the same right-hand wall in "
        f"one smooth move: the bathroom rises toward the top of the frame, the living room comes into view below it, then the lawn "
        f"and the corner of the house at the grass line, where the water pipe's elbow sits beside the top of the long copper rod; a "
        f"copper strap wraps around the water pipe and a thin green wire comes down the corner beside the braided cable, and both "
        f"are bolted into the bronze clamp on the rod. It is the same single two-storey house the whole time; no other rooms or "
        f"floors appear below the ground. {ONE}"),
 "C9": ("K", [], "P", 3, "The camera whips fast up out of the ground and across the front of the house to the top of the wooden "
        "power pole at the left front corner, a quick swing with motion blur, and settles beside its crossarm and grey transformer "
        "can. One continuous move with no cuts."),
 "C10": ("P", ["Pb"], "Es", 6, f"{BOLT[0].upper() + BOLT[1:]} strikes the top of the power pole with a bright flash, and a "
         f"white-blue glow races along the black cable to the house. The camera follows the glow along the cable into the house and "
         f"down to the living room, where bright blue-white sparks burst out of the wall outlets and the panel lights up. {ONE}"),
 # C11A (9a29d6ef, 6 s): the floor beside the sofa became a pool of cyan water around a rock block (the STYLE line leaking in).
 "C11": ("Es", [], "E1", 5, "The camera drifts slowly closer to the electrical panel, then eases back. A small grey box appears on "
         "the wall beside the panel, wired into it; the sparks stop, and a white-blue glow runs out of the panel through the box and "
         "down its green wire into the floor. The floor is solid wood the whole time: nothing is cut open and there is no water "
         "anywhere in the room. The camera keeps drifting slowly the whole time."),
 "C12": ("E1", [], "B", 5, f"The camera rises from the living room up through the house, along the copper water pipe in the wall, "
         f"to the upstairs bathroom, where the shower is running into the tub and the small yellow rubber duck floats in the bath "
         f"water. {ONE}"),
 "C13": ("B", [], "Bd", 4, "The camera pushes in slowly toward the bathtub the whole time. The shower keeps running and the small "
         "yellow rubber duck bobs gently in the bath water."),
 "C14": ("Bd", [], "Bo", 3, "The shower turns off and the water stops falling from the shower head; the bath water stays calm and "
         "still, with the small yellow rubber duck floating on it. The camera eases back slowly the whole time."),
 "C15": ("Bo", ["W1B"], "Gg", 6, f"The camera pulls fast back and up out of the bathroom until the whole sliced-open house is in "
         f"view, and a huge {BOLT[2:]} slams into the metal rod on the peak of the roof with a blinding flash. Then the camera swoops down the "
         f"outside of the right-hand wall, following the bright glow as it races down the copper cable into the copper rod in the "
         f"soil, where the glow spreads out into the ground like roots of light. Nothing inside the house glows. {ONE}"),
 "C16": ("Gg", [], "W1", 6, f"The glow in the soil fades away. The camera pulls back and rises smoothly out of the ground until the "
         f"whole sliced-open house is in view again, rain still falling, and settles in the opening view. The pipes and wires inside "
         f"the house stay dark. {ONE}"),
}
J = {}
for l in open(__file__.replace("09-clips.py", "09-jobs.tsv")):
    if l.strip() and not l.startswith("#") and not l.startswith("key"):
        k, j = l.split("\t")[:2]; J[k] = j.strip()
FOLDER = "783ef666-4a82-436a-90f9-36e3983264a4"  # Higgsfield project "HBX – What Lightning Does Inside Your House"

def req(clip, secs=None):
    start, mids, end, s, motion = C[clip]
    return {"model": "kling4_0", "mode": "image-to-video", "resolution": "720p", "aspect_ratio": "9:16", "duration": secs or s,
            "folder_id": FOLDER, "prompt": f"{STYLE} {STORMV} {motion} {NOBODY} {TAIL}",
            "medias": [{"role": "start_image", "value": J[start]}] + [{"role": "image_references", "value": J[m]} for m in mids]
                      + [{"role": "end_image", "value": J[end]}]}

if __name__ == "__main__":
    out = []
    for i, a in enumerate(sys.argv[1:]):
        clip, _, secs = a.partition(":")
        out.append({"index": i, "params": req(clip, int(secs) if secs else None)})
    print(json.dumps(out, ensure_ascii=False))
