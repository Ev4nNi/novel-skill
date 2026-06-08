# Phase 00 — Overview (Cross-Phase Rules)

This file contains rules that apply across all phases. It is read **before every phase** alongside the current phase file.

## Core Principles

1. **8 phases, not freeform.** Every project passes through `spark -> positioning -> world -> characters -> master-outline -> volume -> chapter -> prose`.
2. **One phase at a time.** Never produce output for a later phase before the current phase is confirmed.
3. **Pre-checks before generation.** Before generating a volume card or a chapter card, re-read the relevant setting files and write a recap (Pre-Volume Review / Pre-Chapter Brief).
4. **Two-tier repair.** Run a Micro-Repair after every chapter, and a Volume Repair after every volume.
5. **Decisions are logged.** Every stage confirmation, conflict resolution, and skip/rollback is recorded in `10-review/decisions-log.md` with a timestamp.
6. **Continuity is enforced.** A change to setting/character/plot requires the matching file update before drafting the next chapter.
7. **Skip and rollback are explicit.** If the user wants to jump or fall back, log the reason and impact in the decision log.
8. **The prose guide is mandatory.** `00-project/正文写作指南.md` must exist before any chapter draft is written.

## Hard Style Rules (read before every draft)

These are non-negotiable. They shape how every chapter is drafted.

1. **人工书写 (manually written), not Markdown.** No bullet lists, no bold/italic for emphasis, no headers, no inline code spans, no `>` blockquotes, no horizontal rules.
2. **Markdown structure belongs in the chapter card and the repair report, never in the chapter draft itself.** Use blank lines only for paragraph breaks.
3. **破折号 is 严禁过多使用.** Default action for any middle dash is **delete**, not replace.
4. **省略号 is 严禁过多使用.** Only `……` is valid. Default action is **delete**, not replace.
5. **引号 is 严禁过多使用.** Disallowed: nested quotes, scare-quotes, quoting common words.
6. **Density is enforced by the Punctuation Sweep.** If a chapter is over budget, the user must edit or log a `prose-style-exception` row.
7. **These rules are part of the prose guide.** When the prose guide is created or updated, these rules MUST be copied into it.
8. **The first line of every chapter draft is the title.** Format: `第N章"title"` (Chinese numerals, quotes of any type accepted: Chinese double/single, English double/single). Missing or invalid title = hard error, no exception.

### Quality Rules (正文质量强制规则)

These rules govern writing quality, not formatting. They are equally non-negotiable. See `references/prose-writing-guide-template.md` for the full specification.

**Q1. 展示而非告知（Show, Don't Tell）：** 禁止直接陈述情绪或状态（"他很紧张"、"她感到害怕"），必须用动作、表情、感官细节来表现。这是消除AI腔调的第一规则。

**Q2. 角色声音差异化：** 每个角色必须有2-3个独特的说话特征（句式长短、口头禅、语气词、称呼方式等）。遮住角色名后，读者应能分辨谁在说话。

**Q3. AI腔调禁用词：** 严禁使用"就在这时"、"与此同时"、"他心想"、"仿佛"、"莫名的"、"说不出的"等AI典型标记词。详见正文写作指南的禁用词清单。

**Q4. 感官细节强制：** 每个新场景第一段必须有至少1个具体感官细节。每500字至少2个。细节必须具体可感知，禁止形容词堆砌。

**Q5. 句子节奏控制：** 禁止连续3句以上长度相近。每段必须包含至少一个≤8字短句。紧张场景短句≥50%。

**Q6. 对话质量：** 对话必须有潜台词。禁止纯对话连续超过5轮（必须穿插动作）。禁止用对话解释设定。禁止"他说道"等AI式对话引导词。

**Q7. 场景过渡：** 新场景第一句必须用具体细节标记时空，禁止"第二天早上"、"与此同时"等抽象说明。

**Q8. 具体细节优先：** 禁止空泛名词（"武器"、"食物"）和空泛副词（"格外"、"异常"）。必须用具体名词和动词。

**Q9. 代词去重：** 禁止同一段内连续3次以上同一代词开头（"他站起来。他走到门口。他打开门。"）。能省略就省略，或用名字/身份/动作替代代词。

> Reminder: "Default" punctuation actions prefer **delete** over **replace**. The goal is fewer showy marks, not just different showy marks.

## Two-Tier Repair System

| Level | Trigger | Output | Files to update |
| --- | --- | --- | --- |
| Micro-Repair | After every chapter draft | `10-review/micro-reports/Chapter-XXX-repair.md` | character / worldbuilding / foreshadowing / timeline / lore-index / progress |
| Volume Repair | After every volume completes | `10-review/volume-reports/Volume-XX-repair.md` | master-outline / foreshadowing / reveals / timeline / lore-index / 正文写作指南 (if rhythm changes) |
| Project Repair | After all volumes complete (optional) | `10-review/project-repair.md` | every file |

Skipping a Micro-Repair blocks the next chapter. Skipping a Volume Repair blocks the next volume's Pre-Volume Review.

## File Update Timing

File updates are **event-driven, not continuous**. Only update when an event fires, and log the event.

| File | Create | Update (event-driven) | Review (passive) | Reference while |
| --- | --- | --- | --- | --- |
| `00-project/spark.md` | Phase 0 | Skip/rollback to Phase 0 | — | every later phase |
| `00-project/positioning.md` | Phase 1 | Phase 1 confirmation revision | — | every later phase |
| `01-worldbuilding/*` | Phase 2 | Micro-Repair (only if this chapter changes a world rule) | Volume Repair (whole-volume integrity) | Pre-Volume Review; Pre-Chapter Brief; Prose |
| `02-characters/*` | Phase 3 | Micro-Repair (only if this chapter changes a character state) | Volume Repair (arc integrity) | Pre-Chapter Brief; Prose |
| `03-plot/master-outline.md` | Phase 4 | **Contract — only on Phase 4 → 5 rollback**; never on whim. | Volume Repair (does the volume still serve the spine?) | Pre-Volume Review; Volume Repair |
| `03-plot/foreshadowing.md` | Phase 4 | **Every** Micro-Repair that plants or pays off a foreshadowing item | Volume Repair (density & balance) | Pre-Chapter Brief; Prose; Micro-Repair |
| `03-plot/reveals.md` | Phase 4 | Micro-Repair that fires a reveal | Volume Repair (pacing) | Pre-Chapter Brief; Prose |
| `03-plot/timeline.md` | Phase 4+ | Micro-Repair (if this chapter is on the timeline) | Volume Repair (sequence check) | Pre-Chapter Brief; Prose |
| `04-volumes/Volume-XX.md` | Phase 5 | Only by Phase 5 rollback | — | Pre-Chapter Brief; Prose |
| `05-chapter-cards/Chapter-XXX.md` | Phase 6 | Only by Phase 6 rollback | — | Prose |
| `06-chapter-drafts/Chapter-XXX.md` | Phase 7 | Punctuation Sweep → Micro-Repair | — | next chapter's Pre-Chapter Brief |
| `00-project/正文写作指南.md` | Before first Phase 7 draft | Volume Repair (if style drift detected) | Volume Repair | **Every** Prose draft (mandatory) |
| `10-review/micro-reports/Chapter-XXX-repair.md` | After every chapter (mandatory) | Append-only | — | **Next chapter's Pre-Chapter Brief (mandatory)** |
| `10-review/volume-reports/Volume-XX-repair.md` | After every volume (mandatory) | Append-only | — | next volume's Pre-Volume Review |
| `10-review/project-repair.md` | After all volumes (optional) | Append-only | — | final pass |
| `10-review/decisions-log.md` | At project start | **Append** on every event below | — | always |
| `00-project/progress.md` | At project start | Every phase advance, repair completion, skip/rollback | — | always |

### Decision Log Trigger Events

Append a row on **any** of the following (append-only; never rewrite history):

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

The **previous chapter's micro-repair report** is the source of truth for "where the world is right now". Read it in **both** Pre-Chapter Brief and Prose draft. The prose guide is style rules and is read **only** during Prose draft.

## Skip & Rollback Rules

**Skip (jump forward):**

- Allowed only if the target phase's prerequisites are already on disk.
- Must log: source phase, target phase, reason, impacted files.
- Must run a verification pass on the skipped phases before continuing.

**Rollback (jump backward):**

- Allowed any time.
- Must log: current phase, target phase, reason.
- Must run a regression pass: read everything produced after the target phase and flag any content that needs to be re-checked.

Both actions must update `00-project/progress.md`.

## References Index

| Template | Use |
| --- | --- |
| `references/spark-template.md` | Phase 0 spark capture |
| `references/positioning-template.md` | Phase 1 project positioning |
| `references/worldbuilding-template.md` | Phase 2 worldbuilding files |
| `references/character-template.md` | Phase 3 character cards |
| `references/master-outline-template.md` | Phase 4 master outline |
| `references/foreshadowing-template.md` | Phase 4 foreshadowing tracker |
| `references/reveals-template.md` | Phase 4 reveals tracker |
| `references/timeline-template.md` | Phase 4+ timeline events |
| `references/pre-volume-review-template.md` | Phase 5 pre-volume recap |
| `references/volume-template.md` | Phase 5 volume card |
| `references/volume-repair-template.md` | Phase 5 volume repair |
| `references/pre-chapter-brief-template.md` | Phase 6 pre-chapter brief |
| `references/chapter-template.md` | Phase 6 chapter card |
| `references/prose-writing-guide-template.md` | Phase 7 prose guide (mandatory) |
| `references/micro-repair-template.md` | Phase 7 micro-repair |
| `references/decisions-log-template.md` | decision log entry format |
| `references/progress-template.md` | `00-project/progress.md` tracker |
