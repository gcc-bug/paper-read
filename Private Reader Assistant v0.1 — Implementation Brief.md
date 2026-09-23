# Private Reader Assistant v0.1

## Goal

Build a simple private reading and knowledge system based on:

- Git/GitHub for sync and history
- Markdown for durable knowledge
- Codex for reading, reasoning, note organization, and connection discovery
- A few reusable Skills for stable workflows

Do not optimize yet for thousands of papers, vector databases, RAG, Zotero, graph databases, or complicated indexing.

The priority is:

1. low friction
2. easy use by Codex
3. understandable long-term notes
4. preservation of my own thinking
5. gradual discovery of connections between different sources and fields

---

# 1. Initial repository structure

Create:

```text
reader/
├── README.md
├── AGENTS.md
│
├── inbox/
│
├── papers/
│   └── <paper-name>/
│       ├── source.pdf
│       └── note.md
│
├── books/
│   └── <book-name>/
│       ├── source.pdf
│       ├── index.md
│       └── chapters/
│
├── concepts/
│
├── connections/
│
├── questions/
│
├── maps/
│
├── journal/
│
├── templates/
│   ├── paper.md
│   ├── book.md
│   ├── chapter.md
│   ├── concept.md
│   └── connection.md
│
└── skills/
    ├── read-paper/
    │   └── SKILL.md
    ├── read-book/
    │   └── SKILL.md
    ├── connect-notes/
    │   └── SKILL.md
    └── knowledge-review/
        └── SKILL.md
```

Keep the structure simple and easy to change later.

---

# 2. Core knowledge model

Use this conceptual flow:

```text
Source
  ↓
Reading note
  ↓
Reusable concept
  ↓
Connection
  ↓
Open question
```

Not every source needs to generate concepts or connections.

Avoid creating files merely because something can be extracted.

Prefer improving an existing note over creating duplicate notes.

---

# 3. Important distinction between information types

Never mix these silently:

```text
what the source says
what I understand
what I personally think
what Codex infers
```

Paper/book notes should explicitly separate them.

For example:

```markdown
## Source claims

## My understanding

## My thoughts

## Possible connections

## Open questions
```

AI-generated hypotheses must be clearly marked.

Example:

```markdown
> [!hypothesis]
> Possible connection suggested by Codex.
> This has not yet been verified.
```

Do not turn an AI hypothesis into an established fact automatically.

---

# 4. Paper workflow

Create a `read-paper` skill.

When reading a paper:

1. Identify the problem the paper is trying to solve.
2. Understand the motivation.
3. Identify its main idea or mechanism.
4. Identify assumptions.
5. Identify important results.
6. Identify limitations.
7. Distinguish experimental/theoretical evidence from author interpretation.
8. Compare it with existing repository notes.
9. Find concepts I already know.
10. Identify genuinely new ideas.
11. Identify conflicts or differences from previous work.
12. Suggest possible connections.
13. Record useful open questions.
14. Update the paper note.

Do not immediately produce a huge section-by-section summary.

Focus first on understanding:

```text
problem
→ mechanism
→ evidence
→ significance
→ limitations
```

Suggested paper template:

```markdown
---
type: paper
title:
authors:
year:
status:
tags:
---

# Why I am reading this

# Problem

# Main idea

# Mechanism

# Assumptions

# Important results

# Evidence

# Limitations

# My understanding

# My thoughts

# Connections

# Open questions

# Important locations

- page:
- section:
- figure:
```

---

# 5. Book workflow

Books should not be treated as very long papers.

Create a `read-book` skill.

Maintain:

```text
books/<book-name>/
    source.*
    index.md
    chapters/
        01.md
        02.md
        ...
```

For each chapter:

1. understand the chapter argument
2. record important ideas
3. record examples only when useful
4. track concepts recurring across chapters
5. track disagreement or uncertainty
6. update the current understanding of the whole book

The book-level `index.md` should evolve during reading.

Later chapters may change the interpretation of earlier chapters.

Therefore Codex should periodically ask:

```text
Does this chapter change our current model of what the book is arguing?
```

Only extract something into `concepts/` when it appears reusable outside that particular book.

---

# 6. Concepts

`concepts/` is the shared knowledge layer.

Concepts should not be separated rigidly by research field.

For example:

```text
concepts/
    pareto-optimization.md
    redundancy.md
    partial-observability.md
    leakage.md
```

A concept may connect:

```text
quantum computing
mathematics
computer science
psychology
economics
history
other books
```

Avoid creating duplicate concepts such as:

```text
pareto.md
pareto-2.md
weighted-pareto.md
pareto-thought.md
```

Prefer one evolving file:

```text
pareto-optimization.md
```

Suggested concept format:

```markdown
# Concept

## Current understanding

## Intuition

## Formal definition

## Why it matters

## Examples

## Related sources

## Related concepts

## Open questions

## History of changes in my understanding
```

Not every section needs to be filled.

---

# 7. Connections

Connections are first-class knowledge.

A connection should explain WHY two ideas are related rather than merely linking them.

Create `connections/` for important relationships.

Possible relation types:

```text
supports
contradicts
extends
generalizes
uses
analogy
```

Example:

```markdown
# Leakage and partial observability

## Sources

- [[paper-a]]
- [[paper-b]]
- [[partial-observability]]

## Connection

...

## Relation

generalizes

## Confidence

medium

## Why this may matter

...

## Questions

...
```

Codex may suggest tentative connections.

Do not create permanent connection notes for weak similarities unless they appear useful.

---

# 8. Questions

Treat good unanswered questions as valuable knowledge.

Maintain `questions/`.

Questions may originate from:

- a paper
- a book
- disagreement between sources
- missing explanation
- possible research direction
- cross-domain analogy

Questions should be revisited later.

If later reading answers or changes a question, update the existing note rather than deleting its history.

---

# 9. Knowledge maps

`maps/` contains high-level navigation, not detailed knowledge.

Examples:

```text
maps/
    quantum-computing.md
    optimization.md
    mathematics.md
    psychology.md
```

Maps should point toward important concepts, sources, questions, and connections.

Do not force every note into a fixed hierarchy.

The system should remain friendly to completely unrelated reading areas.

---

# 10. Inbox workflow

`inbox/` is the low-friction entry point.

I may put things such as:

```text
paper.pdf
book.epub
notes.txt
interesting-document.pdf
```

into `inbox/`.

Create a workflow that can:

1. inspect the new source
2. identify what it is
3. rename it consistently
4. move it to an appropriate location
5. create an initial note
6. search existing knowledge for relevant concepts
7. suggest connections
8. add useful questions
9. leave the final changes visible for review

Do not aggressively classify everything.

---

# 11. `connect-notes` skill

Create a skill for discovering relationships.

Given a note or concept, search for:

- same idea under different terminology
- common mechanism
- common mathematical structure
- supporting evidence
- contradictory evidence
- generalization
- specialization
- analogous mechanism in another field
- a new source that answers an old question
- assumptions shared by multiple works

Separate:

```text
strong connection
plausible connection
speculative analogy
```

Do not overproduce links.

A small number of meaningful connections is preferable to dozens of weak ones.

---

# 12. `knowledge-review` skill

Create a periodic review workflow.

When reviewing recent knowledge, do NOT merely summarize every document.

Instead identify:

- recurring ideas
- unresolved questions
- contradictions
- isolated notes
- concepts that should be merged
- concepts that have become important
- old hypotheses that gained evidence
- old hypotheses that lost support
- cross-domain connections
- changes in my understanding
- potentially valuable next reading directions

Possible commands:

```text
Review what I read this week.
```

```text
Review everything related to leakage.
```

```text
What important questions have remained unresolved?
```

```text
What connections appeared between different fields?
```

```text
How has my understanding of this topic changed?
```

---

# 13. Git workflow

Use Git primarily for:

```text
sync
history
diff
backup
evolution of thinking
```

Normal workflow:

```bash
git pull
```

Work with Codex.

Inspect:

```bash
git diff
```

Then manually approve useful changes:

```bash
git add .
git commit -m "read paper X and update related concepts"
git push
```

Do not automatically commit every Codex operation initially.

Git history may later be used to answer questions such as:

```text
How has my understanding of this concept changed over time?
```

---

# 14. Rules for Codex

Put the important stable rules in `AGENTS.md`.

Core rules:

```text
1. This repository is a long-term personal reading and knowledge system.

2. The objective is understanding, not maximizing the number of summaries.

3. Clearly distinguish source claims, my thoughts, and AI inference.

4. Mark uncertain conclusions as uncertain.

5. Do not silently overwrite my personal notes.

6. Prefer updating existing knowledge over creating duplicate files.

7. Search existing notes before creating a new concept.

8. Preserve useful contradictions rather than forcing sources to agree.

9. Look for meaningful connections across different fields.

10. Do not create large numbers of weak links.

11. Preserve important questions.

12. Use exact page/section/figure references when useful.

13. Avoid premature taxonomy and complicated infrastructure.

14. Keep Markdown human-readable without requiring special software.

15. Make changes easy to inspect using git diff.
```

---

# 15. Things explicitly NOT needed in v0.1

Do not implement yet:

```text
Zotero integration
vector database
embeddings
RAG infrastructure
graph database
complex ontology
automatic citation database
large-scale PDF management
Git LFS unless actually needed
web frontend
custom database backend
```

Do not solve problems that do not currently exist.

The system should first accumulate real usage.

Infrastructure can be improved later when actual limitations become visible.

---

# 16. First implementation milestone

For v0.1, finish only:

```text
repository structure
AGENTS.md
paper template
book template
chapter template
concept template
connection template

read-paper skill
read-book skill
connect-notes skill
knowledge-review skill

basic inbox workflow
README explaining normal usage
```

Then test the system using:

1. one research paper related to my current work
2. one research paper from an adjacent area
3. one book or chapter unrelated to my main research

Check whether the system can preserve their differences while still finding useful connections.

---

# Design principle

The system should grow like:

```text
read
 ↓
understand
 ↓
record
 ↓
connect
 ↓
question
 ↓
read again
```

The repository should become a record not only of what I have read, but also of how my understanding develops over time.