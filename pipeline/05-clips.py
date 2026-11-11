# Video 05 (idea #1 Aquarius, Classic look, Middle B tier): motion prompts and request builder for the 15 animated beats.
# usage: python3 05-clips.py C1:4 C3:5 ...  -> JSON requests for generate_video_batch (index = clip number)
# kling4_0 image-to-video 720p, 3-30 s, 2.25 cr/s. Build clips pass end_image too (start and end keyframes on neighbouring stages).
# The STYLE formula is the same byte-identical text as in 05-prompts.py. Lessons: say what must NOT change (3.4e); for shots with no
# mascot say "No people, no swimmers, no characters" (3.4d).
import importlib.util, json, sys
spec = importlib.util.spec_from_file_location("p05", __file__.replace("05-clips.py", "05-prompts.py")); p05 = importlib.util.module_from_spec(spec); spec.loader.exec_module(p05)
STYLE = p05.STYLE
GUY = "The man in the yellow hard hat only gestures and does not talk; his mouth stays closed."
TAIL = "Motion starts on frame 1. No text, no captions, no letters."
NOBODY = "No people, no swimmers, no characters."
C = {
 # clip: (beat, start still, end still or None, motion)
 "C1": ("B1", "S0", None, f"Slow push-in. The crane cable lowers the long white tank steadily down toward the sand; a few bubbles trail "
        f"up from it; the man in the yellow hard hat swims beside it with one hand on its side, guiding it down, fins kicking slowly. "
        f"Small fish dart away and the sun rays shimmer. {GUY}"),
 "C2": ("B2", "FLOAT", None, f"The tank bobs upward, tilting nose-up and rising toward the surface; a cloud of bubbles and sand swirls "
        f"below it; the man in the yellow hard hat clings to its strap, legs kicking. {GUY}"),
 "C3": ("B3", "S0", "S2", f"Four thick steel legs and a heavy dark steel base frame rise up out of the sand under the tank and lock onto "
        f"it as the tank settles down onto them; puffs of sand burst out around the legs; the crane cable goes slack; the man in the "
        f"yellow hard hat gives a thumbs-up. The tank keeps its shape and size. {GUY}"),
 "C4": ("B4", "DOOR", None, f"The sea blasts in through the open door as a thick foaming jet, and the water spreads fast across the "
        f"floor; the man in the yellow hard hat stumbles backward with his arms up. {GUY}"),
 "C5": ("B5", "MOONPOOL", None, f"The man in the yellow hard hat climbs up the ladder out of the square pool of water and steps onto "
        f"the dry floor, water dripping off him. Gentle ripples spread across the water in the opening, but the water stays exactly "
        f"level with the floor and never spills into the room; the floor stays dry. {GUY}"),
 "C6": ("B9", "S2", "S3", f"The crane barge drifts away out of the frame and a big round yellow buoy floats into place on the "
        f"surface right above the tank; a thick black hose unrolls down from the buoy and connects to the top of the tank. The tank "
        f"and its legs do not move. {GUY}"),
 "C7": ("B10", "SPONGE", None, f"Very slow push-in. The man in the yellow hard hat breathes in slowly; more and more tiny glowing blue "
        f"bubbles drift from the air into his chest and fade into the soft blue glow. {GUY}"),
 "C8": ("B14", "SHARK", None, f"A big grey reef shark glides slowly past the porthole from left to right, outside the glass; the man in "
        f"the yellow hard hat watches it calmly and lifts his mug for a sip. The glass stays intact and no water comes in. {GUY}"),
 "C9": ("B15", "RUSH", None, f"The camera tilts up following the man in the yellow hard hat as he kicks hard and shoots upward toward the "
        f"bright surface; streams of tiny fizzing white bubbles keep bursting out from his arms and legs. {GUY}"),
 "C10": ("B20", "AQUANAUTS", None, f"The two divers in white suits bounce slowly across the sand in big floaty moonwalk steps, raising "
         f"small puffs of sand at each step; small fish drift past; the tank behind them does not move."),
 "C11": ("B21", "STORM", None, f"Black clouds race across the sky, huge grey waves roll and break along the surface, rain lashes down "
         f"and the yellow buoy pitches violently; far below, the tank on its legs stays perfectly still, its portholes glowing. {NOBODY}"),
 "C12": ("B22", "ESCAPE", None, f"Tracking shot: the small boat speeds toward the island throwing white spray, bouncing over the waves, "
         f"while the black storm wall rolls closer behind it. {GUY}"),
 "C13": ("B23", "BUOYRIP", None, f"A huge grey wave slams into the yellow buoy; the chain and hose snap and the buoy tumbles away across "
         f"the foaming sea; rain and spray fly sideways. {NOBODY}"),
 "C14": ("B24", "PAYOFF", None, f"Above, the storm churns the surface with crashing waves and foam; below, the tank sits perfectly still "
         f"on its legs with its portholes glowing; the snapped hose end sways gently; small fish hide by the coral. {NOBODY}"),
 "C15": ("B25", "END", None, f"The man in the yellow hard hat waves at the camera with a big friendly wave; schools of small fish swim "
         f"around the tank; sun rays shimmer through the water. {GUY}"),
}
J = {}
for l in open(__file__.replace("05-clips.py", "05-jobs.tsv")):
    if l.strip() and not l.startswith("#") and not l.startswith("key"):
        k, j = l.split("\t")[:2]; J[k] = j.strip()
FOLDER = "696a691c-e24b-415f-96a3-427d896b05e2"
def req(clip, secs):
    beat, start, end, motion = C[clip]
    prm = {"model": "kling4_0", "mode": "image-to-video", "resolution": "720p", "aspect_ratio": "9:16", "duration": int(secs),
           "folder_id": FOLDER, "prompt": f"{STYLE} {motion} {TAIL}", "medias": [{"role": "start_image", "value": J[start]}]}
    if end: prm["medias"].append({"role": "end_image", "value": J[end]})
    return {"index": int(clip[1:]), "params": prm}
if __name__ == "__main__":
    print(json.dumps([req(a.split(":")[0], a.split(":")[1]) for a in sys.argv[1:]], ensure_ascii=False))
