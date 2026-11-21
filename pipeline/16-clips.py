# Video 16 (B3, "How to Turn Your House Into a Christmas Light Show"): motion prompts and request builder for the 13 clips.
# usage: python3 16-clips.py C1 C3 ...  (or C1:5 to override the length) -> JSON requests for generate_video_batch
# kling4_0 image-to-video 720p, 2.50 cr/s (21 Nov 2026). Lengths are the beat sheet's until the narration exists; then they come
# from 16-plan.json (16-timing.py). 61 s of clips in all. Eight clips fly the camera between two positions, each a real still
# (C3, C4, C6, C7, C8, C10, C11, C12); C1, C2, C5, C9 and C13 stay at one position (add PUSH in the edit if the camera comes
# back still). C2, C6 and C7 pass a middle keyframe (image_references).
# STYLE is byte-identical to 16-prompts.py (the dusk line approved at Gate A). Lessons carried over (CLAUDE.md 7.2): every keyframe
# of a clip agrees on the state of things; say what must not change; ONEHOUSE on every flight along the house (a move up or
# down a wall can stack a second copy of the building); WHOLE outdoors (the STYLE line's cut ground leaks into outdoor clips);
# the sign is blank in every frame (its words are an overlay); "No people, no characters" on every clip, the dog named as the
# only animal where he shows; "Motion starts on frame 1". The dog is in C1, C2, C3 (left behind), C6 (at the end), C7 (at the
# start), C10, C11, C12 and C13.
import importlib.util, json, sys
spec = importlib.util.spec_from_file_location("p16", __file__.replace("16-clips.py", "16-prompts.py")); p16 = importlib.util.module_from_spec(spec); spec.loader.exec_module(p16)
STYLE = p16.STYLE
DUSK = ("It is blue dusk the whole time: the sky stays deep blue with an orange glow low on the horizon; it never becomes day "
        "and never becomes black night.")
ONEHOUSE = "There is only one house: it never doubles, stretches, grows extra floors or changes shape."
WHOLE = "The lawn, the paving and the road stay whole: no hole, pit, trench or new cut face of ground appears anywhere."
CUTFACE = "The cut face of soil at the bottom of the frame stays exactly as it is."
BLANK = "The sign stays plain white and blank the whole time: nothing is ever written on it."
ONE = "One smooth, continuous camera move with no cuts."
NOBODY = "No people, no characters, no animals."
DOGONLY = "No people, no characters; the only animal is one small scruffy tan terrier with a red collar, the same dog the whole time."
TAIL = "Motion starts on frame 1. No text, no captions, no letters."
C = {
 # clip: (start key, middle keys, end key or None, seconds, motion, who)
 "C1": ("F0", [], "F0b", 4, "On the first frame, the loose end of the string of bulbs whips up off the lawn and clips itself along "
        "the rest of the front roof edge, and the bulbs come on one after another from the left end of the gutter to the right, "
        "each glowing bright warm white: by the first second the whole string along the roof edge is lit. The string wound round "
        "the dog lights up too, and the dog looks down at it and wags its tail. Then the camera pushes in very slowly toward the "
        f"roof edge. The ladder, the house and the lawn stay exactly where they are. {CUTFACE} {ONEHOUSE}", DOGONLY),
 "C2": ("F0b", ["F1"], "F1x", 5, "Many more strings of small warm white bulbs snap on all over the house, fast, one after "
        "another: round the windows, round the front door, along the porch, round the garage door and over the bushes, until the "
        "whole house blazes with light; the ladder slides away out of the left edge of the frame. Then, at about the middle of "
        "the clip, every light goes out in a single instant, like a power cut: every string, the porch lamp and the lit window "
        "go dark together and stay dark to the end, so the house is a dark shape against the dusk sky. The string round the dog "
        f"goes dark too, and the dog looks round, puzzled. The camera pushes in very slowly. {CUTFACE} {ONEHOUSE}", DOGONLY),
 "C3": ("F1x", [], "GU", 5, "The camera rises from the lawn and flies up and in toward the front roof edge of the dark house, "
        "leaving the dog below, and arrives very close to the white gutter near its left end, looking along it. As it arrives, the "
        "dark bulbs clipped along the gutter come back on one after another, each one now a clear faceted bulb with a tiny square "
        "light inside, glowing warm white, and the window below lights up again. Nothing is cut open on the way: the wall and "
        f"the roof stay whole. {ONEHOUSE} {ONE}", DOGONLY),
 "C4": ("GU", [], "OU1", 4, "The camera pulls back from the gutter and sinks down and to the right past the front wall, coming in "
        "low beside the front wall of the garage, where an outdoor outlet sits in the wall and green cords with plug joins lie on "
        "the pale paving. Rain begins to fall on the way down; the wall and the paving turn wet and shiny, a shallow puddle "
        "spreads round the plug joins, and the lit bulbs flicker and go dark, every one. "
        f"{WHOLE} {ONEHOUSE} {ONE}", NOBODY),
 "C5": ("OU1", [], None, 5, "Rain falls steadily and drops splash in the puddle round the plug joins. The camera pushes in slowly "
        "on the outdoor outlet in the wall. A thin thread of pale blue light runs from the wet plug joins on the paving up the "
        "green cord to the outlet; then, with one clear, bright blue-white spark that lights the wall for an instant, the small "
        "red button on the outlet pops out and the thread of blue light vanishes. The strings of bulbs round the garage door stay "
        f"dark the whole time. {WHOLE}", NOBODY),
 "C6": ("OU1", ["OU2"], "F1", 4, "Small dark green plastic boxes snap shut over each plug join on the wet paving, one after "
        "another, and the strings of bulbs round the garage door light up again, warm white. Then the camera pulls back and up, "
        "away from the wall and out over the lawn, to a view of the whole front of the house covered in lit strings, with the dog "
        "sitting on the lawn; as it arrives the rain stops, and all the lights on the house blink off and on together, twice. "
        f"{CUTFACE} {ONEHOUSE} {ONE}", DOGONLY),
 "C7": ("F1", ["PX"], "HI3", 6, "The camera flies up and in to the front roof edge, leaving the dog below, and comes very close to "
        "one bulb on the gutter, which changes into a clear bullet-shaped pixel with a tiny green circuit board and a small black "
        "chip inside it, glowing red; its neighbours glow orange, yellow, green and blue. Then the camera pulls away and climbs "
        "high above the front lawn, looking down at the whole house: every edge of the house is now outlined in pixels, and waves "
        "of colour run along the roof edges, round the windows and across the garage, changing all the time. "
        f"{WHOLE} {ONEHOUSE} {ONE}", DOGONLY),
 "C8": ("HI3", [], "RO3", 4, "The camera swoops down from high above the lawn to the left end of the front roof edge and levels "
        "out just in front of the gutter, looking along the line of lights toward the far end of the house. On the way down the "
        "running colours all turn white. As the camera arrives, the lights from the middle of the line to its far end fade from "
        "white to pale pink and grow dim, while the nearest ones stay pure bright white. "
        f"{WHOLE} {ONEHOUSE} {ONE}", NOBODY),
 "C9": ("RO3", [], "RO4", 4, "A black cable rises from under the eave, bends over the white gutter and clicks into the line of "
        "lights at its middle with a small black connector. At once the pink lights beyond it brighten and turn pure white, one "
        "after another, all the way to the far end of the line. The camera drifts slowly forward along the roof edge. "
        f"{ONEHOUSE}", NOBODY),
 "C10": ("RO4", [], "ST5", 3, "The camera swings away from the roof edge and swoops down and back, off the roof, over the lawn "
         "and the curb, to a low view from the road between two parked cars, looking back at the house, whose lights now pulse in "
         "colour to a beat. On the lawn beside a blank white sign, the dog throws its head back and howls. Far up the road, the "
         f"windows of other houses light up one after another. {BLANK} {WHOLE} {ONEHOUSE} {ONE}", DOGONLY),
 "C11": ("ST5", [], "SG", 8, "For the first half of the clip the camera holds low on the road between the two parked cars: "
         "inside each car the dashboard lights up with a soft warm glow, first one car and then the other; the windows of the "
         "houses far up the road go dark again; the dog stops howling, lowers its head and tilts it to one side. For the second "
         "half the camera glides slowly forward over the curb to the edge of the lawn and comes in close on the blank white sign "
         "on its wooden post, with the dog sitting beside the post. The lights on the house keep pulsing softly in colour. "
         f"{BLANK} {WHOLE} {ONEHOUSE} {ONE}", DOGONLY),
 "C12": ("SG", [], "FR6", 4, "The camera pulls back and up from the sign, away from the road, to a wide view of the front of the "
         "house from the edge of the lawn. As it pulls back, a tall cone-shaped tree made of strings of green light rises on the "
         "lawn and a white star lights on its top; four candy-striped arches of light pop up one after another in a row across "
         "the driveway; a snowman made of white lights lights up beside the porch. The dog trots across the lawn and sits down in "
         f"the middle of it, wearing small reindeer antlers that glow. {BLANK} {CUTFACE} {ONEHOUSE} {ONE}", DOGONLY),
 "C13": ("FR6", [], None, 5, "The finished light show plays. Colours run in waves along the lights on the roof edges and round "
         "the windows; bands of light spiral up the cone-shaped tree; the four arches light up one after another, so the light "
         "seems to leap from arch to arch; the snowman's round mouth opens and closes as if it were singing. The dog's antlers "
         f"blink and it wags its tail. The camera pushes in very slowly. {BLANK} {CUTFACE} {ONEHOUSE}", DOGONLY),
}
J = {}
FOLDER = None
for l in open(__file__.replace("16-clips.py", "16-jobs.tsv")):
    if l.startswith("# Higgsfield project "):
        FOLDER = l.split()[3]
    if l.strip() and not l.startswith("#") and not l.startswith("key"):
        k, j = l.split("\t")[:2]; J[k] = j.strip()

try:  # clip lengths from the real timings (16-timing.py writes plan.json; a copy is kept as 16-plan.json)
    PLAN = {x["seg"]: x["clip_s"] for x in json.load(open(__file__.replace("16-clips.py", "16-plan.json")))["segments"]}
except FileNotFoundError:
    PLAN = {}

def req(clip, secs=None):
    start, mids, end, s, motion, who = C[clip]
    s = PLAN.get(clip, s)
    medias = [{"role": "start_image", "value": J[start]}] + [{"role": "image_references", "value": J[m]} for m in mids]
    if end: medias.append({"role": "end_image", "value": J[end]})
    prompt = " ".join(x for x in (STYLE, DUSK, motion, who, TAIL) if x)
    return {"model": "kling4_0", "mode": "image-to-video", "resolution": "720p", "aspect_ratio": "9:16", "duration": secs or s,
            "folder_id": FOLDER, "prompt": prompt, "medias": medias}

if __name__ == "__main__":
    out = []
    for i, a in enumerate(sys.argv[1:]):
        clip, _, secs = a.partition(":")
        out.append({"index": i, "params": req(clip, int(secs) if secs else None)})
    print(json.dumps(out, ensure_ascii=False))
