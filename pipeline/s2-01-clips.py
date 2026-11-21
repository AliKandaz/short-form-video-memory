# s2-01 (style 2): motion prompts and request builder for the 17 clips (beat sheet: pipeline/s2-01-beat-sheet.md).
# usage: python3 s2-01-clips.py C1 C11 ...        -> JSON requests for generate_video_batch on kling4_0 (720p, 9:16)
#        python3 s2-01-clips.py --wan C1 C11 ...  -> the same clips on wan2_7 (720p, 9:16, its own sound; a SOUND line added)
#        C16:5 overrides a clip's length.
# Lines from strategy2.md 6.3: HOOK (C1), TIMELAPSE (chains), REALSPEED (close-ups, the witness, the last touch, the payoff),
# ONLY (who is in the picture). Lessons carried over (CLAUDE.md 7.2): every keyframe of a clip agrees on the state of things; say
# what must not change; Kling invents people unless told who is in the scene; "Motion starts on frame 1".
# Prices on 21 Nov 2026: kling4_0 2.50 a second at 720p (3 s minimum), wan2_7 4.50 a 3 s clip.
import json, sys

ONLY2 = "The only people in the picture are the builder and the woman on the steps: no other people."
ONLY1 = "The only person in the picture is the builder: no other people."
ONLYW = "The only person in the picture is the woman: no other people."
HANDS = "No faces, no other people."
TAIL = "No text, no logos."
LOCK = "The camera is locked and never moves."
YARD = "The house, the back steps, the fence and the trees stay exactly as they are; the woman stays on the house's back steps."
ROOM = "The room keeps its size and shape, and the window stays in the same place in the back wall."
TL = ("Time-lapse from a locked camera that never moves: between the first and the last frame {what}, moving fast and slightly "
      "blurred, tools and materials appearing and disappearing; the light stays the same. Motion starts on frame 1. The builder "
      "stays the same person.")
RS = "Real speed, handheld with a slight drift: {what} Motion starts on frame 1."

C = {
 # clip: (start key, end key or None, seconds, prompt, wan sound line)
 "C1": ("O0", "O1", 3,
        "On the first frame the old coop's sagging roof starts to give way, and by one second it has crashed down into the coop "
        "with a big burst of straw and dust that fills the middle of the frame: the five hens in front of the coop flap away "
        "across the frosty lawn, unhurt, the builder steps back with one hand on his head, and the woman on the back steps bursts "
        f"out laughing. Real speed. {LOCK} {YARD} Motion starts on frame 1. {ONLY2} {TAIL}",
        "Sound: old wood creaking and cracking, a heavy crash of boards, hens squawking and flapping, a woman laughing."),
 "C2": ("R", None, 3,
        RS.format(what="the woman laughs behind her white mug, steam rising from it; then her laugh fades to a doubtful look and "
        "she lowers the mug a little, still looking out at the yard. The hands have five fingers; the mug keeps its shape.")
        + f" {ONLYW} {TAIL}",
        "Sound: a woman laughing outdoors on a quiet frosty morning, then quiet."),
 "C3": ("O1", "O2", 3,
        TL.format(what="the dust settles and the builder pulls away the broken roof and the old grey boards, straightens the old "
        "frame and sets it on new timber posts with a new raised plywood floor, and builds a small wooden hen house where the old "
        "wire run was; the hens come back and peck around it") + f" {YARD} {ONLY2} {TAIL}",
        "Sound: fast hammering, a pry bar squealing, boards dropping, a circular saw, hens clucking."),
 "C4": ("O2", "O3", 3,
        TL.format(what="the builder raises new pale rafters, lays a dark grey metal roof over them and sheathes the walls in "
        "plywood, leaving openings for a window and a door") + f" {YARD} {ONLY2} {TAIL}",
        "Sound: fast hammering, an impact driver, metal roofing sheets clanking, a circular saw."),
 "C5": ("O3", "O4", 3,
        TL.format(what="the builder fits a window and a glazed door, closes in the gable and clads the walls in vertical "
        "board-and-batten siding") + f" {YARD} {ONLY2} {TAIL}",
        "Sound: fast hammering, a nail gun, a drill."),
 "C6": ("O4", "O5", 3,
        TL.format(what="the builder paints the cabin deep green with cream trim, builds a small cream porch with a railing and "
        "two steps in front of the door, and paints the little hen house to match") + f" {YARD} {ONLY2} {TAIL}",
        "Sound: a paint roller, hammering, a saw."),
 "C7": ("O5", "O6", 3,
        TL.format(what="the builder hangs a black lantern beside the door, sets a planter of small evergreens and a doormat on "
        "the porch, and carries away the pile of old boards; the hens peck around the porch") + f" {YARD} {ONLY2} {TAIL}",
        "Sound: boards being stacked and carried, hens clucking, a light breeze."),
 "C8": ("CA", None, 3,
        RS.format(what="the gloved hands drive the long screw up into the pale rafter with the impact driver; curls of sawdust "
        "fly and the screw head sinks flush into the wood. The hands have five fingers; the tool keeps its shape.")
        + f" {HANDS} {TAIL}",
        "Sound: an impact driver rattling a long screw into timber."),
 "C9": ("I0", "I1", 3,
        TL.format(what="the builder pulls down the broken roof boards and the torn tar paper, rips out the roosting bars and the "
        "nest boxes and sweeps out the straw and the cobwebs, until only the four bare old board walls are left, open to the "
        "sky, and he carries out the last nest box") + f" {ROOM} {ONLY1} {TAIL}",
        "Sound: boards ripping, a pry bar, sweeping, straw rustling."),
 "C10": ("I1", "I2", 3,
        TL.format(what="the old grey boards come off, new pale studs and joists go up, a new roof closes over the room, pink "
        "insulation fills the spaces between the studs and the joists, and a pale plywood subfloor goes down; the builder "
        "presses the last batt of insulation into place") + f" {ROOM} {ONLY1} {TAIL}",
        "Sound: hammering, a drill, a staple gun, insulation rustling, in a small wooden room."),
 "C11": ("I2", "I3", 3,
        TL.format(what="the builder lines the walls and the ceiling with pale pine boards and lays a wide honey-coloured plank "
        "floor, board by board, then runs a gloved hand along the new boards") + f" {ROOM} {ONLY1} {TAIL}",
        "Sound: a nail gun, boards knocking into place, a saw, in a small wooden room."),
 "C12": ("I3", "I4", 3,
        TL.format(what="the builder carries in and sets up a wooden bed under the window, a small desk and chair along the right "
        "wall and two shelves on the left wall") + f" {ROOM} {ONLY1} {TAIL}",
        "Sound: furniture being carried in, a drill, wood knocking."),
 "C13": ("I4", "I5", 3,
        TL.format(what="the builder makes the bed with a patchwork quilt, two pillows and a grey throw, lays a round braided "
        "rug, sets books and a plant on the shelves, a lamp on a little table by the bed and a mug on the desk, then steps back "
        "behind the chair") + f" {ROOM} {ONLY1} {TAIL}",
        "Sound: fabric rustling, soft footsteps, a mug set down."),
 "C14": ("I5", "I6", 3,
        "Time-lapse from a locked camera that never moves: between the first and the last frame the daylight outside the window "
        "fades to a deep blue dusk, light snow begins to fall outside, and the room grows dim and blue; the builder walks over to "
        "the bed and reaches toward the lamp; the lamp stays switched off. Motion starts on frame 1. The builder stays the same "
        f"person. {ROOM} {ONLY1} {TAIL}",
        "Sound: a quiet room, wind outside, faint footsteps."),
 "C15": ("CB", None, 3,
        RS.format(what="the gloved hand presses the pine board flat and the nail gun fires twice with a small kick, pinning it "
        "to the wall. The hands have five fingers; the tool keeps its shape.") + f" {HANDS} {TAIL}",
        "Sound: two sharp nail-gun shots into pine."),
 "C16": ("I6", None, 4,
        RS.format(what="the builder switches on the bedside lamp and the little room fills with warm golden light; he plumps the "
        "pillow on the bed and steps back to look; outside the window snow keeps falling in the blue dusk. The hands have five "
        "fingers.") + f" {ONLY1} {TAIL}",
        "Sound: a lamp switch click, a soft pillow thump, quiet, wind outside."),
 "C17": ("P", None, 3,
        "Real speed, the camera locked: light snow falls in the blue dusk; the cabin's window and glazed door glow warm and the "
        "lantern glows softly; the hen on the porch rail turns its head to peer in through the window; on the house's back "
        "steps the woman stands staring at the cabin and slowly lowers her mug. Motion starts on frame 1. "
        f"{ONLYW} {TAIL}",
        "Sound: a quiet snowy evening, a hen clucking softly."),
}
J = {}
for l in open(__file__.replace("s2-01-clips.py", "s2-01-jobs.tsv")):
    if l.strip() and not l.startswith("#") and not l.startswith("key"):
        k, j = l.split("\t")[:2]; J[k] = j.strip()
FOLDER = "44326d13-708b-4085-89e4-eaab34db660b"  # Higgsfield project "S2 – The chicken coop that became a guest cabin"

def req(clip, wan=False, secs=None):
    start, end, s, prompt, sound = C[clip]
    medias = [{"role": "start_image", "value": J[start]}]
    if end: medias.append({"role": "end_image", "value": J[end]})
    if wan:
        return {"model": "wan2_7", "resolution": "720p", "aspect_ratio": "9:16", "duration": secs or s, "folder_id": FOLDER,
                "prompt": prompt + " " + sound, "medias": medias}
    return {"model": "kling4_0", "mode": "image-to-video", "resolution": "720p", "aspect_ratio": "9:16", "duration": secs or s,
            "folder_id": FOLDER, "prompt": prompt, "medias": medias}

if __name__ == "__main__":
    args = sys.argv[1:]; wan = "--wan" in args; args = [a for a in args if a != "--wan"]
    out = []
    for i, a in enumerate(args):
        clip, _, secs = a.partition(":")
        out.append({"index": i, "params": req(clip, wan, int(secs) if secs else None)})
    print(json.dumps(out, ensure_ascii=False))
