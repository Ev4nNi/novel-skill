# Phase 6 — Chapters

**Goal:** Turn each volume card into a sequence of chapter cards.

**Input:** `04-volumes/Volume-XX.md`, previous chapter card, previous chapter's micro-repair report
**Output:** `07-pre/chapters/Chapter-XXX-pre-brief.md`, `05-chapter-cards/Chapter-XXX.md`

**Prerequisite:** Current volume card confirmed.

## Pre-Chapter Brief (mandatory for every chapter, including chapter 001)

1. Read the current volume card.
2. Read the previous chapter card (or volume opening notes for chapter 001).
3. Read the previous chapter's micro-repair report at `10-review/micro-reports/Chapter-XXX-repair.md` (or volume opening notes for chapter 001). The repair report is the **latest world state** — it is the source of truth for character positions, active foreshadowing, and open conflicts. The character / worldbuilding files are the baseline, but the repair report is the delta applied on top. Skipping it is the most common source of continuity bugs.
4. Read the involved character / worldbuilding files.
5. Fill `references/pre-chapter-brief-template.md` and save it as `07-pre/chapters/Chapter-XXX-pre-brief.md`.

## Chapter card

1. Use `references/chapter-template.md` and save to `05-chapter-cards/Chapter-XXX.md`.
2. The card's `Pre-Chapter Brief` field must reference the brief file.
3. Confirm with the user.

**Note:** `07-pre/chapters/` contains the pre-briefs (intermediate product). `05-chapter-cards/` contains the chapter cards (stable product). They are separate to avoid loading all pre-briefs when reading chapter cards.

**Read before starting:** `phases/00-overview.md`
