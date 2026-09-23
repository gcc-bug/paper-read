---
name: read-book
description: Read or ingest a book or chapter in this private reader repository, maintaining chapter notes and an evolving book argument. Use for sequential or selective book reading across any subject.
---

# Read a book

Read [AGENTS.md](../../AGENTS.md) for authorship, intake, and Git rules. Use the
[book](../../templates/book.md) and [chapter](../../templates/chapter.md)
templates when creating notes.

## Establish scope

Locate the source, edition, existing index, and chapter notes. Follow the inbox
intake workflow for new material. An intake-only request creates an unread index;
it does not require chapter summaries. Preserve the original PDF/EPUB bytes.

Read the chapter or range requested. If asked to begin a whole book without a
specified range, inspect its contents and begin with its opening substantive
chapter, stating the scope. Do not summarize unread chapters from their titles.
Use the EPUB package spine for chapter order rather than ZIP member order. Cite
chapter/heading and internal location when no stable page numbers exist. For
PDFs distinguish printed pages and PDF indices, and check meaningful visual
material when extraction is insufficient.

## Read and revise

- Record the chapter's argument, important ideas, assumptions, evidence, and
  limitations. Include examples only when they help explain a mechanism or idea.
- Track recurring concepts, disagreements, and uncertainties across the chapters
  actually read. Separate source claims, reader statements, and Codex analysis.
- Maintain `books/<slug>/chapters/01.md`, `02.md`, etc., using the book's actual
  numbering. Use descriptive names for unnumbered material where useful. Link
  each note back to `index.md` and add its link to the index.
- Update the index's provisional model of the book's argument. Later chapters
  can revise earlier interpretations; record dated revisions and their evidence
  instead of erasing the earlier model or rewriting the reader's opinions.
- Periodically ask the reader: “Does this chapter change our current model of
  what the book is arguing?” Show the relevant change in Codex's provisional
  interpretation, and leave any proposed reader understanding unconfirmed until
  the reader responds. This reflective question need not block authorized work.
- Search existing notes before extracting a concept. Extract only ideas useful
  outside this particular book. Preserve the book's disciplinary context when
  suggesting cross-domain relationships.
- Keep questions and useful candidate connections in the chapter or index; link
  existing question/concept notes when appropriate. Label speculative analogies.

Record reading dates and coverage in the index and changed chapter notes. Keep
the book status `reading` while substantial unread material remains. A source
containing only one chapter must be described as an excerpt.

Apply [Automatic commits](../../AGENTS.md#automatic-commits) to the completed task,
keeping the source, chapter notes, and index changes together. Commit the requested
reading scope once, rather than making an intermediate commit for every chapter.
This also applies to intake-only work; when called within a larger task, let that
task make the final commit. Finish with the chapter insight, how the provisional
book model changed, changed paths, the next useful reading step, and the commit
hash/subject (or the reason no commit was made).
