# Novel Skill

A structured, 8-phase workflow for building and maintaining long-form novel projects in Obsidian or plain Markdown. The skill walks a user from raw idea to chapter drafts through a two-tier repair system, with every non-content decision recorded in a central decision log.

## 8 Phases

| # | Phase File | Phase |
|---|---|---|
| 0 | `phases/00-overview.md` | **Cross-phase rules** (read first, every time) |
| 1 | `phases/01-spark.md` | Phase 0 — Spark → `00-project/spark.md` |
| 2 | `phases/02-positioning.md` | Phase 1 — Positioning → `00-project/positioning.md` |
| 3 | `phases/03-world.md` | Phase 2 — World → `01-worldbuilding/` |
| 4 | `phases/04-characters.md` | Phase 3 — Characters → `02-characters/` |
| 5 | `phases/05-master-outline.md` | Phase 4 — Master Outline → `03-plot/` |
| 6 | `phases/06-volumes.md` | Phase 5 — Volumes → `04-volumes/` + `07-pre/volumes/` |
| 7 | `phases/07-chapters.md` | Phase 6 — Chapters → `05-chapter-cards/` + `07-pre/chapters/` |
| 8 | `phases/08-prose.md` | Phase 7 — Prose → `06-chapter-drafts/` |

Plus:

- Volume Repair after every volume → `10-review/volume-reports/`
- Project Repair after all volumes (optional) → `10-review/project-repair.md`

## Two-Tier Repair

| Level | Trigger | Output |
| --- | --- | --- |
| Micro-Repair | After every chapter draft | `10-review/micro-reports/Chapter-XXX-repair.md` |
| Volume Repair | After every volume completes | `10-review/volume-reports/Volume-XX-repair.md` |
| Project Repair | After all volumes (optional) | `10-review/project-repair.md` |

## Decision Log

`10-review/decisions-log.md` is the append-only record of every phase confirmation, conflict resolution, skip, rollback, and repair completion.

## Skip and Rollback

- Skip forward: allowed only if the target phase's prerequisites exist on disk. Log the reason.
- Rollback: allowed any time. Run a regression pass on content produced after the rollback target.

Both actions update `00-project/progress.md`.

## Project Mode

Choose between `Obsidian` and `folder + Markdown` before scaffolding. Both modes use the same directory layout; Obsidian mode adds frontmatter and `[[double links]]`.

See `references/project-structure.md` for the full directory layout and folder responsibilities.

## Templates

All templates live in `references/`:

- `spark-template.md`, `positioning-template.md` (Phase 0-1)
- `worldbuilding-template.md`, `character-template.md` (Phase 2-3)
- `master-outline-template.md`, `foreshadowing-template.md`, `reveals-template.md`, `timeline-template.md` (Phase 4+)
- `pre-volume-review-template.md`, `volume-template.md`, `volume-repair-template.md` (Phase 5)
- `pre-chapter-brief-template.md`, `chapter-template.md` (Phase 6)
- `prose-writing-guide-template.md`, `micro-repair-template.md` (Phase 7)
- `decisions-log-template.md`, `progress-template.md` (cross-phase)

## Mandatory Files

- `00-project/正文写作指南.md` must exist before any chapter draft is written
- `00-project/progress.md` must be updated on every phase transition
- `10-review/decisions-log.md` must be updated on every confirmed decision

## Scripts

Three helper scripts live in `scripts/`:

- `scripts/check_dash.py` — quick punctuation sweep (read-only)
- `scripts/fix_dash.py` — apply agreed fixes (read-write, idempotent)
- `scripts/check_density.py` — detailed density audit (read-only)

All operate on `06-chapter-drafts/` by default. Pass a different folder as the first CLI argument.
