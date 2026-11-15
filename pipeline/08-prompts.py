# Video 08 (C1, "Why Your House Doesn't Smell Like the Sewer", the first Cutaway video under the 15 Nov 2026 rules): still prompts
# for seedream_v5_pro 1k 9:16. Usage: python3 08-prompts.py KEY -> prints the prompt as a JSON string.
# STYLE is the Cutaway default of 3.3 Step 4: it names no objects and no place (3.4 Rule 4). SET carries the place and its colours;
# HOUSE lists the objects once, for S0 only. Every other still is an edit of the one named in REFS, with the framing lock (LOCK).
STYLE = ("Photoreal 3D cutaway render: the ground is sliced open like a cake toward the camera, showing clean layers and what is "
"buried in them. Bright soft daylight, warm tones, soft shadows, mild depth of field, clean realistic materials, translucent cyan "
"water, tidy and uncluttered. Vertical 9:16 composition: the subject sits in the upper 60% of the frame, and the lower 40% is plain, "
"calm, low-detail ground. No text, no letters, no numbers, no captions, no logos, no watermark.")
SET = ("a small two-storey suburban house with cream walls and a terracotta tile roof, shown as a cutaway model: its whole front wall "
"is removed like a dollhouse, so both floors and the attic under the roof show inside. The house stands on a square block of ground "
"with a narrow strip of green lawn in front of it and a strip of grey street along the front edge. The front of the block is cut "
"straight down like a slice of cake, so the cut face shows clean layers of brown and tan soil")
CAMERA = ("Camera: straight-on from the front, slightly raised, centred on the house. The house, from the roof peak down to its "
"foundation, fills the upper half of the frame, with a little sky above the roof. The big pipe under the street sits about 60% of the "
"way down the frame. The lower 40% of the frame is plain, even, dark-brown soil with nothing in it")
HOUSE = ("The plumbing is drawn like a clear diagram: every drain pipe is grey and cut open along its length, so we can see inside it. "
"One grey main pipe runs straight up and down inside the cut left side wall, from the upstairs bathroom ceiling, where it ends with a "
"closed cap, down through both floors to below the house; nothing comes out of the roof. "
"Upstairs is a bathroom with white tiles: on the left a white toilet, cut open down the middle like a model so the water standing in "
"its bowl and the curved passage behind it are visible; on the right a small white sink with a U-shaped drain pipe under it holding "
"cyan water; in the middle of the tiled floor a small round metal floor drain, with a short U-shaped pipe under the floor holding cyan "
"water; and a small round exhaust fan in the ceiling. "
"Downstairs is a kitchen with pale wood cabinets and a steel sink; the cabinet doors under the sink are open, and its drain pipe runs "
"straight down and across into the main pipe with no bend at all, holding no water. "
"The toilet, the bathroom sink, the floor drain and the kitchen sink all drain into the main pipe. Below the house, the main pipe turns "
"and slopes gently down toward the front, under the lawn, into one big grey sewer pipe that runs left to right under the street, cut "
"open along its length so its inside shows")
LOCK = ("Same scene as the first reference image. Keep exactly the same camera position, zoom and framing as that image: the house, "
"its rooms, the roof, the lawn, the street, every pipe and the cut face of the ground stay exactly where they are and the same size.")
KEEP = "Everything else identical."
NOBODY = "No people, no animals."
HAZE = "a faint haze of sewer gas"
HAZEIS = ("The haze is translucent yellow-green, soft and see-through like thin mist; it is not smoke, not steam and not fire.")
NIGHT = ("IT IS NIGHT, with no daylight at all (the daylight described above does not apply to this picture): the same picture lit "
"by cool blue moonlight, with a dark blue night sky and a few stars above the roof and only dim light inside the house. The water "
"keeps exactly the same translucent cyan colour as in the reference; nothing glows and no lamps are lit")
RAT = "a single small brown rat"
NIGHTZ = ("IT IS NIGHT, with no daylight at all (the daylight described above does not apply to this picture): cool blue "
"moonlight falls from above, exactly the colour of the reference image; the water keeps exactly the same translucent cyan colour; "
"nothing glows")
STILLNIGHT = "It is still night, lit exactly like the reference image, with no daylight at all."
LOCKZ = ("Same scene as the first reference image. Keep exactly the same camera position, zoom and framing as that image: the "
"pipes, the flap and the soil stay exactly where they are and the same size.")

P = {
 # ---- the main view (stage ladder) ----
 # S0A: the first generation. Good look, but the sewer pipe sat ~75% down the frame, under the captions (Rule 5). It was shrunk to
 # 76% and lifted so the roof peak sits at ~10% (clear of TikTok's top bar) and the sewer pipe at ~63%, with the edges extended
 # locally (S0DRAFT, an upload); S0 is the seedream clean-up of that draft and the base of every other still.
 "S0A": f"{STYLE} Scene: {SET}. {CAMERA}. {HOUSE}. {NOBODY}",
 "S0": f"{STYLE} {LOCK} Change only this: the left and right edges of the picture are smeared and streaky; repaint them so the sky, "
       f"the distant flat land, the green lawn, the grey street and the brown soil layers continue cleanly and naturally out to both "
       f"edges of the frame, and the big grey sewer pipe runs straight out to both edges, cut open along its length like the rest of "
       f"it. The bottom of the frame is plain, even, dark-brown soil with nothing in it. {KEEP} {NOBODY}",
 "S0H": f"{STYLE} {LOCK} Change only this: {HAZE} rises from the big sewer pipe, up the straight kitchen drain pipe, and drifts out "
        f"of the kitchen sink into the kitchen. {HAZEIS} {KEEP} {NOBODY}",
 "S1": f"{STYLE} {LOCK} Change only this: the straight drain pipe under the kitchen sink now has a U-shaped bend, like the one under "
       f"the bathroom sink, and the bottom of the U holds clean translucent cyan water. {KEEP} {NOBODY}",
 # S1D (first try 40ebbf81) drew the falling water as a waterfall in the kitchen, outside the pipe, and emptied the toilet; the clip
 # animates the flush, so the end picture only needs the empty kitchen U with the haze.
 "S1D": f"{STYLE} {LOCK} Change only this: the U-bend under the kitchen sink is now empty, with no water at all in its bottom, and "
        f"{HAZE} rises up out of the empty U-bend and out of the kitchen sink. {HAZEIS} The toilet bowl, the bathroom sink's U-bend and "
        f"the floor drain's U-shaped pipe keep their cyan water exactly as in the reference. {KEEP} {NOBODY}",
 # S2 (first try 10c4d7ad) ran the pipe high above the roof peak like a flagpole; real vents end in a short stub.
 "S2": f"{STYLE} {LOCK} Change only this: the grey main pipe no longer stops with a cap in the attic. It now continues straight up "
       f"and pokes out through the left slope of the roof tiles as a short open stub, only about as tall as one row of roof tiles; its "
       f"open top stays well below the height of the roof peak. {KEEP} {NOBODY}",
 "S2X": f"{STYLE} {LOCK} Change only this, in the upstairs bathroom only: the U-bend under the bathroom sink and the U-shaped pipe "
        f"under the floor drain are empty and dry, and the water in the toilet bowl has sunk lower. {HAZE[0].upper()+HAZE[1:]} hangs through the bathroom. {HAZEIS} "
        f"The kitchen is unchanged, and its U-bend is still full of cyan water. {KEEP} {NOBODY}",
 # S2R-1 (fdc383ce) put a white steam-like wisp beside the sink instead of at the floor drain; S2R is an edit of it that removes it
 # (the clip after it animates the haze rising from the floor drain, so the start frame needs none).
 "S2R": f"{STYLE} {LOCK} Change only this: remove the thin white wisp of steam beside the bathroom sink. There is no haze, mist, "
        f"steam or smoke anywhere in the picture. {KEEP} {NOBODY}",
 # S2HK-1 (23ac69bc) also leaked haze into the kitchen and started the stream at the toilet, not the floor drain.
 "S2HK-2": f"{STYLE} {LOCK} Change only this: a stream of faint sewer-gas haze rises out of the small round floor drain at the left "
         f"end of the bathroom floor, next to the grey main pipe, and curves up across the bathroom into the round exhaust fan in the "
         f"ceiling, as if the fan is pulling it up. {HAZEIS} There is no haze anywhere else: none in the kitchen and none around the "
         f"toilet or the sink. {KEEP} {NOBODY}",
 # S2HK-2 (908dd328): right path, but the plume started on the kitchen floor below the floor drain; S2HK is an edit of it.
 "S2HK": f"{STYLE} {LOCK} Change only this: remove all the haze below the bathroom floor, in the kitchen. The stream of haze now "
         f"starts at the small round floor drain on the bathroom floor and rises from there into the ceiling fan, exactly as in the "
         f"reference above the floor. {KEEP} {NOBODY}",
 "S3": f"{STYLE} {LOCK} Change only this: a thin copper pipe now runs from the water supply under the bathroom sink, down the wall and "
       f"under the bathroom floor, to the floor drain's U-shaped pipe, which is full of clean cyan water. {KEEP} {NOBODY}",
 "S3N": f"{STYLE} {LOCK} Change only this: {NIGHT}. {KEEP} {NOBODY}",
 # S3NC-1 (a8e58fd7) sat the rat on top of the sewer pipe; S3NC-2 (607d7b45) put it on the outside of the house pipe and added a
 # second rat. Seedream would not put things inside a pipe at this distance, so the rat swims in the sewer pipe's window (S3NS) and
 # the flap gets a close-up (S4NZ, S4NZR): the camera pushes in to it and pulls back out for the ending (Rule 3).
 "S3NS": f"{STYLE} {LOCK} Change only this: {RAT} swims inside the big grey sewer pipe, in the cyan water in its left cut-open "
         f"window, seen through the window, heading toward the house pipe. Its whole body is inside the pipe; nothing is on top of or "
         f"outside the pipes. It is the only animal in the scene. {STILLNIGHT} {KEEP} No people.",
 "S3NT": f"{STYLE} {LOCK} Change only this: {RAT} pokes its head and front paws up out of the water in the toilet bowl upstairs, seen "
         f"through the cut-open toilet. It is the only animal in the scene. {STILLNIGHT} {KEEP} No people.",
 # S4-1 (2b09fdc1), S4-2 (73feb580), S4-3 (9b3b0d48) all put the flap outside the pipes in the wide view.
 "S4NZ": f"{STYLE} Same scene, materials and night lighting as the reference image, but the camera has moved in close: an extreme "
         f"close-up of the spot under the lawn where the sloping grey house pipe joins the big grey sewer pipe under the street. The two "
         f"pipes fill the upper part of the frame, cut open along their length like a diagram, with translucent cyan water inside, "
         f"set in the same brown soil; the bottom 40% of the frame is plain dark soil. Inside the house pipe, just before it joins the "
         f"sewer pipe, a small round stainless-steel flap hangs down from a hinge at the top of the pipe and closes the pipe like a "
         f"little door; the flap is entirely inside the pipe and fills its opening. {NIGHTZ}. No people, no animals.",
 "S4NZR-1": f"{STYLE} {LOCKZ} Change only this: {RAT} swims inside the big sewer pipe, in its cyan water, up to the end of the house "
          f"pipe, its nose almost touching the closed steel flap from below. Its whole body is inside the pipes. It is the only animal "
          f"in the scene. {STILLNIGHT} {KEEP} No people.",
 # S4NZR-1 (2f162a9a) put the rat in the sloping house pipe, on the house side of the flap; S4NZR is an edit of it.
 "S4NZR": f"{STYLE} {LOCKZ} Change only this: move the rat. It is now inside the big horizontal sewer pipe at the bottom, in its "
          f"cyan water, just below the junction, its nose pointing up at the closed steel flap from the sewer side. There is no rat in "
          f"the sloping house pipe above the flap. It is the only animal in the scene. {STILLNIGHT} {KEEP} No people.",
}
# References per still (keys of 08-jobs.tsv). The first reference is the picture being edited.
REFS = {"S0A": [], "S0": ["S0DRAFT"], "S0H": ["S0"], "S1": ["S0"], "S1D": ["S1"], "S2": ["S1"], "S2X": ["S2"],
        "S2R": ["S2R-1"], "S2HK-2": ["S2R"], "S2HK": ["S2HK-2"], "S3": ["S2"], "S3N": ["S3"], "S3NS": ["S3N"], "S3NT": ["S3N"], "S4NZ": ["S3N"],
        "S4NZR-1": ["S4NZ"], "S4NZR": ["S4NZR-1"]}
AR = {}

if __name__ == "__main__":
    import json, sys
    print(json.dumps(P[sys.argv[1]]))
