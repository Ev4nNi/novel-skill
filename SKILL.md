---
name: novel-skill
description: Use when guiding a user through building a long-form novel project step by step, confirming structure for worldbuilding, characters, outlines, and chapters before drafting, and organizing the project in Obsidian or Markdown.
---

# Novel Skill

## Overview

Use this skill to guide a user through building and maintaining a long-form novel project step by step instead of generating a full story in one go.

Confirm the project structure with the user before each major stage. Do not treat "write me a whole novel" as a request to generate the entire finished story at once.

## Core Workflow

1. Detect the user's current stage before writing.
2. Ask the user which project mode to use: `Obsidian` or `folder + Markdown`.
3. Continue from the current stage instead of rebuilding the whole project.
4. Confirm the framework for the current stage with the user before creating files or content.
5. Default to this order unless the user explicitly asks to skip ahead:
   `idea -> positioning -> worldbuilding -> characters -> master outline -> volumes -> chapter cards -> chapter drafts -> prose -> knowledge-base updates`
6. Before drafting prose, read the project's `00-project/正文写作指南.md` if it exists. If it does not exist, confirm whether to create it first.
7. Write prose from a chapter card in `05-chapter-cards/`, save the draft to `06-chapter-drafts/`.
8. Treat knowledge-base updates as part of writing, not optional cleanup.
9. Guide the user one step at a time. Do not generate the complete story content in a single response.

## Detect the Current Stage

Classify the request before acting:

- only an idea
- partial setting
- existing character files
- existing outline
- active chapter cards
- active chapter drafting
- prose generation
- continuity repair or revision

If files already exist, read the relevant ones before proposing new material.

## Choose the Project Mode

Do not assume the storage mode.

Ask the user to choose between:

- `Obsidian`
- `folder + Markdown`

If the user chooses Obsidian, use Obsidian-compatible organization.

If the user chooses folder plus Markdown, keep the same folder structure with plain Markdown files.

Read `references/project-structure.md` before scaffolding a new novel project or reorganizing an existing one.

## Confirm Each Framework Before Advancing

Before moving to a new major stage, confirm the framework for that stage with the user.

At minimum, explicitly confirm:

- project positioning and target readership
- worldbuilding scope and rule system
- character roster and role structure
- master outline structure
- volume breakdown approach
- chapter card format

Do not silently invent the full framework for all stages at once. Present the current stage, get confirmation, then move forward.

If the user wants adjustments, revise the current stage before continuing.

## Use the References

- Read `references/worldbuilding-template.md` when building setting files.
- Read `references/character-template.md` when creating or updating character files.
- Read `references/master-outline-template.md` when building the story-level outline.
- `04-volumes/` when creating or updating volume cards.
- `05-chapter-cards/` when drafting a chapter card.
- `06-chapter-drafts/` when writing chapter prose.
- Read `references/prose-writing-guide-template.md` when creating or updating `00-project/正文写作指南.md`.
- Read `references/foreshadowing-template.md` when planting or paying off a setup.
- Read `references/timeline-template.md` when a scene changes chronology or event order.

If the user points to an existing prose guide file, treat it as required reading before generating正文. For example, if the project includes a file like `D:\programproject\novel-test\novel-framework-choice\00-project\正文写作指南.md`, read it first and follow it.

## Guide Step by Step

Lead the user through the project in controlled stages.

When the user is early in the process:

- focus on the current stage only
- present structure before large content
- ask for confirmation before advancing

When the user requests full-story generation, redirect to the staged workflow:

1. explain that this skill is for structured long-form development
2. identify the current stage
3. complete that stage first
4. move to the next stage only after confirmation

Do not generate a complete novel, full multi-volume story, or end-to-end finished manuscript in one pass. That is outside this skill's job.

## Stabilize Prose Drafting

Before generating any chapter正文:

1. read the current chapter card
2. read the previous relevant chapter or summary
3. read the involved character files
4. read the relevant worldbuilding files
5. read `03-plot/foreshadowing.md`
6. read `00-project/正文写作指南.md` if present

If the prose guide is missing and the user wants stable long-form drafting, suggest creating or confirming it before continuing.

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

When a volume is completed, immediately review and repair the related core files before moving to the next volume:

- `01-worldbuilding/` core setting files
- `03-plot/master-outline.md`
- `03-plot/foreshadowing.md`
- `03-plot/reveals.md`
- `07-timeline/` timeline files

Treat these repairs as mandatory maintenance, not optional cleanup.

## Handle Conflicts Explicitly

When new writing conflicts with the existing project files:

1. Name the conflict clearly.
2. Offer two or three repair options.
3. Ask whether to change the setting, outline, or current chapter direction.

Escalate instead of silently rewriting continuity.
