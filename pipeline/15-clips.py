# Video 15 (V6, "Why This NFL Field Is Sitting on 546 Wheels"): motion prompts and request builder for the 14 clips.
# usage: python3 15-clips.py C1 C14 ...  (or C1:5 to override the length) -> JSON requests for generate_video_batch
# kling4_0 image-to-video 720p, 2.50 cr/s (21 Nov 2026). Lengths from the real timings (15-plan.json: take A x1.08, 61 s of clips
# for a 63.05 s video). Every clip flies the camera from one position to another, each a real still, except C6 (the motor), C9
# (the layers) and C12 (the orbit), which have one position and a start still only (add PUSH in the edit if the camera stays
# still). C2 passes a middle keyframe (image_references). STYLE is byte-identical to 15-prompts.py. Lessons carried over (7.2):
# every keyframe of a clip agrees on the state of things (the field moves only in C4, inside -> out; the roof closes only in C3;
# the solid face moves only in C1 and C14); say what must not change; ONEFIELD wherever the field shows (HI0 try A had drawn a
# second field inside the bowl); CUTSIDE where the cut face shows during a flight (a flight can close a cut-open structure,
# video 13); NOPIT outdoors and on the floor; "No people, no characters" on every clip (the tortoise named as the only animal
# where it shows); "Motion starts on frame 1". The tortoise appears only in C13.
import importlib.util, json, sys
spec = importlib.util.spec_from_file_location("p15", __file__.replace("15-clips.py", "15-prompts.py")); p15 = importlib.util.module_from_spec(spec); spec.loader.exec_module(p15)
STYLE = p15.STYLE
SUN = "Bright, hot desert daylight the whole time; sunlight falls through the open roof onto the field."
OUT = "Bright, hot desert daylight the whole time."
SHADE = "Inside, under the closed roof, cool even shade the whole time; outside, through the opening, bright desert sun."
CUTSIDE = ("The near side stays cut away for the whole move: the cut face of the field's layers and the row of wheels stays open, "
           "and nothing closes up across it.")
ONEFIELD = "There is only one football field: it never doubles, splits, bends or appears in two places."
NOPIT = "No holes, pits or trenches open in the ground or in the floor."
ONE = "One smooth, continuous camera move with no cuts."
NOBODY = "No people, no characters."
TORTONLY = "No people, no characters; the only animal is one desert tortoise."
TAIL = "Motion starts on frame 1. No text, no captions, no letters."
LAYERS = ("the cut face of the field: green grass and roots, a thick layer of tan sand, a black drainage mat, a white pipe, the "
          "steel tray, and under it a row of big round steel wheels sitting on a steel rail")
C = {
 # clip: (start key, middle keys, end key or None, seconds, light, motion, who)
 "C1": ("SIDE0", [], "SIDE1", 3, SUN, "On the first frame, the solid grey face below the edge of the grass drops smoothly straight "
        "down into the ground and is gone, cleanly, like a slice of cake being taken away, with no dust and no debris, revealing "
        f"{LAYERS}. The field, the rails at the right, the stands, the open roof and the opening stay exactly where they are. Once "
        f"the face is gone the camera pushes in slowly. {ONEFIELD} {ONE}", NOBODY),
 "C2": ("SIDE1", ["WH0"], "RF0", 5, SUN, "The camera dives down to the row of big round steel wheels under the cut-open edge of "
        "the field and skims along them, close, as the wheels begin to turn slowly on their rail; then it rises up and over the "
        "green field, climbing high inside the stadium to just under the open roof, looking down along the field toward the huge "
        f"opening in the end wall with the sunny desert beyond. {CUTSIDE} {ONEFIELD} {ONE}", NOBODY),
 "C3": ("RF0", [], "RF1", 5, "", "The roof's two huge middle panels slide together and close over the stadium; the band of hot "
        "sunlight on the green field narrows and disappears, and the whole field falls into cool shade, the grass turning pale and "
        "dull. At the same time the camera sinks slowly down toward the grass, still looking along the field toward the opening "
        f"at the far end, where the desert outside stays bright in the sun. {ONEFIELD} {ONE}", NOBODY),
 "C4": ("HI1", [], "HI0", 4, OUT, "The whole green football field, on its steel tray, slides slowly and steadily straight out of "
        "the huge opening in the stadium's end wall, along the steel rails, into the bright sunny desert lot, and stops there. The "
        "tray moves as one solid, flat piece; nothing else moves; the stadium stays exactly where it is with its roof closed, and "
        f"no grass is left inside it. The camera drifts slowly. {ONEFIELD} {NOPIT}", NOBODY),
 "C5": ("HI0", [], "RA0", 6, OUT, "The camera swoops down from high above the lot to the ground beside the long side of the "
        "field's steel tray and comes in low and close: the tall flat steel side of the tray with the edge of the grass on top, "
        "and under it a row of big round steel wheels on a steel rail, with a small grey motor on the nearest wheel's axle; the "
        f"rails run on toward the stadium's opening. {ONEFIELD} {NOPIT} {ONE}", NOBODY),
 "C6": ("RA0", [], None, 4, OUT, "The camera pushes in slowly on the nearest big steel wheel and the small grey electric motor "
        "on its axle; the motor turns the wheel slowly and the wheel rolls a little way along the steel rail, and the huge steel "
        f"tray above creeps along with it. {NOPIT} {ONE}", NOBODY),
 "C7": ("RA0", [], "HI0", 3, OUT, "The camera rises fast from the ground beside the tray, climbing high above the sunny desert "
        "lot until it looks back down at the stadium and the whole green field sitting on its rails in the lot; the shadows of the "
        f"cacti and of the tray sweep slowly across the ground as time passes. {ONEFIELD} {ONE}", NOBODY),
 "C8": ("HI0", [], "LA0", 3, OUT, "The camera swoops down from high above the lot to the edge of the field's tray and comes in "
        "very close to its cut face: the green grass at the top, where small sprinkler heads among the blades start spraying fine "
        "jets of water over the grass, and the water soaks down into the thick tan sand below. Water only from the sprinklers. "
        f"{ONE}", NOBODY),
 "C9": ("LA0", [], None, 4, OUT, "The camera drifts slowly down the cut face of the layers: water trickles down from the grass "
        "through the thick tan sand and through the black drainage mat into the white pipe, and runs away along the inside of the "
        f"pipe. The layers stay still; only the water moves. {ONE}", NOBODY),
 "C10": ("FL0", [], "FL1", 8, SHADE, "Inside the stadium, the camera drifts slowly forward over the bare grey concrete floor "
         "with its steel rails, toward the huge opening in the end wall, where the whole green field sits outside in the bright "
         "sun. Then, in the middle of the floor, pale wooden basketball court panels slide together into a court, two hoops on "
         "stands roll into place at its ends, rows of grey seats appear around it, and bright white lights come on over it. The "
         f"field stays outside the whole time. {ONEFIELD} {NOPIT} {ONE}", NOBODY),
 "C11": ("FL1", [], "HI0", 3, OUT, "The camera rises and flies forward over the basketball court, out through the huge opening "
         "in the end wall into the bright sun, and climbs high above the desert lot, turning to look back down at the stadium and "
         f"the whole green field sitting on its rails in the lot. {ONEFIELD} {ONE}", NOBODY),
 "C12": ("HI0", [], None, 7, OUT, "The camera circles slowly high above the desert lot, like a TV blimp camera, looking down at "
         "the whole green football field sitting on its steel rails beside the stadium in bright sun; soft cloud shadows drift "
         f"slowly across the ground. The field does not move. {ONEFIELD} {ONE}", NOBODY),
 "C13": ("HI0", [], "TO0", 3, OUT, "The camera swoops down from high above the lot to the ground beside the long side of the "
         "field's steel tray, landing low next to a desert tortoise that is walking along beside the rail; the huge tray creeps "
         f"along slowly beside it and the tortoise steadily pulls ahead of it. {ONEFIELD} {ONE}", TORTONLY),
 "C14": ("SIDE1", [], "SIDE0", 4, SUN, "The solid grey face rises smoothly straight back up out of the ground into place in "
         "front of the field, covering the cut face, the layers and the row of wheels, cleanly, with no dust; the field, the rails "
         "at the right, the stands, the open roof and the opening stay exactly where they are; the camera pulls back slowly to the "
         f"starting view. {ONEFIELD} {ONE}", NOBODY),
}
J = {}
for l in open(__file__.replace("15-clips.py", "15-jobs.tsv")):
    if l.strip() and not l.startswith("#") and not l.startswith("key"):
        k, j = l.split("\t")[:2]; J[k] = j.strip()
FOLDER = "7537e99d-691b-4212-8723-c068ec0f29ba"  # Higgsfield project "HBX – Why This NFL Field Is Sitting on 546 Wheels"

try:  # clip lengths from the real timings (15-timing.py writes plan.json; a copy is kept as 15-plan.json)
    PLAN = {x["seg"]: x["clip_s"] for x in json.load(open(__file__.replace("15-clips.py", "15-plan.json")))["segments"]}
except FileNotFoundError:
    PLAN = {}

def req(clip, secs=None):
    start, mids, end, s, light, motion, who = C[clip]
    s = PLAN.get(clip, s)
    medias = [{"role": "start_image", "value": J[start]}] + [{"role": "image_references", "value": J[m]} for m in mids]
    if end: medias.append({"role": "end_image", "value": J[end]})
    prompt = " ".join(x for x in (STYLE, light, motion, who, TAIL) if x)
    return {"model": "kling4_0", "mode": "image-to-video", "resolution": "720p", "aspect_ratio": "9:16", "duration": secs or s,
            "folder_id": FOLDER, "prompt": prompt, "medias": medias}

if __name__ == "__main__":
    out = []
    for i, a in enumerate(sys.argv[1:]):
        clip, _, secs = a.partition(":")
        out.append({"index": i, "params": req(clip, int(secs) if secs else None)})
    print(json.dumps(out, ensure_ascii=False))
