---
title: novel-skill design
date: 2026-06-03
status: approved-in-chat
---

# novel-skill

## Goal

Create a reusable Codex skill for building long-form novels from scratch in the current repository root.

The skill should support general genre switching, prefer Obsidian vault organization, fall back to plain folder plus Markdown organization, and enforce a staged workflow:

`idea -> positioning -> worldbuilding -> characters -> master outline -> volumes -> chapters -> prose -> knowledge-base updates`

The skill is not a one-shot prose prompt pack. It is an engineering-style writing workflow for planning, drafting, and maintaining a full novel project over time.

## Primary Use Case

The primary use case is:

- Start from a rough premise or a single sentence idea.
- Build the novel foundation step by step.
- Generate a long-form work chapter by chapter.
- Maintain consistency for settings, characters, foreshadowing, and timeline as the manuscript grows.

## Scope

The first version should:

- Support long-form novel creation from zero.
- Remain genre-agnostic by default.
- Prefer Obsidian-style knowledge management.
- Also work in a plain folder plus Markdown setup.
- Maintain project files for world rules, character data, plot structure, foreshadowing, and timeline.
- Require knowledge-base updates as part of chapter generation.

The first version should not:

- Build custom visualization scripts or graph-generation tools.
- Build advanced pacing analytics or word-count dashboards.
- Manage multiple books in a shared meta-library.
- Ship genre-specialized rule packs in the initial release.

## Recommended Skill Shape

Use a workflow plus templates design.

The first version should include:

- `SKILL.md`
- `agents/openai.yaml`
- `references/`

Do not require scripts in v1 unless implementation reveals a specific repetitive task that is fragile enough to justify automation.

## Skill Name

Use `novel-skill`.

Rationale:

- Matches the repository root, which is the actual skill folder.
- Broad enough to cover planning plus drafting.
- Clear enough to trigger on long-form novel building requests instead of generic creative writing.

## Triggering Intent

The skill should trigger when the user wants Codex to help with any of the following:

- Create a long-form novel from scratch.
- Build a novel project structure.
- Plan worldbuilding, character systems, master outline, volume outline, or chapter outline for a novel.
- Draft chapters while maintaining consistency across existing novel files.
- Maintain or update novel knowledge-base files such as setting notes, character notes, timeline, or foreshadowing tracker.
- Organize a novel project in Obsidian or in folder plus Markdown form.

The skill should not primarily target:

- Short stories.
- Poetry.
- Screenplays.
- Single-scene improvisation with no project continuity requirements.

## Workflow

The skill should instruct Codex to determine the user's current stage first, then continue from that point instead of always rebuilding the project from zero.

### Stage 1: Project Initiation

When the user only has a rough idea, produce and maintain:

- `00-project/idea.md`
- `00-project/goals.md`
- `00-project/style-guide.md`
- `00-project/progress.md`

This stage defines:

- premise
- target readership
- genre and tone
- expected length
- narrative promises
- stylistic boundaries

### Stage 2: Worldbuilding

Create and maintain files under `01-worldbuilding/`, including:

- `world-overview.md`
- `geography.md`
- `factions.md`
- `power-system.md`
- `rules-and-taboo.md`

This stage defines the rules that later prose must respect.

### Stage 3: Character System

Create and maintain files under `02-characters/`, including:

- `protagonist.md`
- `deuteragonists.md`
- `antagonists.md`
- `supporting-cast.md`
- `relationship-map.md`

This stage defines:

- role
- motivation
- inner conflict
- external conflict
- arc
- secrets
- relationships
- first appearance
- major turning points

### Stage 4: Plot Architecture

Create and maintain files under `03-plot/`, including:

- `master-outline.md`
- `arc-list.md`
- `conflict-design.md`
- `foreshadowing.md`
- `reveals.md`

This stage defines the high-level dramatic structure and promise delivery.

### Stage 5: Volume Planning

Create and maintain files under `04-volumes/`, with one file per volume, for example:

- `volume-01-outline.md`
- `volume-02-outline.md`

Each volume should capture:

- thematic focus
- stage objective
- major escalation
- climax
- character movement

### Stage 6: Chapter Planning

Create and maintain files under `05-chapters/`, with one file per chapter.

Each chapter should be based on a chapter card before prose is drafted. The chapter card should at minimum include:

- chapter goal
- conflict
- information gain
- character-state changes
- foreshadowing setup or payoff
- timeline position

### Stage 7: Prose Drafting

Draft prose from the chapter card, not directly from raw user intent, unless the user explicitly requests a lighter workflow.

### Stage 8: Knowledge-Base Update

After any meaningful prose generation, update all impacted project files before considering the step complete.

This is a hard rule for the skill.

## Knowledge Management Mode

Default to Obsidian-compatible organization.

If the user does not want Obsidian, use the same folder structure with plain Markdown files.

In Obsidian mode, encourage:

- `[[double links]]` for people, places, factions, events, items, and chapters
- chapter-to-character links
- character-to-event links
- foreshadowing records that link setup and payoff chapters

The skill should never require exclusive Obsidian features to function. Obsidian is the preferred viewing and navigation layer, not a hard dependency.

## Proposed Directory Layout

```text
novel-project/
  00-project/
    idea.md
    goals.md
    style-guide.md
    progress.md
  01-worldbuilding/
    world-overview.md
    geography.md
    factions.md
    power-system.md
    rules-and-taboo.md
  02-characters/
    protagonist.md
    deuteragonists.md
    antagonists.md
    supporting-cast.md
    relationship-map.md
  03-plot/
    master-outline.md
    arc-list.md
    conflict-design.md
    foreshadowing.md
    reveals.md
  04-volumes/
    volume-01-outline.md
    volume-02-outline.md
  05-chapters/
    chapter-001.md
    chapter-002.md
  06-timeline/
    global-timeline.md
    event-log.md
  07-lore-index/
    glossary.md
    locations.md
    items.md
  08-review/
    consistency-check.md
    revision-notes.md
```

## Required References

Create these reference files in `references/`:

- `project-structure.md`
- `character-template.md`
- `worldbuilding-template.md`
- `master-outline-template.md`
- `volume-template.md`
- `chapter-template.md`
- `foreshadowing-template.md`
- `timeline-template.md`

### Reference Responsibilities

`project-structure.md`

- Explain the directory layout.
- Explain how Obsidian mode and plain Markdown mode map to the same structure.
- Explain what each folder is for and when Codex should update it.

`character-template.md`

- Provide a reusable character card.
- Include identity, role, desire, fear, contradiction, arc, key relationships, first appearance, and major events.

`worldbuilding-template.md`

- Provide a reusable worldbuilding structure.
- Include era, geography, factions, rules, taboo, economics, power system, and societal consequences.

`master-outline-template.md`

- Provide a reusable story-level outline.
- Include premise, central conflict, escalation path, key reversals, climax, resolution, and thematic statement.

`volume-template.md`

- Provide a reusable volume outline.
- Include volume goal, turning points, new pressure, climax, aftermath, and state changes.

`chapter-template.md`

- Provide a reusable chapter card.
- Include objective, conflict, scene outcome, information release, emotional movement, setup or payoff, and time markers.

`foreshadowing-template.md`

- Provide a tracker with fields for setup chapter, expected payoff, actual payoff, status, and notes.

`timeline-template.md`

- Provide a tracker with fields for event ordering, participants, location, consequence, and continuity notes.

## Interaction Model

When invoked, the skill should first identify the user's current state:

- only an idea
- partial setting
- existing character notes
- existing outline
- active chapter drafting
- revision or continuity repair

Then it should continue from the current state instead of restarting everything.

The skill should allow a lighter mode only if the user explicitly asks for speed over structure.

Even in lighter mode, the skill should still encourage at least a chapter card before prose.

## Consistency Rules

The skill should enforce this rule:

`No chapter advancement without project-file maintenance.`

At minimum, Codex should update the relevant files when:

- a new character is introduced
- a relationship changes
- a new setting rule appears
- a foreshadowing element is planted
- a foreshadowing element is paid off
- a timeline event changes the global chronology
- a volume ends

## Conflict Handling

When new writing conflicts with existing project files, the skill should pause and surface the issue rather than silently rewriting history.

The skill should instruct Codex to:

1. identify the conflict clearly
2. propose two or three repair options
3. ask the user whether to change the setting, outline, or current chapter direction

Typical conflict categories:

- setting-rule contradiction
- motivation contradiction
- foreshadowing mismatch
- impossible timeline overlap
- tone or ending drift

## Style of Instructions

Write the skill in imperative form.

Keep `SKILL.md` concise and procedural. Put longer structural details into `references/`.

The body of `SKILL.md` should focus on:

- stage detection
- workflow order
- update requirements
- when to open each reference file

## Validation Criteria

The finished skill is successful if it enables another Codex instance to:

- recognize when to use the skill
- choose Obsidian-first organization by default
- scaffold a novel project in Markdown
- continue the project from partial user material
- draft new chapters while maintaining consistency files
- stop and escalate when continuity conflicts appear

## Implementation Notes

Version 1 should prioritize:

- strong triggering description
- clean folder conventions
- clear stage-by-stage workflow
- strong update discipline
- reusable Markdown templates

Version 1 should avoid:

- overlong explanations
- genre-specific bloat
- unnecessary automation

## Next Step

After this spec is approved in-file, create the skill and validate it with the standard skill validation flow.
