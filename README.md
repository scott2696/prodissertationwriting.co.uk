# prodissertationwriting.co.uk — PoundPlay

Independent UK guide to online casinos and betting sites, built as a static site
and served from this repo's root by GitHub Pages.

## Building

```sh
python3 _build/gen_images.py    # favicons, OG card, org logo
python3 _build/gen_reviews.py   # writes the reviews hub + 11 review fragments
python3 _build/build.py         # writes every page, sitemap.xml and robots.txt
```

`build.py` is the whole site generator. It reads `_build/pages/*.html` fragments —
JSON front matter in a `<!--@ ... @-->` block, then authored body markup — and
writes clean-URL pages at `{url}index.html`. No `.html` extensions anywhere:
every page is a directory containing an `index.html`.

Stylesheet is `assets/css/home.css` (the one `build.py` links). There is no
second stylesheet.

## Two numbers are computed, never typed

* **The operator score**, from the five published weights in `WEIGHTS`.
* **The bonus clearance cost**, from each operator's own first-deposit terms.

Both appear in prose, tables and schema. Because the build derives them, they
cannot drift out of sync with the methodology page. There is no field anywhere
in this system where a score can simply be written by hand.

## Build-time assertions

The build fails rather than shipping a silent structural break:

* FAQ items in markup must equal FAQ items in `FAQPage` schema
* `<div>` tags must balance
* exactly one `<h1>` per page
* no unresolved `{{token}}`
* no internal link carrying a `.html` extension
* the sitemap must list exactly the indexable pages that were written
* `lastmod`, `changefreq` and `priority` must be valid
* every meta description must be 158 characters or fewer, because that value
  feeds the meta tag, the Open Graph and Twitter cards and the schema
  `description` at once — over the limit and the last clause is lost everywhere

## Authoring a page

Add a fragment to `_build/pages/`. Front matter takes `url`, `title`,
`description`, `h1`, `author`, `crumbs`, and optionally `itemlist` (renders the
offer table), `lbHeading`, `lbIntro`, `lbNotes`, `reviewOf`, `extraSchema`,
`pageType`, `allAuthors`, `dataset`, and `rg: false` to suppress the
responsible-gambling panel.

Body markup uses an authoring vocabulary that `transform()` maps onto the
template's classes — `<div class="answer">`, `<div class="callout tip|warn|note|law">`,
`<div class="table-scroll"><table class="data">`, `<div class="toc">`,
`<div class="faq"><details>`, `<div class="pros-cons">`, `<ol class="howto">`,
`<div class="grid grid-3">` of `.link-card`s, `<div class="cta-band">`.

Note: a `.link-card` **must** contain an `<h3>` or it will not be converted.

Tokens: `{{aff:slug}}`, `{{affs:slug}}`, `{{op:slug:Field}}`, `{{score:slug}}`,
`{{clear:slug:bonus|turnover|cost|net}}`, `{{monthyear}}`, `{{updated}}`,
`{{nextreview}}`.

Generated blocks: `<!--gen:weights-table-->`, `<!--gen:clearance-table a,b,c-->`,
`<!--gen:compare-table a,b,c-->`, `<!--gen:compare-table-sports a,b,c-->`,
`<!--gen:ledger-table-->`, `<!--gen:scorecard slug-->`.

## Deliberate deviation from the brief

**Canonicals are self-referencing, not homepage-pointing.** Pointing every
canonical at `/` would tell Google the other 38 pages are duplicates and drop
them from the index — the opposite of the ranking goal in the same brief. This
was raised and confirmed before the build. Set `CANONICAL_TO_HOME = True` in
`_build/build.py` for the literal behaviour; nothing else needs to change.

## Data that must be replaced before launch

`_build/operators.json` carries the tested figures for all eleven operators —
`ledgerN`, `ledgerMedian`, `ledgerWorst`, `kycStage`, `kycDocs`, `kycHours`,
`payoutFast`, `payoutCard`, `scores` — plus the wagering terms behind the
clearance model (`wagering`, `d1Match`, `d1Max`, `wagerBase`, `wagerX`) and the
overround figures quoted on the betting pages.

**Every one of those is placeholder data this build was authored against and
must be replaced with real logged measurements and real published terms before
the site goes live.** The entire editorial position of the site is that these
numbers were measured rather than asserted, so shipping them unverified would
undo the thing that makes the site worth reading.

Confirmed against the supplied operator sheet: names, casino/sports/crypto
flags, commission rates and both affiliate links per operator — with one
deliberate departure. The sheet marks **EvoSpin** `sports: TRUE` with a betting
affiliate link, but EvoSpin is treated as casino-only here, so it carries
`sports: false` and a null `sportsLink` and appears on no betting page. A build
assertion enforces that: listing a `sports: false` operator in a sports page's
`itemlist`, or in a `compare-table-sports` block, fails the build. Welcome offers
are as supplied for **EvoSpin**, **Spin Pin** and **Spin Kings**; the other
eight were authored against placeholder offers and must be confirmed at each
cashier.

Prose depends on these figures in ways a find-and-replace will not catch: the
site-wide totals (74 payouts, eleven operators, 34 crypto and 17 card requests),
and the "two positive, seven negative" summary on the bonuses page. Change the
data and re-read those.

`images/authors/*.jpg` are supplied photographs of the two named reviewers,
committed to the repo and not generated by any build step. Each is cropped
square on the face and written at two sizes — `<slug>.jpg` at 128px for the
byline avatar and `<slug>@2x.jpg` at 256px for the author cards, which render
at 38px and 124px respectively. To change a reviewer, edit `AUTHORS` in
`_build/build.py` and drop replacement images in at the same paths and sizes.

**The biographies remain placeholder copy** and should be checked against what
these two people actually did before launch: the site asserts specific
backgrounds (card acquiring and chargeback operations; financial services
compliance) and a Manchester base, and those claims are load-bearing for the
E-E-A-T argument the whole site rests on.

## Layout notes

This site uses the **house template** shared with the other sites in this group:
`.site-header` / `.hero` (with the tick `.scale`) / `.afl-list` offer table /
`.datatable` / `.callout` / `.snippet` / `.toc` / `.faq` / `.rg` /
`.site-footer`, set in Archivo, Inter and IBM Plex Mono over the petrol-and-brass
palette. `assets/css/home.css` is that template's stylesheet plus one appended
block of rules for the components this build adds on top of it — the offer
table's proof line and labelled sponsored row, the author cards, the numbered
how-to lists, and the computed scorecard.

**The offer table leads the content column.** `render()` takes it as a separate
argument and emits it at the top of `.content`, directly under the hero.

**The hero carries the whole introduction**, in template order: identity strip,
wordmark, H1, lede, gauges, CTAs, badges, small print, byline.

**The mobile fold is handled by hiding and compacting, not reordering**, and
it is measured rather than assumed. The requirement is that the first phone
viewport carries the H1, the byline with the update date, the offer table's H2
and the first offer row *including its button*.

Two blocks at the bottom of `home.css` do this:

* `@media (max-width:760px)` hides the wordmark, tagline, identity strip,
  gauges, hero CTAs, badges, the hero small print and the table's intro
  paragraph; clamps the lede to two lines; reduces the H1 size so the longest
  title on the site wraps to three lines rather than four; and compacts the
  first offer card.
* `@media (max-width:760px) and (max-height:660px)` handles short viewports
  (375x553 and 360x640), additionally hiding the lede, dropping the score bar
  and clamping the proof line to one line.

Verified across all 16 pages that carry an offer table at 360x640, 375x553 and
390x664 — 48 combinations, all passing, with at least 20px of clearance below
the first offer button. To re-run that check, serve the site and measure the
pages in same-origin iframes sized to those viewports; the numbers that matter
are the bottom edge of `h1`, `.meta-line`, `#leaderboard` and
`.afl-row .cta-btn` against the viewport height.

Three things to know before editing those blocks. `.content > h2#leaderboard + p`
in the base template carries an ID, so a plain `.lb-intro` selector loses to it.
`.meta-line` must stay `flex-wrap:nowrap` or the text drops below the avatar and
costs 24px. And `.afl-bonus` renders its "WELCOME OFFER" label as a block-level
`::before`, so a `-webkit-line-clamp` there must allow three line boxes, not
two, or the label eats one and a half-cut line bleeds under the ellipsis.

**The `.upd` verification strip** (last updated, author, fact-checker, next
review) is inserted after the first `.snippet`, or at the top of the content on
pages that have no short answer. It is never anchored to the first H2 — on
`/authors/` that H2 sits inside a card.

**Review pages carry their CTA in the hero**, since a review has no offer table.

## Internal strategy documents

`research/` holds the competitor analysis, keyword strategy and SERP plan. Both
`_build/` and `research/` are excluded from the published site in `_config.yml`.
