# Video 06 (idea #9 Petra, Classic look, Middle tier, one build in one main view): motion prompts and request builder for the
# 14 animated clips. usage: python3 06-clips.py C1:5 C2:4 ...  -> JSON requests for generate_video_batch (index = clip number)
# kling4_0 image-to-video 720p, 3-30 s, 2.25 cr/s. Build clips pass end_image too (start and end keyframes on neighbouring stages).
# Durations come from the real timings (06-timeline.json): ceil(len - 0.06), min 3. The STYLE formula is the same byte-identical
# text as in 06-prompts.py. Lessons: say what must NOT change (3.4e); shots without the mascot get NOBODY or their own tail (3.4d).
import importlib.util, json, sys
spec = importlib.util.spec_from_file_location("p06", __file__.replace("06-clips.py", "06-prompts.py")); p06 = importlib.util.module_from_spec(spec); spec.loader.exec_module(p06)
STYLE = p06.STYLE
GUY = "The man in the yellow hard hat only gestures and does not talk; his mouth stays closed."
TAIL = "Motion starts on frame 1. No text, no captions, no letters."
NOBODY = "No people, no characters."
FIXED = "The camera stays in the same place looking at the same cliff."
C = {
 # clip: (beats, start still, end still or None, motion)
 "C1": ("B1-B2", "S0", None, f"Slow push-in. The man in the yellow hard hat steps out of the narrow slot canyon into the sunny sand "
        f"plaza and looks around at the towering blank cliff; then he lifts his clay jar and tips it upside down, and only a trickle of "
        f"dry sand pours out. Heat shimmer rises off the sand. The cliff face stays blank. {GUY}"),
 "C2": ("B3", "S0", "S1", f"{FIXED} A narrow channel cuts itself along the foot of the canyon wall, short round clay pipes roll into "
        f"place inside it one after another, and clear water starts to flow out of the canyon through the pipes into a small stone "
        f"basin; the man in the yellow hard hat kneels and fills his jar, smiling. The cliff face stays blank. {GUY}"),
 "C3": ("B4", "STORM", None, f"{FIXED} Heavy grey rain pours down; thin muddy waterfalls stream down the cliff faces and a shallow "
        f"brown flood rushes across the plaza toward the slot canyon; the man in the yellow hard hat holds his jar over his head in the "
        f"rain. The cliff face stays blank. {GUY}"),
 "C4": ("B5", "STORM", "S2", f"{FIXED} The rain stops and the clouds roll away to a clear blue sky; the rock at the front of the plaza "
        f"opens into a big carved square tank, and the flood water pours into it until it is full to the brim with clear blue water; "
        f"the plaza dries. The man in the yellow hard hat lowers his jar and looks up at the cliff. {GUY}"),
 "C5": ("B8", "S2", "S3b", f"{FIXED} Thin pale chalk lines draw themselves across the blank cliff face, tracing the outline of a grand "
        f"two-storey facade, and the man in the yellow hard hat climbs quickly up to a small ledge at the very top of the outline with "
        f"a hammer and chisel. The rock stays flat and uncarved. {GUY}"),
 "C6": ("B9", "BOTTOMUP", None, f"{FIXED} Chunks of loose rock break off high on the cliff and tumble down; one smashes into a "
        f"half-carved column at the bottom, which breaks apart in a burst of dust and fragments; the man in the yellow hard hat ducks "
        f"with his arm over his hard hat and scrambles back. The chalk outline above stays the same. {GUY}"),
 "C7": ("B10", "S3b", "S5", f"{FIXED} The facade is carved from the top down: the urn and the round kiosk emerge first at the very "
        f"top, then the half-pediments and the upper columns, while the man in the yellow hard hat steps down from ledge to ledge on the "
        f"uncut rock below them, chiselling as he goes; broken rock falls to the foot of the cliff, away from the finished carving. "
        f"Nothing above him changes once it is carved. {GUY}"),
 "C8": ("B11", "S5", "S6", f"{FIXED} The lower storey finishes carving itself: the columns, the pediment and the dark doorway "
        f"appear as the last rough steps disappear; the man in the yellow hard hat hops down to the plaza and puts his hands on his "
        f"hips. The upper storey does not change. {GUY}"),
 "C9": ("B15", "BROKE", "S7", f"{FIXED} A line of camels loaded with bulging sacks walks out of the slot canyon into the plaza; gold "
        f"coins pile up on the man's small toll table as he holds out his hand; small houses and a little columned temple of stacked "
        f"stone blocks rise up along the right side of the plaza. The carved facade does not change. {GUY}"),
 "C10": ("B16", "S7", "S8", f"{FIXED} Earthquake: the whole scene shakes hard; the stacked-block houses and the little temple crack "
         f"and collapse into heaps of rubble in clouds of dust; the camels run back into the canyon; the toll table tips over and coins "
         f"scatter. The carved facade in the cliff stays completely intact and never cracks. {GUY}"),
 "C11": ("B17", "S8", None, f"Very slow push-in toward the untouched carved facade as the dust slowly settles and drifts away; the man "
         f"in the yellow hard hat sits up in the rubble, brushes the dust off his hard hat and looks up at the facade in relief. The "
         f"facade does not move or crack. {GUY}"),
 "C12": ("B20", "EXPLORER", None, f"{FIXED} The bearded man in white and brown robes walks slowly out of the slot canyon into the empty "
         f"sandy plaza, leading the small goat on its rope, with the guide beside him; he stops, looks up at the carved facade and stares "
         f"in awe while the guide points at it; the goat nibbles a dry shrub. The facade does not change. The men only gesture and do "
         f"not talk; their mouths stay closed."),
 "C13": ("B22", "URN", "URNHOLES", f"Static close-up. Small chips burst off the stone urn one after another with little puffs of dust, "
         f"leaving round pockmarks all over its surface, until it is covered in holes. The urn keeps its shape. No guns. {NOBODY}"),
 "C14": ("B24", "END", None, f"{FIXED} Warm golden sunlight. The man in the yellow hard hat waves at the camera with a big friendly "
         f"wave; the water in the basin glitters and a little sand blows across the plaza. The facade does not change. {GUY}"),
}
J = {}
for l in open(__file__.replace("06-clips.py", "06-jobs.tsv")):
    if l.strip() and not l.startswith("#") and not l.startswith("key"):
        k, j = l.split("\t")[:2]; J[k] = j.strip()
FOLDER = "452e85a7-bd8f-4644-bdab-cb74b076b356"
def req(clip, secs):
    beat, start, end, motion = C[clip]
    prm = {"model": "kling4_0", "mode": "image-to-video", "resolution": "720p", "aspect_ratio": "9:16", "duration": int(secs),
           "folder_id": FOLDER, "prompt": f"{STYLE} {motion} {TAIL}", "medias": [{"role": "start_image", "value": J[start]}]}
    if end: prm["medias"].append({"role": "end_image", "value": J[end]})
    return {"index": int(clip[1:]), "params": prm}
if __name__ == "__main__":
    print(json.dumps([req(a.split(":")[0], a.split(":")[1]) for a in sys.argv[1:]], ensure_ascii=False))
