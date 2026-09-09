# Three CC-BY files were dropped from the library because they genuinely
# require credit and this site no longer carries any. Their derivatives are
# deleted, not merely unlinked:
#   family-885254b1-6cd, family-a352b666-464, re-yard-b48c0db7-0a8
# Frames added after the first build, from two sources that did not exist then:
#
#   L<stem>  ~/Downloads/wirewalk-photos/licensed/<stem>.jpg
#            PROPERLY-LICENSED REFERENCE IMAGERY. NOT the studio's own work.
#            CC0, PDM or CC-BY only; share-alike was excluded on purpose so
#            there is never an argument about what the surrounding page
#            becomes. Provenance comes from licensed_manifest.json and is
#            written into _data/licensed.yml by the builder, never retyped.
#            The builder prefixes "Reference frame: " onto every alt below,
#            which is the convention the existing 44 reference frames use.
#
#   O<name>  ~/Downloads/wirewalk-photos/selects/<name>.jpg
#            The owner's OWN photography. No prefix; these are portfolio work.
#
# Fields: slug, source, ratio(w/h), role, anchor(0=top..1=bottom), alt
#
# Ratios are chosen to lose the least of each frame. Several sources are only
# 960-1024px on the long edge, so a ratio that crops across the long edge
# (a 4:5 out of a 3:2, say) leaves a rendition too small to publish. Where
# that was the case the native orientation was kept instead. build_licensed.py
# prints the rendered width of every frame and fails the build under 600px,
# so this cannot rot quietly.
NEW = [

# ══ PROPERTY — THE OWNER'S OWN WORK ══════════════════════════════════════
# These lead the property section. Reference frames follow, clearly separated.
("prop-timber",     "Oproperty-249",(3,2),"feature",.5,"Timber house with a metal roof and a pickup on the drive"),
("prop-timber-t",   "Oproperty-249",(4,5),"grid",   .45,"Timber house with a metal roof, seen from the drive"),
("prop-barn",       "Oproperty-085",(3,2),"feature",.5,"A barn standing in long summer grass"),
("prop-garden",     "Oproperty-254",(3,2),"feature",.5,"A landscaped garden with a white footbridge and a gazebo"),
("prop-garden-t",   "Oproperty-254",(4,5),"grid",   .5,"A landscaped garden with a white footbridge"),
("prop-pergola",    "Oproperty-140",(4,3),"feature",.5,"A vine-covered pergola with seating beneath it"),
("prop-modern",     "Oproperty-083",(3,2),"feature",.5,"Modern architecture stepping down to a water feature"),

# ══ FAMILY AND CHILDREN — REFERENCE FRAMES ═══════════════════════════════
("ref-fam-laugh",    "Lfamily-7b4ec082-444",(3,2),"feature",.4,"a father holding a laughing child up in a field"),
("ref-fam-laugh-t",  "Lfamily-7b4ec082-444",(4,5),"feature",.35,"a father holding a laughing child up in a field"),
("ref-fam-sisters",  "Lfamily-cf5b09d7-ac3",(3,2),"feature",.45,"two girls laughing with their arms around each other among autumn leaves"),
("ref-fam-carry",    "Lfamily-f2017cc7-6bd",(3,2),"grid",.45,"a parent carrying a toddler, close and candid"),
("ref-fam-woods",    "Lfamily-f8a41c63-45a",(3,2),"grid",.5,"a parent and a small child walking a woodland path, backlit"),
("ref-fam-beach",    "Lfamily-dcc3a88a-64d",(3,2),"grid",.5,"a parent carrying a child along a wide empty beach"),
("ref-fam-grass-dog","Lfamily-01c62e71-cd1",(3,2),"grid",.5,"a family lying on the grass with their dog"),
("ref-fam-puppy",    "Lfamily-36c7c0bd-6a1",(3,2),"grid",.5,"a family sitting on the grass with a puppy"),
("ref-fam-leaves",   "Lfamily-5b972778-7b7",(3,2),"grid",.5,"a family's feet gathered in a drift of autumn leaves"),
("ref-fam-surf-bw",  "Lfamily-618fe7c9-394",(4,3),"grid",.5,"children wading in the surf, in monochrome"),
("ref-fam-shore",    "Lfamily-9079f62f-7da",(4,5),"grid",.5,"a family walking a misted shoreline at sunset"),

# ══ NEWBORN — REFERENCE FRAMES ═══════════════════════════════════════════
# These illustrate the SERVICE. They are not evidence of newborn work done.
("ref-nb-star",     "Lnewborn-bb140918-b1b",(4,5),"feature",.5,"a newborn's hand resting open on a star-patterned blanket"),
("ref-nb-finger",   "Lnewborn-7ae5d76c-ce4",(3,2),"grid",.5,"a newborn's fingers closed around an adult finger"),
("ref-nb-feet",     "Lnewborn-d50f4017-289",(3,2),"grid",.5,"newborn feet cupped in a pair of adult hands, in monochrome"),
("ref-nb-muslin",   "Lnewborn-da67bde8-ebc",(3,2),"grid",.5,"a newborn's hand curled on soft muslin"),

# ══ PROPERTY — REFERENCE FRAMES, EXTERIORS ═══════════════════════════════
("ref-re-ext-dusk", "Lre-exterior-776abccf-f74",(3,2),"feature",.5,"a house at dusk with its windows lit and a pool in the foreground"),
("ref-re-ext-walk", "Lre-exterior-00f6a15b-26c",(4,5),"feature",.5,"a white clapboard house behind a planted front walk"),

# ══ PROPERTY — REFERENCE FRAMES, INTERIORS ═══════════════════════════════
("ref-re-int-glazing","Lre-interior-1f6ae721-045",(4,3),"grid",.5,"a living room behind floor-to-ceiling glazing"),
("ref-re-int-outlook","Lre-interior-06204d58-e78",(3,2),"grid",.5,"an open lounge with a city outlook"),
("ref-re-int-navy",   "Lre-interior-4d47e4f8-3f0",(3,2),"grid",.5,"a living room with a deep navy gallery wall"),
("ref-re-int-minimal","Lre-interior-5c1b8889-c9d",(3,2),"grid",.5,"a minimal living room in a neutral palette"),
("ref-re-int-bright", "Lre-interior-7424bd95-7f4",(3,2),"grid",.5,"a bright living room with a patterned armchair"),
("ref-re-int-dining", "Lre-interior-c6b1bca4-744",(4,5),"grid",.5,"a bright dining room with a long table and panelled walls"),

# ══ PROPERTY — REFERENCE FRAMES, KITCHENS ════════════════════════════════
("ref-re-kit-island", "Lre-kitchen-0b015b64-536",(1,1),"grid",.5,"a kitchen island with bar stools and pale cabinetry"),
("ref-re-kit-sink",   "Lre-kitchen-3c0a0e94-5b9",(3,2),"grid",.5,"a farmhouse sink set under a bay window"),
("ref-re-kit-compact","Lre-kitchen-2196bf51-fa0",(3,2),"grid",.5,"a compact kitchen with integrated appliances"),
("ref-re-kit-galley", "Lre-kitchen-81e90529-fb6",(3,2),"grid",.5,"a galley kitchen with a patterned splashback"),

# ══ PROPERTY — REFERENCE FRAMES, BEDROOMS AND BATHROOMS ══════════════════
("ref-re-bed-corner", "Lre-bedroom-1b7a9f3d-da8",(21,9),"grid",.5,"a bedroom with corner windows and a fireplace"),
("ref-re-bed-timber", "Lre-bedroom-82cb7fca-4fd",(16,9),"grid",.5,"a bedroom with a timber feature wall"),
("ref-re-bed-study",  "Lre-bedroom-61817c40-ddb",(3,2),"grid",.5,"a bedroom with a study corner under a warm lamp"),
("ref-re-bed-teal",   "Lre-bedroom-93b1e6b4-21e",(3,2),"grid",.5,"a made bed with teal cushions in morning light"),
("ref-re-bath-tub",   "Lre-bath-2a6f7783-f77",(4,3),"grid",.5,"a freestanding tub standing on stone tile"),
("ref-re-bath-vanity","Lre-bath-2a8189c6-f0f",(4,5),"grid",.5,"a white bathroom with vanity seating"),
("ref-re-bath-view",  "Lre-bath-82f59a13-810",(3,2),"grid",.5,"a bathroom with a city view"),
("ref-re-bath-door",  "Lre-bath-89cea2aa-8c5",(3,2),"grid",.5,"a bathroom seen through a bedroom doorway"),

# ══ PROPERTY — REFERENCE FRAMES, GROUNDS ═════════════════════════════════
("ref-re-yard-terrace","Lre-yard-0d5a95a5-8ef",(21,9),"grid",.5,"a planted garden running up to a seating terrace"),
("ref-re-yard-patio",  "Lre-yard-13ed51cc-13c",(3,2),"grid",.5,"a covered patio with an outdoor fireplace and grill"),
("ref-re-yard-deck",   "Lre-yard-1c8a6cdd-baf",(3,2),"grid",.5,"a pool with a timber deck surround"),
("ref-re-yard-loungers","Lre-yard-20a0f861-638",(3,2),"grid",.5,"a pool terrace set with loungers"),
("ref-re-yard-border",  "Lre-yard-69c7e457-8ec",(3,2),"grid",.5,"a fenced border in full summer flower"),
("ref-re-yard-path",    "Lre-yard-8715a77e-417",(3,2),"grid",.5,"a stone path running through a formal garden"),
("ref-re-yard-bench",   "Lre-yard-9e9171d3-957",(4,5),"grid",.45,"a bench under a tree on an autumn lawn"),

# ══ PROPERTY — REFERENCE FRAMES, AERIALS ═════════════════════════════════
("ref-re-air-treelined","Lre-aerial-b83979c0-88a",(3,2),"feature",.5,"an aerial of tree-lined suburban streets"),
("ref-re-air-townhouses","Lre-aerial-47eea1c1-832",(3,2),"grid",.5,"an aerial over townhouses and the streets between them"),
("ref-re-air-park",     "Lre-aerial-71fea6c8-bf5",(4,3),"grid",.5,"an overhead view of a residential neighbourhood and its park"),
("ref-re-air-crescent", "Lre-aerial-a846bc75-1ab",(3,2),"grid",.5,"an aerial of a suburban crescent"),
("ref-re-air-street",   "Lre-aerial-af9c5198-fa7",(3,2),"grid",.5,"an aerial of a street and the green space beside it"),
("ref-re-air-snow",     "Lre-aerial-abe94307-7fa",(16,9),"grid",.5,"a drone view of a house in snow"),
]

# ─────────────────────────────────────────────────────────────────────────
# SECOND SWEEP. The library grew from 50 frames to 124 once the source was
# constrained to Openverse's `photograph` category, which removed the
# clipart, the 1900s studio portraits and the museum scans that polluted the
# first pass. Same rules, same manifest, same labelling: every one of these
# is a REFERENCE frame and the builder prefixes "Reference frame: " to the
# alt text below.
#
# EVENTS ARE A KNOWN GAP AND ARE NOT PAPERED OVER. The library contains no
# wedding and no conference photography under an acceptable licence -- the
# searches returned political ceremonies and museum objects. The five event
# frames below are PARTY DETAILS and are used as party details: a sparkler,
# a cake, cupcakes, a flat lay, balloons. None of them is placed where it
# could read as wedding or conference coverage. That category still needs
# the owner's own work and the page says so in as many words.
#
# Most of these sources are 960x640, which is 3:2 exactly, so r32 crops
# nothing at all. Where a 4:5 tile was wanted the frame had to be natively
# portrait -- cropping 4:5 out of a 960x640 leaves a 512px rendition, which
# is not publishable. Portrait sources are used for the tall slots instead.
NEW += [

# ══ FAMILY AND CHILDREN — REFERENCE FRAMES, SECOND SWEEP ═════════════════
# Faces, eye contact and warmth: what the section actually needed, and what
# the studio's own four child frames -- shot from behind or at distance --
# cannot carry on their own.
("ref-fam-hug",      "Lfamily-7673b1b2-060",(3,2),"feature",.45,"a family in a group hug, all of them laughing"),
("ref-fam-lift",     "Lfamily-31d35e4b-4ba",(3,2),"feature",.4,"a mother holding her daughter close, backlit"),
("ref-fam-baking",   "Lfamily-2d4b99d9-995",(3,2),"feature",.45,"a grandmother and her granddaughter baking together"),
("ref-fam-newbaby",  "Lfamily-55827c02-ce7",(3,2),"feature",.45,"a family together in bed meeting the new baby"),
("ref-fam-cheek",    "Lfamily-412012f3-8ab",(3,2),"grid",.4,"a mother and daughter cheek to cheek with their eyes closed"),
("ref-fam-bed",      "Lfamily-1ad85d17-d24",(3,2),"grid",.45,"parents playing with a toddler on the bed in morning light"),
("ref-fam-sibkiss",  "Lfamily-84005e87-a2a",(3,2),"grid",.4,"an older sibling kissing the new baby"),
("ref-fam-newborn3", "Lfamily-e3b39ad7-8a7",(3,2),"grid",.45,"parents and children together in bed with a newborn"),
("ref-fam-twogen",   "Lfamily-271d8797-31e",(4,3),"grid",.4,"two generations together, a monochrome portrait"),
("ref-fam-adult",    "Lfamily-8e1238ca-38d",(3,2),"grid",.4,"a mother and her adult daughter embracing"),
("ref-fam-golden",   "Lfamily-a514e487-56b",(3,2),"grid",.45,"a mother and daughter outdoors at golden hour"),
("ref-fam-closeport","Lfamily-f51e9fa3-a82",(3,2),"grid",.4,"a mother and daughter photographed close, outdoors"),
("ref-fam-picnic",   "Lfamily-4e287743-f54",(3,2),"grid",.5,"a family picnic on the grass with a football"),
("ref-fam-park",     "Lfamily-4ef13789-c93",(3,2),"grid",.5,"a family playing together in the park"),
("ref-fam-dogport",  "Lfamily-74d31a89-d2e",(3,2),"grid",.5,"a family portrait on the grass with their dog"),
("ref-fam-point",    "Lfamily-79942813-3a1",(3,2),"grid",.45,"a father pointing something out to the children"),
("ref-fam-walk",     "Lfamily-cdaf5bb8-314",(3,2),"grid",.5,"a family walking hand in hand through the park"),
("ref-fam-four",     "Lfamily-f80b8668-340",(3,2),"grid",.45,"a relaxed outdoor portrait of a family of four"),
("ref-fam-tree",     "Lfamily-c9861abf-8f3",(4,5),"feature",.5,"a family gathered at the foot of a tree"),
("ref-fam-newmum",   "Lfamily-f04cbdf1-db1",(4,5),"feature",.4,"a mother holding a newborn with her older child alongside"),

# ══ NEWBORN — REFERENCE FRAMES, SECOND SWEEP ═════════════════════════════
("ref-nb-wool",     "Lnewborn-34f35733-bc5",(3,2),"grid",.5,"newborn feet against knitted wool"),
("ref-nb-cream",    "Lnewborn-3ee8a1f6-029",(3,2),"grid",.5,"newborn feet on a cream blanket"),
("ref-nb-sleep",    "Lnewborn-7596daff-064",(4,3),"grid",.5,"a newborn sleeping in soft daylight"),
("ref-nb-cupped",   "Lnewborn-e1a9c5f8-f02",(3,2),"grid",.5,"newborn feet cupped in a parent's hands"),

# ══ PETS — REFERENCE FRAMES ══════════════════════════════════════════════
("ref-pet-leap",    "Lpets-5073498f-a15",(3,2),"feature",.45,"a border collie leaping on the sand"),
("ref-pet-shepherd","Lpets-6c60a81e-1e7",(4,5),"feature",.4,"a german shepherd at full stretch on the beach"),
("ref-pet-shore",   "Lpets-6145605f-c32",(3,2),"grid",.5,"a small dog running along a turquoise shoreline"),
("ref-pet-beagle",  "Lpets-7ee2bf1c-e92",(4,3),"grid",.5,"a beagle running through shallow surf"),
("ref-pet-two",     "Lpets-8d6304ac-6bb",(3,2),"grid",.5,"two dogs together on the beach"),
("ref-pet-husky",   "Lpets-8da705b6-e41",(4,5),"grid",.4,"a husky running alongside its owner"),
("ref-pet-collies", "Lpets-b894c49d-d96",(16,9),"grid",.5,"two collies running through shallow water"),
("ref-pet-retriever","Lpets-ba620708-fa0",(3,2),"grid",.5,"a golden retriever running towards the camera"),
("ref-pet-labrador","Lpets-e4972749-c4f",(3,2),"grid",.5,"a black labrador sprinting, seen from a low angle"),
("ref-pet-walk",    "Lpets-7ac7ee02-fd5",(3,2),"grid",.5,"an owner walking a dog down a tree-lined path"),
("ref-pet-pergola", "Lpets-babb5ecd-fe9",(3,2),"grid",.5,"walking the dog under a pergola walk"),
("ref-pet-horse",   "Lpets-019b340d-ddf",(3,2),"grid",.5,"a horse photographed in its paddock"),
# 574px on the long edge across the frame: a portrait source can only be
# trimmed in height, so no ratio recovers width. Published at its native
# 9:16 rather than cropped, and used small.
("ref-pet-horse-graze","Lpets-4932ba43-87d",(9,16),"tile",.5,"a horse grazing, photographed close"),

# ══ PORTRAITS AND BUSINESS — REFERENCE FRAMES ════════════════════════════
("ref-port-atrium", "Lportrait-3399da31-a35",(3,2),"feature",.4,"a senior professional photographed in an office atrium"),
("ref-port-folded", "Lportrait-2cd309b9-3aa",(3,2),"grid",.4,"a professional portrait, arms folded, colleagues behind"),
("ref-port-open",   "Lportrait-e45075af-0e7",(3,2),"grid",.4,"a professional portrait, arms folded, an open office behind"),
("ref-port-smile",  "Lportrait-813aa247-80b",(3,2),"grid",.4,"a professional portrait with a natural smile, workplace setting"),
("ref-port-coffee", "Lportrait-23980511-186",(3,2),"grid",.4,"a professional portrait with the office behind and coffee in hand"),
("ref-port-phone",  "Lportrait-47630adb-c42",(3,2),"grid",.4,"a professional on the phone with the team behind"),
("ref-port-meeting","Lportrait-eb2c686a-d74",(3,2),"grid",.4,"a professional portrait with a meeting going on behind"),
("ref-port-desk",   "Lportrait-fe9c0e44-93d",(3,2),"grid",.4,"a seated portrait at a desk against a clean backdrop"),
("ref-biz-meeting", "Lbusiness-012ee794-a3a",(3,2),"grid",.45,"a team meeting around a table"),
("ref-biz-discuss", "Lbusiness-ffe2fa81-8e9",(3,2),"grid",.45,"a mixed team in discussion in a workplace"),

# ══ AUDIO — REFERENCE FRAMES ═════════════════════════════════════════════
("ref-aud-faders",   "Laudio-28ffeeda-2f5",(3,2),"feature",.5,"hands riding the faders on a lit mixing console"),
("ref-aud-popshield","Laudio-adeb472b-35b",(3,2),"feature",.4,"a vocalist tracking behind a pop shield"),
("ref-aud-condenser","Laudio-9785b844-4d3",(4,5),"feature",.45,"a large-diaphragm condenser microphone in a shock mount"),
("ref-aud-vintage",  "Laudio-53395626-8cb",(4,3),"grid",.5,"vintage ribbon and condenser microphones"),
("ref-aud-tracking", "Laudio-57c84a8f-501",(3,2),"grid",.4,"recording vocals in headphones at the microphone"),
("ref-aud-boom",     "Laudio-ad4e0d70-2a8",(3,2),"grid",.5,"a microphone on a boom against a dark backdrop"),
("ref-aud-desk",     "Laudio-bfcf32e0-540",(3,2),"grid",.5,"a home studio desk with monitors and a laptop"),
("ref-aud-strip",    "Laudio-d0777300-f6a",(3,2),"grid",.5,"a console channel strip in close-up"),
("ref-aud-vocal-bw", "Laudio-f2a47c85-883",(3,2),"grid",.4,"a vocalist at the microphone, in monochrome"),
("ref-aud-session",  "Laudio-fc35e82c-4b3",(16,9),"grid",.5,"a tracking session with the artist at the microphone"),

# ══ VIDEO — REFERENCE FRAMES ═════════════════════════════════════════════
("ref-vid-set",   "Lvideo-138b3efe-806",(16,9),"feature",.5,"an empty studio with lights and stands set for a shoot"),
("ref-vid-floor", "Lvideo-344bf044-48c",(3,2),"feature",.5,"a production set with lighting and monitors"),
("ref-vid-stage", "Lvideo-ab4ea1cf-f06",(3,2),"grid",.5,"filming a performer on a lit stage"),
("ref-vid-rig",   "Lvideo-ede9b715-f2b",(4,5),"grid",.45,"a cinema camera rig under coloured light"),

# ══ PRODUCT — REFERENCE FRAMES ═══════════════════════════════════════════
("ref-prod-mug-white","Lproduct-3722e9c2-f01",(1,1),"grid",.5,"a glass mug photographed as a clean packshot on white"),
("ref-prod-lamp-white","Lproduct-bf8a8bc8-575",(1,1),"grid",.5,"a stage light unit photographed as a packshot on white"),
("ref-prod-basil",   "Lproduct-ec9c3c28-89d",(3,2),"grid",.5,"fresh basil on a white background"),
("ref-prod-flatlay", "Lproduct-81e41852-8d5",(3,2),"grid",.5,"a flat lay of coffee, flowers and stationery"),
("ref-prod-latte",   "Lproduct-89c87780-125",(3,2),"grid",.5,"a latte with poured art, photographed overhead"),
("ref-prod-honey",   "Lproduct-60a2315e-ed2",(4,5),"grid",.5,"a honey jar still life on dark wood"),
("ref-prod-burger",  "Lproduct-07dd3331-bf9",(4,5),"grid",.45,"a burger and fries styled with drinks"),

# ══ EVENTS — REFERENCE FRAMES, PARTY DETAIL ONLY ═════════════════════════
# Read the block comment above before using any of these anywhere near
# wedding or conference copy. They are cake, confetti and sparklers.
("ref-ev-sparkler", "Levent-4081e0ae-e3c",(3,2),"grid",.5,"a sparkler held in a pair of hands at dusk"),
("ref-ev-cake",     "Levent-75e7ccf2-1aa",(3,2),"grid",.5,"a lit birthday cake carried through a dark room"),
("ref-ev-cupcakes", "Levent-189934f2-040",(3,2),"grid",.5,"cupcakes and candles styled on wood"),
("ref-ev-flatlay",  "Levent-4c7dc997-60e",(3,2),"grid",.5,"a party flat lay with confetti and cake"),
("ref-ev-balloons", "Levent-7e0d5bc9-d83",(4,5),"grid",.4,"balloons against a white brick wall"),
]

# ─────────────────────────────────────────────────────────────────────────
# THIRD PASS — HERO CROPS, after the pages were looked at in a real browser.
#
# What was wrong: the homepage hero was family-198, the owner's own frame of
# a child photographed FROM BEHIND, and /family/ opened with family-075 in a
# 21:9 band -- a crop that throws away 36% of the frame's HEIGHT and took the
# top of a head with it. On a site selling family portraits the largest image
# showed a child's back.
#
# The rule these entries exist to enforce: A CROP THAT TRIMS HEIGHT CAN CUT A
# HEAD OFF; A CROP THAT TRIMS SIDES CANNOT. Every source here is 3:2, so
# cropping to 4:3 trims 11% off the SIDES and touches no vertical pixel --
# which is why the hero slots moved from 4:5 to 4:3 rather than the frames
# moving to fit the old slots. 4:5 out of a 3:2 source would have thrown away
# 47% of the width and left a 512px rendition; both are worse than a slot
# that is slightly less tall.
#
# The one wide crop below trims height, so it is anchored at 0.05 -- hard to
# the top, where heads are -- and takes its 16% out of the ground instead.
NEW += [
("ref-fam-hug-43",     "Lfamily-7673b1b2-060",(4,3),"feature",.5,"a family in a group hug, all of them laughing"),
("ref-fam-lift-43",    "Lfamily-31d35e4b-4ba",(4,3),"feature",.5,"a mother lifting her laughing daughter, backlit"),
("ref-fam-cheek-43",   "Lfamily-412012f3-8ab",(4,3),"feature",.5,"a mother and daughter cheek to cheek in golden light"),
("ref-fam-sibkiss-43", "Lfamily-84005e87-a2a",(4,3),"grid",.5,"an older sibling kissing the new baby"),
("ref-fam-baking-43",  "Lfamily-2d4b99d9-995",(4,3),"grid",.5,"a grandmother and her granddaughter baking together"),
("ref-fam-golden-43",  "Lfamily-a514e487-56b",(4,3),"feature",.5,"a mother and daughter outdoors at golden hour"),
("ref-fam-dogport-43", "Lfamily-74d31a89-d2e",(4,3),"grid",.5,"a family on the grass with their dog, facing the camera"),
("ref-fam-newborn3-43","Lfamily-e3b39ad7-8a7",(4,3),"grid",.5,"parents and children together in bed with the newborn"),
("ref-nb-hat-43",      "Lnewborn-1f6e6288-bb1",(4,3),"feature",.5,"a newborn asleep, wrapped, in a striped hat"),
# 4898x3265 source, so 16:9 still lands at 4898px wide. Anchored to the top:
# the child in this frame is held UP, and the 16% this crop costs comes out
# of the field at the bottom rather than off anybody's head.
("ref-fam-laugh-wide", "Lfamily-7b4ec082-444",(16,9),"hero",.05,"a father holding a laughing child up in a field"),
]

# ─────────────────────────────────────────────────────────────────────────
# HEAD-SAFE RE-ANCHORS of the owner's own frames.
#
# An audit of all 312 crops for "how much does this take off the TOP" found
# five containing people that were centring their vertical trim -- so a
# close portrait lost 7-17% off the top of the frame, which is precisely how
# a forehead gets cut. Same slug content, same ratio, same layout; only the
# anchor moves to 0, which takes the whole trim off the BOTTOM instead.
# Heads are at the top of photographs of people; ground is at the bottom.
#
# These are the owner's own work (F = his Flickr, O = the studio archive) and
# carry no "Reference frame:" prefix.
NEW += [
("ppl-smoker-t2", "Fpeople-53693994437",(3,2),"feature",0,"Older man outdoors, cigarette in his lips, weathered face filling the frame"),
("ppl-bench-t2",  "Fpeople-53695094818",(3,2),"grid",0,"Man in a flat cap sitting alone on a park bench among fallen leaves"),
("ppl-tower-t2",  "Fpeople-53744800312",(3,2),"tile",0,"Two lifeguards on a yellow beach tower, rescue buoys planted in the sand"),
("ppl-quad-t2",   "Fpeople-53695324610",(3,2),"grid",0,"Beach patrol rider crossing the sand on a quad bike"),
("fam-dress-w2",  "Ofamily-198",(3,2),"grid",0,"Small child in a purple dress in dappled light"),
]

# ─────────────────────────────────────────────────────────────────────────
# THE CC0 LIBRARY. C<stem> = ~/Downloads/wirewalk-photos/cc0/<stem>.jpg
#
# No attribution is required for any of these, so none of them carries a
# label, a caption of provenance, or an entry on a credits page -- all three
# were a precaution I took, not a licence condition, and on a photographer's
# portfolio they read as a confession. Alt text describes the picture, which
# is what alt text is for.
#
# WEDDINGS were the category the site had to talk around; there are now 18
# frames and it does not. Business gained warehouse, construction, laboratory
# and workshop work that the commercial sections needed.
#
# Ratios follow the same rule as everything above: a crop that trims SIDES
# cannot cut a head off, a crop that trims HEIGHT can, so anything with a
# person in it either trims sides or is anchored towards the top.
NEW += [

# ══ WEDDINGS ═════════════════════════════════════════════════════════════
("wed-bride",       "Cwedding-1239b72f-6e0",(4,5),"feature",.1,"Bride holding her bouquet, photographed outdoors"),
("wed-couple-tree", "Cwedding-d240f575-611",(3,2),"feature",.5,"A couple standing together beneath an old tree"),
("wed-embrace",     "Cwedding-c97e60ed-2e4",(3,2),"feature",.4,"A couple embracing, the bouquet still in her hand"),
("wed-woodland",    "Cwedding-63a89c1d-dc7",(3,2),"feature",.4,"A couple in woodland, bouquet between them"),
("wed-firstdance",  "Cwedding-429c9f30-342",(3,2),"feature",.2,"The first dance, in monochrome"),
("wed-veil",        "Cwedding-fd64e867-360",(3,2),"grid",.4,"Hands joined, the veil behind them"),
("wed-rings",       "Cwedding-e039e02b-77a",(3,2),"grid",.5,"Rings and hands resting over the bouquet"),
("wed-hands",       "Cwedding-377b2380-8ba",(3,2),"grid",.5,"Hands and bouquet, close"),
("wed-bouquet-pair","Cwedding-226dd76d-c7b",(3,2),"grid",.5,"The bouquet held between bride and groom"),
("wed-wildflower",  "Cwedding-95c6e010-2f2",(3,2),"grid",.5,"A bride holding a wildflower bouquet"),
("wed-sunflower",   "Cwedding-b1a5149d-140",(1,1),"grid",.5,"A sunflower bouquet, the couple behind it"),
("wed-bouquet-face","Cwedding-a7648903-ac2",(4,5),"grid",.15,"A bouquet raised to the face"),
("wed-pastel",      "Cwedding-a6be7f05-8cc",(3,2),"grid",.5,"A pastel bouquet, close in"),
("wed-arrangement", "Cwedding-d9556713-f74",(3,2),"grid",.5,"A flower arrangement in soft light"),
("wed-toptable",    "Cwedding-a838ddb8-42c",(3,2),"grid",.5,"The top table set for the reception"),
("wed-cake",        "Cwedding-a8594dcc-7ca",(3,2),"grid",.5,"The cake on its stand, styled for the room"),
("wed-placesetting","Cwedding-c1663d5c-313",(16,9),"grid",.5,"A place setting with its name card"),
("wed-tablerun",    "Cwedding-96722af6-af4",(4,5),"grid",.3,"A reception table laid, detail running along it"),

# ══ EVENTS ═══════════════════════════════════════════════════════════════
("ref-ev-banquet",  "Cevent-ecaf6429-24f",(3,2),"feature",.5,"A banquet hall laid for a function"),
("ref-ev-reception","Cevent-fe5237f2-518",(3,2),"grid",.4,"Guests talking at a reception"),

# ══ BUSINESS, INDUSTRY AND SCIENCE ═══════════════════════════════════════
("ref-biz-lab",       "Cbusiness-691ab668-bd1",(3,2),"feature",.4,"Two researchers working at the bench"),
("ref-biz-warehouse", "Cbusiness-9a916b23-95f",(3,2),"feature",.5,"A warehouse aisle and its racking"),
("ref-biz-crane",     "Cbusiness-a2559f13-927",(3,2),"feature",.5,"Tower cranes against open sky"),
("ref-biz-workbench", "Cbusiness-17650262-1fa",(4,5),"feature",.15,"A maker at a workbench, a dog beside him"),
("ref-biz-testrig",   "Cbusiness-b8587c19-614",(3,2),"grid",.4,"A technician working inside a test rig"),
("ref-biz-instrument","Cbusiness-00bc7a06-f90",(4,5),"grid",.3,"An operator at an instrument under red light"),
("ref-biz-engineers", "Cbusiness-8ddfe4be-c72",(3,2),"grid",.4,"Engineers setting up equipment"),
("ref-biz-concrete",  "Cbusiness-06861cd8-d36",(3,2),"grid",.4,"Cutting concrete on site"),
("ref-biz-excavator", "Cbusiness-72cad48e-fc0",(3,2),"grid",.4,"An excavator and crew on a dig"),
("ref-biz-paving",    "Cbusiness-af99d058-ecb",(3,2),"grid",.4,"A paving crew at work"),
("ref-biz-forklift",  "Cbusiness-03d4aeeb-67e",(16,9),"grid",.1,"A forklift moving stacked produce"),
("ref-biz-pallets",   "Cbusiness-e266024e-6d1",(3,2),"grid",.5,"Palletised goods in a warehouse"),
("ref-biz-distrib",   "Cbusiness-e50fe955-cc2",(3,2),"grid",.4,"A distribution floor with a forklift working"),
("ref-biz-desk-window","Cbusiness-5a376ddf-785",(3,2),"grid",.4,"Working at a desk by the window"),
("ref-biz-openplan",  "Cbusiness-de00d39b-da7",(3,2),"grid",.5,"An open-plan office, desks empty"),
("ref-biz-crane-bw",  "Cbusiness-7eef9c8d-5df",(4,5),"grid",.3,"A tower crane, in monochrome"),

# ══ PRODUCT AND FOOD ═════════════════════════════════════════════════════
("ref-prod-table",   "Cproduct-274240fe-2be",(3,2),"grid",.5,"A table of dishes photographed from above"),
("ref-prod-plated",  "Cproduct-3c9e97fd-34d",(3,2),"grid",.5,"A plated dish, styled for a restaurant"),
("ref-prod-bowl",    "Cproduct-f9186605-22a",(4,3),"grid",.5,"A bowl of food on a yellow plate"),

# ══ AUDIO ════════════════════════════════════════════════════════════════
("ref-aud-control",  "Caudio-0c4e0f70-691",(16,9),"grid",.5,"A control room, monitors and desk"),
("ref-aud-strips",   "Caudio-7a4553ae-31e",(3,2),"grid",.5,"Mixing console channel strips"),
]
