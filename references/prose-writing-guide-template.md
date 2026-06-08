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
- **Plot rhythm:** 句子长短交替。短句造紧张感，长句铺陈氛围。每段落必须至少包含一个≤8字的短句。
- **Consequence realism (no deus-ex-machina without setup):** 一切结果必须有前置因果。意外必须有铺垫，转折必须有征兆。
- **Character consistency (voice and behavior must match the character card):** 每个角色说话方式、行为习惯、思考角度必须与角色卡一致。两个角色互换台词后，读者应该能分辨出谁说的是什么。
- **Foreshadowing discipline (every payoff traces back to a logged setup):** 每个伏笔有来源记录。每个揭晓追溯回设置。禁止无中生有。
- **POV discipline (no head-hopping without chapter card approval):** 每章固定视角人物。禁止在同一场景内跳转视角。如需切换，必须用空行分隔并明确新视角人物。

## Hard Writing Rules (强制规则 — 非建议)

### 1. 展示而非告知（Show, Don't Tell）— 强制

这是本skill最核心的写作规则。AI倾向于"告知"，真人写作靠"展示"。违反本规则是AI腔调的第一来源。

**禁止直接陈述情绪或状态，必须用行为、细节、感官来表现。**

| 禁止（告知） | 必须改为（展示） |
|---|---|
| 他很紧张 | 他握紧杯柄，指节发白 |
| 她很伤心 | 她盯着桌上那滴水，看了很久 |
| 房间很乱 | 衣服堆在椅子上，床单一半垂在地上 |
| 天气很冷 | 窗玻璃结了薄霜，呼出的气变成白雾 |
| 他是个勇敢的人 | 刀架在他脖子上，他没眨眼 |
| 她很漂亮 | 她走进来时，桌上三双筷子同时停了 |

**强制规则：**
- 禁止使用"他感到X"、"她觉得X"、"他很X"等直接情绪标签（X=紧张、害怕、开心、愤怒、伤心等）
- 必须用**动作、表情、环境互动、生理反应**来替代
- 每300字内至少有一个具体的感官细节（视觉、听觉、触觉、嗅觉、味觉中的至少一种）

### 2. 角色声音差异化 — 强制

每个角色必须有独特的说话方式。如果遮住说话人的名字，读者应该能猜出是谁在说话。

**差异化维度（每个角色至少占2-3个）：**
- 句式长短：有人说话简短，有人喜欢长篇大论
- 口头禅/习惯用语：特定词汇或句式
- 语气词：有人用"嘛"、有人用"呢"、有人从不用语气词
- 称呼方式：直呼其名、用绰号、用敬语、用代词
- 是否喜欢打断别人说话
- 是否习惯用问句
- 是否喜欢用比喻或典故
- 说话前是否有动作（如先叹气、先咳嗽、先点烟）

**在写作前必须做的步骤：**
1. 阅读当前场景涉及的所有角色卡
2. 为每个角色在脑中确认至少2个声音特征
3. 写完后检查：遮住角色名，能否分辨出谁在说话？

### 3. AI腔调禁用词/句式 — 强制

以下词语和句式是AI写作的典型标记，**严禁在正文中使用**：

**禁用过渡词/时间词：**
- 就在这时、就在此时、就在这时侯
- 与此同时、同一时刻
- 话说回来、话分两头
- 突然、忽然（除非确实是瞬间发生的事，且有前后铺垫）
- 渐渐地、慢慢地（除非后面接具体动作，如"慢慢地把手伸进口袋"）

**禁用心理描写套话：**
- 他心想、她心想、她暗自想
- 不知为何、不知道为什么
- 一种X的感觉涌上心头（X=温暖、不安、恐惧等）
- 心中暗想、心里盘算着
- 隐隐约约觉得
- 莫名的（不安/熟悉感/预感）

**禁用比喻套话：**
- 仿佛/好像/宛如 + 抽象比喻（如"仿佛时间静止了"、"好像整个世界都崩塌了"）
- 如同 + 陈词滥调（如"如同一把刀割在心上"）
- X得像Y一样（如"快得像闪电"、"冷得像冰"）
- 用"仿佛"开头或结尾的段落

**禁用空洞描述：**
- 一切显得那么X（X=安静、美好、诡异等）
- 说不出的X感（X=熟悉、不安、诡异等）
- 令人X的X（X=难忘、震撼、恐惧等双形容词堆叠）
- 说不出的、难以言表的、无法形容的（既然无法形容就不要说）
- 格外、格外地、异常、异常地（空洞的程度副词）

**禁用对话引导词套话：**
- 他说道、她说道（用"说"即可，"说道"是AI腔调）
- 缓缓说道、轻声说道、淡淡地说（除非后面接具体动作支撑）
- 回答道、回应道（用"答"或直接写对话）

**禁止重复句式：**
- 同一章内，禁止连续3句以上以相同主语开头
- 禁止连续3句以上使用"他X了"句式
- 同一场景内，禁止重复使用同一个比喻或意象

### 4. 感官细节强制 — 强制

真人写作靠细节，AI写作靠概括。每段场景描写必须包含具体感官细节。

**硬性要求：**
- 每个新场景的**第一段**必须包含至少1个具体的感官细节（声音、气味、触感、光线变化等）
- 每500字内至少包含2个具体感官细节
- 细节必须是**具体的、可感知的**，不是抽象形容词

**细节层级（优先级从高到低）：**
1. 具体物象：茶杯上的裂纹、鞋底的泥、门把手的锈迹
2. 具体动作：手指在桌面上敲了三下、用指甲抠掉标签、把纸折了两次
3. 具体声音：远处狗叫了两声、鞋底摩擦地面的声音、钥匙转了两圈
4. 具体气味：霉味、油烟味、雨后的土腥味
5. 具体触感：粗糙的砂纸、黏腻的糖浆、冰凉的金属
6. 具体光线：台灯在墙上投下的影子、窗帘缝里的一缕光

**禁止用形容词堆砌代替细节：**
- ❌ "昏暗阴冷的房间"
- ✅ "墙角的灯罩裂了，灯泡忽明忽暗。窗缝里漏进来的风带着湿气。"

### 5. 句子节奏控制 — 强制

真人写作的句子长短不一，AI写作的句子长度趋于一致。节奏感是好小说的第一要素。

**强制规则：**
- 每段必须包含至少一个≤8字的短句
- 禁止连续3句以上长度相近（相差≤4字视为长度相近）
- 紧张场景：短句比例≥50%（制造急促感）
- 舒缓场景：长短交替，长句≤20字的句子占比≤40%
- 对话段落：对话本身算作一句，对话+动作说明的整体节奏也要变化

**节奏工具箱：**
- 紧张感：连续短句。"他听到了。脚步声。在楼梯上。"
- 沉重感：长句后接极短句。"他看着桌上那封信，信封是淡蓝色的，上面的字已经很模糊了，像是被水打湿过又被太阳晒干。信不是给他的。"
- 轻松感：中等长度句，夹杂口语化短句。
- 悬念感：用句号切断句子。"门开了。没有人。"

### 6. 对话改进规则 — 强制

对话是小说的灵魂。AI写的对话太直白，真人写的对话有潜台词。

**强制规则：**
- **潜台词优先：** 角色说的和想的不一样。"我没事"可能意味着"我快崩溃了"。对话不能100%传达角色的真实想法。
- **禁止信息直给：** 角色不应该像念说明书一样说话。信息应该通过对话的侧面、对话中的矛盾、对话中的停顿来传递。
- **动作打断对话：** 对话中必须穿插动作，不能纯对话连续超过5轮。每2-3轮对话必须有至少一个动作或环境描写插入。
- **对话引导词最小化：** 能用动作代替"他说"就不要用"他说"。
  - ❌ `"你来了。"他说。` → ✅ `他抬了抬眼皮。"你来了。"`
  - ❌ `"我知道。"她回答道。` → ✅ `她把杯子放下。"我知道。"`
- **对话不是问答机：** 角色可以答非所问、可以反问、可以沉默、可以用行动回答。
- **禁止用对话解释设定：** 设定信息应该通过角色的行动、环境的暗示来传递，而不是角色互相讲解。
- **对话必须有目的：** 每段对话必须至少达成一个：推动情节、揭示性格、制造冲突、传递信息（侧面）、建立/改变关系。纯闲聊除非用于特定目的（如拖延时间、试探），否则删除。

### 7. 场景切换与过渡 — 强制

**切换规则：**
- 场景切换必须用**空行**分隔
- 新场景的第一句必须明确时间和空间（通过具体细节，而非抽象说明）
  - ❌ "第二天早上"
  - ✅ "阳光从窗帘缝里照进来，桌上那杯隔夜茶已经凉了"
- 禁止用"与此同时"、"话分两头"等直接告诉读者要切换。让读者通过细节自己感知。

**过渡规则：**
- 时间跳跃用具体细节标记，不用抽象词
  - ❌ "三天后"
  - ✅ "日历上的红圈已经过了三个"
- 如果确实需要标明时间，用极简方式："三天后。"（句号，独立成段）

### 8. 具体细节优先 — 强制

**禁止空泛描述，必须用具体名词和动词。**

| 禁止（空泛） | 必须改为（具体） |
|---|---|
| 他拿起武器 | 他从墙上的皮鞘里抽出匕首 |
| 她穿得很好看 | 她穿了一件藏青色的旗袍，领口绣着银线 |
| 桌上放着食物 | 桌上有一碗面，汤面上漂着两片青菜叶 |
| 房间里有很多书 | 书架塞满了，地上还摞着两摞，最高的一摞快碰到窗台 |
| 他喝了一口 | 他端起碗，仰头灌了一大口，喉结上下动了动 |

**名词/动词优先于形容词/副词：**
- ❌ "他愤怒地关上了沉重的门"
- ✅ "他把门摔上，墙上的照片歪了"

**数字具体化：**
- ❌ "很多人" → ✅ "十七个人"
- ❌ "走了很远" → ✅ "走了三里地"
- ❌ "等了很久" → ✅ "香烧了一半"

### 9. 人工书写（manual handwriting），not Markdown

The chapter draft is a wall of prose a human typed on a page. It is **not** a structured document.

- No `**bold**`, `*italic*`, `_underline_`, `~~strike~~` for emphasis.
- No `#`, `##`, `###` headers in the body of the chapter.
- No `- bullets`, `* bullets`, `1. numbered lists`, `- [ ]` checklists.
- No `> blockquotes`, no `---` horizontal rules.
- No backticks for code spans, even when referring to a term — italicize the term by context, not by Markdown.
- If a list is structurally necessary, fold it into natural sentence flow ("三件事：他欠了钱、他撒了谎、他跑了。") — do not render it as a Markdown list.
- Blank lines are paragraph breaks. They are the **only** structural mark allowed in the draft.

Markdown structure belongs in the chapter card and the repair report, **never** in the chapter draft itself.

### 10. 破折号 / 省略号 — 严禁过多使用

These marks are the "showy" punctuation of Chinese prose. They are easy to over-use and hard to read when they pile up. The Punctuation Sweep enforces a strict per-chapter budget. If a chapter is over budget, the user must either edit the chapter or log a `prose-style-exception` row in `10-review/decisions-log.md`.

| Mark | Per-chapter budget (≈3000 words) | Default action when over budget |
| --- | --- | --- |
| 破折号 (all variants: `—` `–` `――` `――` `--`) | **≤ 6** total, ideally ≤ 3 | **delete** the dash, do not replace |
| 省略号 (`……` only) | **≤ 6** total, ideally ≤ 3 | **delete** the extra ellipsis |
| 中文字数 (Chinese character count) | ideal 2500-3500, acceptable 1500-5000 | **split or merge** the chapter |

Density is **per chapter**, not per scene.

The word count is a hard warning (not an exception-eligible style choice). It is a structural concern — chapters that are too short or too long are usually a sign of bad chapter boundaries, not a style preference.

### 11. 标点符号细则

- **破折号 (dashes).** Only used for a true break in thought or a hard aside. Never as a stand-in for a comma, never as decorative flourishes, never as Markdown list markers in the draft. The only legitimate form is the em-dash `—` (or full-width `——` for emphasis). Variants like `–` (en-dash), `―` (horizontal bar), and `--` (double hyphen) are normalization errors and are replaced with `—` or deleted.
- **省略号 (ellipsis).** Only the 6-dot Chinese form `……` is allowed. The 3-dot `...` and the double-period `。。` are normalization errors and are normalized to `……` (or deleted if the chapter is over budget).

### 12. 章节标题（首行，强制）

Every chapter draft MUST start with a title line. This is the only structural exception to the "no Markdown in the body" rule.

- **Format:** `第N章"title"` — e.g. `第一章"雨夜来客"`, `第十二章"迷宫"`, `第一百零三章"重逢"`.
- `第N章` uses **Chinese numerals** (一/二/三/…/十/百/千/零/〇). Arabic numerals (`第1章`) are not allowed in the title line.
- The title text must be wrapped in **quotes** (any type accepted). Supported: Chinese double `""`, Chinese single `''`, English double `"`, English single `'`. The opening quote comes immediately after `章` (no space). The closing quote comes immediately after the last character of the title.
- The title is the **only** content on the first line. No leading whitespace, no trailing punctuation after the closing quote, no Markdown hash header.
- If the first line is missing or does not match this format, the Punctuation Sweep flags it as a hard error. **No exception allowed** — the title is mandatory and the chapter is invalid without it.

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
- **角色声音特征确认：** 每个出场角色的2-3个声音差异化特征已确认
- **感官细节计划：** 当前场景需要的具体感官细节已规划（至少3个）

## Drafting Rules
- Keep character voice consistent with the character card
- Respect world rules and costs (no rule invented in the chapter)
- Do not skip chapter-card obligations
- Do not invent major setting changes without user confirmation
- If a new setting rule emerges, log it for lore-index update
- If a new foreshadowing is planted, log it in `03-plot/foreshadowing.md` before ending the chapter
- **每写完一段，检查：** 是否有告知替代了展示？是否有AI腔调词？是否所有细节都具体化了？

## Post-Draft Self-Check (Micro-Repair前置自检)

在运行Micro-Repair之前，必须对正文做以下自检：

1. **展示vs告知检查：** 逐段检查，是否有任何"他很X"、"她感到X"的直接情绪陈述？如有，改为动作/细节/感官。
2. **AI腔调检查：** 全文搜索禁用词清单中的词语（就在这时、与此同时、他心想、仿佛、莫名的等），全部删除或改写。
3. **角色声音检查：** 遮住角色名字，能否分辨每段对话是谁说的？如果不能，增加声音差异化。
4. **感官细节检查：** 每500字是否包含至少2个具体感官细节？如不足，补充。
5. **句子节奏检查：** 是否有连续3句以上长度相近？是否有连续3句以上同一主语开头？如有，改写。
6. **对话检查：** 是否有纯对话连续超过5轮？对话是否有潜台词？是否有角色像念说明书一样解释设定？如有，改写。
7. **具体化检查：** 是否有空泛描述（如"武器"、"食物"、"很好看"）？改为具体名词。

## Post-Draft Checklist (Micro-Repair input)
- Character files updated if any state changed
- Foreshadowing tracker updated (plant / payoff / status)
- Reveals tracker updated if a reveal happened
- Timeline updated if chronology changed
- Lore-index updated if a new term / place / item appeared
- `00-project/progress.md` updated
- `10-review/decisions-log.md` updated

## Punctuation Rules (enforced by Punctuation Sweep)

The skill runs `scripts/check_dash.py` and `scripts/fix_dash.py` against `06-chapter-drafts/` after every chapter draft. The rules below MUST match what the scripts apply. If you change these rules, update the scripts in the same commit and log a `prose-guide-update` event in `10-review/decisions-log.md`.

### Dash handling

- Line-start dash: keep (Markdown list marker — but see the Writing Style rule above: in the chapter draft itself, no line-start dashes are expected)
- Trailing dash at end of file/paragraph: **delete**
- Dash immediately before a closing quote (`"…—"`, `…—"`): **delete**
- Middle dash in any other context: **delete by default.** Do not replace with `，` — the goal is fewer showy marks, not different showy marks. The semantic replacement (tone particle / example / transition) only fires when the user has explicitly opted in via a `prose-style-exception` row in `10-review/decisions-log.md`.
- Variants (`–` en-dash, `―` horizontal bar, `——` full-width, `――` full-width alt, `--` double hyphen): normalize to `—` first, then apply the rules above. If the result is "delete", the variant is deleted.

### Ellipsis handling

- Three-dot form `...`: normalize to `……` (then apply budget check).
- Double-period `。。`: normalize to `……` (then apply budget check).
- Six-dot form `……`: keep, but counts against the per-chapter budget.
- If the chapter exceeds the budget, the script deletes the **earliest** occurrences (closest to the start) and reports which ones were dropped, so the user can see the most-needed ones were preserved.

### Quote handling

- Half-width quotes `"` `'` inside Chinese sentences: acceptable. The scripts no longer force-convert half-width to full-width.
- Supported quote types: 中文双引号 `""` (`\u201c` `\u201d`), 中文单引号 `''` (`\u2018` `\u2019`), 英文双引号 `"`, 英文单引号 `'`. All are treated equally.
- Nested quotes: delete the inner pair.
- Inconsistent left/right pairing: normalize.

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
- **风格漂移检查：** 检查正文中是否有新的AI腔调词出现，如有，补充到禁用词清单

## Project-Level Repair Rule

After the final volume completes, run a Project Repair:

- Cross-volume foreshadowing close-out
- Character arc end-state confirmation
- Theme payoff audit
- Final timeline and lore-index pass
````