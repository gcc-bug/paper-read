---
name: read-paper
description: Read or ingest research papers in this private reader repository, maintain evidence-grounded paper notes, and relate them to existing knowledge. Use for understanding a paper rather than editing its manuscript.
---

# Read a paper

Read [AGENTS.md](../../AGENTS.md) for authorship, intake, and Git rules. Use
[the paper template](../../templates/paper.md) for a new note, preserving any
existing personal text when updating one.

## Establish scope

Identify the local source and existing note. For inbox items, follow the intake
workflow in AGENTS.md. If the request is intake only, create an unread note and
proceed to the commit step without a substantive reading. Otherwise follow the
requested reading depth. Start with problem → mechanism → evidence → significance
→ limitations rather
than producing an exhaustive section-by-section summary.

Use local extraction or page rendering. Verify equations, figures, tables, and
ambiguous extraction against the source when they matter. If relevant material
is inaccessible, state the limit and do not infer its contents. Record what was
actually read, including partial coverage and the distinction between printed
pages and PDF page indices.

## Build understanding

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

Update `papers/<slug>/note.md` with confirmed metadata, an actual source link,
reading dates, and status (`unread`, `reading`, or `read`), keeping partial scope
explicit. Do not mark an entire paper read after an abstract-only pass. Leave
unsupported sections empty or omit them rather than inventing content.

Apply [Automatic commits](../../AGENTS.md#automatic-commits) to the completed task,
keeping the source, note, and related knowledge updates in one focused commit.
When called within a larger task, defer the commit to that task's completion.
Finish with the main insight, its limits, changed paths, reading coverage, useful
next questions, and the commit hash/subject (or the reason no commit was made).
