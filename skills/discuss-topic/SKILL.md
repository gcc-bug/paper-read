---
name: discuss-topic
description: Discuss a topic, dataset, or question using supporting literature and preserve the discussion with its references. Use when understanding the topic is the task rather than reading a selected paper or book.
---

# Discuss a topic

Read [AGENTS.md](../../AGENTS.md) for authorship, source handling, and Git rules.

Establish the question and inspect relevant existing discussions, concepts,
questions, and sources before creating notes. Explain the mechanism and evidence
in conversation, following the reader's questions. A supporting paper supplies
evidence for this discussion; it is not automatically a paper-reading task.

When the reader asks to save notes or a checkpoint, use
`discussions/<topic>/note.md`. Reuse an existing discussion when the topic
continues across sessions; record actual dates without inventing a transcript
or declaring an unfinished discussion complete. Keep reader statements, source
claims, and Codex interpretation distinct. Link reusable concepts and persistent
questions rather than duplicating them in every discussion.

Keep newly acquired supporting files in the discussion's `references/`, using
descriptive source filenames and preserving original bytes. Link an existing
local source instead of copying it. Annotate the relevant sources in the note
or an optional `references.md` when those annotations would obscure the main
discussion. Record title, known authors/year/version, original filename,
provenance, consultation dates, passages used, and extraction limits. Keep
source-specific caveats and incompatible definitions attributed to their source.
Do not assign standalone paper-reading status to these references.

If the reader later selects a supporting paper for its own reading, follow
[read-paper](../read-paper/SKILL.md), reuse the source, and update affected links
if it moves. Preserve the discussion's historical coverage and annotations.

Apply [Automatic commits](../../AGENTS.md#automatic-commits) once for a completed
discussion-note task or requested checkpoint. Report changed paths, consultation
coverage and remaining questions, and the commit result. Ongoing conversation
alone does not require creating notes or a commit.
