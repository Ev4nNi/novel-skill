# Phase 7 — Prose

**Goal:** Draft the chapter prose from the chapter card, with continuity enforcement.

**Input:** `05-chapter-cards/Chapter-XXX.md`, previous chapter's draft, previous chapter's micro-repair report
**Output:** `06-chapter-drafts/Chapter-XXX.md`, `10-review/micro-reports/Chapter-XXX-repair.md`

**Prerequisite:** Current chapter card confirmed.

## Mandatory pre-draft reading

1. The current chapter card.
2. The previous chapter's draft (or volume opening notes for chapter 001).
3. The previous chapter's micro-repair report at `10-review/micro-reports/Chapter-XXX-repair.md` (or volume opening notes for chapter 001). The repair report is the **latest world state** — character positions, active foreshadowing, and open conflicts. Without it, prose will reuse the stale character / world files as if no chapter had happened.
4. Every involved character file.
5. Every relevant worldbuilding file.
6. `03-plot/foreshadowing.md`.
7. `00-project/正文写作指南.md` — this file is mandatory; if it does not exist, create it using `references/prose-writing-guide-template.md` and confirm with the user before continuing.

## Draft

1. Write the chapter prose and save to `06-chapter-drafts/Chapter-XXX.md`.
2. The **first line** MUST be the chapter title in format: `第N章"title"` (Chinese numerals, any quote type accepted: Chinese double/single, English double/single). Examples: `第一章"雨夜来客"`, `第十二章'迷宫'`, `第三章'重逢'`.
3. Pause for user feedback after the draft.

## Micro-Repair (mandatory after every chapter draft)

1. Run the **Punctuation Sweep** first (see `references/punctuation-sweep.md`). Use `scripts/check_dash.py` to inspect, then `scripts/fix_dash.py` to repair. Log the sweep stats in the micro-repair report.
2. Fill `references/micro-repair-template.md` and save to `10-review/micro-reports/Chapter-XXX-repair.md`.
3. Update the impacted files (character, worldbuilding, foreshadowing, timeline, lore-index).
4. Update `00-project/progress.md`.
5. Log the repair in the decision log.

## Punctuation Sweep

The skill ships with two helper scripts in `scripts/`:

- `scripts/check_dash.py` — quick sweep. Reports every punctuation issue with a fix suggestion + per-chapter density table. Read-only.
- `scripts/fix_dash.py` — applies the agreed fixes in place. Idempotent.

All scripts operate on `06-chapter-drafts/` (relative to the current working directory) by default. Pass a different folder as the first CLI argument to override.

### Workflow per chapter

```bash
# 1. Quick sweep
python scripts/check_dash.py

# 2. Review the report with the user
#    - title must be valid, word count in range
#    - density warnings: edit chapter or log prose-style-exception

# 3. Apply fixes
python scripts/fix_dash.py

# 4. Re-inspect to confirm clean
python scripts/check_dash.py

# 5. Record stats in micro-repair report
```

The Sweep is mandatory before Micro-Repair on every chapter.

**Read before starting:** `phases/00-overview.md`, `references/prose-writing-guide-template.md`, `references/punctuation-sweep.md`
