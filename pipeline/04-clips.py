# Video 04 (H15 seawater): motion prompts and request builder for the 8 animated beats.
# usage: python3 04-clips.py C1:minimax:4 C2:kling:4 ...  -> JSON requests for generate_video_batch (index = clip number)
# minimax_h3: 2K, 4-15 s, 2 cr/s. kling4_0: image-to-video 720p, 3-30 s, 2.25 cr/s (lessons 3.4d/3.4e: queued minimax jobs fail;
# kling is the reliable fallback). The STYLE formula is the same byte-identical text as in 04-prompts.py.
import importlib.util, json, sys
spec = importlib.util.spec_from_file_location("p04", __file__.replace("04-clips.py", "04-prompts.py")); p04 = importlib.util.module_from_spec(spec); spec.loader.exec_module(p04)
STYLE = p04.STYLE
TAIL = "Motion starts on frame 1. No text, no captions."
C = {
 # clip: (beat, start still, motion)
 "C1": ("B1", "S0", "Slow push-in toward the beach. Cyan seawater flows steadily up through the cut-open grey pipe, from its mouth in the "
        "sea, past the small pump hut and up the hill toward the town. Small waves lap the beach, the seagrass sways, and the yellow fish "
        "swims slowly near the pipe mouth. No people, no swimmers, no characters."),
 "C2": ("B3", "BOIL", "Very slow push-in. Inside the sliced-open steel tank the seawater boils hard, with big bubbles rising over the blue "
        "flames; thick white steam rises into the top pipe; clear drops fall steadily from the copper coil into the small tank. The white "
        "salt crust stays at the bottom of the big tank. No people, no characters."),
 "C3": ("B6", "MEMBRANE", "Static camera with a very slow push-in. On the left, the cyan seawater full of sparkling white salt crystals "
        "pushes hard against the cream-coloured sheet; the salt crystals bump into it, stop and pile up on the left side, while on the "
        "right only clear water droplets seep through the sheet and run down into the clean channel. The sheet stays in place. No people."),
 "C4": ("B9", "INTAKE", "Underwater. A strong current pulls water into the big pipe mouth: the school of small silver fish swirls "
        "helplessly toward the dark opening and disappears inside, and the yellow fish struggles at the edge of the current, flapping hard. "
        "Sunbeams flicker. No people, no divers."),
 "C5": ("B11", "CAP", "Underwater, slow push-in on the round concrete cap. Water slides slowly and sideways into the gap under the rim of "
        "the cap, with fine particles drifting in horizontally; the yellow fish swims up to the cap, feels the gentle pull, turns calmly "
        "and swims away. The seagrass sways gently. No people, no divers."),
 "C6": ("B21", "PLUME", "Underwater. The heavy, cloudy white plume keeps pouring out of the pipe end, sinks and rolls slowly downhill "
        "along the seabed like fog, spreading over the seagrass and covering it. Sunbeams flicker. No fish, no people, no divers."),
 "C7": ("B22", "DIFFUSER", "Underwater. Each short nozzle along the pipe shoots a clear angled jet upward; the jets swirl and fade quickly "
        "into the sea. The green seagrass sways and the yellow fish swims calmly through. There is no white plume anywhere. No people, "
        "no divers."),
 "C8": ("B25", "PAYOFF", "Static camera. The tap pours a strong, steady stream of crystal-clear water into the glass held by the hand, "
        "and the glass fills up; outside the window, heat shimmer rises over the dry brown hills and the white plant by the sea. The hand "
        "stays still."),
}
J = {}
for l in open(__file__.replace("04-clips.py", "04-jobs.tsv")):
    if l.strip() and not l.startswith("#") and not l.startswith("key"):
        k, j = l.split("\t")[:2]; J[k] = j.strip()
FOLDER = "95b78d03-a34b-4999-b679-1c8f5371f9de"
def req(clip, model, secs):
    beat, still, motion = C[clip]
    prm = {"model": model, "aspect_ratio": "9:16", "duration": int(secs), "folder_id": FOLDER,
           "prompt": f"{STYLE} {motion} {TAIL}", "medias": [{"role": "start_image", "value": J[still]}]}
    if model == "minimax_h3": prm["resolution"] = "2K"
    else: prm.update(mode="image-to-video", resolution="720p")
    return {"index": int(clip[1:]), "params": prm}
if __name__ == "__main__":
    M = {"minimax": "minimax_h3", "kling": "kling4_0"}
    print(json.dumps([req(a.split(":")[0], M[a.split(":")[1]], a.split(":")[2]) for a in sys.argv[1:]], ensure_ascii=False))
