# Punctuation Sweep

The Punctuation Sweep is the first step of every Micro-Repair. It enforces the punctuation and style rules declared in `00-project/正文写作指南.md` and in the Hard Style Rules section of `SKILL.md`.

## Scripts

Two helper scripts live in `scripts/` (relative to the novel-skill repo root):

- `scripts/check_dash.py` — quick sweep. Read-only. Prints every punctuation issue with a fix suggestion and a context snippet, plus a per-chapter density table at the end. Also reports word count and title validity.
- `scripts/fix_dash.py` — read-write. Applies fixes in place. Idempotent (running it twice does nothing on the second run). Outputs a post-fix density table. Reports word count and title warnings.

Both scripts operate on `06-chapter-drafts/` (relative to the current working directory) by default. Pass a different folder as the first CLI argument to override. The user is expected to run the scripts from the novel project root (so that `06-chapter-drafts/` is the chapter folder of the project being worked on).

## What the Scripts Enforce

The Punctuation Sweep enforces **two kinds of rules**: shape rules (format) and density rules (count).

### Shape Rules

| Issue | Detection | Fix |
| --- | --- | --- |
| em-dash `—`, en-dash `–`, horizontal bar `―`, full-width `——`/ `――`, double `--` | every occurrence | normalize variants to `—`, then apply middle-dash rule (see below) |
| ellipsis forms: `...` `。。` `……` `\u2026` | every occurrence | normalize to `……` |
| duplicate commas `，，` | substring match | collapse to `，` |
| terminal-comma `。，` `！，` `？，` `；，` `：，` | substring match | drop the comma |
| leading-line comma `\n，` | regex | drop the comma |
| Markdown structural marks: `**bold**` `*italic*` `__` `_` `# headers` `- lists` `> blockquotes` `` `code` `` `---` | regex per pattern | **flag only, do not auto-fix** (user must edit) |

### Density Rules (per chapter, ~3000 words)

| Mark | Budget | Action when over budget |
| --- | --- | --- |
| 破折号 (all variants) | ≤ 6 (ideal ≤ 3) | flag, request edit or `prose-style-exception` row |
| 省略号 (`……` only) | ≤ 6 (ideal ≤ 3) | auto-delete earliest occurrences, report |
| Markdown structural marks in body | 0 | flag only, user must edit |

## Middle-Dash Default: DELETE (Strict Mode)

The default action for a middle dash in any context is **delete**, not replace. This is a hard rule from the project style. The previous "semantic replacement" behavior (replace with `，` `；` `:`) is now gated by a `SEMANTIC_REPLACE` flag in both `scripts/check_dash.py` and `scripts/fix_dash.py`:

- `SEMANTIC_REPLACE = False` (default): every middle dash is deleted
- `SEMANTIC_REPLACE = True`: middle dashes are replaced based on the surrounding context (tone particle → `，`, example/clarification → `:`, transition → `；`, default → delete)

If the user wants to opt in to semantic replacement, set the flag to `True` in both `scripts/check_dash.py` and `scripts/fix_dash.py` and log a `prose-style-exception` row in `10-review/decisions-log.md`. The decision log row is required — silent opt-in is not allowed.

## Word Count (硬警告)

Each chapter should fall within these thresholds (counted as Chinese characters in CJK Unified Ideographs):

| Bucket | Chinese character count | Status |
| --- | --- | --- |
| 理想 (ideal) | 2500-3500 | OK |
| 允许范围 (acceptable) | 1500-5000 | 可接受 (low / high) |
| 低于最小 | < 1500 | 硬警告 — 章节过短, 考虑合并相邻章节 |
| 高于最大 | > 5000 | 硬警告 — 章节过长, 考虑拆分 |

Out-of-range chapters are reported as `[HARD WARNING]` by `check_dash.py`. `fix_dash.py` does **not** auto-fix word count — it must be done by editing the chapter (split or merge). The event is logged in `10-review/decisions-log.md` as a `chapter-length` row.

## Title Validity (硬错误)

The first line of every chapter draft MUST match the format `第N章"title"` where `N` uses Chinese numerals (一/二/三/…/十/百/千/零/〇) and the title is wrapped in full-width Chinese quotes `""`. Examples:

- Valid: `第一章"雨夜来客"`, `第十二章"迷宫"`, `第一百零三章"重逢"`
- Invalid: `第一章 雨夜来客` (no quotes), `第一章 "雨夜来客"` (space), `第1章"雨夜来客"` (Arabic), `# 第一章"雨夜来客"` (Markdown header)

A missing or invalid title is reported as `[HARD ERROR]` by both scripts. No exception is allowed — the title is mandatory. The scripts do not auto-fix it; the user must edit the chapter.

## Workflow

After saving a chapter draft to `06-chapter-drafts/Chapter-XXX.md`:

```bash
# 1. Quick sweep
python scripts/check_dash.py
#    - prints every issue with a fix suggestion
#    - prints title status (OK / NO)
#    - prints word count and the density table at the end
#    - any row marked [ERR] is a title hard error (no exception)
#    - any row marked [!LEN] is a word-count hard warning (split or merge)
#    - any row marked [!] is over density budget (edit or exception)

# 2. Review the report with the user
#    - pay attention to title and word-count warnings
#    - for density warnings, the user must either:
#      a) edit the chapter to bring counts under budget, OR
#      b) append a prose-style-exception row to `10-review/decisions-log.md`
#    - for title errors, the user MUST edit (no exception allowed)
#    - for Markdown structural marks in the body, the user MUST edit

# 3. Apply fixes
python scripts/fix_dash.py
#    - title errors: NOT auto-fixed; user must edit
#    - word-count warnings: NOT auto-fixed; user must split/merge
#    - punctuation: auto-fixed in place (idempotent)

# 4. Re-inspect to confirm clean
python scripts/check_dash.py
#    - the density table should now show no [!] / [ERR] / [!LEN] flags, OR
#    - the remaining flags are covered by a logged prose-style-exception

# 5. Record the sweep stats in the micro-repair report
#    - use the new "Style Density Check" block in micro-repair-template.md
```

## Line-Start Dashes

A dash at the start of a line is treated as a Markdown list marker and is left alone by the dash handler. **However, the chapter draft itself is supposed to contain no Markdown structural marks at all** (see Hard Style Rules in `SKILL.md`). If a line-start dash appears in `06-chapter-drafts/`, it is almost certainly a bug in the draft and the user should fix it manually.

## Idempotence

`scripts/fix_dash.py` is safe to run multiple times. After a successful sweep, a second run should report zero changes (only `variants_normalized` may show small numbers for non-standard inputs).

## What the Scripts Do Not Catch (manual review needed)

- Half-width punctuation inside Chinese sentences OTHER than quotes (e.g. `中文, 标点` — fix_dash only handles comma pairs, not free-floating ASCII commas)
- Spacing around punctuation (full-width vs half-width spaces)
- Tone of dialogue matching the character card (style, not shape)
- Tone of description (句式节奏, 视角)
- "Showy" words beyond the three marks — the skill relies on the user + Volume Repair for this
- Nested quote patterns where 4 quotes span more than 30 characters (the conservative auto-detection skips these; the user must edit)
- Word count itself — `fix_dash.py` does not split or merge chapters; the user must edit the chapter boundaries

These are not currently automated. Add them to this file when extending the scripts.

## Updating the Rules

If the user wants to change a rule (e.g. "default middle-dash behavior becomes replace, not delete"), the change must be applied in **four places in lock-step**:

1. The `classify_middle_dash` function (or its caller) in `scripts/check_dash.py` and `scripts/fix_dash.py`
2. The constants (`SEMANTIC_REPLACE`, `MIN_CHARS`, `MAX_CHARS`) in `scripts/check_dash.py` (which `fix_dash.py` imports)
3. The `Hard Style Rules` and `Writing Style` sections in `SKILL.md` and `prose-writing-guide-template.md`
4. Append a `prose-guide-update` row to `10-review/decisions-log.md`

The same rule must also be reflected in the `## Punctuation Rules` and `## Word Count` sections of the user's own `00-project/正文写作指南.md` file.
