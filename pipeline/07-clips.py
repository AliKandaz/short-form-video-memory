# Video 07 (P4, 1959 car vs 2009 car, Classic look, Middle tier, one arena in one main view): motion prompts and request builder
# for the 11 animated clips. usage: python3 07-clips.py C1:3 C2:9 ...  -> JSON requests for generate_video_batch (index = clip number)
# kling4_0 image-to-video 720p, 3-30 s, 2.25 cr/s. Clips that move the crash on pass end_image too (start and end keyframes on
# neighbouring stills). Durations come from the real timings (07-timeline.json, take A x1.03); a clip up to ~4% shorter than its beat
# is played slightly slower instead of buying another second. The STYLE formula is the same byte-identical text as in 07-prompts.py.
# Lessons: FIXED on every clip (3.4h: Kling reads "push-in" as a dolly); say what must NOT change (3.4e).
import importlib.util, json, sys
spec = importlib.util.spec_from_file_location("p07", __file__.replace("07-clips.py", "07-prompts.py")); p07 = importlib.util.module_from_spec(spec); spec.loader.exec_module(p07)
STYLE = p07.STYLE
GUY = "The man in the yellow hard hat only moves as described and does not talk; his mouth stays closed."
TAIL = "Motion starts on frame 1. No text, no captions, no letters."
FIXED = ("The camera stays completely still, high above the diorama, looking down at the same two cars; no zoom and no camera "
         "movement.")
SLOW = "Everything happens in extreme slow motion."
C = {
 # clip: (beats, start still, end still or None, motion)
 "C1": ("B1", "S0", None, f"{FIXED} The man in the yellow hard hat, belted into the red car, waves up at the camera through the "
        f"windshield with a friendly smile; the dummy in the turquoise car sits still with its hands on the wheel. The two cars stay "
        f"touching nose to nose and nothing is crushed yet; a few tiny sparks glint where the bumpers meet. {GUY}"),
 "C2": ("B2-B3", "S0", "S1b", f"{FIXED} {SLOW} The crash begins: the front of the red car crumples and folds back in zigzag pleats "
        f"like an accordion, its hood buckling up; the turquoise car's chrome grille and bumper bend and tear; small chips of glass and "
        f"plastic float up into the air. The man in the yellow hard hat stops waving, grips the steering wheel with both hands and "
        f"braces. Both cabins stay intact. {GUY}"),
 "C3": ("B5", "S1b", None, f"{FIXED} The man in the yellow hard hat, belted into the red car behind its crumpled hood, gives the camera "
        f"a calm thumbs-up through the windshield and nods; nothing else moves except a few floating chips of glass. The crushed fronts "
        f"do not change. {GUY}"),
 "C4": ("B6-B7", "S1b", "S2b", f"{FIXED} {SLOW} The crash keeps going into the turquoise car: its hood folds up into a heap of torn "
        f"metal that pushes back over the windshield frame, its dashboard and floor shove back into the cabin toward the dummy's knees, "
        f"and its steering wheel tips up toward the dummy's head. The red car's crumpled front and its cabin with the man in the yellow "
        f"hard hat do not change at all. {GUY}"),
 "C5": ("B10-B11", "S2b", "S3", f"{FIXED} {SLOW} Both drivers lurch forward. The crash-test dummy in the turquoise car, with no seat "
        f"belt, slides forward off its seat and its head and chest hit the steering wheel and the bare metal dashboard. The man in the "
        f"yellow hard hat in the red car leans forward only a little, held firmly by his shoulder belt. The crushed fronts of both cars "
        f"do not change. {GUY}"),
 "C6": ("B12", "S3", None, f"{FIXED} {SLOW} The shoulder belt across the man in the yellow hard hat pulls tight and pins him back into "
        f"his seat. Nothing else moves; the dummy stays slumped over its steering wheel. {GUY}"),
 "C7": ("B14-B15", "S3", "S4b", f"{FIXED} {SLOW} The man's head tips forward, and a white airbag bursts out of his steering wheel and "
        f"fills in front of his face and chest. Nothing else changes. {GUY}"),
 "C8": ("B20", "S4b", None, f"{FIXED} Extreme slow motion, almost frozen: small glittering chips of glass and flakes of paint drift "
        f"slowly through the air around the two crushed cars, and a thin haze of dust hangs over the point where they meet. The cars, "
        f"the dummy and the man in the yellow hard hat stay still. {GUY}"),
 "C9": ("B21", "S4b", "S6", f"{FIXED} {SLOW} The turquoise car comes apart: its driver's door swings wide open, its windshield pops out "
        f"of its frame and slides onto the crumpled hood, and its bench seat tears loose from the floor and tips forward with the dummy "
        f"on it. The two cars bounce a short way apart. In the red car the airbag goes soft and sags, and the man in the yellow hard hat "
        f"sits back up in his seat; the red car's cabin stays intact. {GUY}"),
 "C10": ("B22", "S6", "S7", f"{FIXED} The man in the yellow hard hat unbuckles, opens the red car's door and climbs out onto the "
         f"concrete; he stands on his right foot and rubs his left foot with a wry smile. The dummy stays slumped in the wrecked "
         f"turquoise car. {GUY}"),
 "C11": ("B23", "S7", "END", f"{FIXED} The man in the yellow hard hat puts his left foot down, walks a few steps away from the wrecked "
         f"cars toward the camera and waves up at the camera with a big friendly wave. The wrecked cars do not change. {GUY}"),
}
J = {}
for l in open(__file__.replace("07-clips.py", "07-jobs.tsv")):
    if l.strip() and not l.startswith("#") and not l.startswith("key"):
        k, j = l.split("\t")[:2]; J[k] = j.strip()
FOLDER = "f5ea6596-e005-46f2-a7b0-cd016a6cf293"  # Higgsfield project "HBX – 1959 Car vs 2009 Car"
def req(clip, secs):
    beat, start, end, motion = C[clip]
    prm = {"model": "kling4_0", "mode": "image-to-video", "resolution": "720p", "aspect_ratio": "9:16", "duration": int(secs),
           "folder_id": FOLDER, "prompt": f"{STYLE} {motion} {TAIL}", "medias": [{"role": "start_image", "value": J[start]}]}
    if end: prm["medias"].append({"role": "end_image", "value": J[end]})
    return {"index": int(clip[1:]), "params": prm}
if __name__ == "__main__":
    print(json.dumps([req(a.split(":")[0], a.split(":")[1]) for a in sys.argv[1:]], ensure_ascii=False))
