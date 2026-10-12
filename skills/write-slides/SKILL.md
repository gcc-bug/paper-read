---
name: write-slides
description: Discuss presentation style and write or revise concise research slides with companion explanatory Markdown notes. Use for slide-writing preferences, presentation outlines, and reducing slide text while preserving the fuller explanation.
---

# Write slides with companion notes

Read [AGENTS.md](../../AGENTS.md) for authorship, evidence, and Git rules.

## Confirmed starting preference

On 2026-10-12, the reader identified too much text and explanation in the
calibration slides and proposed moving some explanation and background knowledge
into a note about the slides. Build on that preference. Visual themes, exact
text limits, and a fixed storytelling structure have not been agreed.

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

Apply [Automatic commits](../../AGENTS.md#automatic-commits) after a completed
writing or maintenance task. When refining the skill itself, retain confirmed
preferences and label open style choices accurately. Report changed paths,
validation, and the local commit result.
