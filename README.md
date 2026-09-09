# studio.wirewalk.com

Marketing site for Wirewalk Studio — photography, video and audio production.
Jekyll on GitHub Pages, served at the root of the custom domain.

## The one rule that breaks everything

`_config.yml` **must** keep `baseurl: ""`.

A `CNAME` file is present, so GitHub serves the site at the root of
`studio.wirewalk.com` and **not** under `/studio-wirewalk/`. A non-empty
`baseurl` makes every Liquid-generated link render as `/studio-wirewalk/...`
and 404 on the live domain — while the pages still look fine locally and in
the repo preview, because the CSS is inline. This has already broken two
other Wirewalk sites. Do not set it.

Verify after any deploy:

    python3 ~/Downloads/site/tools/check-sites.py studio

## Layout

    _config.yml            site metadata; baseurl must stay ""
    _data/photos.yml       generated: one entry per frame (srcset, size, alt, provenance)
    _data/credits.yml      generated: CC0 / public-domain reference frames and their licences
    _data/own.yml          generated: the owner's own photographs
    _includes/style.html   the entire stylesheet, inlined
    _includes/photo.html   renders a <picture> from a photos.yml slug
    _layouts/base.html     shell, plus ~40 lines of vanilla JS (menu + scroll reveal)
    assets/img/            committed derivatives — WebP with JPEG fallback, several widths
    tools/                 the image pipeline (excluded from the build)

Pages: `/`, `/family/`, `/business/`, `/photography/`, `/video/`, `/audio/`,
`/work/`, `/process/`, `/credits/`, `/thanks/`, `404.html`.

## What the site is about

It is a booking site, not a portfolio. The home page leads with the services
people actually commission -- family and children, portraits, pets, events,
business, product, property, video, audio -- each as its own section with a
heading, a fact block (what it covers, how long, what you get, how it is
priced) and a booking link. Landscape, city and aerial work sits near the
bottom under "Personal work" and is labelled as personal work, because nobody
commissions a dune. Keep that order if you edit this.

## Images

Nothing is hotlinked. Every frame is committed as a derivative.

* **The owner's own photography** — developed and cropped from his masters.
  This is the portfolio and is credited as such. Where a manifest entry
  carries a `use` path it points at a hand-graded retouched master; the
  pipeline uses that file and skips its own develop pass, so the two sets of
  contrast moves cannot stack. That retouching is colour, contrast and tone
  only — never the person: no smoothing, no reshaping. Say it that way if you
  ever write about it.
* **Reference frames** — CC0 or public domain, retrieved from Wikimedia
  Commons with the licence read from the Commons API at fetch time. Used only
  to illustrate services the public portfolio does not cover (business,
  product, real estate, event, wedding, equipment). Every section that uses
  them says so, their alt text begins "Reference frame:", and all of them are
  listed on `/credits/`. **Never present these as the studio's work.**

No commercial stock and no machine-generated imagery is used anywhere.

**Newborn:** `/family/#newborn` offers newborn sessions but shows three empty,
labelled image slots, because the studio has no newborn frames. Do not fill
them with stock photographs of infants — on a photographer's site every image
reads as "I took this", and that would invite a parent to book on the strength
of work that does not exist. Fill them with real sessions, with permission.

**People:** the street portraits are identifiable members of the public
photographed in public places, with no model releases. They appear as
portfolio work only, are never presented as endorsements, and must not be
licensed on for commercial or advertising use. The site states this on
`/photography/#people`, `/work/` and `/process/#rights`.

### Rebuilding the derivatives

    cd tools && python3 build_images.py

Reads `manifest.py` (slug, source, aspect ratio, role, crop anchor, alt text),
develops and crops each frame, writes WebP + JPEG at several widths into
`assets/img/`, and regenerates the three `_data` files. It never upscales: a
1024px source simply gets fewer `srcset` entries. Requires Pillow and the
source libraries referenced at the top of `manifest.py`.

## Contact form

Plain HTML POST to FormSubmit, delivering to sales@wirewalk.com, with a
honeypot and a `_next` redirect to `/thanks/`. There is deliberately **no**
JavaScript success handler: a handler that prints "thanks" without a confirmed
send silently discarded every enquiry on the main site for months. The visitor
reaches `/thanks/` only because the POST actually happened.
