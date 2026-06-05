# Punctuation Sweep

The Punctuation Sweep is the first step of every Micro-Repair. It enforces the punctuation rules declared in `00-project/正文写作指南.md`.

## Scripts

Two helper scripts live at the novel-skill repo root:

- `check_dash.py` — read-only. Prints every punctuation issue with a fix suggestion and a context snippet. Does not modify files.
- `fix_dash.py` — read-write. Applies fixes in place. Idempotent (running it twice does nothing on the second run).

Both scripts operate on `d:\programproject\novels\悬疑小说\06-chapter-drafts\` by default. Adjust the `FOLDER` constant at the top of each script for a different project.

## Workflow

After saving a chapter draft to `06-chapter-drafts/Chapter-XXX.md`:

```bash
# 1. Inspect
python check_dash.py

# 2. Review the report with the user.
#    Pay special attention to "default-replaced" middle-dash cases.

# 3. Apply fixes
python fix_dash.py

# 4. Re-inspect to confirm clean
python check_dash.py
# expect: "共发现 0 个问题"

# 5. Record the sweep stats in the micro-repair report
```

## What the Scripts Catch

| Issue | Detection | Fix |
| --- | --- | --- |
| em-dash `—`, en-dash `–`, horizontal bar `―`, full-width `——`, double `--` | every occurrence | context-dependent (see below) |
| Duplicate commas `，，` | substring match | collapse to `，` |
| Terminal-comma `。，` `！，` `？，` `；，` `：，` | substring match | drop the comma |
| Leading-line comma `\n，` | regex | drop the comma |

## Middle-Dash Semantic Replacement

A middle dash is one that is **not** at the start of a line, **not** at the end of a file/paragraph, and **not** immediately before a closing quote. For middle dashes, the script reads up to 5 characters before and after to classify the context:

| Context word (preceding or following) | Replaced with | Examples |
| --- | --- | --- |
| tone particle (`啊 哦 呀 呢 嘛 吧 唉 哼 嘿 哈 呵 嗯 呜`) | `，` | `我——啊` -> `我，啊` |
| example / clarification (`如 比如 例如 即 也就是`) | `:` | `符号——意思是` -> `符号:意思是` |
| transition (`但 可 却 然而 不过 只是 可惜`) | `；` | `他没说话——但` -> `他没说话；但` |
| default | `，` | everything else |

**Always confirm the "default" cases with the user.** They are the most likely to need a different choice (e.g. a longer pause, a question mark, or a literal dash preserved for stylistic effect).

## Line-Start Dashes

A dash at the start of a line is treated as a Markdown list marker and is left alone. If the user is using a line-start dash for narrative dialogue (a non-standard but possible choice), the user must mark it explicitly or move it into the body of the line — the script will not detect this automatically.

## Idempotence

`fix_dash.py` is safe to run multiple times. After a successful sweep, a second run should print zero or near-zero changes (only if the user manually added new issues between runs).

## What the Scripts Do Not Catch

- Half-width punctuation inside Chinese sentences (e.g. `中文, 标点`)
- Spacing around punctuation
- Inconsistent quotation marks (`"` vs `"` vs `"`)
- Style issues (over-using 顿号 `、` where 逗号 `，` is more appropriate)
- 章节标题或元数据的格式问题

These are not currently automated. Add them to this file when extending the scripts.

## Updating the Rules

If the user wants to change a rule (e.g. "default replacement becomes `；` instead of `，`"), the change must be applied in **two places in lock-step**:

1. The `classify_middle_dash` function in `fix_dash.py`
2. The corresponding row in `references/prose-writing-guide-template.md` (which the user copies into `00-project/正文写作指南.md`)

Then append a `prose-guide-update` row to `09-review/decisions-log.md`.
