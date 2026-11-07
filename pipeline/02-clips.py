# Video 02 clip prompts (minimax_h3 2K 9:16). BEATS: beat -> (start_still, end_still or None, duration_s, motion)
from prompts import STYLE
TAIL = "Motion starts on frame 1. The character only gestures and does not talk; mouth closed. No text, no captions, no letters."
M = "The man in the yellow hard hat"
BEATS = {
 "B1":  ("S0", "S1", 6, f"Slow push-in. {M} pushes the big fallen log off the sand; it rolls into the shallow water and floats, and he climbs on and lies on his stomach along the top of it, arms dangling in the water, gentle ripples spreading."),
 "B2":  ("S1", None, 4, f"Static camera with a slight shake. The floating log suddenly rolls over sideways and {M.lower()} tumbles off into the water with a big splash, then surfaces spluttering while the log keeps bobbing and turning."),
 "B3":  ("FIRE", "S2", 5, f"Slow push-in. Small orange flames flicker along the top of the log and burn down into a long charred groove while {M.lower()} crouches and scrapes black charcoal out with a white seashell; the log steadily becomes a long hollow dugout canoe with a charred black inside, and the flames die out."),
 "B4":  ("S2", None, 6, f"Slow orbit around the dugout canoe from left to right, keeping it centred. {M} kneels beside it, runs his hand along the smooth charred inside, then looks up proudly. Gentle ripples on the water, palm leaves swaying."),
 "B5":  ("TIP", None, 4, f"Static camera. The narrow round-bottomed dugout rolls hard to one side as {M.lower()} leans; he flails his arms to keep his balance, water slops over the rim, and the canoe wobbles violently back and forth."),
 "B6":  ("STEAM", "S3", 6, f"Slow push-in. {M} drops a glowing red stone into the water-filled canoe with wooden tongs; thick steam billows up, the softened sides of the hull slowly spread outward, and three wooden crosspieces wedge into place across it as the steam thins."),
 "B7":  ("CRACK", None, 4, "Very slow macro push-in. Under the harsh sun and heat shimmer, the long split in the dry pale wood slowly creeps along and widens, tiny splinters lifting, fine dust drifting."),
 "B8":  ("SINK", None, 4, f"Slow push-in. {M} sets the last rock inside the canoe and it slowly settles and sinks onto the sandy bottom under the clear rippling water, sunlight caustics dancing over it."),
 "B9":  ("LAKEBED", None, 4, "Slow push-in through the water toward the old canoes on the bottom. Light rays shimmer, fine particles drift, waterweeds sway gently, the surface ripples above."),
 "B10": ("WAVES", None, 4, f"Low angle with a gentle handheld sway. Choppy waves roll in and splash over the low sides of the canoe; water sloshes inside while {M.lower()} paddles hard and gets soaked by spray."),
 "B11": ("S3", "S4", 5, f"Slow push-in. Long wooden planks rise into place along both top edges of the canoe and rows of brown coconut-fibre stitches appear along them as {M.lower()} pulls the rope tight."),
 "B12": ("CROC", None, 4, f"Slow push-in. The crocodile glides silently past right beside the canoe, leaving a V-shaped wake; {M.lower()} freezes and watches it; the camera slowly sinks toward the dark waterline."),
 "B13": ("CAPSIZE", None, 4, "The camera drifts with the current. The empty canoe spins and is swept downstream by the fast brown current, foam swirling, the lone paddle tumbling away in the water. No people."),
 "B14": ("S4", "S5", 6, f"Slow push-in. Two straight wooden poles slide across the top of the canoe and a long slim log float drops into place beside it and is lashed on; {M.lower()} climbs in, sits down and settles with a paddle across his knees, steady and smiling."),
 "B15": ("STORM", None, 6, "Slow push-in. Big foaming waves roll in from the sea, palm trees whip in the wind, heavy rain slants down, and the tall tree topples into the river with a big splash while the small outrigger canoe rises and falls on the swell."),
 "B16": ("PAYOFF", None, 4, f"Slow push-in. The outrigger canoe rides up and over the big foaming wave and comes down level, the float skimming flat on the water, {M.lower()} paddling firmly through the spray and rain."),
 "B17": ("S5", "END", 8, f"Slow push-in. The light brightens into clear sunshine and the water sparkles; a short mast with a woven palm-leaf sail rises on the canoe, a fishing spear and a round gourd appear, and {M.lower()} steps out onto the sand and waves at the camera."),
}
def prompt(b): return f"{STYLE} {BEATS[b][3]} {TAIL}"
if __name__ == "__main__":
    import sys, json
    FOLDER = "6f533c69-8a0f-4734-8c9d-cb3f40f12e49"
    J = dict(l.split('\t') for l in open('jobs.tsv').read().split('\n') if l.strip())
    out = []
    for i, b in enumerate(sys.argv[1:]):
        s, e, d, _ = BEATS[b]
        med = [{"role": "start_image", "value": J[s].strip()}] + ([{"role": "end_image", "value": J[e].strip()}] if e else [])
        out.append({"index": int(b[1:]), "params": {"model": "minimax_h3", "resolution": "2K", "aspect_ratio": "9:16", "duration": d,
                    "prompt": prompt(b), "medias": med, "folder_id": FOLDER}})
    print(json.dumps(out))
