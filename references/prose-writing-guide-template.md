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

## Writing Style (Hard Rules — non-negotiable)

These rules define the project's writing style. They are not suggestions. They are enforced by the Punctuation Sweep (`check_dash.py` / `fix_dash.py`) and verified in every Micro-Repair.

### 1. 人工书写 (manual handwriting), not Markdown

The chapter draft is a wall of prose a human typed on a page. It is **not** a structured document.

- No `**bold**`, `*italic*`, `_underline_`, `~~strike~~` for emphasis.
- No `#`, `##`, `###` headers in the body of the chapter.
- No `- bullets`, `* bullets`, `1. numbered lists`, `- [ ]` checklists.
- No `> blockquotes`, no `---` horizontal rules.
- No backticks for code spans, even when referring to a term — italicize the term by context, not by Markdown.
- If a list is structurally necessary, fold it into natural sentence flow ("三件事：他欠了钱、他撒了谎、他跑了。") — do not render it as a Markdown list.
- Blank lines are paragraph breaks. They are the **only** structural mark allowed in the draft.

Markdown structure belongs in the chapter card and the repair report, **never** in the chapter draft itself.

### 2. 破折号 / 省略号 / 引号 — 严禁过多使用

These three marks are the "showy" punctuation of Chinese prose. They are easy to over-use and hard to read when they pile up. The Punctuation Sweep enforces a strict per-chapter budget. If a chapter is over budget, the user must either edit the chapter or log a `prose-style-exception` row in `09-review/decisions-log.md`.

| Mark | Per-chapter budget (≈3000 words) | Default action when over budget |
| --- | --- | --- |
| 破折号 (all variants: `—` `–` `―` `——` `――` `--`) | **≤ 6** total, ideally ≤ 3 | **delete** the dash, do not replace |
| 省略号 (`……` only) | **≤ 6** total, ideally ≤ 3 | **delete** the extra ellipsis |
| 引号 (dialogue + nested + scare-quotes combined) | **≤ 30** total, ideally ≤ 20 | **delete** the unnecessary quote |

Density is **per chapter**, not per scene. If a single dialogue-heavy scene is over budget, the user is expected to either trim quotes or split the scene.

### 3. Mark-specific rules

- **破折号 (dashes).** Only used for a true break in thought or a hard aside. Never as a stand-in for a comma, never as decorative flourishes, never as Markdown list markers in the draft. The only legitimate form is the em-dash `—` (or full-width `——` for emphasis). Variants like `–` (en-dash), `―` (horizontal bar), and `--` (double hyphen) are normalization errors and are replaced with `—` or deleted.
- **省略号 (ellipsis).** Only the 6-dot Chinese form `……` is allowed. The 3-dot `...` and the double-period `。。` are normalization errors and are normalized to `……` (or deleted if the chapter is over budget).
- **引号 (quotation marks).** Allowed for direct speech and for marking a term that is being defined in the chapter. Disallowed: nested quotes (`""…""`), scare-quotes for emphasis, quoting a phrase the narrator is using as a stylistic device. If a phrase doesn't need a quote to be readable, remove the quote.

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

- Line-start dash: keep (Markdown list marker — but see the Writing Style rule above: in the chapter draft itself, no line-start dashes are expected)
- Trailing dash at end of file/paragraph: **delete**
- Dash immediately before a closing quote (`"…—"`, `…—"`): **delete**
- Middle dash in any other context: **delete by default.** Do not replace with `，` — the goal is fewer showy marks, not different showy marks. The semantic replacement (tone particle / example / transition) only fires when the user has explicitly opted in via a `prose-style-exception` row in `09-review/decisions-log.md`.
- Variants (`–` en-dash, `―` horizontal bar, `——` full-width, `――` full-width alt, `--` double hyphen): normalize to `—` first, then apply the rules above. If the result is "delete", the variant is deleted.

### Ellipsis handling

- Three-dot form `...`: normalize to `……` (then apply budget check).
- Double-period `。。`: normalize to `……` (then apply budget check).
- Six-dot form `……`: keep, but counts against the per-chapter budget.
- If the chapter exceeds the budget, the script deletes the **earliest** occurrences (closest to the start) and reports which ones were dropped, so the user can see the most-needed ones were preserved.

### Quote handling

- Half-width quotes `"` `'` inside Chinese sentences: normalize to full-width `"` `'` `"` `'`.
- Nested quotes `"…"…"": delete the inner pair.
- Inconsistent left/right pairing: normalize.
- If the chapter exceeds the budget, the script deletes the **earliest** scare-quote occurrences (skipping direct dialogue).

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