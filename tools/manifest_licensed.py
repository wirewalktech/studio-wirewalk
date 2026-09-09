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
("ref-fam-table-bw", "Lfamily-a352b666-464",(4,3),"grid",.45,"a father and daughter at a table together, in monochrome"),
("ref-fam-shore",    "Lfamily-9079f62f-7da",(4,5),"grid",.5,"a family walking a misted shoreline at sunset"),
("ref-fam-biscuits", "Lfamily-885254b1-6cd",(4,5),"grid",.4,"a child reaching across a table for decorated biscuits"),

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
("ref-re-yard-curve",   "Lre-yard-b48c0db7-0a8",(4,3),"grid",.5,"a curved pool set into a planted back garden"),
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
("ref-nb-hat",      "Lnewborn-1f6e6288-bb1",(3,2),"grid",.5,"a newborn asleep, wrapped, in a striped hat"),
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
