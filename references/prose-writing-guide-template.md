# Prose Writing Guide Template

Use this template for `00-project/正文写作指南.md` (Phase 7). This file is **mandatory** before drafting any chapter. If it does not exist when Phase 7 starts, create it first and confirm with the user.

````markdown
# 正文写作指南

## Status
- Mandatory: yes
- Created in phase: Phase 7
- Last updated:
- Trigger for update: (e.g. volume repair, prose drift)

## User Confirmation
- Tone confirmed:
- Rhythm confirmed:
- Conflict intensity confirmed:
- Prose density confirmed:
- Sign-off date:

## Core Principles
- Plot rhythm (clause pacing, sentence rhythm):
- Consequence realism (no deus-ex-machina without setup):
- Character consistency (voice and behavior must match the character card):
- Foreshadowing discipline (every payoff traces back to a logged setup):
- POV discipline (no head-hopping without chapter card approval):

## Required Reading Before Drafting
- Current chapter card
- Current chapter pre-brief
- Previous relevant chapter draft (or volume opening notes for chapter 001)
- Involved character files
- Relevant worldbuilding files
- `03-plot/foreshadowing.md`
- `03-plot/reveals.md` (if the chapter is scheduled to reveal something)
- Timeline files for any event ordering

## Pre-Draft Checklist
- Chapter objective confirmed:
- Chapter conflict confirmed:
- Required information release confirmed:
- Required setup or payoff confirmed:
- Continuity risks checked (foreshadowing / timeline / lore):

## Drafting Rules
- Keep character voice consistent with the character card
- Respect world rules and costs (no rule invented in the chapter)
- Do not skip chapter-card obligations
- Do not invent major setting changes without user confirmation
- If a new setting rule emerges, log it for lore-index update
- If a new foreshadowing is planted, log it in `03-plot/foreshadowing.md` before ending the chapter

## Post-Draft Checklist (Micro-Repair input)
- Character files updated if any state changed
- Foreshadowing tracker updated (plant / payoff / status)
- Reveals tracker updated if a reveal happened
- Timeline updated if chronology changed
- Lore-index updated if a new term / place / item appeared
- `00-project/progress.md` updated
- `09-review/decisions-log.md` updated

## Punctuation Rules (enforced by Punctuation Sweep)

The skill runs `check_dash.py` and `fix_dash.py` against `06-chapter-drafts/` after every chapter draft. The rules below MUST match what the scripts apply. If you change these rules, update the scripts in the same commit and log a `prose-guide-update` event in `09-review/decisions-log.md`.

### Dash handling

- Line-start dash: keep (Markdown list marker)
- Trailing dash at end of file/paragraph: delete
- Dash immediately before a closing quote (`"…—"`, `…—"`): delete
- Middle dash followed by tone particle (`啊 哦 呀 呢 嘛 吧 唉 哼 嘿 哈 呵 嗯 呜`) or preceded by one: replace with `，`
- Middle dash followed by example/clarification word (`如 比如 例如 即 也就是`) or preceded by one: replace with `:`
- Middle dash followed by transition word (`但 可 却 然而 不过 只是 可惜`) or preceded by one: replace with `；`
- Middle dash in any other context: replace with `，` (default)

### Other punctuation

- No `，，` (duplicate commas)
- No `。，` `！，` `？，` `；，` `：，` (terminal-comma combinations)
- No leading-line comma
- All Chinese punctuation, no half-width punctuation inside Chinese sentences

## Volume-End Repair Rule

When a volume is completed, in addition to the per-chapter micro-repairs, run a Volume Repair:

- Worldbuilding core files
- Master outline
- Foreshadowing tracker
- Reveals tracker
- Timeline files
- Lore-index
- 正文写作指南.md itself, if writing rhythm or guardrails need adjustment

## Project-Level Repair Rule

After the final volume completes, run a Project Repair:

- Cross-volume foreshadowing close-out
- Character arc end-state confirmation
- Theme payoff audit
- Final timeline and lore-index pass
````