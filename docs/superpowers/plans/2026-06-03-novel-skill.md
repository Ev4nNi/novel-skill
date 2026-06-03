# Novel Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the `novel-skill` skill in the current repository root so Codex can create and maintain long-form novel projects with an Obsidian-first, Markdown-compatible workflow.

**Architecture:** Turn the repository root into a self-contained skill package with a concise `SKILL.md`, UI metadata in `agents/openai.yaml`, and reusable writing templates in `references/`. Validate the skill structure with the official `quick_validate.py` script and verify the content against the approved design spec before calling it complete.

**Tech Stack:** Markdown, YAML, PowerShell, Python utility scripts from `C:\Users\90919\.codex\skills\.system\skill-creator\scripts`

---

## File Structure

The implementation will create this skill package at the repository root:

- `SKILL.md`
  The skill frontmatter and the procedural workflow another Codex instance should follow.
- `agents/openai.yaml`
  UI-facing metadata for skill lists and invocation chips.
- `references/project-structure.md`
  The novel project layout and update rules.
- `references/character-template.md`
  Reusable character card template.
- `references/worldbuilding-template.md`
  Reusable worldbuilding template.
- `references/master-outline-template.md`
  Reusable story outline template.
- `references/volume-template.md`
  Reusable volume template.
- `references/chapter-template.md`
  Reusable chapter card template.
- `references/foreshadowing-template.md`
  Reusable foreshadowing tracker template.
- `references/timeline-template.md`
  Reusable timeline tracker template.

The implementation will also maintain this supporting documentation:

- `docs/superpowers/plans/2026-06-03-novel-skill.md`
  This implementation plan.

## Task 1: Establish the skill baseline and create the root package

**Files:**
- Create: `d:\programproject\novel-skill\SKILL.md`
- Create: `d:\programproject\novel-skill\agents\openai.yaml`
- Create: `d:\programproject\novel-skill\references\`

- [ ] **Step 1: Run a baseline directory check before creating the skill**

Run:

```powershell
Get-ChildItem -Force d:\programproject\novel-skill
```

Expected: The repository contains docs and root files, and no nested skill folder is required.

- [ ] **Step 2: Create the skill files directly at the repository root**

Create these root-level paths:

- `d:\programproject\novel-skill\SKILL.md`
- `d:\programproject\novel-skill\agents\openai.yaml`
- `d:\programproject\novel-skill\references\`

Expected: The repository root itself becomes a valid skill package.

- [ ] **Step 3: Verify the root package exists**

Run:

```powershell
Get-ChildItem -Force d:\programproject\novel-skill
```

Expected: `SKILL.md`, `agents`, and `references` are present at the repository root.

## Task 2: Write the skill body and triggering description

**Files:**
- Modify: `d:\programproject\novel-skill\SKILL.md`
- Reference: `d:\programproject\novel-skill\docs\superpowers\specs\2026-06-03-novel-skill-design.md`

- [ ] **Step 1: Replace the scaffold frontmatter with the final skill metadata**

Write this frontmatter into `d:\programproject\novel-skill\SKILL.md`:

```markdown
---
name: novel-skill
description: Use when creating a long-form novel from scratch, planning or extending a novel project, drafting chapters that must stay consistent with existing setting or character files, or organizing novel knowledge in Obsidian or Markdown.
---
```

- [ ] **Step 2: Write the procedural skill body**

Write a concise body that includes these exact sections:

```markdown
# Novel Architect

## Overview

Use this skill to build and maintain a long-form novel project instead of generating disconnected prose. Prefer an Obsidian vault, but use the same Markdown structure when the user does not want Obsidian.

## Core Workflow

1. Detect the user's current stage before writing.
2. Continue from the current stage instead of rebuilding the whole project.
3. Default to this order unless the user explicitly asks to skip ahead:
   `idea -> positioning -> worldbuilding -> characters -> master outline -> volumes -> chapters -> prose -> knowledge-base updates`
4. Write prose from a chapter card, not directly from a vague prompt, unless the user explicitly asks for a lighter workflow.
5. Treat knowledge-base updates as part of writing, not optional cleanup.

## Detect the Current Stage

Classify the request before acting:

- only an idea
- partial setting
- existing character files
- existing outline
- active chapter drafting
- continuity repair or revision

If files already exist, read the relevant ones before proposing new material.

## Choose the Project Mode

Default to Obsidian-compatible organization.

If the user does not want Obsidian, keep the same folder structure with plain Markdown files.

Read `references/project-structure.md` before scaffolding a new novel project or reorganizing an existing one.

## Use the References

- Read `references/worldbuilding-template.md` when building setting files.
- Read `references/character-template.md` when creating or updating character files.
- Read `references/master-outline-template.md` when building the story-level outline.
- Read `references/volume-template.md` when splitting the story into volumes or arcs.
- Read `references/chapter-template.md` before drafting a chapter.
- Read `references/foreshadowing-template.md` when planting or paying off a setup.
- Read `references/timeline-template.md` when a scene changes chronology or event order.

## Enforce Continuity

Do not advance the manuscript without updating impacted project files.

Update the knowledge base whenever:

- a new character appears
- a relationship changes
- a new setting rule appears
- a foreshadowing element is planted
- a foreshadowing element is paid off
- a timeline event changes the chronology
- a volume ends

## Handle Conflicts Explicitly

When new writing conflicts with the existing project files:

1. Name the conflict clearly.
2. Offer two or three repair options.
3. Ask whether to change the setting, outline, or current chapter direction.

Escalate instead of silently rewriting continuity.
```

- [ ] **Step 3: Review the skill body against the spec**

Run:

```powershell
Get-Content d:\programproject\novel-skill\SKILL.md
```

Expected: The file is concise, imperative, and matches the approved workflow and boundaries from the spec.

## Task 3: Fill the reusable reference templates

**Files:**
- Modify: `d:\programproject\novel-skill\references\project-structure.md`
- Modify: `d:\programproject\novel-skill\references\character-template.md`
- Modify: `d:\programproject\novel-skill\references\worldbuilding-template.md`
- Modify: `d:\programproject\novel-skill\references\master-outline-template.md`
- Modify: `d:\programproject\novel-skill\references\volume-template.md`
- Modify: `d:\programproject\novel-skill\references\chapter-template.md`
- Modify: `d:\programproject\novel-skill\references\foreshadowing-template.md`
- Modify: `d:\programproject\novel-skill\references\timeline-template.md`

- [ ] **Step 1: Write the project structure guide**

Write `d:\programproject\novel-skill\references\project-structure.md` with:

```markdown
# Project Structure

Use this layout for a new novel project:

```text
novel-project/
  00-project/
  01-worldbuilding/
  02-characters/
  03-plot/
  04-volumes/
  05-chapters/
  06-timeline/
  07-lore-index/
  08-review/
```

Use the same layout for Obsidian and plain Markdown.

## Folder Responsibilities

- `00-project`: premise, goals, style guide, progress
- `01-worldbuilding`: rules, factions, geography, power system
- `02-characters`: character cards and relationship updates
- `03-plot`: master outline, arcs, conflict design, foreshadowing
- `04-volumes`: volume or arc plans
- `05-chapters`: chapter cards and chapter drafts
- `06-timeline`: chronology and event log
- `07-lore-index`: locations, terms, items
- `08-review`: consistency checks and revision notes

## Update Rules

Update the matching files immediately after any new prose changes project facts.

In Obsidian mode, prefer `[[double links]]` for people, places, organizations, items, and events.
```

- [ ] **Step 2: Write the character template**

Write `d:\programproject\novel-skill\references\character-template.md` with:

```markdown
# Character Template

```markdown
# [[Character Name]]

## Identity
- Role:
- Public identity:
- Hidden identity or secret:
- Age or life stage:

## Core Psychology
- Primary desire:
- Primary fear:
- Central contradiction:
- Moral boundary:

## Story Function
- Narrative role:
- First appearance:
- Core conflict:
- Character arc:

## Relationships
- Allies:
- Rivals:
- Family:
- Romance:

## Key Events
- Past defining event:
- Mid-story turning point:
- Late-story transformation:

## Notes
- Voice cues:
- Physical markers:
- Continuity notes:
```
```

- [ ] **Step 3: Write the worldbuilding template**

Write `d:\programproject\novel-skill\references\worldbuilding-template.md` with:

```markdown
# Worldbuilding Template

```markdown
# Worldbuilding Core

## Overview
- Premise:
- Genre mode:
- Tone:
- Era or age:

## Geography
- Core regions:
- Important cities or sites:
- Environmental constraints:

## Power and Order
- Governments or ruling structures:
- Major factions:
- Economic drivers:
- Social hierarchy:

## Rules
- Natural or supernatural rules:
- Costs and limits:
- Public knowledge vs hidden truth:
- Taboos:

## Pressure Points
- Historic trauma:
- Active instability:
- Scarcity:
- Upcoming crisis:
```
```

- [ ] **Step 4: Write the master outline template**

Write `d:\programproject\novel-skill\references\master-outline-template.md` with:

```markdown
# Master Outline Template

```markdown
# Master Outline

## Story Promise
- Premise:
- Target readership:
- Core emotional promise:
- Unique hook:

## Main Spine
- Protagonist goal:
- Main opposition:
- Stakes:
- Point of no return:

## Escalation
- Early pressure:
- Midpoint reversal:
- Late crisis:
- Final confrontation:

## Resolution
- Ending state:
- Thematic statement:
- Major payoff list:
```
```

- [ ] **Step 5: Write the volume template**

Write `d:\programproject\novel-skill\references\volume-template.md` with:

```markdown
# Volume Template

```markdown
# Volume XX Outline

## Volume Identity
- Theme:
- Stage purpose:
- Emotional flavor:

## Plot Movement
- Opening situation:
- New pressure:
- Major turn:
- Climax:
- Ending hook:

## Character Movement
- Main character shift:
- Supporting cast shift:
- Relationship changes:

## Continuity
- New lore:
- Foreshadowing planted:
- Foreshadowing paid off:
- Timeline notes:
```
```

- [ ] **Step 6: Write the chapter template**

Write `d:\programproject\novel-skill\references\chapter-template.md` with:

```markdown
# Chapter Template

```markdown
# Chapter XXX

## Chapter Card
- Objective:
- Conflict:
- Scene outcome:
- Information released:
- Emotional movement:
- Foreshadowing setup:
- Foreshadowing payoff:
- Timeline position:

## Draft Notes
- Point of view:
- Required callbacks:
- Required continuity checks:
```
```

- [ ] **Step 7: Write the foreshadowing and timeline templates**

Write `d:\programproject\novel-skill\references\foreshadowing-template.md` with:

```markdown
# Foreshadowing Template

```markdown
| Setup | Setup Chapter | Expected Payoff | Actual Payoff | Status | Notes |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | planned |  |
```
```

Write `d:\programproject\novel-skill\references\timeline-template.md` with:

```markdown
# Timeline Template

```markdown
| Order | Time Marker | Event | Participants | Location | Consequence | Continuity Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  |  |  |  |  |
```
```

- [ ] **Step 8: Review the reference files**

Run:

```powershell
Get-ChildItem -Recurse d:\programproject\novel-skill\references
```

Expected: All eight reference files exist with Markdown content aligned to the approved structure.

## Task 4: Finalize UI metadata and validate the skill package

**Files:**
- Modify: `d:\programproject\novel-skill\agents\openai.yaml`
- Verify: `d:\programproject\novel-skill\`

- [ ] **Step 1: Set the final OpenAI interface metadata**

Write this file to `d:\programproject\novel-skill\agents\openai.yaml`:

```yaml
interface:
  display_name: "Novel Skill"
  short_description: "Plan and maintain long-form novels with an Obsidian-first workflow."
  default_prompt: "Use $novel-skill to build and maintain a long-form novel project from idea to chapter drafting."

policy:
  allow_implicit_invocation: true
```

- [ ] **Step 2: Run the official skill validator**

Run:

```powershell
python C:\Users\90919\.codex\skills\.system\skill-creator\scripts\quick_validate.py d:\programproject\novel-skill
```

Expected: Validation completes successfully with no YAML or naming errors.

- [ ] **Step 3: Inspect git status**

Run:

```powershell
git status --short
```

Expected: The root skill files and plan/spec docs appear as uncommitted changes.

## Task 5: Verify spec coverage and package completeness

**Files:**
- Verify: `d:\programproject\novel-skill\docs\superpowers\specs\2026-06-03-novel-skill-design.md`
- Verify: `d:\programproject\novel-skill\SKILL.md`
- Verify: `d:\programproject\novel-skill\references\*.md`
- Verify: `d:\programproject\novel-skill\agents\openai.yaml`

- [ ] **Step 1: Compare the skill package against the design spec**

Check that the final package covers:

```text
- Obsidian-first organization with Markdown fallback
- Stage detection
- Workflow order from idea to prose
- Knowledge-base update requirement
- Conflict escalation behavior
- Reference templates for structure, characters, world, outline, volume, chapter, foreshadowing, and timeline
```

Expected: Every required behavior from the spec maps to either `SKILL.md`, `openai.yaml`, or a reference file.

- [ ] **Step 2: Confirm there are no placeholders**

Search:

```powershell
rg -n "TODO|TBD|placeholder" d:\programproject\novel-skill
```

Expected: No matches.

- [ ] **Step 3: Mark the package ready for forward use**

Run:

```powershell
Get-ChildItem -Recurse d:\programproject\novel-skill
```

Expected: The skill package is complete and ready for future invocation and further forward-testing.
