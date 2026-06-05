---
name: novel-skill
description: Use when guiding a user through building a long-form novel project in 8 controlled phases from spark to prose, with a two-tier repair system and a centralized decision log, organized in Obsidian or plain Markdown.
---

# Novel Skill

## Overview

Use this skill to guide a user through building and maintaining a long-form novel project in 8 controlled phases instead of generating a full story in one go.

Confirm the project structure with the user before each major stage. Do not treat "write me a whole novel" as a request to generate the entire finished story at once.

## Core Principles

1. **8 phases, not freeform.** Every project passes through `spark -> positioning -> world -> characters -> master-outline -> volume -> chapter -> prose`.
2. **One phase at a time.** Never produce output for a later phase before the current phase is confirmed.
3. **Pre-checks before generation.** Before generating a volume card or a chapter card, re-read the relevant setting files and write a recap (Pre-Volume Review / Pre-Chapter Brief).
4. **Two-tier repair.** Run a Micro-Repair after every chapter, and a Volume Repair after every volume.
5. **Decisions are logged.** Every stage confirmation, conflict resolution, and skip/rollback is recorded in `09-review/decisions-log.md` with a timestamp.
6. **Continuity is enforced.** A change to setting/character/plot requires the matching file update before drafting the next chapter.
7. **Skip and rollback are explicit.** If the user wants to jump or fall back, log the reason and impact in the decision log.
8. **The prose guide is mandatory.** `00-project/正文写作指南.md` must exist before any chapter draft is written.

## Hard Style Rules (read before every draft)

These are non-negotiable. They are not "guidelines" or "preferences" — they are the writing style of the project, and they shape how every chapter is drafted.

1. **The prose is 人工书写 (manually written), not Markdown.** No bullet lists, no bold/italic for emphasis, no headers, no inline code spans, no `>` blockquotes, no horizontal rules. The chapter draft is meant to read like prose a human typed on a page, not like a structured document. If a list is structurally necessary, fold it into natural sentence flow ("三件事：他欠了钱、他撒了谎、他跑了。") — do not render it as a Markdown list.
2. **Markdown structure belongs in the chapter card and the repair report, never in the chapter draft itself.** The chapter draft is `06-chapter-drafts/Chapter-XXX.md`, but its **content** is a wall of prose, not a structured document. Use blank lines only for paragraph breaks. Do not use `**bold**`, `*italic*`, `# headers`, `- bullets`, `1. numbered lists`, `> quotes`, or backticks for code.
3. **破折号（em-dash `—` and all variants）is 严禁过多使用.** Each chapter should have a small, deliberate number of dashes — never more than 1 dash per ~500 words of prose, and ideally much less. The default action for a middle dash in any context is **delete**, not replace. A dash is a hammer; use it when nothing else will do.
4. **省略号 is 严禁过多使用.** Each chapter should have a small, deliberate number of ellipses — never more than 1 ellipsis per ~500 words, and ideally much less. The only valid form is the Chinese 6-dot `……` (not `...` and not `。。`). The default action for an extra ellipsis is **delete**, not replace.
5. **引号 is 严禁过多使用.** Dialogue uses 引号 normally, but **nested quotes**, **scare-quotes for emphasis**, and **quoting common words for stylistic effect** are all prohibited. If a phrase does not need a quote to be readable, remove the quote.
6. **Density is enforced by the Punctuation Sweep.** `check_dash.py` and `fix_dash.py` measure the count of dashes / ellipses / quotes per chapter and warn when the density is too high. The micro-repair report must record the density and the user's sign-off. If a chapter is over budget, the user must either edit the chapter or explicitly log a `prose-style-exception` row in `09-review/decisions-log.md`.
7. **These rules are part of the prose guide.** When the prose guide is created or updated, these rules MUST be copied into it. Changing the limits (e.g. raising the per-chapter budget) is a `prose-guide-update` event logged in the decision log.

> Reminder: "Default" punctuation actions in the Punctuation Sweep prefer **delete** over **replace** for dashes and ellipses. The goal is fewer showy marks, not just different showy marks.

## Stage Map

```text
Phase 0  Spark            -> 00-project/spark.md
Phase 1  Positioning      -> 00-project/positioning.md
Phase 2  World            -> 01-worldbuilding/
Phase 3  Characters       -> 02-characters/
Phase 4  Master Outline   -> 03-plot/master-outline.md
Phase 5  Volumes          -> 04-volumes/  (per-volume Pre-Volume Review required)
Phase 6  Chapters         -> 05-chapter-cards/  (per-chapter Pre-Chapter Brief required)
Phase 7  Prose            -> 06-chapter-drafts/  (Micro-Repair required after each chapter)
+
Repair   Volume Repair    -> 09-review/volume-reports/  (per volume)
Repair   Project Repair   -> 09-review/project-repair.md  (after all volumes)
```

## Detect the Current Stage

Classify the request before acting:

- only an idea / spark
- partial setting
- existing character files
- existing outline
- existing volume cards
- active chapter cards
- active chapter drafting
- prose generation
- continuity repair or revision
- completed project (review only)

If files already exist, read the relevant ones before proposing new material. If `09-review/decisions-log.md` exists, read it first to recover prior decisions.

## Choose the Project Mode

Do not assume the storage mode. Ask the user to choose between:

- `Obsidian` — uses `[[double links]]`, dataview-friendly frontmatter, MOC files
- `folder + Markdown` — plain Markdown with the same folder structure

Both modes use the same directory layout. Obsidian mode adds frontmatter and double links on top.

Read `references/project-structure.md` before scaffolding a new novel project or reorganizing an existing one.

## Phase 0 — Spark

Goal: capture the raw story idea before it is shaped.

Steps:

1. Ask the user to describe the idea in freeform, no framework yet.
2. Fill `references/spark-template.md` and save to `00-project/spark.md`.
3. Confirm with the user before advancing.

Required output file: `00-project/spark.md`.

## Phase 1 — Positioning

Goal: turn the spark into a project with a clear audience, promise, and unique hook.

Steps:

1. Read `00-project/spark.md`.
2. Walk through `references/positioning-template.md` and confirm every section with the user: genre, target readership, premise, emotional promise, unique hook, length range, hard limits.
3. Save to `00-project/positioning.md`.
4. Log the confirmation in `09-review/decisions-log.md`.

Required output file: `00-project/positioning.md`.

## Phase 2 — World

Goal: define the rules of the world tightly enough that later phases can rely on them.

Steps:

1. Read `00-project/spark.md` and `00-project/positioning.md`.
2. Walk through `references/worldbuilding-template.md` section by section.
3. Save core files in `01-worldbuilding/` (split by topic, e.g. `rules.md`, `factions.md`, `geography.md`, `power-system.md`).
4. Confirm "Hard limits" explicitly: things the world will never allow.
5. Log decisions in the decision log.

Required output folder: `01-worldbuilding/`.

## Phase 3 — Characters

Goal: build the character roster and lock the major arcs.

Steps:

1. Read `00-project/positioning.md` and `01-worldbuilding/`.
2. Identify major characters (POV characters, primary antagonists, recurring allies/rivals).
3. For each major character, fill `references/character-template.md` and save under `02-characters/<name>.md`.
4. Confirm relationship map.
5. Minor characters: capture one-line entries in `02-characters/minor-characters.md`; promote to full cards only when they take a meaningful role.
6. Log decisions in the decision log.

Required output folder: `02-characters/`.

## Phase 4 — Master Outline

Goal: define the story's main spine, escalation, and resolution before any volume work.

Steps:

1. Read everything in `00-project/`, `01-worldbuilding/`, `02-characters/`.
2. Walk through `references/master-outline-template.md`: story promise, main spine, escalation curve, resolution.
3. Save to `03-plot/master-outline.md`.
4. Create the foreshadowing and reveals trackers using `references/foreshadowing-template.md` and `references/reveals-template.md` (save under `03-plot/`).
5. Confirm with the user that the spine is stable. Spine changes after Phase 5 require a logged rollback.

Required output files: `03-plot/master-outline.md`, `03-plot/foreshadowing.md`, `03-plot/reveals.md`.

## Phase 5 — Volumes

Goal: split the story into volumes, each volume a self-contained escalation step.

Pre-Volume Review (mandatory for every volume, including volume 01):

1. Read every relevant file from earlier phases.
2. Fill `references/pre-volume-review-template.md` and save it as `04-volumes/Volume-XX-pre-review.md`.
3. List conflicts and present 2-3 repair options for each.
4. Get user sign-off before drafting the volume card.

Volume card:

1. Use `references/volume-template.md` and save to `04-volumes/Volume-XX.md`.
2. Reference the Pre-Volume Review file from the volume card.
3. Confirm with the user.

Volume Repair (mandatory after the volume is fully drafted):

1. Fill `references/volume-repair-template.md` and save to `09-review/volume-reports/Volume-XX-repair.md`.
2. Update master-outline, foreshadowing, reveals, timeline, lore-index.
3. Log the repair in the decision log.

Required output: per volume — `04-volumes/Volume-XX-pre-review.md`, `04-volumes/Volume-XX.md`, `09-review/volume-reports/Volume-XX-repair.md`.

## Phase 6 — Chapters

Goal: turn each volume card into a sequence of chapter cards.

Pre-Chapter Brief (mandatory for every chapter, including chapter 001):

1. Read the current volume card.
2. Read the previous chapter card (or volume opening notes for chapter 001).
3. Read the previous chapter's micro-repair report at `09-review/micro-reports/Chapter-XXX-repair.md` (or volume opening notes for chapter 001). The repair report is the **latest world state** — it is the source of truth for character positions, active foreshadowing, and open conflicts. The character / worldbuilding files are the baseline, but the repair report is the delta applied on top. Skipping it is the most common source of continuity bugs.
4. Read the involved character / worldbuilding files.
5. Fill `references/pre-chapter-brief-template.md` and save it as `05-chapter-cards/Chapter-XXX-pre-brief.md`.

Chapter card:

1. Use `references/chapter-template.md` and save to `05-chapter-cards/Chapter-XXX.md`.
2. The card's `Pre-Chapter Brief` field must reference the brief file.
3. Confirm with the user.

Required output: per chapter — `05-chapter-cards/Chapter-XXX-pre-brief.md`, `05-chapter-cards/Chapter-XXX.md`.

## Phase 7 — Prose

Goal: draft the chapter prose from the chapter card, with continuity enforcement.

Mandatory pre-draft reading:

1. The current chapter card.
2. The previous chapter's draft (or volume opening notes for chapter 001).
3. The previous chapter's micro-repair report at `09-review/micro-reports/Chapter-XXX-repair.md` (or volume opening notes for chapter 001). The repair report is the **latest world state** — character positions, active foreshadowing, and open conflicts. Without it, prose will reuse the stale character / world files as if no chapter had happened.
4. Every involved character file.
5. Every relevant worldbuilding file.
6. `03-plot/foreshadowing.md`.
7. `00-project/正文写作指南.md` — this file is mandatory; if it does not exist, create it using `references/prose-writing-guide-template.md` and confirm with the user before continuing.

Draft:

1. Write the chapter prose and save to `06-chapter-drafts/Chapter-XXX.md`.
2. Pause for user feedback after the draft.

Micro-Repair (mandatory after every chapter draft):

1. Run the **Punctuation Sweep** first (see `references/punctuation-sweep.md`). Use `check_dash.py` to inspect, then `fix_dash.py` to repair. Log the sweep stats in the micro-repair report.
2. Fill `references/micro-repair-template.md` and save to `09-review/micro-reports/Chapter-XXX-repair.md`.
3. Update the impacted files (character, worldbuilding, foreshadowing, timeline, lore-index).
4. Update `00-project/progress.md`.
5. Log the repair in the decision log.

Required output: per chapter — `06-chapter-drafts/Chapter-XXX.md`, `09-review/micro-reports/Chapter-XXX-repair.md`.

## Punctuation Sweep

The skill ships with two helper scripts at the repo root: `check_dash.py` and `fix_dash.py`. They operate on `06-chapter-drafts/` and apply the punctuation rules in `00-project/正文写作指南.md`.

Workflow per chapter:

1. Run `python check_dash.py` — produce a read-only report of every punctuation issue with a fix suggestion.
2. Review the report with the user. Confirm any non-obvious cases (semantic middle-dash replacements).
3. Run `python fix_dash.py` — apply the agreed fixes. The script is idempotent.
4. Record the sweep stats (issues found, fixes applied) in the micro-repair report.

The Sweep is mandatory before Micro-Repair on every chapter. It is also recommended (but not mandatory) after large Volume Repair rewrites.

### What the scripts catch

- em-dash `—`, en-dash `–`, horizontal bar `―`, full-width `——`, double `--`
- duplicate commas `，，`
- redundant terminal commas (`。，`, `！，`, `？，`, `；，`, `：，`)
- leading-line commas

### Middle-dash semantic replacement

When a dash sits between characters (not at line start, line end, or before a quote), the script replaces it based on the surrounding context:

| Context | Replaced with |
| --- | --- |
| tone particle (`啊` `哦` `呀` `呢` `嘛` `吧` `唉` `哼` `嘿` `哈` `呵` `嗯` `呜`) | `，` |
| example/clarification (`如` `比如` `例如` `即` `也就是`) | `:` |
| transition (`但` `可` `却` `然而` `不过` `只是` `可惜`) | `；` |
| default | `，` |

Always confirm the "default" cases with the user before applying — they are the most likely to need a different choice.

## Two-Tier Repair System

The skill has three levels of repair, each with a different trigger and scope:

| Level | Trigger | Scope | Output |
| --- | --- | --- | --- |
| Micro-Repair | After every chapter draft | Single chapter delta: character state, foreshadowing, timeline, lore | `09-review/micro-reports/Chapter-XXX-repair.md` |
| Volume Repair | After every volume completes | Whole-volume integrity: spine, foreshadowing balance, reveals, timeline, lore-index, prose guide | `09-review/volume-reports/Volume-XX-repair.md` |
| Project Repair | After all volumes complete (optional) | Cross-volume consistency, character arcs end-state, foreshadowing close-out, theme payoff | `09-review/project-repair.md` |

Skipping a Micro-Repair to "save time" is not allowed. Skipping a Volume Repair blocks the next volume's Pre-Volume Review.

## File Update Timing

File updates are **event-driven, not continuous**. Each file has a defined creation point, update trigger, and review point. Do not "sync" files arbitrarily — only update them when an event below fires, and log the event in `09-review/decisions-log.md`.

### Timing Table

| File | Create | Update (event-driven) | Review (passive) | Reference while |
| --- | --- | --- | --- | --- |
| `00-project/spark.md` | Phase 0 | Skip/rollback to Phase 0 | — | every later phase |
| `00-project/positioning.md` | Phase 1 | Phase 1 confirmation revision | — | every later phase |
| `01-worldbuilding/*` | Phase 2 | Micro-Repair (only if this chapter changes a world rule) | Volume Repair (whole-volume integrity) | Pre-Volume Review; Pre-Chapter Brief; Prose |
| `02-characters/*` | Phase 3 | Micro-Repair (only if this chapter changes a character state) | Volume Repair (arc integrity) | Pre-Chapter Brief; Prose |
| `03-plot/master-outline.md` | Phase 4 | **Contract — only on Phase 4 → 5 rollback**; never on whim. Any change requires a logged rollback. | Volume Repair (does the volume still serve the spine?) | Pre-Volume Review; Volume Repair |
| `03-plot/foreshadowing.md` | Phase 4 | **Every** Micro-Repair that plants or pays off a foreshadowing item | Volume Repair (density & balance) | Pre-Chapter Brief; Prose; Micro-Repair |
| `03-plot/reveals.md` | Phase 4 | Micro-Repair that fires a reveal | Volume Repair (pacing) | Pre-Chapter Brief; Prose |
| `03-plot/timeline.md` | Phase 4+ | Micro-Repair (if this chapter is on the timeline) | Volume Repair (sequence check) | Pre-Chapter Brief; Prose |
| `04-volumes/Volume-XX.md` | Phase 5 | Only by Phase 5 rollback | — | Pre-Chapter Brief; Prose |
| `05-chapter-cards/Chapter-XXX.md` | Phase 6 | Only by Phase 6 rollback | — | Prose |
| `06-chapter-drafts/Chapter-XXX.md` | Phase 7 | Punctuation Sweep (mandatory) → Micro-Repair (prose polish) | — | next chapter's Pre-Chapter Brief (as prior state) |
| `00-project/正文写作指南.md` | Before first Phase 7 draft (mandatory) | Volume Repair (if style drift detected) | Volume Repair | **Every** Prose draft (mandatory) |
| `09-review/micro-reports/Chapter-XXX-repair.md` | After every chapter (mandatory) | Append-only | — | **Next chapter's Pre-Chapter Brief (mandatory)** |
| `09-review/volume-reports/Volume-XX-repair.md` | After every volume (mandatory) | Append-only | — | next volume's Pre-Volume Review |
| `09-review/project-repair.md` | After all volumes (optional) | Append-only | — | final pass |
| `09-review/decisions-log.md` | At project start | **Append** on every event below; never rewrite history | — | always |
| `00-project/progress.md` | At project start | Every phase advance, repair completion, skip/rollback | — | always |

### Decision Log Trigger Events

Append a row to `09-review/decisions-log.md` on **any** of the following (append-only; never delete or rewrite history):

- Phase confirmation (with date)
- Conflict raised and the chosen repair
- Skip or rollback between phases
- Micro-Repair, Volume Repair, or Project Repair completion
- Prose-guide creation or update
- Master-outline change (rare; always tied to a rollback)
- Punctuation Sweep stats summary (issues found, fixes applied)

### Per-Phase Pre-Read Cheatsheet

| Phase | Mandatory pre-read | Mandatory reference during |
| --- | --- | --- |
| Phase 5 Pre-Volume Review | all of `00-project/`, `01-worldbuilding/`, `02-characters/`, `03-plot/`, prior volume's Volume Repair | — |
| Phase 6 Pre-Chapter Brief | current volume card; previous chapter card; **previous chapter's micro-repair report**; involved character / world files | — |
| Phase 7 Prose draft | current chapter card; previous chapter's draft; **previous chapter's micro-repair report**; all involved character / world files; `03-plot/foreshadowing.md`; `00-project/正文写作指南.md` (mandatory) | — |
| Micro-Repair | this chapter's draft; chapter card; involved character / world files | — |

The **previous chapter's micro-repair report** is the source of truth for "where the world is right now". The character / world files are the baseline. The repair report is the delta applied on top. Read it in **both** Pre-Chapter Brief and Prose draft. The prose guide is style rules and is read **only** during Prose draft — it is not used for planning.

## Decision Log

`09-review/decisions-log.md` is the single source of truth for non-content decisions.

Log entries for:

- every phase confirmation (with date)
- every conflict and its chosen repair
- every skip or rollback between phases
- every repair completion (Micro / Volume / Project)
- every prose-guide update

Use `references/decisions-log-template.md` for the entry format. Append a new row per event; never delete or rewrite old entries.

## Skip & Rollback Rules

Skip (jump forward):

- Allowed only if the target phase's prerequisites are already on disk.
- Must log: source phase, target phase, reason, impacted files.
- Must run a verification pass on the skipped phases before continuing.

Rollback (jump backward):

- Allowed any time.
- Must log: current phase, target phase, reason.
- Must run a regression pass: read everything produced after the target phase and flag any content that needs to be re-checked.

Both actions must update `00-project/progress.md`.

## Use the References

- `references/spark-template.md` — Phase 0 spark capture
- `references/positioning-template.md` — Phase 1 project positioning
- `references/worldbuilding-template.md` — Phase 2 worldbuilding files
- `references/character-template.md` — Phase 3 character cards
- `references/master-outline-template.md` — Phase 4 master outline
- `references/foreshadowing-template.md` — Phase 4 foreshadowing tracker
- `references/reveals-template.md` — Phase 4 reveals tracker
- `references/timeline-template.md` — Phase 4+ timeline events
- `references/pre-volume-review-template.md` — Phase 5 pre-volume recap
- `references/volume-template.md` — Phase 5 volume card
- `references/volume-repair-template.md` — Phase 5 volume repair
- `references/pre-chapter-brief-template.md` — Phase 6 pre-chapter brief
- `references/chapter-template.md` — Phase 6 chapter card
- `references/prose-writing-guide-template.md` — Phase 7 prose guide (mandatory)
- `references/micro-repair-template.md` — Phase 7 micro-repair
- `references/decisions-log-template.md` — decision log entry format
- `references/progress-template.md` — `00-project/progress.md` tracker

If the user points to an existing prose guide file, treat it as required reading before generating正文.

## Guide Step by Step

Lead the user through the project in controlled phases.

When the user is early in the process:

- focus on the current phase only
- present structure before large content
- ask for confirmation before advancing

When the user requests full-story generation, redirect to the staged workflow:

1. explain that this skill is for structured long-form development
2. identify the current phase
3. complete that phase first
4. move to the next phase only after confirmation

Do not generate a complete novel, full multi-volume story, or end-to-end finished manuscript in one pass. That is outside this skill's job.

## Handle Conflicts Explicitly

When new writing conflicts with the existing project files:

1. Name the conflict clearly.
2. Offer two or three repair options.
3. Ask whether to change the setting, outline, or current chapter direction.
4. Log the decision in `09-review/decisions-log.md`.

Escalate instead of silently rewriting continuity.