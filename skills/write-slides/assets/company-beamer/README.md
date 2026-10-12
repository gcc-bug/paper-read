# Company Beamer template — 弧光量子

2026-10-12 — Initial design proposal for presentations given as a company member.
The reader supplied the logo and requested a basic Beamer style. The visual
choices below are proposed defaults, not official brand specifications.

[Preview PDF](preview.pdf) · [Preview image](preview.png) ·
[Companion explanatory note](notes.md) · [Editable theme](beamerthemeArclight.sty)

## Basic style

- Widescreen 16:9; white background and dark text.
- Logo-derived red as a restrained accent for rules and selected annotations.
- Sans-serif typography, consistent 9 mm side margins, and 11 pt base text.
- Full logo on the cover; a 22 mm logo in a reserved content-header zone.
- Quiet footer with company name, short talk title, and slide number.
- Figures and short messages on slides; fuller explanations in `notes.md`.

The preview includes a cover, optional section divider, diagram, paired curves,
and closing page. Its curves are explicitly illustrative, not experimental data.
The speaker field is a placeholder. No existing calibration deck was restyled.

## Use the template

Copy this directory into the intended presentation folder, or reuse its theme
and `brand/` assets beside the deck source. Start from `preview.tex`, replace the
metadata and sample content, and update the companion note. The theme is loaded
with `\usetheme{Arclight}`. It is independent of the sample content and does not
set fonts itself.

For Chinese presentations the example uses `ctexbeamer`, XeLaTeX,
`TeX Gyre Heros`, and `Droid Sans Fallback`, matching the existing calibration
deck's available fonts. Replace the CJK font settings if these are unavailable
on another machine. English presentations can use ordinary `beamer` with the
same theme and their chosen fonts. The footer defaults to `Arclight`; the Chinese
example sets it to `弧光量子`. Keep the logo on a white background.

The logo path and footer company label are configurable:

```latex
\usetheme{Arclight}
\arclightsetlogo{brand/logo.pdf}
\arclightsetcompany{弧光量子}
\title[Short talk title]{Full talk title}
\author{Actual speaker}
\institute{Actual affiliation}
\date{Actual presentation date}
```

Use a `[plain]` frame for `\titlepage`. Optional transition/closing frames use
`\arclightdivider{Title}{Short supporting line}`. The content header reserves
space for the logo; long frame titles wrap within their own area. Use a concise
optional title in `\title[...]{...}` to keep the footer legible.

## Build and inspect

Run from this directory:

```bash
bash build.sh
```

Requires XeLaTeX, latexmk, the example fonts, Poppler's `pdftoppm`, Python 3,
and Pillow. Build intermediates are ignored under `build/`; the current PDF and
contact-sheet PNG are kept alongside their editable source. To compile a copied
deck without making the preview PNG, use:

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=build preview.tex
```

Inspect the actual render after changing the fonts, title lengths, or theme.
The base text size is a starting point; fix crowded content by revising its
layout or moving explanation into the companion note.

The initial five-page Chinese preview was compiled and all pages were visually
inspected. A separate English Beamer smoke build checked a long wrapped title,
subtitle, equation, block, and bullets. Both builds finished without overflow,
missing-character, or undefined-reference warnings. Logo conversion was rerun,
and the stored Illustrator source's SHA-256 matches the supplied attachment.

## Logo source and provenance

- Original filename: `弧光量子 源文件.ai`.
- Original SHA-256: `52c3144fc1ccc82c535b25b8925412687be76c25c81b890c792b84fb5700f0b4`.
- Provenance: user attachment supplied in the slide-style discussion on 2026-10-12.
- Original is retained byte-for-byte under `brand/` as an editable Illustrator
  source. It is a PDF-compatible Illustrator file with two artboards/pages.
- Page 1 is square; page 2 contains the horizontal logo used here. Both pages
  were visually inspected. The artwork includes the ARCLIGHT wordmark and the
  Chinese company name.
- `brand/logo.pdf` selects page 2 and crops the outer whitespace with a 4 pt
  margin. Artwork is kept as vector PDF; it is not redrawn or recolored.
- `ArclightRed` (`#E7211B`) and `ArclightInk` (`#231916`) are theme colors sampled
  from the PDF's rendered solid areas, not verified official color standards.

To reproduce the PDF asset, install MuPDF's `mutool`, `pdfcrop`, and its TeX/
Ghostscript dependencies, then run `bash prepare-logo.sh`. The original attachment
remains intact. Supplied brand artwork is retained for the requested company
presentation context; no additional reuse license is asserted.
