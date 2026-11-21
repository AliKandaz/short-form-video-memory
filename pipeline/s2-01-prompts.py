# s2-01 (style 2, strategy2.md): the chicken coop that became a guest cabin. Still prompts for seedream_v5_pro 1k 9:16.
# Usage: python3 s2-01-prompts.py KEY -> prints the prompt. Lines follow strategy2.md 6.3 (REAL, BUILDER, ONLY, VIEW, CLOSE, COZY).
# Stills: B (the builder key, reused by every style-2 video), R (the witness close-up, also her key), O0-O6 and P (the locked
# outside view), I0-I6 (the locked inside view from the coop's door), CA and CB (tool close-ups). Each stage is an edit of the
# stage before it (LOCKV keeps the framing). The coop keeps its footprint (about 2.5 m wide) so the inside view stays consistent.
REAL = ("Photorealistic photo, like a frame from a phone video shot with a slightly wide lens: natural light, true-to-life colours, "
"real textures and wear. No text, no letters, no numbers, no signs, no logos, no brand names, no flags, no watermark.")
BUILDER = ("a man in his forties with a short salt-and-pepper beard, a navy knit beanie, an orange work jacket, grey cargo trousers, "
"tan work boots and grey work gloves")
WITNESS = ("a woman in her forties with dark hair in a loose bun, an oversized cream knit cardigan over a grey top, blue jeans and "
"slippers, holding a white mug")
HENS = "five hens, three russet-brown and two white"
YARD = ("a suburban back yard on a cold, clear late-autumn day: frosty grass with scattered brown leaves, a low weathered wooden "
"fence and bare trees along the right side, and the back of a two-storey house with pale grey siding, a white back door and "
"three wooden steps at the upper left of the frame")
COOP = ("a small, sagging old wooden chicken coop about 2.5 metres wide and tall enough to stand in: weathered grey boards with gaps "
"between them, a sagging roof of torn black tar paper, a little ramp up to a hatch, a rusty chicken-wire run along its left side, "
"straw poking out")
VIEWOUT = ("Camera: in the far corner of the yard, about 2.5 metres up, looking back toward the house at a slight downward angle. The "
"coop stands in the middle of the frame and fills about a third of it; the house's back door and steps are behind it at the upper "
"left; the fence and bare trees on the right; frosty lawn in the foreground.")
VIEWIN = ("Camera: in the coop's doorway at chest height with a wide lens, looking straight in at the back wall and its small square "
"window; the floor and both side walls are in the frame.")
ONLY2 = "The only people in the picture are the builder and the woman on the steps: no other people."
ONLY1 = "The only person in the picture is the builder: no other people."
NOONE = "There are no people in the picture except as described."
LOCKV = ("Keep exactly the same camera position, lens, height and framing as the reference image, and the same people, hens, house, "
"fence and trees. Change only this: ")
SAME = " Everything else is identical, including the light and the weather."
LOCKI = ("Keep exactly the same camera position, lens, height and framing as the reference image, and the same builder. "
"Change only this: ")  # the inside view: no hens, house, fence or trees to keep

P = {}
P["B"] = (REAL + " Full-length photo of the builder standing on a plain light grey studio background, facing the camera, relaxed, with "
"a slight smile: " + BUILDER + ". Even soft light. The whole figure from the head to the boots is in the frame and the face is "
"clear. " + ONLY1)
P["R"] = (REAL + " Close-up of " + WITNESS + ", standing on the wooden back steps of a house on a frosty late-autumn morning, laughing "
"behind the mug with steam rising from it, looking off to the side toward the yard. Her face and shoulders fill most of the "
"frame; the pale grey siding and the white back door are soft behind her. She is the only person in the picture.")
P["CA"] = (REAL + " Extreme close-up outdoors: a pair of hands in grey work gloves, with the cuffs of an orange work jacket, drive a "
"long screw into a new pale timber rafter with a plain dark grey cordless impact driver; curls of sawdust fly. The rafter and the "
"hands fill most of the frame; behind them, out of focus, bare tree branches and a pale winter sky. The tool has no text, no logos "
"and no brand colours. No faces in the picture.")
P["CB"] = (REAL + " Extreme close-up indoors: a pair of hands in grey work gloves, with the cuffs of an orange work jacket, press a pale "
"pine board into place on a wall and fix it with a plain dark grey nail gun. The board and the hands fill most of the frame; more "
"pine boards and pink insulation in soft focus behind. The tool has no text, no logos and no brand colours. No faces in the picture.")
P["O0"] = (REAL + " " + YARD[0].upper() + YARD[1:] + ". In the middle of the yard stands " + COOP + ". In front of it " + HENS + ", peck at "
"the frosty grass. The builder, the man in the first reference image (" + BUILDER + "), stands beside the coop holding a long "
"crowbar and looking at its sagging roof. On the back steps of the house stands the woman in the second reference image (" + WITNESS
+ "), smirking. " + VIEWOUT + " " + ONLY2)
P["O1"] = (LOCKV + "the coop's sagging roof has just collapsed down into the coop: its broken boards and torn tar paper hang inside the "
"walls and a big cloud of straw and dust bursts up out of it; the five hens are flapping away across the lawn with their wings "
"spread, none of them hurt; the builder has stepped back with one hand on his head; the woman on the steps is laughing." + SAME +
" " + ONLY2)
P["O2"] = (LOCKV + "a few days later the old coop's collapsed roof and grey boards are gone: its old timber frame stands stripped bare "
"and straightened on new pale timber posts, on a new raised floor of fresh plywood, on exactly the same spot and the same size; "
"where the old wire run was, at its left, stands a small new wooden hen house with a little ramp, and the five hens peck around it; a pile of old grey "
"boards and torn tar paper lies by the fence; the builder works on the frame; the woman on the steps watches with her mug." + SAME +
" " + ONLY2)
P["O3"] = (LOCKV + "the frame now has new pale timber rafters and a dark grey metal roof, and its walls are sheathed in plain plywood "
"with an opening for a window in the front wall and one for a door beside it; the builder stands at the door opening with a "
"drill; the woman on the steps watches, no longer smiling, her mug lowered." + SAME + " " + ONLY2)
P["O4"] = (LOCKV + "a window is fitted in the window opening and a glazed door in the door opening, the open gable above "
"the front wall is closed in, and all the walls and the gable are clad in vertical board-and-batten siding of new unpainted wood; "
"the builder stands on the lawn beside the cabin, fixing the last batten; the woman on the steps watches." + SAME + " " + ONLY2)
# O5.A put the porch on the house's back steps and the builder in front of the woman, so O5.B places both (21 Nov 2026).
P["O5"] = (LOCKV + "the little cabin is painted: deep green walls with cream trim round the window, the door and the corners; the "
"small hen house at the left is painted the same deep green with cream trim, like a tiny copy of it; a small wooden porch painted "
"cream is built right in front of the cabin's glazed door: a little deck level with the door's sill, a cream railing and two wide "
"steps coming down toward the camera onto the lawn; the house's back steps stay exactly as they are; the builder stands on the "
"lawn at the right of the porch, in front of the pile of old boards, holding a paint roller; the woman stays on the house's back "
"steps, fully in view, watching." + SAME + " " + ONLY2)
P["O6"] = (LOCKV + "a black lantern hangs beside the door (switched off), a wooden planter of small evergreens stands by the porch "
"steps and a doormat lies on the porch; the pile of old boards and tar paper is gone; the five hens peck around their house; the builder "
"stands on the lawn at the right, looking at the finished cabin; the woman on the house's back steps watches." + SAME + " " + ONLY2)
# P keeps the set but not the people of O6: the builder is inside, the hens in their house, one hen on the porch rail.
P["P"] = ("Keep exactly the same camera position, lens, height and framing as the reference image, and the same house, cabin, porch, "
"hen house, fence and trees. Change only this: IT IS DUSK, with no daylight left: a deep blue sky, light snow falling and a thin "
"layer of fresh snow on the roofs, the porch rail and the lawn; warm golden light glows from the cabin's window and glazed door, "
"and the lantern beside the door is lit; a small warm light glows in the little hen house, where the hens have gone in for the "
"night; one hen sits on the porch rail peering in through the cabin's window; the builder is not in view (he is inside the cabin); "
"the woman stands on the house's back steps in her cardigan with her mug, staring at the glowing cabin in surprise. The only "
"person in the picture is the woman on the steps.")
P["I0"] = (REAL + " Inside a small old wooden chicken coop, about 2.5 metres wide and tall enough to stand in: rough weathered grey "
"boards with thin gaps of daylight between them, two roosting bars across the right side, a row of three wooden nest boxes full of "
"straw on the left wall, a droppings board, cobwebs in the corners, straw and dust on the floor, dusty sunbeams. The builder, the "
"man in the reference image (" + BUILDER + "), stands inside looking around with his hands on his hips. " + VIEWIN + " " + ONLY1)
P["I3"] = (LOCKI + "the walls and the ceiling are lined with warm pale pine boards, the floor is wide honey-coloured planks, and the "
"window has a neat pine frame; the builder runs a gloved hand along the new boards." + SAME + " " + ONLY1)
P["I4"] = (LOCKI + "a bed with a plain wooden frame stands against the back wall under the window, a small wooden desk and chair along "
"the right wall, and two wooden shelves on the left wall; the builder sets the chair at the desk." + SAME + " " + ONLY1)
P["I5"] = (LOCKI + "the bed has a patchwork quilt in muted reds and creams, two white pillows and a grey wool throw at its foot; a round "
"braided rug lies on the floor; books and a small green plant stand on the shelves; a small bedside lamp with a linen shade stands "
"on a little wooden table at the left end of the bed, switched off; a mug sits on the desk; the builder has moved to the right "
"side of the room and stands behind the desk chair with one hand on its back, looking at the bed, so the whole bed, the lamp and "
"the left wall are in view." + SAME + " " + ONLY1)
P["I6"] = (LOCKI + "IT IS DUSK outside: the window shows a deep blue sky with light snow falling, and the room is dim and cool, lit "
"only by the last blue light from the window; the bedside lamp is still switched off; the builder stands in the middle of the room "
"beside the bed and reaches his hand toward the lamp's switch; the lamp stays in full view."
+ " The room, its furniture and its colours are otherwise identical. " + ONLY1)

REFS = {"B": [], "R": [], "CA": [], "CB": [], "O0": ["B", "R"], "O1": ["O0"], "O2": ["O0"], "O3": ["O2"], "O4": ["O3"],
        "O5": ["O4"], "O6": ["O5"], "P": ["O6"], "I0": ["B"], "I1": ["I0"], "I2": ["I1"], "I3": ["I2"], "I4": ["I3"],
        "I5": ["I4"], "I6": ["I5"]}
AR = {}

# Try B of the two view keys (21 Nov 2026): O0.A drew a chest-high coop while I0.A is a walk-in coop, so O0.B enlarges it;
# I0.B caves the roof in, so the inside "before" follows the hook (cut B goes hook -> witness -> inside, guts out -> outside build).
P["O0.B"] = (LOCKV + "the chicken coop is bigger: an old walk-in chicken coop like a small garden shed on short legs, about 2.5 "
"metres wide, tall enough for a grown man to walk in: its eaves are higher than the builder's head and its ridge well above that; "
"a narrow plank door on the side facing the camera. It keeps the same weathered grey boards with gaps between them, the same "
"sagging roof of torn black tar paper, the same little ramp up to a hatch and the same rusty chicken-wire run along its left side, "
"and it stands on the same spot. The woman on the back steps stays fully in view to the left of the coop, and the builder stands "
"just to the right of it with his crowbar." + SAME + " " + ONLY2)
P["I0.B"] = (LOCKI + "the coop's roof has caved in: broken roof boards and torn black tar paper hang down into the coop from a big "
"ragged hole, with bright daylight and pale sky through it; dust and bits of straw float in the light; the roosting bars, the "
"nest boxes, the straw and the cobwebs are still there; the builder looks up at the hole with one hand on his head." + SAME + " "
+ ONLY1)
P["I1"] = (LOCKI + "the roosting bars, the nest boxes, the droppings board, the straw, the cobwebs and the broken roof are all gone: "
"only the four bare old grey board walls are left, open to the pale sky above (there is no roof at all), with daylight through "
"the gaps between the boards and a bare, swept floor; the small window in the back wall stays; the builder carries out the last nest box." + SAME + " " + ONLY1)
P["I2"] = (LOCKI + "a new roof closes the room again: the old grey boards are gone, and the walls and the ceiling are framed with new "
"pale timber studs and joists with pink insulation filling the spaces between them; no daylight shows through the walls; there "
"is a new pale plywood subfloor; the small window in the back wall is in the same place; the builder presses a batt of pink "
"insulation into place between two studs." + SAME + " " + ONLY1)
REFS.update({"O0.B": ["O0.A"], "I0.B": ["I0.A"]})

if __name__ == "__main__":
    import json, sys
    print(json.dumps(P[sys.argv[1]], ensure_ascii=False))
