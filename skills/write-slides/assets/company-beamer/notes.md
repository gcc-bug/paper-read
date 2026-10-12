# Notes for the company Beamer preview

2026-10-12 — Codex design proposal based on the supplied company logo and the
reader's preference for concise slides with separate explanatory notes. The
preview demonstrates a possible house style; it is not an official brand manual
or an experimental report. The speaker field is an explicit placeholder.

[Preview PDF](preview.pdf) · [Editable preview](preview.tex) ·
[Theme and usage](README.md)

## Typography revision — 2026-10-12

The reader accepted the overall company style and requested a more suitable font
for less clear screens. Codex selected Noto Sans SC Medium for Chinese body text,
native Bold for headings, and Open Sans Semibold/Bold for English. The preview
now uses a 12 pt base, larger captions and footer text, and darker secondary text.
The fonts are bundled with their licenses for reproducible output. Extended
caption explanations remain in this note. These changes target legibility; they
do not establish readability on a particular physical screen.

## Slide 1 — 从信号到判断

The cover establishes the company affiliation, talk title, and speaker. The full
supplied logo has room to breathe; its proportions and colors are preserved.
The title and subtitle are separate so a long topic description does not compete
with the main title. Replace the example title, speaker placeholder, and preview
date with actual presentation metadata.

## Slide 2 — 报告目录

The agenda uses native Beamer sections. The headline uses Berlin's native
`miniframes` navigation: clickable section names and frame dots, with the current
frame filled. Overlays within a frame share one dot. Dots show frame positions,
not speaking time. Plain dividers still count toward their sections but omit
navigation and the footer. A full talk keeps appendix sections in a separate
Beamer part and delivers them in the same PDF.

## Slide 3 — 从实验到数据

A section divider gives the audience a short transition. Its question introduces
the next explanation. Use a divider where it helps orientation; it is optional
and does not need to precede every content slide.

## Slide 4 — 控制信号通过实验变成测量记录

### Codex interpretation

The diagram distinguishes a control pulse, the device's response, and the
digitized record. In a typical superconducting-qubit experiment, a microwave
drive changes the qubit state; a readout probe and measurement chain produce the
record. The diagram compresses these into a conceptual sequence and does not
specify a particular chip or wiring arrangement. IQ means in-phase and quadrature
components of a demodulated signal.

For a substantive calibration talk, extend this note using the existing
[calibration discussion](../../../../discussions/superconducting-qubit-calibration/note.md)
and its attributed supporting sources. This preview does not add a new literature
consultation or recover the 0918 acquisition setup.

### Why the slide stays short

The visible diagram supplies the objects and order needed for the spoken
explanation. The background above belongs here because the listener need not
read it while following the diagram. The small logo and fixed header/footer
provide affiliation and navigation without taking the figure's space.

## Slide 5 — 平坦曲线无法确定衰减时间

### Codex interpretation

Both curves are mathematical illustrations authored in PGFPlots, not measured
records. The left curve is $y=\exp(-t/2)$; the right is
$y=0.96-0.002t$, with dimensionless illustrative coordinates. The right-hand
curve is not fitted to a relaxation model. Neither curve estimates an actual
device lifetime.

When a decay measurement shows no resolved change over its acquisition window,
a model's returned time constant can depend strongly on bounds, noise, offset,
or other assumptions. A flat trace alone does not distinguish a genuinely long
lifetime from problems such as an ineffective delay sweep or poor measurement
sensitivity. The substantive diagnosis needs the acquisition sequence, units,
measurement uncertainty, and model. Those distinctions belong in a talk's notes
or a follow-up slide when they become the next reasoning step.

### Why the slide stays short

Aligned panels and direct annotations make the observation visible. The slide
retains the essential label that the curves are illustrative. The longer model
explanation and possible causes remain in this note. Red draws attention to a
feature; it does not serve as an automatic pass/fail or physical-error label.

## Slide 6 — 交流与讨论

The closing page provides a clean endpoint and space for questions. Add a contact
or follow-up link only when the actual details and intended audience are known.

## Navigation and figure-tools revision — 2026-10-12

The reader requested agenda/section progress and established figure tools, and
clarified that “0918” is a private label. The current six-page preview demonstrates
the agenda and shared section footer; its illustrative curves use PGFPlots.
These choices are also recorded in the slide-writing skill. Private labels stay
in provenance records, outside the displayed presentation content.

## Native dot navigation and figure environments — 2026-10-12

The reader subsequently chose Berlin-style native dots and one full PDF. The
shared theme now uses `miniframes` navigation instead of a custom progress
bar/fraction. Both the conceptual diagram and the two illustrative curve panels
use Beamer `figure` environments. Branding and the approved font profile remain
the basis of the template.
