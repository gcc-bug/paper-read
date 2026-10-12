# Company Beamer template — 弧光量子

2026-10-12 — Initial design proposal for presentations given as a company member.
The reader supplied the logo and requested a basic Beamer style, then accepted
the layout and requested improved fonts for less clear screens. The defaults
below incorporate that typography revision; they are not official brand
specifications.

[Preview PDF](preview.pdf) · [Preview image](preview.png) ·
[Companion explanatory note](notes.md) · [Editable theme](beamerthemeArclight.sty)

## Basic style

- Widescreen 16:9; white background and dark text.
- Logo-derived red as a restrained accent for rules and selected annotations.
- Noto Sans SC Medium/Bold for Chinese and Open Sans Semibold/Bold for English;
  consistent 9 mm side margins and 12 pt base text.
- Native bold headings, 10 pt figure labels/captions, an 8 pt footer, and darker
  secondary text for better legibility on less clear screens.
- Full logo on the cover; a 22 mm logo in a reserved content-header zone.
- Quiet footer with company name, short talk title, and slide number.
- Figures and short messages on slides; fuller explanations in `notes.md`.

The preview includes a cover, optional section divider, diagram, paired curves,
and closing page. Its curves are explicitly illustrative, not experimental data.
The speaker field is a placeholder. No existing calibration deck was restyled.

## Use the template

Copy this directory into the intended presentation folder, or reuse its theme
and `brand/`, `fonts/`, and `arclight-fonts.tex` beside the deck source. Start from
`preview.tex`, replace the metadata and sample content, and update the companion
note. The theme is loaded with `\usetheme{Arclight}`. It is independent of the sample content and does not
set fonts itself.

For Chinese presentations use `ctexbeamer` with XeLaTeX and
`\input{arclight-fonts.tex}` before loading the theme. The bundled font files are
loaded directly; no system font installation is needed. When reusing the assets
from another compile directory, define `\arclightfontpath` before loading
`arclight-fonts.tex`, with a relative path ending in `/` to this template's
`fonts/` directory. Its default remains `fonts/`. Add the theme directory to
LaTeX's input search path and set the logo path separately; see the
[0918 deck source](../../../../discussions/superconducting-qubit-calibration/slides/slides.tex)
for a repository-relative example. The original preview
used Droid Sans Fallback with simulated bold; the revised profile uses separate
Medium and Bold Chinese font files. English presentations can use ordinary
`beamer` with the same font profile, which conditionally skips the CJK settings.
The footer defaults to `Arclight`; the Chinese example sets it to `弧光量子`.
Keep the logo on a white background.

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

Requires XeLaTeX, latexmk, Poppler's `pdftoppm`, Python 3,
and Pillow. Build intermediates are ignored under `build/`; the current PDF and
contact-sheet PNG are kept alongside their editable source. To compile a copied
deck without making the preview PNG, use:

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=build preview.tex
```

Inspect the actual render after changing the fonts, title lengths, or theme.
The base text size is a starting point; fix crowded content by revising its
layout or moving explanation into the companion note.

The display profile uses medium/semibold body fonts instead of thin strokes.
Keep useful labels dark and large enough to read. Inspect reduced-resolution
renders as well as full-size slides; simulations help identify weak details but
do not replace checking the actual room and screen.

## Bundled font provenance

The static font files are unmodified and loaded by `arclight-fonts.tex`:

- Noto Sans SC v2.004 Medium and Bold: downloaded on 2026-10-12 from the
  [Noto CJK project's Simplified Chinese subset fonts](https://github.com/notofonts/noto-cjk/tree/main/Sans/SubsetOTF/SC).
  Copyright 2014–2021 Adobe. Distributed under the
  [SIL Open Font License 1.1](fonts/LICENSE-noto.txt).
- Open Sans v1.10 Semibold, Bold, Semibold Italic, and Bold Italic: copied from
  the local `fonts-open-sans` package. Digitized data copyright 2010–2011 Google
  Corporation. Distributed under the [Apache License 2.0](fonts/LICENSE-open-sans.txt).

The CJK files' SHA-256 values identify the downloaded artifacts:

| File | SHA-256 |
| --- | --- |
| `NotoSansSC-Medium.otf` | `7633f5a016d4dd95e685a69633d818aabc4644c4b08e26bd35b1b30c45ed5dda` |
| `NotoSansSC-Bold.otf` | `c6cb5a93abaa9edc8ee7463b7ebb7f42d618d40e6ed2f7a5371c97b0b64767c0` |

Keep the accompanying licenses with copied template fonts. The supplied company
logo has separate provenance below.

The revised five-page Chinese preview was compiled and all pages were visually
inspected. A separate English Beamer build checked a long wrapped title,
subtitle, equation, block, bullets, and native italic text. Both builds finished
without overflow, missing-character, or undefined-reference warnings. PDF font
inspection confirms that the used fonts are embedded. Before/after renders were
also inspected at 854×480 with contrast reduced to 65% and a slight 0.45-pixel
Gaussian blur; this is a simulation, not a physical screen test. The original
logo conversion and byte-integrity checks remain unchanged.

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
