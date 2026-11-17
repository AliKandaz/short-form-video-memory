# Video 10 (X5 cryonics): motion prompts and request builder for the 19 clips.
# usage: python3 10-clips.py C1 C12 ...  (or C1:6 to override the length) -> JSON requests for generate_video_batch
# kling4_0 image-to-video 720p, 2.25 cr/s. Lengths from the real timings (10-plan.json: take A x1.06). Every clip flies the camera
# from one camera position to another (3.4 Rules 2 and 3), each a real still; C4, C6, C8, C10, C11 and C12 pass a middle keyframe
# (image_references). STYLE is byte-identical to 10-prompts.py. LIGHT keeps the daylight and the pale nitrogen; there is no water
# (section 2 rule 2). Lessons carried over: say what must not change (3.4e), "No people, no characters" on every clip but C11
# (the worker), "Motion starts on frame 1" (3.5), no FIXED camera anywhere (Rule 3). T3w was dropped at Gate C: C7 ends on T3
# and C17 goes T3 -> T4; the whip from ROW to the tray before C17 is made in the edit.
import importlib.util, json, sys
spec = importlib.util.spec_from_file_location("p10", __file__.replace("10-clips.py", "10-prompts.py")); p10 = importlib.util.module_from_spec(spec); spec.loader.exec_module(p10)
STYLE = p10.STYLE
LIGHT = ("Bright soft daylight the whole time. The liquid nitrogen stays clear and very pale under rolling white fog; it never "
         "glows, and there is no water anywhere.")
ONE = "One smooth, continuous camera move with no cuts."
NOBODY = "No people, no characters."
TAIL = "Motion starts on frame 1. No text, no captions, no letters."
POD = "the long white sealed pod"
C = {
 # clip: (start key, middle keys, end key, seconds, motion)
 "C1": ("W0", [], "D0", 3, f"The camera glides smoothly down and forward from the wide view of the whole sliced-open building into "
        f"the ground-floor cooling room on the left, flying in through the open front, and arrives low and close by the white "
        f"double doors as they swing open and a steel gurney rolls in, carrying a long white tub with {POD} lying in it. {ONE}"),
 "C2": ("D0", [], "D0f", 4, "The camera pushes in slowly toward the gurney and the heart monitor the whole time. The green heart "
        "line on the monitor's screen beats twice and then goes completely flat. The white pod lies still in the empty white tub."),
 "C3": ("D0f", [], "D1", 4, "The camera keeps drifting slowly around the gurney the whole time. Ice cubes pour into the white tub "
        "around the white pod until it is packed to the rim, and the round rotor on the small white pump cart starts turning, its "
        "two clear tubes running into the pod. The monitor's line stays flat."),
 # C4A (0acf60d9, 6 s): as the camera swooped low over the floor, a white pit with dead roots and stones opened in it (the
 # cutaway STYLE leaking in). C4 says the floor is solid.
 "C4": ("D1", ["T0"], "T1", 6, "The camera swoops up and across the cooling room from the gurney to the white counter along the "
        "back wall and down to a small steel lab tray, arriving very close. The floor is solid grey and nothing is cut open: no "
        "soil, no pit, no roots and no stones anywhere. On the tray, the water in the left-hand glass vial freezes: white ice "
        f"crystals grow through it, spike out of its top and crack the glass. {ONE}"),
 "C5": ("T1", [], "T2", 3, "The camera slides slowly sideways along the tray toward the strawberry the whole time. The frosty red "
        "strawberry thaws: it softens, slumps and collapses into a shapeless red heap, leaking red juice onto its white dish. The "
        "frozen vial stays frozen."),
 # C6A (1739ac32, 3 s): mid-move a pit full of rubble opened in the floor under the table and the tray rode onto the table top;
 # the tubes stayed dark red to the end, so the swap never showed. C6 is 4 s with the floor and the swap spelled out.
 "C6": ("T2", ["B0"], "B1", 4, "The camera pulls back from the tray and swings round to the steel operating table in the middle of "
        "the cooling room, where the white pod lies with two tubes running into it from the pump cart. The floor is solid grey and "
        "nothing is cut open: no soil, no pit, no rubble. The tray stays on the counter. As the camera arrives, pale-blue liquid "
        "flows down from the two bags on the drip stand and pushes the dark red out of both tubes, until both tubes run pale blue "
        f"all the way into the pod. {ONE}"),
 "C7": ("B1", [], "T3", 8, "The camera pushes back in from the table to the counter and down to the steel tray, arriving very "
        "close on the small open steel flask. In the flask, the small vial of pale-blue liquid stands in clear, smoking liquid "
        "nitrogen; thick white vapour pours over the rim and down the sides, and the vial sets into perfectly clear glass, with no "
        f"ice and no crystals. The camera keeps drifting slowly in. {ONE}"),
 "C8": ("T3", ["H0"], "H1", 5, "The camera rises up and away from the tray and flies across the building into the tall storage "
        "hall, up to the steel catwalk, and looks steeply down into the open mouth of the middle tank: the white pod, frosted, hangs "
        f"from the hoist's cable and is lowered slowly, rounded end first, down into the thick white fog. {ONE}"),
 "C9": ("H1", [], "L0", 5, "The pod sinks out of sight into the fog. The camera swoops down past the tanks to the floor of the hall "
        "and sweeps in close to the left edge of the front tank's big see-through window, where the tank's thick double steel wall "
        f"shows in cross-section. {ONE}"),
 "C10": ("L0", [], "L0b", 3, "The camera slides slowly down along the tank's wall to its round steel base on the grey floor. "
         f"Nothing is plugged into the tank: no cable, no wire. The white fog keeps rolling inside the tank. {ONE}"),
 "C11": ("L0b", ["P0"], "P1", 6, "The camera rises straight up the outside of the tanks to the steel catwalk at the top, where white "
         "fog spills from the vent on the middle tank's lid and falls over its edge. A small worker in a blue coverall, gloves and a "
         "frosted face shield pushes the silver hose's nozzle into the tank's fill port, while the camera drifts past a steel coffee "
         f"thermos and a cup of steaming coffee on the railing in the foreground. {ONE}"),
 "C12": ("P1", ["I0"], "I1", 4, "The camera dives down from the catwalk to the front tank and pushes in to its big see-through "
         "window: inside, four long white pods stand upside down in the pale liquid nitrogen around a middle column of small "
         "canisters. The liquid level drops steadily to halfway down the tank, uncovering the frosted upper ends of the pods, while "
         f"their rounded head ends stay deep in the liquid. {ONE}"),
 "C13": ("I1", [], "I2", 4, "The camera glides down along one white pod inside the window to its rounded head end, deep in the "
         f"clear liquid at the bottom of the tank, while fog rolls off the uncovered tops above. The level stays at halfway. {ONE}"),
 "C14": ("I2", [], "I3", 4, "The camera orbits slowly round inside the window to the middle column of small white canisters "
         f"stacked one above the other between the pods. The level stays at halfway. {ONE}"),
 "C15": ("I3", [], "I1", 5, "The camera pulls back from the middle column until the whole window is in view again: four long white "
         f"pods standing upside down around the column, the liquid at halfway. {ONE}"),
 "C16": ("I1", [], "R0", 5, "The camera pulls back from the window and glides along the line of tanks to the right, to the oldest "
         f"tank at the end, duller than the others and crusted with thick white frost that glitters as the camera arrives. {ONE}"),
 "C17": ("T3", [], "T4", 4, "The camera drifts slowly closer to the small steel flask the whole time. White vapour pours over its "
         "rim, and a sharp crack shoots across the clear, glassy pale-blue vial standing in the smoking liquid nitrogen."),
 "C18": ("T4", [], "Wb", 3, "The camera pulls fast back and up from the tray, out of the cooling room, until the whole "
         f"sliced-open building is in view on its deep block of ground. {ONE}"),
 "C19": ("Wb", [], "W0", 6, "The camera drifts slowly up and to the left and settles on the opening view of the whole sliced-open "
         f"building on its deep block of ground. {ONE}"),
}
J = {}
for l in open(__file__.replace("10-clips.py", "10-jobs.tsv")):
    if l.strip() and not l.startswith("#") and not l.startswith("key"):
        k, j = l.split("\t")[:2]; J[k] = j.strip()
FOLDER = "dc9cd687-a9ef-4334-a7db-29df6b684c68"  # Higgsfield project "HBX – Why These People Are Frozen Upside Down"

def req(clip, secs=None):
    start, mids, end, s, motion = C[clip]
    who = "The worker is the only person." if clip == "C11" else NOBODY
    return {"model": "kling4_0", "mode": "image-to-video", "resolution": "720p", "aspect_ratio": "9:16", "duration": secs or s,
            "folder_id": FOLDER, "prompt": f"{STYLE} {LIGHT} {motion} {who} {TAIL}",
            "medias": [{"role": "start_image", "value": J[start]}] + [{"role": "image_references", "value": J[m]} for m in mids]
                      + [{"role": "end_image", "value": J[end]}]}

if __name__ == "__main__":
    out = []
    for i, a in enumerate(sys.argv[1:]):
        clip, _, secs = a.partition(":")
        out.append({"index": i, "params": req(clip, int(secs) if secs else None)})
    print(json.dumps(out, ensure_ascii=False))
