# Punctuation Sweep

The Punctuation Sweep is the first step of every Micro-Repair. It enforces the punctuation and style rules declared in `00-project/正文写作指南.md` and in the Hard Style Rules section of `SKILL.md`.

## Scripts

Two helper scripts live at the novel-skill repo root:

- `check_dash.py` — read-only. Prints every issue with a fix suggestion and a context snippet. Does not modify files. Outputs a per-chapter density table at the end.
- `fix_dash.py` — read-write. Applies fixes in place. Idempotent (running it twice does nothing on the second run). Outputs a post-fix density table.

Both scripts operate on `d:\programproject\novels\悬疑小说\06-chapter-drafts\` by default. Adjust the `FOLDER` constant at the top of each script for a different project.

## What the Scripts Enforce

The Punctuation Sweep enforces **two kinds of rules**: shape rules (format) and density rules (count).

### Shape Rules

| Issue | Detection | Fix |
| --- | --- | --- |
| em-dash `—`, en-dash `–`, horizontal bar `―`, full-width `——`/ `――`, double `--` | every occurrence | normalize variants to `—`, then apply middle-dash rule (see below) |
| ellipsis forms: `...` `。。` `……` `\u2026` | every occurrence | normalize to `……` |
| half-width quotes `"` `'` inside Chinese text | substring match | swap to full-width `"` `"` (left/right by occurrence order) |
| nested quotes (4 quotes within 30 chars) | positional scan | delete the inner pair |
| duplicate commas `，，` | substring match | collapse to `，` |
| terminal-comma `。，` `！，` `？，` `；，` `：，` | substring match | drop the comma |
| leading-line comma `\n，` | regex | drop the comma |
| Markdown structural marks: `**bold**` `*italic*` `__` `_` `# headers` `- lists` `> blockquotes` `` `code` `` `---` | regex per pattern | **flag only, do not auto-fix** (user must edit) |

### Density Rules (per chapter, ~3000 words)

| Mark | Budget | Action when over budget |
| --- | --- | --- |
| 破折号 (all variants) | ≤ 6 (ideal ≤ 3) | flag, request edit or `prose-style-exception` row |
| 省略号 (`……` only) | ≤ 6 (ideal ≤ 3) | auto-delete earliest occurrences, report |
| 引号 (dialogue + nested + scare) | ≤ 30 (ideal ≤ 20) | flag only, do not auto-delete (avoid breaking dialogue) |
| Markdown structural marks in body | 0 | flag only, user must edit |

## Middle-Dash Default: DELETE (Strict Mode)

The default action for a middle dash in any context is **delete**, not replace. This is a hard rule from the project style. The previous "semantic replacement" behavior (replace with `，` `；` `:`) is now gated by a `SEMANTIC_REPLACE` flag in both scripts:

- `SEMANTIC_REPLACE = False` (default): every middle dash is deleted
- `SEMANTIC_REPLACE = True`: middle dashes are replaced based on the surrounding context (tone particle → `，`, example/clarification → `:`, transition → `；`, default → delete)

If the user wants to opt in to semantic replacement, set the flag to `True` in both `check_dash.py` and `fix_dash.py` and log a `prose-style-exception` row in `09-review/decisions-log.md`. The decision log row is required — silent opt-in is not allowed.

## Workflow

After saving a chapter draft to `06-chapter-drafts/Chapter-XXX.md`:

```bash
# 1. Inspect
python check_dash.py
#    - prints every issue with a fix suggestion
#    - prints a per-chapter density table at the end
#    - any row marked [!] in the density table is over budget

# 2. Review the report with the user
#    - pay attention to density warnings
#    - if any chapter is over budget, the user must either:
#      a) edit the chapter to bring counts under budget, OR
#      b) append a prose-style-exception row to 09-review/decisions-log.md
#    - for Markdown structural marks in the body, the user MUST edit (no exception allowed)

# 3. Apply fixes
python fix_dash.py

# 4. Re-inspect to confirm clean
python check_dash.py
#    - the density table should now show no [!] flags, OR
#    - the remaining [!] rows are covered by a logged prose-style-exception

# 5. Record the sweep stats in the micro-repair report
#    - use the new "Style Density Check" block in micro-repair-template.md
```

## Line-Start Dashes

A dash at the start of a line is treated as a Markdown list marker and is left alone by the dash handler. **However, the chapter draft itself is supposed to contain no Markdown structural marks at all** (see Hard Style Rules in `SKILL.md`). If a line-start dash appears in `06-chapter-drafts/`, it is almost certainly a bug in the draft and the user should fix it manually.

## Idempotence

`fix_dash.py` is safe to run multiple times. After a successful sweep, a second run should report zero changes (only `variants_normalized` may show small numbers for non-standard inputs).

## What the Scripts Do Not Catch (manual review needed)

- Half-width punctuation inside Chinese sentences OTHER than quotes (e.g. `中文, 标点`)
- Spacing around punctuation (full-width vs half-width spaces)
- Tone of dialogue matching the character card (style, not shape)
- Tone of description (句式节奏, 视角)
- "Showy" words beyond the three marks — the skill relies on the user + Volume Repair for this
- Nested quote patterns where 4 quotes span more than 30 characters (the conservative auto-detection skips these; the user must edit)

These are not currently automated. Add them to this file when extending the scripts.

## Updating the Rules

If the user wants to change a rule (e.g. "default middle-dash behavior becomes replace, not delete"), the change must be applied in **three places in lock-step**:

1. The `classify_middle_dash` function (or its caller) in `check_dash.py` and `fix_dash.py`
2. The `Hard Style Rules` and `Writing Style` sections in `SKILL.md` and `prose-writing-guide-template.md`
3. Append a `prose-guide-update` row to `09-review/decisions-log.md`

The same rule must also be reflected in the `## Punctuation Rules` section of the user's own `00-project/正文写作指南.md` file.
