---
name: novel-skill
description: Use when creating a long-form novel from scratch, extending a novel project through worldbuilding, characters, outlining, volumes, chapters, and prose, or maintaining novel continuity files in Obsidian or Markdown.
---

# Novel Skill

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
