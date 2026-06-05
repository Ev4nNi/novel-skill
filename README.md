# Novel Skill

A structured, 8-phase workflow for building and maintaining long-form novel projects in Obsidian or plain Markdown. The skill walks a user from raw idea to chapter drafts through a two-tier repair system, with every non-content decision recorded in a central decision log.

## 8 Phases

```text
Phase 0  Spark            -> 00-project/spark.md
Phase 1  Positioning      -> 00-project/positioning.md
Phase 2  World            -> 01-worldbuilding/
Phase 3  Characters       -> 02-characters/
Phase 4  Master Outline   -> 03-plot/master-outline.md
Phase 5  Volumes          -> 04-volumes/  (per-volume Pre-Volume Review required)
Phase 6  Chapters         -> 05-chapter-cards/  (per-chapter Pre-Chapter Brief required)
Phase 7  Prose            -> 06-chapter-drafts/  (Micro-Repair required after each chapter)
```

Plus:

- Volume Repair after every volume
- Project Repair after all volumes (optional)

## Two-Tier Repair

| Level | Trigger | Output |
| --- | --- | --- |
| Micro-Repair | After every chapter draft | `09-review/micro-reports/Chapter-XXX-repair.md` |
| Volume Repair | After every volume completes | `09-review/volume-reports/Volume-XX-repair.md` |
| Project Repair | After all volumes (optional) | `09-review/project-repair.md` |

## Decision Log

`09-review/decisions-log.md` is the append-only record of every phase confirmation, conflict resolution, skip, rollback, and repair completion.

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
- `09-review/decisions-log.md` must be updated on every confirmed decision