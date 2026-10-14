# Beamer conventions

Read this reference when implementing or revising Beamer source. The main
[skill](../SKILL.md) governs the outline, reader-facing notes, and audience-facing
writing. These conventions preserve this reader's agreed presentation choices.

## Formal figures, tables, and captions

Place plots and diagrams in Beamer's nonfloating `figure` environment, including
drawings made directly in LaTeX and figures inside columns. Use `table` for
semantic data tables, with `tabular`, `tabularx`, or a suitable table package
inside it. Use native `\caption{...}` for descriptions, relevant sources, units,
and interpretation conditions; place a useful `\label{...}` after its caption.
Keep captions concise and readable, with extended explanations in the notes.

For a single comparison with multiple panels, use one enclosing figure and a
shared caption. Independent figures in columns can each have their own caption.
Keep measured curves and illustrative models distinguishable. Local panel
annotations should help identify features; the frame takeaway belongs in the body.

Do not use a detached `\src`, manually styled paragraph, or slide footer to
imitate a figure/table caption. A source-only line for a nonfigure claim can
remain separate. Inspect the caption with its owning object, including column
width and reading order. Numbering and labels for equations, algorithms, and
listings follow their own environments and reference needs; generic layout
containers do not require captions.

## Drawing and complex formats

Use `graphicx` for imported graphics, Circuitikz for electrical symbols, TikZ
for conceptual diagrams, and PGFPlots or an existing scientific plotting script
for curves. Prefer library symbols when available and faithful existing plots
when suitable. The drawing environment supplies the contents of the figure.
Preserve data and preprocessing while changing its layout or annotation.

Choose the project's established math, algorithm, listing, and panel packages
for more complex content. Add a suitable established package when it materially
helps the requested format and remains compatible with the build. Keep related
panels, annotations, and captions together. Use Beamer's structural environments
and overlays when they serve the explanation. Avoid duplicate labels and
inconsistent numbered references across overlays.

## Agenda, navigation, and output

For substantial Beamer talks, provide an agenda near the beginning and use native
Berlin-style `miniframes` section names and circular frame markers. Let sections,
subsections, and navigation data determine the displayed structure. Dots represent
frames, with overlays sharing one dot; they do not estimate speaking time.

Separate backup material with Beamer's appendix part so it does not inflate the
main talk's navigation. Keep navigation optional for a short preview. Check the
first and last frames of sections, dot visibility, and clickable links in the
rendered PDF; compile until navigation data settles.

Deliver one full PDF containing the main talk and any appendix by default,
alongside source and notes. Add a main-only PDF when requested. Keep build commands,
filenames, links, and useful note page references aligned with the actual output.

## Company presentation profile

When presenting as a member of 弧光量子, read and reuse the
[company template](../assets/company-beamer/README.md), its theme, logo, and fonts.
For other affiliations, use the appropriate profile. These are reader-approved
defaults, not an official company brand manual.

The company profile uses a white canvas, dark text, restrained red accents,
consistent margins, a small content-slide logo, and larger cover branding.
Its bundled Noto Sans SC Medium/Bold and Open Sans Semibold/Bold provide substantial
strokes for less clear screens. Keep secondary labels dark and legible. Inspect
full-size and reduced-resolution renders; simulated screen conditions are not
measurements of the actual presentation room.

Preserve the logo's proportions and artwork. Use the actual speaker, affiliation,
title, and date, with clear placeholders for unknown fields. Keep theme and fonts
shared rather than forking them per deck. Theme changes still require separate
content-density and layout checks. Read the template documentation for build
paths, font licenses, and asset provenance.

## Confirmed preferences and origin

- **2026-10-12:** The reader requested concise slides with fuller explanatory
  notes, company branding, and clearer fonts. They subsequently chose an agenda,
  native Berlin-style dot navigation, professional drawing tools, consistent
  figure environments, and one PDF including the appendix. Private filing labels
  should remain in filenames and provenance notes.
- **2026-10-13:** Figure descriptions and comments belong in formal captions,
  with conclusions in the slide body.
- **2026-10-14:** The reader confirmed outline discussion, then complete notes,
  then slide production; distinct writing rules for personal notes and audience
  slides; and maintainable source using semantic standard environments beyond
  figures and tables. Notes may explain background the audience already knows
  and include material absent from the slides. Fixed word limits or a universal
  storytelling template have not been agreed.
