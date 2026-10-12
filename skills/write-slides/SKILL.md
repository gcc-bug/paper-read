---
name: write-slides
description: Discuss presentation style and write or revise concise research slides with companion explanatory Markdown notes. Use for slide-writing preferences, presentation outlines, and reducing slide text while preserving the fuller explanation.
---

# Write slides with companion notes

Read [AGENTS.md](../../AGENTS.md) for authorship, evidence, and Git rules.

## Confirmed starting preference

On 2026-10-12, the reader identified too much text and explanation in the
calibration slides and proposed moving some explanation and background knowledge
into a note about the slides. The reader also requested a basic Beamer style for
presenting as a company member and supplied the 弧光量子 logo. Build on these
preferences. The reader accepted the overall company style, then requested a
font change for less clear screens. Exact text limits and a fixed storytelling
structure have not been agreed.

## Discuss or write at the requested scope

Inspect the existing deck and related notes before diagnosing its style. Use
specific slides to discuss what feels excessive and show how a proposed change
would work. During a style discussion, distinguish the reader's confirmed
preferences from Codex suggestions; continue the discussion without treating
every suggestion as an agreed rule or permission to rewrite the deck.

For a writing task, establish the audience, purpose, and whether the deck is
primarily presented live or read independently, using available context. Choose
the explanation's depth accordingly. A request to reduce slide text authorizes
relocating useful explanations into the companion note, preserving their meaning
and evidence. It does not authorize changing scientific conclusions.

## Divide content between the slides and the note

Slides carry what the audience needs to see at that moment: the key point or
question, the relevant figure or example, and enough labels to interpret it.
Prefer short statements and annotations placed beside the features they explain.
Move extended background, definitions, derivations, detailed figure walkthroughs,
alternative explanations, and follow-up reasoning into the note when they are
useful but do not need to occupy the slide.

Keep assumptions and qualifications visible when omitting them would change the
meaning of a displayed claim. Retain legible units, comparison labels, and source
attribution. The note can hold full references, provenance, and methodological
details. Reduce text by selecting and relocating content, rather than shrinking
fonts or turning explanations into unexplained fragments. Let the content decide
whether a slide needs splitting; do not impose a universal word or bullet limit.

## Make the companion note useful for understanding

Reuse an existing slide-specific note when suitable; otherwise place `notes.md`
beside the deck's source. Link the deck and its underlying discussion or reading
notes using relative Markdown links. Organize explanations by slide title or
section, adding slide numbers when useful and updating them if the deck changes.

The note is a place for fuller explanation and background knowledge, not merely
a transcript of what to say. Explain the reasoning behind a slide, how to read
its figures, and any useful background omitted from it. Reuse existing knowledge
through links where appropriate. Include unresolved questions and distinguish
observations, source claims, and Codex interpretation. Preserve personal text;
do not attribute assistant explanations to the reader.

## Review the pair together

Check that each slide's message is easy to locate and that its essential meaning
survives without the relocated paragraphs. Check that the note explains omitted
reasoning coherently, matches the figures and claims, and remains navigable from
the deck. For substantial changes, try representative slides and their notes
before extending the approach across the presentation. Render and inspect changed
slides in the actual output format; a successful build alone does not establish
readability.

## Company Beamer presentations

When presenting as a member of 弧光量子, start from the reusable
[company Beamer template](assets/company-beamer/README.md), its editable theme,
and the supplied logo. Use this branding in the company context; other contexts
should use their own affiliation and style. Keep the writing principles shared
across themes. Read the template instructions when creating or changing a deck.

The accepted layout uses a white canvas, dark text, restrained red accents,
consistent margins, a small company logo on content slides, and larger branding
on the cover. These are proposed defaults, not an official company brand manual.
For less clear screens, start with the template's bundled medium/semibold
sans-serif body fonts and native bold headings. Prefer open, substantial strokes,
larger readable text, and dark secondary labels. Keep captions legible; move
their extended explanation into the companion note. Check the rendered deck at
reduced resolution as well as full size, and adjust if the actual screen or room
provides better evidence. A simulated preview is not a screen measurement.

Preserve the supplied logo's proportions and artwork. Supply the actual speaker,
affiliation, talk title, and date; leave unknown values as clearly marked
placeholders. Keep detailed explanations in the companion Markdown note.

Changing a theme does not automatically redesign a deck's content. For an
existing presentation, address its text density separately and inspect the
rendered output after changing shared typography or layout.

Apply [Automatic commits](../../AGENTS.md#automatic-commits) after a completed
writing or maintenance task. When refining the skill itself, retain confirmed
preferences and label open style choices accurately. Report changed paths,
validation, and the local commit result.
