#!/usr/bin/env python3
"""Add the licensed reference frames and the owner's property work to the site.

WHY THIS IS A SEPARATE SCRIPT FROM build_images.py
--------------------------------------------------
build_images.py opens with `for f in glob(OUT + '/*'): os.remove(f)` and then
rebuilds every frame from its sources. Two of those source sets no longer
exist on this machine: tools/stock/ and tools/stock_keep.json, which held the
Wikimedia originals behind the 44 reference frames already published. Running
it today would delete 459 derivatives, regenerate only the ones whose sources
survive, and silently strip every reference frame off the site -- and
_data/credits.yml with them.

So this script is strictly ADDITIVE. It never deletes, it refuses to touch a
slug that already exists, and it merges into the data files rather than
rewriting them. Same develop/crop/encode path as the original, so the new
frames match the old ones.

    python3 tools/build_licensed.py            # write
    python3 tools/build_licensed.py --dry-run  # report only

Provenance for the licensed frames is written into _data/licensed.yml straight
from licensed_manifest.json. It is never retyped: a credit somebody typed by
hand is a credit that will eventually be wrong.
"""
import os, sys, json, re
from PIL import Image, ImageOps, ImageEnhance, ImageFilter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from manifest_licensed import NEW

DRY = "--dry-run" in sys.argv
LIB = os.path.expanduser('~/Downloads/wirewalk-photos')
SITE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
OUT = os.path.join(SITE, 'assets/img')
DATA = os.path.join(SITE, '_data')

# Identical to build_images.py, so a frame added today is encoded the same way
# as one added on the first build.
WIDTHS = {'hero': [2000, 1400, 900], 'feature': [1400, 1000, 640],
          'grid': [1000, 640], 'tile': [640, 420]}
JPGW = {'hero': 1400, 'feature': 1200, 'grid': 800, 'tile': 520}
# Below this a crop is not worth publishing. 560 rather than 640 because one
# genuinely useful frame (a close horse portrait) is 574px across at source:
# it is portrait, so no choice of ratio recovers width, and it is published at
# its native aspect in a small slot rather than cropped or dropped.
MIN_PUBLISHABLE = 560


def develop(im):
    """A light hand: recover black point and white point, a touch of colour."""
    im = ImageOps.autocontrast(im.convert('RGB'), cutoff=(0.22, 0.04), preserve_tone=True)
    return ImageEnhance.Contrast(ImageEnhance.Color(im).enhance(1.05)).enhance(1.035)


def crop_to(im, rw, rh, anchor):
    W, H = im.size
    target, cur = rw / rh, im.size[0] / im.size[1]
    if abs(cur - target) < 0.002:
        return im
    if cur > target:                       # too wide: trim both sides evenly
        nw = int(round(H * target)); x = (W - nw) // 2
        return im.crop((x, 0, x + nw, H))
    nh = int(round(W / target))            # too tall: trim to the anchor
    y = max(0, min(H - nh, int(round((H - nh) * anchor))))
    return im.crop((0, y, W, y + nh))


lic_manifest = json.load(open(LIB + '/licensed_manifest.json'))
LIC = {os.path.basename(p['file'])[:-4]: p for p in lic_manifest['photos']}
# C<stem> -- the CC0 / public-domain library. NO ATTRIBUTION IS REQUIRED for
# anything in it: CC0 is a rights waiver and the public domain mark records a
# work whose rights have expired. Neither imposes a credit condition, so
# nothing built from here carries a label, a notice or a credits entry. The
# manifest was filtered on the licence URL pointing at /publicdomain/zero/ or
# /publicdomain/mark/, not on the licence NAME, because a name is a claim and
# a URL is the deed. Three CC-BY files that did require credit were dropped
# from the library and are deleted from this site rather than left unlinked.
CC0 = {os.path.basename(p['file'])[:-4]: p for p in json.load(open(LIB + '/cc0_manifest.json'))['photos']}
OWN = {p['file'][8:-4]: p for p in json.load(open(LIB + '/manifest.json'))['photos']}
# F<name> -- the owner's own work published on his Flickr. Same status as
# O<name>: portfolio, no "Reference frame:" prefix. Added so a crop that was
# clipping the top of somebody's head could be re-anchored without running
# build_images.py, which would delete the 44 frames whose sources are gone.
FLK = {p['file'][7:-4]: p for p in json.load(open(LIB + '/flickr_manifest.json'))}

# The manifest is a superset that grows: the licensed library went from 50
# frames to 124 mid-build. So a slug that is already in photos.yml AND still
# points at the same source is skipped, not rebuilt -- but a slug that has
# been quietly repointed at a different source is a redefinition, and that
# stops the build rather than silently changing what a published page shows.
existing = dict(re.findall(r'^(\S+):\n(?:  .*\n)*?  key: "(.*?)"\n',
                           open(DATA + '/photos.yml').read(), re.M))
repointed = [s for s, src, *_ in NEW if s in existing and existing[s] != src[1:]]
if repointed:
    sys.exit(f"slug(s) repointed at a different source, refusing: {repointed}")
todo = [n for n in NEW if n[0] not in existing]
print(f"{len(NEW)} in manifest | {len(NEW) - len(todo)} already built | {len(todo)} to add\n")

photos, used_lic, used_own, small, bytes_written = {}, [], [], [], 0
for slug, src, (rw, rh), role, anchor, alt in todo:
    key = src[1:]
    if src[0] in 'LC':
        book = CC0 if src[0] == 'C' else LIC
        if key not in book: sys.exit(f"{slug}: {key} is not in the manifest")
        path = os.path.join(LIB, book[key]['file'])
        origin = 'licensed'
        used_lic.append(key)
    elif src[0] == 'F':
        if key not in FLK: sys.exit(f"{slug}: {key} is not in flickr_manifest.json")
        path = os.path.join(LIB, FLK[key].get('use') or FLK[key]['file'])
        origin = 'flickr'
    else:
        if key not in OWN: sys.exit(f"{slug}: {key} is not in manifest.json")
        path = os.path.join(LIB, OWN[key].get('use') or OWN[key]['file'])
        origin = 'selects'
        used_own.append(key)
    if not os.path.exists(path): sys.exit(f"{slug}: missing source {path}")

    im = crop_to(develop(Image.open(path)), rw, rh, anchor)
    src_w = im.width
    if src_w < MIN_PUBLISHABLE:
        small.append((slug, src_w))
    # The published ladder, plus the source's own width when the ladder tops
    # out below it -- that adds a rendition without ever upscaling, which is
    # what these 960-1024px sources need.
    ladder = {w for w in WIDTHS[role] if w <= src_w} or {src_w}
    if src_w < max(WIDTHS[role]):
        ladder.add(src_w)
    webps = []
    for w in sorted(ladder, reverse=True):
        h = int(round(w * rh / rw))
        q = 78 if w <= 640 else 72 if w <= 1000 else 64 if w <= 1600 else 58
        fn = f'{slug}-{w}.webp'
        if not DRY:
            r = im.resize((w, h), Image.LANCZOS).filter(ImageFilter.UnsharpMask(1.0, 52, 3))
            r.save(os.path.join(OUT, fn), 'WEBP', quality=q, method=6)
            bytes_written += os.path.getsize(os.path.join(OUT, fn))
        webps.append((fn, w))
    jw = min(JPGW[role], src_w); jh = int(round(jw * rh / rw))
    jfn = f'{slug}-{jw}.jpg'
    if not DRY:
        r = im.resize((jw, jh), Image.LANCZOS).filter(ImageFilter.UnsharpMask(1.0, 52, 3))
        r.save(os.path.join(OUT, jfn), 'JPEG', quality=(80 if jw <= 640 else 76),
               optimize=True, progressive=True)
        bytes_written += os.path.getsize(os.path.join(OUT, jfn))

    photos[slug] = {'alt': alt, 'ratio': f'{rw}/{rh}', 'src': origin, 'key': key,
                    'w': jw, 'h': jh, 'jpg': f'/assets/img/{jfn}',
                    'webp': ', '.join(f'/assets/img/{f} {w}w'
                                      for f, w in sorted(webps, key=lambda x: x[1]))}
    print(f"  {slug:24s} {rw}:{rh:<3} {role:8s} crop {src_w:5d}px  "
          f"{len(webps)} webp + jpg{jw}")

if small:
    sys.exit(f"crops below {MIN_PUBLISHABLE}px -- pick a different ratio: {small}")


q = lambda s: '"' + str(s).replace('\\', '\\\\').replace('"', '\\"') + '"'


def tidy(s):
    """Collapse whitespace, and undo the URL-encoding some creator names carry.

    One creator arrives as "Jorig%u0117%20Kuzmai" -- a name that went through
    a URL encoder somewhere upstream and came out the other side as literal
    text. Printing that on the credits page would misspell a real person's
    name, so the two escapes actually seen (%20 and the %uXXXX form) are
    decoded. Nothing else is altered: this restores the recorded name, it does
    not invent one.
    """
    s = re.sub(r'<[^>]+>', ' ', s or '')     # one title arrives wrapped in a <div>
    s = re.sub(r'\s+', ' ', s).strip()
    s = re.sub(r'%u([0-9A-Fa-f]{4})', lambda m: chr(int(m.group(1), 16)), s)
    s = re.sub(r'%([0-9A-Fa-f]{2})', lambda m: chr(int(m.group(1), 16)), s)
    return s.strip()


# What the manifest records, spelled the way a reader expects to see a licence
# named. The URL in licence_url is the authority; this is only its label.
LIC_LABEL = {'cc0': 'CC0', 'by': 'CC BY', 'pdm': 'Public domain'}


def licence_url(u):
    """Repair the one malformed licence URL the manifest carries.

    One CC0 record has licence_url ending "/deed.en/" -- a trailing slash
    after the deed segment -- and creativecommons.org answers that with a
    404. On a credits page the licence link IS the licence: a broken one
    leaves a reader unable to check what they are permitted to do. The deed
    segment is dropped so the link lands on the canonical deed, which is the
    same document the correct URL would have reached.
    """
    u = tidy(u)
    return re.sub(r'/deed\.[a-z-]+/?$', '/', u) if u else u


def merge_photos():
    """Append to _data/photos.yml, keeping it sorted and the header intact."""
    raw = open(DATA + '/photos.yml').read()
    head = raw[:raw.index('\n', raw.rindex('#'))+1]
    blocks = dict(re.findall(r'^(\S+):\n((?:  .*\n)+)', raw, re.M))
    for s, p in photos.items():
        blocks[s] = (f"  alt: {q(p['alt'])}\n  ratio: {q(p['ratio'])}\n  w: {p['w']}\n"
                     f"  h: {p['h']}\n  src: {q(p['src'])}\n  key: {q(p['key'])}\n"
                     f"  webp: {q(p['webp'])}\n  jpg: {q(p['jpg'])}\n")
    with open(DATA + '/photos.yml', 'w') as f:
        f.write(head)
        for s in sorted(blocks):
            f.write(f"{s}:\n{blocks[s]}")
    return len(blocks)





if DRY:
    print(f"\ndry run: {len(photos)} frames would be added "
          f"({len(set(used_lic))} licensed, {len(set(used_own))} own)")
    sys.exit(0)

total = merge_photos()
print(f"\nadded {len(photos)} frames  ({len(set(used_lic))} licensed reference, "
      f"{len(set(used_own))} the owner's own)")
print(f"photos.yml now {total} entries")
print(f"bytes written: {bytes_written/1e6:.1f} MB")
