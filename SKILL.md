---
name: novel-skill
description: Use when guiding a user through building a long-form novel project in 8 controlled phases from spark to prose, with a two-tier repair system and a centralized decision log, organized in Obsidian or plain Markdown.
---

# Novel Skill

> **How this skill works:** This file is the entry point. Each phase lives in `phases/<N>-<name>.md`. Cross-phase rules live in `phases/00-overview.md`. **Before any phase, read `00-overview.md` + the current phase file.** No other files are needed.

## Structure Map

```text
novel-project/
  00-project/           spark, positioning, 正文写作指南, progress
  01-worldbuilding/     world rules, factions, geography, power
  02-characters/        major character cards, minor-characters.md
  03-plot/              master-outline, foreshadowing, reveals
  04-volumes/           volume cards (stable products only)
  05-chapter-cards/     chapter cards (stable products only)
  06-chapter-drafts/    prose drafts
  07-pre/               intermediate products:
    volumes/              Volume-XX-pre-review.md
    chapters/             Chapter-XXX-pre-brief.md
  08-timeline/          chronology, event log
  09-lore-index/        rapid lookup index
  10-review/
    decisions-log.md
    micro-reports/        Chapter-XXX-repair.md
    volume-reports/       Volume-XX-repair.md
    project-repair.md
```

## 8 Phases

| # | File | Phase |
|---|------|-------|
| 0 | `phases/00-overview.md` | **Cross-phase rules** (read first, every time) |
| 1 | `phases/01-spark.md` | Phase 0 — Spark |
| 2 | `phases/02-positioning.md` | Phase 1 — Positioning |
| 3 | `phases/03-world.md` | Phase 2 — World |
| 4 | `phases/04-characters.md` | Phase 3 — Characters |
| 5 | `phases/05-master-outline.md` | Phase 4 — Master Outline |
| 6 | `phases/06-volumes.md` | Phase 5 — Volumes |
| 7 | `phases/07-chapters.md` | Phase 6 — Chapters |
| 8 | `phases/08-prose.md` | Phase 7 — Prose |

## 3 Hard Rules

1. **One phase at a time.** Never produce output for a later phase before the current phase is confirmed.
2. **Decisions are logged.** Every confirmation, conflict resolution, and skip/rollback goes into `10-review/decisions-log.md`.
3. **The prose guide is mandatory.** `00-project/正文写作指南.md` must exist before any chapter draft.

For the full 8 Core Principles, 8 Hard Style Rules, File Update Timing, Repair System, and Skip/Rollback rules — read `phases/00-overview.md`.

## How to Start

1. Detect the current stage (what files already exist).
2. Read `10-review/decisions-log.md` if it exists to recover prior decisions.
3. Ask the user to choose project mode (`Obsidian` or `folder + Markdown`).
4. Read `phases/00-overview.md` + the appropriate phase file.
5. Follow the steps in that phase file.

See `references/project-structure.md` for the full directory layout and folder responsibilities.

## Guide Step by Step

Lead the user through the project in controlled phases. When the user requests full-story generation, redirect to the staged workflow. Do not generate a complete novel in one pass.

## Handle Conflicts Explicitly

When new writing conflicts with the existing project files:
1. Name the conflict clearly.
2. Offer two or three repair options.
3. Ask whether to change the setting, outline, or current chapter direction.
4. Log the decision in `10-review/decisions-log.md`.

Escalate instead of silently rewriting continuity.
