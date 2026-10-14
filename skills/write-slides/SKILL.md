---
name: write-slides
description: Discuss presentation outlines and style, develop explanatory notes for the reader, and then create or revise audience-facing slides with maintainable source. Use for report preparation, companion notes, slide writing, and presentation revisions.
---

# Write slides from explanatory notes

Read [AGENTS.md](../../AGENTS.md) for authorship, evidence, and Git rules.

Help the reader understand and organize a subject, then communicate it to an
audience. Notes are primarily for the reader's own study, preparation, and later
review. Slides serve the presentation audience. They share facts and a main
argument, but their background needs, writing style, and coverage can differ.

## Workflow: outline, notes, slides

Inspect the existing materials and confirmed decisions first. Establish the
reader's preparation needs separately from the audience's prior knowledge,
presentation purpose, available time, and live-talk or independent-reading use.
Ask only for information that matters and cannot be inferred from context.

For a new substantial report, use the reader-confirmed staged workflow:

1. **Discuss the outline in plain text.** Identify the central message, what each
   section contributes, why the sections follow that order, and what facts or
   viewpoints remain unclear. Agree on the argument before allocating frames or
   choosing layouts. Keep the outline in conversation unless saving it is useful
   or requested.
2. **Develop and discuss the notes.** After the outline is agreed, write the
   explanation and supporting background. Resolve misunderstandings and gaps,
   and discuss which information the audience needs to see. Notes should provide
   a sound basis for the talk before slide compression begins.
3. **Make the slides when the reader asks to proceed.** Select and reorganize the
   agreed material into frames, then implement, compile, and inspect the output.
   Maintain the notes alongside subsequent content changes.

Reuse approvals and decisions already given. For a local revision, use the
confirmed structure and update the affected slides and notes directly. If the
reader explicitly requests uninterrupted end-to-end delivery, follow this order
within the authorized task without adding approval stops. During a discussion,
keep suggestions distinct from confirmed preferences; discussion alone does not
authorize rewriting the deck or skill.

## Notes writing: for the reader's own understanding

Write connected explanatory prose that the reader can understand independently
of the slide deck. Include the background, definitions, derivations, worked
examples, figure walkthroughs, alternative explanations, and open questions
needed for their preparation. Explain why a claim follows, its evidence, and
its limits. Possible audience questions and their explanations can also help.

Choose depth according to the reader's needs. Background familiar to the audience
may still need explanation in the notes; knowledge familiar to the reader may
still need introduction on a slide. A topic can belong only in the notes.
Do not limit notes to material removed from slides, a slide transcript, or a
speaking script. Do not infer comprehension merely from the reader's profession.

Preserve personal text and separate source claims, the reader's confirmed views,
and Codex interpretation. Distinguish observations and diagnostics from possible
causes; retain unverified hypotheses and unresolved questions as such. Keep useful
provenance and implementation evidence here when they support understanding or
checking without contributing to the audience's message.

Reuse existing notes and concepts where useful. Otherwise keep `notes.md` beside
the deck source and link its underlying discussions and sources. Organize by the
subject and argument, with supplementary background as needed. Notes and slides
need not correspond paragraph by paragraph or frame by frame. Add title or page
references only where useful, and update them when the deck changes.

## Slides writing: for the presentation audience

Give each frame a clear role in the argument: what question or information should
the audience take from it, what supports that message, and how it connects to the
adjacent frames? Use informative titles, natural short sentences, useful figures,
and enough labels to interpret them. Define necessary technical terms before
using them; keep terminology consistent and avoid needless language switching.

Compress by selecting and reorganizing information. Preserve the reasoning links
and prerequisite background that let the audience follow the claim. Keep units,
sources, and assumptions visible when omitting them would change the meaning.
Rewording and compression must preserve scientific claims and their qualifiers.
Detailed explanation can remain in the notes. Let content and available time
determine frame splits; there is no universal word or bullet limit. Fix density
through content and layout choices before shrinking text.

Adapt the narrative to the material:

- **Personal work:** explain the problem, the reader's responsibilities, and what
  they accomplished. Verify ownership before polishing. Commit hashes and
  function names used to check contributions usually belong in the notes.
- **Cases and comparisons:** identify what each side shows, the task-specific
  difference, and the resulting conclusion or next step. A reference can
  have limitations of its own; state them when relevant. Preserve unmatched
  conditions and avoid converting an uncertain mechanism into a diagnosis.
- **Research plans:** explain what prior work established, what opportunity or
  question it supports, the reader's perspective, and the proposed stages.
  Keep mechanism detail proportional to what has been discussed. Present planned
  capabilities and benefits as research aims.

Keep private filing labels, task IDs, and bookkeeping in filenames and provenance
notes. Visible content should name the audience's subject. Maintain traceability
when removing internal labels from the presentation.

## Source structure and maintainability

Choose environments by content semantics and layout needs. Prefer standard
LaTeX/Beamer environments and established packages, starting with those already
used by the project. The following are examples, not an exhaustive format list:

| Content | Suitable structures |
| --- | --- |
| Figures, diagrams, data tables | `figure`, `table`, appropriate panel structures; `tabular` / `tabularx` inside tables |
| Equations and derivations | `equation`, `align`, or related mathematical environments |
| Algorithms, pseudocode, source code | The project's established algorithm or code-listing environments |
| Complex pages and progressive explanation | `columns`, blocks, lists, overlays, and suitable professional drawing environments |

Compose complex layouts from meaningful structures. Apply captions, numbering,
and labels according to the object's role and reference needs. Layout containers,
ordinary lists, and emphasis blocks do not acquire captions just because they
use an environment. Keep figure/table descriptions and necessary interpretation
conditions in their formal captions, local annotations near the relevant
features, and the frame's main conclusion in the body.

Centralize reusable typography, colors, spacing, and styles. Keep content readable
in source; use descriptive labels and maintainable section files where helpful.
Avoid accumulating per-frame style overrides, unexplained negative spacing, or
custom replacements for structures that established environments already supply.
Use manual positioning when the layout requires it, with a clear local purpose.

Keep generated material's source of truth clear: edit its generator, regenerate,
and verify that the output agrees. Do not independently hand-edit generated
frames. A formatting change must preserve data, preprocessing, models, and
reported values unless changing them is part of the authorized task.

For Beamer work, read [Beamer conventions](references/beamer.md) for formal
captions, drawing tools, native navigation, delivery, and company-template use.

## Review and delivery

Before typesetting, check the argument: contribution scope, factual support,
reader versus audience background needs, transitions, comparison meaning, and
the boundary between findings and proposals. Discuss material gaps before
turning uncertain content into polished slides.

After typesetting, check the source structure and the actual output. Inspect
environment choices, captions, unique useful labels, references, shared styles,
and generator consistency. Compile and resolve content-related overflow, missing
characters, and undefined references. Render and visually inspect the affected
pages, including title length, graph labels, reading order, and navigation.
Try representative layouts before extending a substantial layout change.
For a substantial revision, inspect the whole deck for flow and consistency.
A successful build alone does not establish readability.

Review the notes and slides together for consistent facts, claims, and links,
while retaining their different explanatory depth and coverage. Deliver editable
source, the requested presentation output, and the companion notes. Report the
changes, checks, and remaining content questions. Apply the repository's
[automatic commit workflow](../../AGENTS.md#automatic-commits) to completed file
changes; an ongoing discussion alone does not require a new artifact or commit.
