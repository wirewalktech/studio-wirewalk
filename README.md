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

Pages: `/`, `/business/`, `/photography/`, `/video/`, `/audio/`, `/work/`,
`/process/`, `/credits/`, `/thanks/`, `404.html`.

## Images

Nothing is hotlinked. Every frame is committed as a derivative.

* **The owner's own photography** — developed and cropped from his masters.
  This is the portfolio and is credited as such.
* **Reference frames** — CC0 or public domain, retrieved from Wikimedia
  Commons with the licence read from the Commons API at fetch time. Used only
  to illustrate services the public portfolio does not cover (business,
  product, real estate, event, wedding, equipment). Every section that uses
  them says so, their alt text begins "Reference frame:", and all of them are
  listed on `/credits/`. **Never present these as the studio's work.**

No commercial stock and no machine-generated imagery is used anywhere.

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
