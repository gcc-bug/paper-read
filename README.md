# Private reader assistant

A personal reading repository built from source files, Markdown, Git, and Codex.
It keeps source claims, your understanding, your thoughts, and Codex's interpretations
distinct, while letting concepts and useful connections develop over time.

PDFs and EPUBs are stored in Git with the notes. This directory is the repository
root; there is no additional `reader/` directory to enter.

## Start reading

1. Put a PDF, EPUB, or text note in [inbox/](inbox/).
2. Open Codex in this repository and make a request such as:

   ```text
   Read the paper in inbox/example.pdf. Start with its problem, mechanism,
   evidence, and limitations, and compare it with what I already have here.
   ```

   ```text
   Organize inbox/example.epub as a book, then read only chapter 1.
   Keep the book index provisional as we work through it.
   ```

   ```text
   Organize the sources in inbox and create initial notes without reading them yet.
   ```

3. Tell Codex your own reactions as you read. For example: “Add this to My thoughts:
   I think this assumption fails when observations are delayed.” Codex leaves
   personal sections blank until you supply or confirm their content.
4. Codex checks the completed work and makes a focused local commit, then reports
   its hash and summary. Inspect that commit and push when you want to sync.
   Say “leave changes uncommitted” whenever you prefer to review before committing.

The [repository rules](AGENTS.md) route these requests to the four workflows in
[skills/](skills/). They work through those local instructions without installing
anything globally. You can also explicitly ask Codex to follow a particular
`skills/<name>/SKILL.md` file.

## Where things live

| Path | Purpose |
| --- | --- |
| `inbox/` | New sources and unprocessed personal notes |
| `papers/<slug>/source.pdf` and `note.md` | A paper's original file and reading note |
| `books/<slug>/source.pdf` or `source.epub` | A book's original file |
| `books/<slug>/index.md` and `chapters/01.md` | Evolving book argument and chapter notes |
| `concepts/` | Reusable ideas shared across reading areas |
| `connections/` | Important relationships, with explanations and evidence |
| `questions/` | Questions worth revisiting, including their history |
| `maps/` | Lightweight navigation across notes |
| `journal/` | Dated knowledge reviews |
| `templates/` | Starting points for paper, book, chapter, concept, and connection notes |
| `skills/` | Reading, connection discovery, and review workflows |

Source extensions are preserved. Folder names use descriptive lowercase words
separated by hyphens; full titles and the original filename stay in the notes.
Links use normal relative Markdown paths, so no special note-taking app is required.
Empty folders have `.gitkeep` files so Git preserves the initial structure.

## Continue and connect

Useful requests include:

- “Continue with chapter 2. Does it change our interpretation of the book?”
- “Find meaningful connections between this note and existing concepts.”
- “Review what I read this week.”
- “Review everything related to leakage.”
- “Which important questions remain unresolved?”
- “How has my understanding of this topic changed?”

Concepts are created only when useful beyond one source. Connections explain
why ideas are related and distinguish strong evidence, plausible relationships,
and speculative analogies. A Codex hypothesis remains labeled until evidence
supports changing its assessment. Reviews use reading records and available Git
history; they explicitly state when those records are incomplete.

## Review and sync

Once a private GitHub remote and upstream branch are configured, start a session
with `git pull --ff-only` when the working tree is ready to update. Completed
reading, intake, connection, review, and maintenance tasks automatically produce
one local commit when they change files. Codex checks the changes, includes the
relevant PDF/EPUB sources, and uses a message describing the actual work.

Related source, note, concept, and question changes stay together. Workflows used
inside another task share that task's final commit. Unfinished work remains
uncommitted, and a task that changes nothing creates no commit. This supersedes
the manual-commit default in the original implementation brief.

After a completed task, inspect the reported commit (replace `HEAD` with its hash
to inspect an earlier task):

```bash
git status --short
git log -5 --oneline
git show --stat HEAD
git show HEAD
```

Automatic commits include only the current task. If unrelated edits are already
staged, or earlier edits cannot be safely separated from the task, Codex leaves
them intact and explains why it did not commit. Git failures are reported rather
than bypassed. You can inspect pending work with `git diff` and
`git diff --cached`; open untracked files separately to see their contents.

For manual review, ask Codex to leave changes uncommitted. When ready, stage the
specific files you reviewed with `git add -- <paths>`, inspect
`git diff --cached`, and use `git commit` to record them.

To sync committed work:

```bash
git push
```

PDFs and EPUBs appear as binary changes; open them to inspect their contents.
The scaffold does not configure a GitHub remote; connect one separately.
For the first sync, create an empty **private** GitHub repository, add its URL with
`git remote add origin <private-repository-url>`, commit any pending changes, and run
`git push -u origin HEAD`. Subsequent pushes use `git push`.

Local commits do not automatically push or change repository visibility. Saving
a Codex hypothesis in Git does not mark it as verified or reader-approved.
There is no LFS, database, frontend, or indexing service in v0.1. If an actual
source file encounters GitHub's size limits, resolve that specific case before
changing the storage approach.

Private Git hosting controls repository access. Reading with Codex still uses
your configured Codex service; this is not an offline inference system. Source
extraction uses local tools, without a separate document-upload service.

## Reading tools

No application build or dependency installation is required. Codex can use local
PDF text extraction and page rendering (`pdftotext` and `pdftoppm` are available
in this workspace). EPUBs can be inspected as ZIP archives, following the package
spine for reading order and using chapter/heading references. Scanned PDFs may
need visual reading or OCR; inaccessible content must be marked as unread.

## First real-use check

The scaffold is ready for the three reading trials in the implementation brief.
They have not been performed because no reading sources have been supplied yet.

1. Read one paper related to your current work.
2. Read one paper from an adjacent area.
3. Read one unrelated book or chapter, then review all three together.

Check that source bytes are preserved, claims have traceable locations, your
thoughts remain distinct, and book notes track only the chapters actually read.
Check that existing concepts are reused, hypotheses are labeled, and questions
retain their history. Accept a finding of “no useful connection” when appropriate.
Inspect the resulting commit's Markdown and binary changes before syncing.
