# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

Personal study notes for Data Structures & Algorithms in Python. Each file is a transcription of a concept (static/dynamic arrays, singly/doubly linked lists, queues) plus a few LeetCode-style problems built on top of it. There is no build system, no test suite, no `requirements.txt` — files are standalone and not wired together.

Run a single file with `python3 <path>` (most files only define classes/functions and don't execute anything when run).

## Layout convention

Topics are grouped by data structure, with subfolders per variant:

- `arrays/static arrays/`, `arrays/dynamic arrays/`
- `linked-lists/singly-linked-lists/`, `linked-lists/double-linked-lists/`, `linked-lists/queues/`

Within each folder, the file named after the structure itself (e.g. `static-arrays.py`, `singly-linked-list.py`, `queues.py`) is the canonical implementation/notes file. Sibling files are problems that *use* the structure (e.g. `reverse-linked-list.py`, `implement-stack-using-queues.py`).

When adding a new topic, follow the same pattern: one implementation file named after the structure, plus one file per problem. Folder names use spaces (`static arrays`); preserve that — don't rename to kebab-case.

## Working with these files

- **The files contain transcription typos on purpose-adjacent code** (`lenght` for `length`, `dequeu` for `dequeue`, `__init` for `__init__`, missing `from collections import deque`). These are study artifacts, not bugs to hunt down. Only fix a typo if the user explicitly asks, or if it's in code you're actively modifying for them.
- Comments mix English and Indonesian (e.g. `# pointer ke node setelahnya`). Match the existing language of the file you're editing.
- Visual diagrams in comments (`head <-> A <-> B <-> tail` before/after blocks) are part of the teaching style — preserve them when editing nearby code.
- Indentation is inconsistent across files (some 2-space, some 4-space). Match the file you're in; don't normalize across files.

## Commits

Commit messages follow `learn: <topic>` (see `git log`). Use that prefix when committing new topics.
