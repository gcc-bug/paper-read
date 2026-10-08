---
name: read-paper
description: Read papers selected by the reader or ingest them for later reading, maintaining evidence-grounded reading notes. Topic discussions using supporting papers belong to discuss-topic; manuscript editing is outside this workflow.
---

# Read a paper

Read [AGENTS.md](../../AGENTS.md) for authorship, intake, and Git rules. Use
[the paper template](../../templates/paper.md) for a new note, preserving any
existing personal text when updating one.

## Establish scope

First establish whether the paper itself is the reading target. Looking up a
paper to answer a calibration, dataset, or topic question does not make it a
standalone reading. For that task use
[discuss-topic](../discuss-topic/SKILL.md), storing its supporting references
with the discussion. If a paper already has a reading note, link it rather than
duplicating its source. Further papers consulted during a paper reading remain
supporting references: keep them in that paper's `references/` with attributed
annotations in its note, unless they already have a local source to link.

Identify the local source and existing note. For inbox items, follow the intake
workflow in AGENTS.md. If the request is intake only, create an unread note and
proceed to the commit step without a substantive reading. Otherwise follow the
requested reading depth. Treat an invitation to "read together" as an ongoing
discussion, not a request to finish and file a note in one turn.

Use local extraction or page rendering. Verify equations, figures, tables, and
ambiguous extraction against the source when they matter. If relevant material
is inaccessible, state the limit and do not infer its contents. Record what was
actually read, including partial coverage and the distinction between printed
pages and PDF page indices.

## Explain and discuss

After reading the source, explain the paper in the conversation before writing
substantive notes. Give the reader a coherent first pass through the broader
background, the concrete problem, the proposed method, and the main results.
Include the motivation and gap in prior work when they clarify the contribution.
Explain unfamiliar terms and the causal steps in the method rather than listing
section headings or only reporting numbers. Point to key figures, sections, or
pages so the reader can check the explanation. Distinguish measured results from
the authors' interpretation and from Codex's assessment.

Before sending the first substantive reply to a "read together" request, check
that it explains the specific bottleneck, why it matters, and how the method
turns its inputs into the claimed result. An abstract-style summary, performance
numbers, or a closing question cannot substitute for this explanation. Begin
the discussion in that reply by examining a consequential assumption,
comparison, or limitation grounded in the source, and invite the reader's view.

As the discussion develops, answer confusions from the source, revisit relevant
figures or derivations, and discuss limitations, possible improvements, or
future directions. Do not infer agreement or claim the reader understands a
point merely because it has been explained. Keep track of useful unresolved
questions and changes in understanding across turns.

When the reader says the discussion is finished or asks for notes, consolidate
the discussion into the paper note. A preliminary note or source already in the
repository may remain in place during discussion; do not silently present it as
the final record of the reader's understanding. Intake-only work remains an
exception: it creates the minimal unread note required by AGENTS.md.

## Build the final note

- Identify the problem, motivation, main idea, mechanism, assumptions, results,
  and limitations, with source locations for important claims.
- Separate theorem statements and their conditions, experimental observations
  and baselines, and the authors' interpretation. Do not inflate a reported
  result into a broader guarantee.
- Put your explanation of significance and additional critique in **Codex
  interpretation**. Keep **My understanding**, **My thoughts**, and the reading
  motivation for the reader's own words or confirmed paraphrases.
- Search existing papers, books, and concepts for familiar mechanisms and
  terminology. Distinguish ideas already recorded from ideas new to this
  repository; do not infer what the reader knows from the repository alone.
- Preserve conflicts and explain different assumptions or evidence. Mark
  unverified connections as Codex hypotheses, with a possible verification step.
- Keep useful questions in the note, or update an existing standalone question
  if it is worth revisiting across sources. Create reusable concepts sparingly.

At the end of the discussion, update `papers/<slug>/note.md` with confirmed
metadata, an actual source link, reading dates, and status (`unread`, `reading`,
or `read`), keeping partial scope explicit. Synthesize the explanation and the
reader's confirmed understanding, questions, and any changes of mind; preserve
the distinction between their words, source claims, and Codex interpretation.
Do not mark an entire paper read after an abstract-only pass. Leave unsupported
sections empty or omit them rather than inventing content.

Apply [Automatic commits](../../AGENTS.md#automatic-commits) when the reading
discussion is complete, keeping its source, note, and related knowledge updates
in one focused commit. When called within a larger task, defer the commit to
that task's completion. The first-pass conversation should end with an opening
for discussion, not a note or commit report. At the end of the reading task,
report the main insight, its limits, changed paths, reading coverage, useful
next questions, and the commit hash/subject (or the reason no commit was made).
