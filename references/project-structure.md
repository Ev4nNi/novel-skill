# Project Structure

Before creating any project files, ask the user to choose one mode:

- `Obsidian` — uses `[[double links]]`, dataview-friendly frontmatter, MOC files
- `folder + Markdown` — plain Markdown with the same folder structure

Both modes use the same directory layout. Obsidian mode adds frontmatter and double links on top.

## Directory Layout

```text
novel-project/
  00-project/
    spark.md                  # Phase 0
    positioning.md            # Phase 1
    正文写作指南.md             # Phase 7 (mandatory before any draft)
    progress.md               # Updated on every phase transition / skip / rollback
  01-worldbuilding/           # Phase 2
  02-characters/              # Phase 3
  03-plot/
    master-outline.md         # Phase 4
    foreshadowing.md          # Phase 4+
    reveals.md                # Phase 4+
  04-volumes/
    Volume-01-pre-review.md   # Phase 5 (mandatory per volume)
    Volume-01.md              # Phase 5
    Volume-02-pre-review.md
    Volume-02.md
    ...
  05-chapter-cards/
    Chapter-001-pre-brief.md  # Phase 6 (mandatory per chapter)
    Chapter-001.md            # Phase 6
    Chapter-002-pre-brief.md
    Chapter-002.md
    ...
  06-chapter-drafts/
    Chapter-001.md            # Phase 7
    Chapter-002.md
    ...
  07-timeline/               # Phase 4+
  08-lore-index/              # Phase 4+ (rapid lookup index)
  09-review/
    decisions-log.md          # central decision log (append-only)
    micro-reports/
      Chapter-001-repair.md   # Phase 7 (mandatory per chapter)
      Chapter-002-repair.md
      ...
    volume-reports/
      Volume-01-repair.md     # Phase 5 (mandatory per volume)
      Volume-02-repair.md
      ...
    project-repair.md         # after all volumes (optional)
```

## 8-Phase Stage Rule

Do not build every folder in one pass and then start writing the whole story. Move one phase at a time:

1. **Phase 0 Spark** — capture the raw idea, save to `00-project/spark.md`
2. **Phase 1 Positioning** — confirm genre, audience, promise, save to `00-project/positioning.md`
3. **Phase 2 World** — write rules, factions, geography, power system in `01-worldbuilding/`
4. **Phase 3 Characters** — major character cards in `02-characters/`
5. **Phase 4 Master Outline** — `03-plot/master-outline.md`, `foreshadowing.md`, `reveals.md`
6. **Phase 5 Volumes** — per volume: Pre-Volume Review, Volume card, Volume Repair
7. **Phase 6 Chapters** — per chapter: Pre-Chapter Brief, Chapter card
8. **Phase 7 Prose** — per chapter: Draft, Micro-Repair

Advance only after the user confirms the current phase and the confirmation is logged in `09-review/decisions-log.md`.

A previous phase can be revisited only via a logged rollback (see SKILL.md > Skip & Rollback Rules).

## Folder Responsibilities

- `00-project/spark.md`: the raw idea in the user's own words; non-negotiable project seed
- `00-project/positioning.md`: genre, audience, premise, emotional promise, hook, length range, hard limits
- `00-project/正文写作指南.md`: stable prose drafting rules, tone guardrails, continuity reminders, chapter-writing checks (mandatory before Phase 7)
- `00-project/progress.md`: current phase, last completed phase, current volume, current chapter, recent decisions (mirror of decisions log)
- `01-worldbuilding/`: rules, factions, geography, power system — split by topic into multiple files
- `02-characters/`: major character cards; `minor-characters.md` holds one-line entries for minor cast
- `03-plot/master-outline.md`: story promise, main spine, escalation, resolution
- `03-plot/foreshadowing.md`: setup / expected payoff / actual payoff table
- `03-plot/reveals.md`: revealed truths and the chapter that revealed them
- `04-volumes/`: per volume — Pre-Volume Review and Volume card
- `05-chapter-cards/`: per chapter — Pre-Chapter Brief and Chapter card
- `06-chapter-drafts/`: per chapter — final prose draft
- `07-timeline/`: chronology and event log
- `08-lore-index/`: rapid index of locations, terms, items, characters for consistency checks
- `09-review/decisions-log.md`: append-only log of phase confirmations, conflicts, repairs, skips, rollbacks
- `09-review/micro-reports/`: per-chapter repair report
- `09-review/volume-reports/`: per-volume repair report
- `09-review/project-repair.md`: whole-project repair after the final volume

## Update Rules

- Update the matching files immediately after any new prose changes project facts.
- After every chapter draft, run a Micro-Repair and update all impacted files.
- After every volume, run a Volume Repair and update master-outline, foreshadowing, reveals, timeline, lore-index.
- After every prose-guide change, log it in the decision log.
- In Obsidian mode, prefer `[[double links]]` for people, places, organizations, items, and events.
- Every change to a project fact must be reflected in `08-lore-index/` so the index does not drift.

## Two-Tier Repair Triggers

| Level | Trigger | File to create | Files to update |
| --- | --- | --- | --- |
| Micro-Repair | After every chapter draft | `09-review/micro-reports/Chapter-XXX-repair.md` | character / worldbuilding / foreshadowing / timeline / lore-index / progress |
| Volume Repair | After every volume completes | `09-review/volume-reports/Volume-XX-repair.md` | master-outline / foreshadowing / reveals / timeline / lore-index / 正文写作指南 (if rhythm changes) |
| Project Repair | After all volumes complete (optional) | `09-review/project-repair.md` | every file |

Skipping a Micro-Repair blocks the next chapter. Skipping a Volume Repair blocks the next volume's Pre-Volume Review.

## Confirmation Record

Track which phases are confirmed before moving on (each row also appears in `09-review/decisions-log.md`):

- Project mode confirmed:
- Phase 0 Spark confirmed:
- Phase 1 Positioning confirmed:
- Phase 2 World framework confirmed:
- Phase 3 Character framework confirmed:
- Phase 4 Master outline confirmed:
- Volume XX Pre-Review signed off:
- Volume XX card confirmed:
- Volume XX Repair completed:
- Chapter XXX Pre-Brief signed off:
- Chapter XXX card confirmed:
- Chapter XXX Micro-Repair completed: