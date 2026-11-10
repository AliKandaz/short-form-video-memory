# Video 04 (H15 seawater to tap water, Hidden By Design look): still prompts for seedream_v5_pro 1k 9:16.
# Usage: python3 04-prompts.py KEY  -> prints the prompt as a JSON string. References per still are in REFS (keys of 04-jobs.tsv).
STYLE = ("Photoreal 3D render in a clean cutaway-diagram style: objects sliced open to show their insides, bright soft sunny daylight, "
"warm tones, soft shadows, mild depth of field, clean realistic materials (concrete, white plastic, stainless steel, blue-painted pumps, "
"pale sand), translucent cyan water, tidy and uncluttered, vertical 9:16 composition with the subject in the centre third, no text, "
"no letters, no numbers, no captions, no logos, no watermark.")
FISH = "one small bright yellow fish with a single blue stripe along its side"
WORLD = ("a small sunny coastal town: a pale sandy beach and a turquoise sea at the front, and behind them a green hill covered with "
"cream houses with terracotta roofs and blue shutters")
CAMERA = ("Camera: elevated three-quarter view of a block of coastline sliced open toward the camera like a cake. The lower third of the "
"frame is the cut face of the sea: translucent cyan water above a sandy seabed with rocks and seagrass, and under the seabed, clean "
"layers of sand and rock. The centre third is the beach. The upper third is the green hill with the town")
SAME = "Same scene, same camera angle and framing as the first reference image."
KEEP = "Everything else identical."
NOPEOPLE = "No people, no divers."

P = {
 # ---- ladder on the hero angle ----
 "S0": f"{STYLE} Scene: {WORLD}. {CAMERA}. A single plain grey pipe starts as an open mouth on the seabed just off the beach, runs "
       f"under the sand, past a small concrete pump hut on the beach, and climbs straight up the hill into the town. The pipe is cut "
       f"open along its whole length, so the cyan seawater flowing inside it is visible. {FISH} swims near the pipe's open mouth on the "
       f"seabed. No people.",
 "END": f"{STYLE} {SAME} Change only this: on the beach where the small pump hut stood there is now a long, low, modern white "
        f"desalination plant with its roof sliced off, showing rows of white tubes, blue pumps and big concrete filter basins inside. "
        f"Under the seabed the grey pipe now runs much further out to sea and rises into a short riser topped by a wide flat round "
        f"concrete cap. A second grey pipe runs back out along the seabed and ends in a row of short nozzles spraying gentle clear jets. "
        f"Clear cyan fresh water flows up the cut-open pipe to the town. Warm golden late-afternoon light. {FISH} swims beside the cap. "
        f"{KEEP}",
 # ---- kitchen ----
 "TAP": f"{STYLE} Close-up inside a bright, simple kitchen: a chrome kitchen tap over a white sink pours water into a clear drinking "
        f"glass held by one hand. The tap spout and the rim of the glass are crusted with thick white salt crystals, and white salt "
        f"streaks stain the sink. Through the window behind, a turquoise sea and a sandy beach in soft focus. Only the hand is visible, "
        f"no face.",
 "TAPSALT": f"{STYLE} {SAME} Change only this: the tap spout, the falling stream of water and the rim of the glass are crusted with "
            f"thick, chunky white salt crystals like frost, the water in the glass is cloudy and grey-white, and white salt crust "
            f"streaks the sink. {KEEP}",
 "PAYOFF": f"{STYLE} {SAME} Change only this: through the window behind, the view is now dry brown hills under a harsh white sun, and "
           f"down by the blue sea stands a long, low white desalination plant. The tap still pours a strong stream of crystal-clear "
           f"water into the glass held by the hand, and the tap and glass are clean and shiny. {KEEP}",
 # ---- distillation ----
 "BOIL": f"{STYLE} On a sandy beach beside a turquoise sea, a large upright steel tank sliced open down the middle to show inside: "
         f"seawater boiling hard with big bubbles over blue gas flames, thick white steam rising from the surface into a pipe at the "
         f"top, and the pipe running into a coiled copper pipe that drips clear fresh water into a second, smaller tank, also cut open. "
         f"A thick white crust of salt coats the floor and walls of the boiling tank. The town on the green hill in the background. "
         f"No people.",
 "FUEL": f"{STYLE} {SAME} Change only this: beside the boiling steel tank there is now a huge black mountain of coal, taller than the "
         f"tank, and a tall brick chimney pours thick black smoke that drifts across the sky over the town on the hill. Hazy, slightly "
         f"darker light. {KEEP}",
 # ---- the plant ----
 "HALL": f"{STYLE} Inside a modern desalination plant hall with the roof sliced away, seen from an elevated three-quarter angle: long "
         f"rows of white plastic pressure tubes stacked horizontally on blue steel racks, thick stainless steel pipes, and at the near "
         f"end giant blue high-pressure pumps with silver motors. Clean grey concrete floor, bright daylight pouring in from above, "
         f"the turquoise sea visible through tall windows at the back. No people.",
 "MEMBRANE": f"{STYLE} Extreme macro cutaway diagram of the wall of a filter tube: in the middle of the frame a thin, translucent, "
             f"cream-coloured plastic sheet stands upright like a wall. On the left side, cyan seawater crowded with sparkling white salt "
             f"crystals presses hard against the sheet, and the salt crystals pile up along its left face. On the right side of the "
             f"sheet, only crystal-clear water droplets come through into a clean, empty channel. Bright clean lighting.",
 "CLOG": f"{STYLE} {SAME} Change only this: the thin cream-coloured plastic sheet is now caked in a thick layer of brown sand grains "
         f"and slimy green algae, the clear channel on the right is dry and empty, and nothing passes through. {KEEP}",
 "GAUGE": f"{STYLE} Extreme close-up: a big round analog pressure gauge fills most of the frame, mounted on a thick stainless steel "
          f"pipe in the plant hall from the reference image, with soft-focus blue pumps and white tubes behind it. The gauge face is "
          f"plain white with simple black tick marks and NO numbers and NO letters, a wide red zone at the top end, and the black "
          f"needle pointing deep into the red zone. Shallow depth of field.",
 "POWER": f"{STYLE} Inside the same plant hall as the reference image: a row of giant blue high-pressure pumps with big silver electric "
          f"motors, fed by thick black power cables that run along the floor to a humming electrical substation with glowing orange "
          f"coils. Tall power-line towers outside the windows. Bright, slightly dramatic lighting. No people.",
 "PX": f"{STYLE} In the same plant hall as the reference image, a long silver steel cylinder lies on its side on a blue rack, sliced "
       f"open lengthwise to show a white ceramic rotor inside, drilled with many long straight ducts. Dark navy-blue brine flows into the "
       f"ducts from the left end and pushes bright light-cyan seawater out of the ducts toward the right end; inside every duct the "
       f"dark blue and the light cyan water meet. Bright clean lighting. No people.",
 "SAND": f"{STYLE} Inside the same plant as the reference image: a row of big open concrete filter basins sliced open toward the "
         f"camera, showing murky green-brown seawater on top, then a deep layer of pale sand, then layers of grey gravel and pebbles, "
         f"and clear cyan water collecting in pipes at the very bottom. Bright daylight from above. No people.",
 "LIME": f"{STYLE} Inside the same plant as the reference image: a tall glass-walled tank seen in cutaway, filled with a deep bed of "
         f"crushed white limestone chips, with crystal-clear water trickling down through the white stones from a pipe at the top and "
         f"collecting at the bottom. Bright clean daylight. No people.",
 "CORRODE": f"{STYLE} Extreme close-up cutaway of an old cast-iron water pipe sliced lengthwise, carrying perfectly crystal-clear "
            f"water. The pipe's inner wall is badly pitted and eaten away, with bright orange rust flakes and small holes, and tiny "
            f"orange rust particles swirling in the clear water. Dramatic close lighting.",
 # ---- the sea ----
 "INTAKE": f"{STYLE} Underwater view just off the sandy beach from the reference image, the seabed sliced open in front to show its sand "
           f"layers: a big open grey pipe mouth about two metres wide lies on the seabed, sucking water in. A swirling school of small "
           f"silver fish is being pulled helplessly toward the dark opening, and {FISH} struggles at the edge of the current. Sunbeams "
           f"slant down through translucent cyan water. {NOPEOPLE}",
 "CAP": f"{STYLE} Underwater view far offshore in deeper cyan water, with the same seabed as the reference image sliced open in front "
        f"to show the grey intake pipe running under the sand. The pipe rises out of the seabed as a short vertical concrete riser about "
        f"as tall as a person, topped by a wide, flat, round concrete cap like a giant table, with an open gap all around between the "
        f"cap and the top of the riser where water slips in sideways. {FISH} swims calmly beside the cap. Seagrass and rocks on the "
        f"seabed, sunbeams from the surface. {NOPEOPLE}",
 "PLUME": f"{STYLE} Underwater view of the seabed near the shore, the same seabed as the reference image, sliced open in front: the "
          f"open end of a grey pipe lying on the seabed pours out a thick, heavy, cloudy white plume that sinks and creeps along the "
          f"seabed like fog, flowing downhill over a meadow of seagrass and smothering it, the covered seagrass turning grey. Sunbeams "
          f"from above. No fish. {NOPEOPLE}",
 "DIFFUSER": f"{STYLE} {SAME} Change only this: the grey pipe on the seabed now has a long row of short upright nozzles along its top, "
             f"each shooting a clear angled jet upward that swirls and fades into the sea within a few metres. There is no white plume "
             f"and no fog anywhere on the seabed; the seagrass is bright green and healthy, and {FISH} swims among it. {KEEP}",
 # ---- stats, joke, that's why ----
 "GLASSES": f"{STYLE} On a clean white counter against a soft pale blue background: on the left, one clear drinking glass full of "
            f"sparkling clear water; on the right, one identical glass completely full of milky white cloudy brine, and beside it a "
            f"second identical glass only half full of the same milky white brine. Three glasses in a row. Bright soft studio light, "
            f"simple and clean.",
 "PEBBLE": f"{STYLE} Extreme close-up on a white kitchen counter: a single small white limestone pebble plunges into a clear drinking "
           f"glass full of water, with a splash crown and droplets frozen in mid-air. Bright soft window light, the blue sea out of "
           f"focus in the background.",
 "BOTTLE": f"{STYLE} Close-up of an ordinary sealed clear plastic bottle of drinking water, NOT cut open, filled only with plain "
           f"clear water and nothing else inside, standing on a sunny kitchen counter. Its plain blue-and-white paper label faces the "
           f"camera, with a few thin blurry grey lines of fine print in one small corner, no readable words and no brand. Soft "
           f"window light, the sea out of focus behind.",
 # ---- drought and ending ----
 "DROUGHT": f"{STYLE} An ordinary street view, not a cutaway: a street in a small sunny coastal town during a severe drought, cream "
            f"houses with terracotta roofs and blue shutters, lawns burnt brown and dead, a cracked dry garden bed, an empty dusty stone "
            f"fountain, a harsh white sun in a pale hazy sky and heat shimmer above the road. No sea, no pipes, no water anywhere. "
            f"No people.",
 "DROUGHT3": f"{STYLE} {SAME} Change only this: remove the square pool of water, the blue tap and the white pipes from the foreground; "
             f"that whole area is now dry, cracked brown earth with dead grass, exactly like the rest of the ground. There is no water "
             f"anywhere in the picture. {KEEP}",
 "RESERVOIR": f"{STYLE} A concrete dam among dry brown hills holding an almost empty reservoir: the water shrunk to a small muddy pool "
              f"far below the old pale waterline marks on the banks, the exposed bed cracked into deep dry plates, and a small wooden "
              f"rowing boat stranded on the cracked mud. Harsh white sun, hazy pale sky. No people.",
 "PERTH": f"{STYLE} Elevated view of a sunny modern coastal city: a cluster of glass skyscrapers beside a wide blue river, suburbs and "
          f"green parks stretching along a sandy coast, and in the foreground on the shore a long, low white desalination plant with "
          f"pipes running out under the turquoise sea. Clear bright sky. No signs.",
}

# first reference = the image "SAME" refers to
REFS = {
 "S0": [], "END": ["S0"], "TAP": [], "TAPSALT": ["TAP"], "PAYOFF": ["TAP"], "BOIL": ["S0"], "FUEL": ["BOIL"], "HALL": [], "MEMBRANE": [], "CLOG": ["MEMBRANE"],
 "GAUGE": ["HALL"], "POWER": ["HALL"], "PX": ["HALL"], "SAND": ["HALL"], "LIME": ["HALL"], "CORRODE": [], "INTAKE": ["S0"],
 "CAP": ["INTAKE"], "PLUME": ["INTAKE"], "DIFFUSER": ["PLUME"], "GLASSES": [], "PEBBLE": [], "BOTTLE": [], "DROUGHT": [], "DROUGHT3": ["DROUGHT2"],
 "RESERVOIR": [], "PERTH": [],
}

if __name__ == "__main__":
    import json, sys
    print(json.dumps(P[sys.argv[1]]))
