---
name: knowledge-review
description: Review reading over a period or topic in this private reader repository, identifying unresolved questions, contradictions, evolving concepts, and changes in understanding rather than summarizing every document.
---

# Review knowledge

Read [AGENTS.md](../../AGENTS.md). Establish the requested topic or time window
and state it in the review. For “this week,” use the current local calendar week
(Monday through today) and state the dates. Follow any reader-specified range.

Use reading dates, journal records, and available Git history to find relevant
material. Commit dates indicate changes, not necessarily reading. Missing dates
or history limit what can be concluded; say so rather than inferring a chronology
from file modification times. An empty repository should yield a concise report
of no reading records, not an invented review.

Include relevant topic discussions, but distinguish reference consultation by
Codex from papers selected for reader-led reading. Consultation dates and source
annotations are evidence of what supported a discussion, not evidence that the
reader read or endorsed those papers.

Read relevant notes and enough linked context to assess:

- Recurring ideas and concepts that have become important.
- Unresolved questions, new answers, and useful next reading directions.
- Contradictions and the assumptions or evidence behind them.
- Isolated notes and meaningful cross-domain connections.
- Duplicate concepts that could be merged, including distinct meanings that
  should remain separate.
- Earlier hypotheses that gained evidence, lost support, or remain untested.
- Changes in the reader's stated understanding, distinguished from changes in
  Codex's interpretation.

Use focused searches and, where appropriate, Git diffs for relevant files. Do not
substitute a summary of every document for an account of what changed or matters.
For connection assessment, consult
[connect-notes](../connect-notes/SKILL.md) when needed.

For a requested review, create or update `journal/YYYY-MM-DD-<scope>.md` with the
scope, linked findings, evidence limits, changes in understanding, and useful
follow-ups. For a narrow factual question, answer directly; do not create a
journal entry solely to record that an answer was given.

Update existing questions or hypothesis assessments when evidence warrants it,
recording the date and rationale. Preserve earlier states. Recommend conceptual
merges with reasons; when asked to perform a merge, preserve personal text,
distinct definitions, provenance, and incoming links. Do not automatically erase
notes or create a large new taxonomy during a review.

Apply [Automatic commits](../../AGENTS.md#automatic-commits) once for the completed
review, including the journal entry and any related knowledge updates. Defer
commits from nested connection workflows to this step. A direct answer that
changes no files needs no commit. End with the most consequential findings,
changed paths, and commit hash/subject (or why no commit was made). Clearly
separate reader-confirmed changes in understanding from Codex's proposed
interpretations even after they have been committed.
