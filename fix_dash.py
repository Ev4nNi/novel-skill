"""修复中文小说正文中的标点问题。

处理范围:
  - 双引号 + 逗号 -> 双引号
  - 句末多余逗号 (。，/！，/？，/；，/：，)
  - 行首逗号
  - 破折号 (em-dash — / en-dash – / horizontal bar ― / 连续 -- / 全角 ——):
      1. 行首破折号 -> 跳过 (Markdown 列表标记)
      2. 末尾破折号 (后面无字符) -> 删除
      3. 引号前的破折号 -> 删除
      4. 中间破折号 -> 按语义替换:
         - 语气词 (啊/哦/呀/呢/嘛/吧/唉/哼/嘿/哈/呵/嗯) 前后 -> ，
         - 补充/举例 (如/比如/例如/即/也就是) 前后 -> :
         - 转折 (但/可/却/然而/不过/只是) 前后 -> ;
         - 其它情况 -> ，

只扫描 06-chapter-drafts 下的 .md 文件。
"""

import os
import re

FOLDER = r'd:\programproject\novels\悬疑小说\06-chapter-drafts'

# 各种破折号变体
DASH_CHARS = ['——', '――', '—', '–', '―']
DASH_RE = re.compile(r'(——|――|—|–|―)')

# 行首破折号: 在行首 (可能有空白) 跟随空白
LINE_START_DASH_RE = re.compile(r'(?m)^\s*(——|――|—|–|―)\s')

# 末尾破折号: 破折号出现在字符串末尾 (允许尾随空白/换行)
TRAILING_DASH_RE = re.compile(r'(——|――|—|–|―)\s*$')

# 破折号紧贴左引号: "...内容—"  其中 " 为左/右中文双引号
DASH_BEFORE_QUOTE_RE = re.compile(r'(——|――|—|–|―)(["\u201d\u2019])')

# 语义判断词
TONE_WORDS = '啊哦呀呢嘛吧唉哼嘿哈呵嗯呜'
TRANSITION_WORDS = '但可却然而不过只是可惜'
EXAMPLE_WORDS = '如比如例如即也就是'


def classify_middle_dash(text_before: str, text_after: str) -> str:
    """根据破折号前后的内容决定替换为何种标点。

    返回: 替换标点 (单个字符), 或 '' 表示直接删除
    """
    after_stripped = text_after.lstrip()

    # 如果后面直接是引号 -> 已经在 DASH_BEFORE_QUOTE_RE 处理过, 这里不触发
    # 如果后面没有内容 -> 已经在 TRAILING_DASH_RE 处理过, 这里不触发

    # 语气词
    if after_stripped and after_stripped[0] in TONE_WORDS:
        return '，'
    if text_before and text_before[-1] in TONE_WORDS:
        return '，'

    # 补充/举例
    if after_stripped and after_stripped[0] in EXAMPLE_WORDS:
        return ':'
    if text_before and text_before[-1] in EXAMPLE_WORDS:
        return ':'

    # 转折
    if after_stripped and after_stripped[0] in TRANSITION_WORDS:
        return '；'
    if text_before and text_before[-1] in TRANSITION_WORDS:
        return '；'

    # 默认 -> 中文逗号
    return '，'


def fix_dash_in_text(s: str) -> tuple[str, dict]:
    """对单段文本执行破折号修复, 返回 (新文本, 统计)."""
    stats = {
        'trailing_deleted': 0,
        'before_quote_deleted': 0,
        'tone_replaced': 0,
        'example_replaced': 0,
        'transition_replaced': 0,
        'default_replaced': 0,
        'line_start_skipped': 0,
    }

    # 跳过行首破折号的位置
    line_start_positions = set()
    for m in LINE_START_DASH_RE.finditer(s):
        line_start_positions.add(m.start(1))
        stats['line_start_skipped'] += 1

    # 末尾破折号 -> 删除
    def _del_trailing(m: re.Match) -> str:
        stats['trailing_deleted'] += 1
        return ''
    s = TRAILING_DASH_RE.sub(_del_trailing, s)

    # 破折号在引号前 -> 删除
    def _del_before_quote(m: re.Match) -> str:
        if m.start(1) in line_start_positions:
            return m.group(0)
        stats['before_quote_deleted'] += 1
        return m.group(2)
    s = DASH_BEFORE_QUOTE_RE.sub(_del_before_quote, s)

    # 重新找行首位置 (前面的 sub 可能改变偏移, 不再有效, 用新一次扫描)
    line_start_positions = {m.start(1) for m in LINE_START_DASH_RE.finditer(s)}

    # 中间破折号 -> 按语义替换
    out_parts = []
    last = 0
    for m in DASH_RE.finditer(s):
        if m.start() in line_start_positions:
            continue
        out_parts.append(s[last:m.start()])
        before = s[max(0, m.start() - 5):m.start()]
        after = s[m.end():m.end() + 5]
        repl = classify_middle_dash(before, after)
        if repl == '，':
            stats['default_replaced'] += 1
        elif repl == ':':
            stats['example_replaced'] += 1
        elif repl == '；':
            stats['transition_replaced'] += 1
        out_parts.append(repl)
        last = m.end()
    out_parts.append(s[last:])
    s = ''.join(out_parts)

    return s, stats


def fix_punct_in_text(s: str) -> tuple[str, int]:
    """原有标点修复, 保持行为不变."""
    diff = 0
    pairs = [
        ('"，', '"'),
        ('，"', '"'),
        ('""，', '""'),
        ('，""', '""'),
        ('。，', '。'),
        ('！，', '！'),
        ('？，', '？'),
        ('；，', '；'),
        ('：，', '：'),
    ]
    for a, b in pairs:
        if a in s:
            n = s.count(a)
            diff += n * (len(a) - len(b))
            s = s.replace(a, b)
    before = s
    s = re.sub(r'\n，', '\n', s)
    diff += len(before) - len(s)
    return s, diff


def main() -> None:
    total_punct = 0
    total_dash_stats = {
        'trailing_deleted': 0,
        'before_quote_deleted': 0,
        'tone_replaced': 0,
        'example_replaced': 0,
        'transition_replaced': 0,
        'default_replaced': 0,
        'line_start_skipped': 0,
    }

    for f in sorted(os.listdir(FOLDER)):
        if not f.endswith('.md'):
            continue
        p = os.path.join(FOLDER, f)
        with open(p, 'r', encoding='utf-8') as fp:
            original = fp.read()

        s, punct_diff = fix_punct_in_text(original)
        s, dash_stats = fix_dash_in_text(s)

        if s == original:
            continue

        with open(p, 'w', encoding='utf-8') as fp:
            fp.write(s)

        total_punct += punct_diff
        for k, v in dash_stats.items():
            total_dash_stats[k] += v

        print(f'{f}: 标点修复 {punct_diff} 字符, 破折号处理 {sum(dash_stats.values())} 处')
        for k, v in dash_stats.items():
            if v:
                print(f'    - {k}: {v}')

    print(f'\n总计标点修复: {total_punct} 字符')
    print('总计破折号处理:')
    for k, v in total_dash_stats.items():
        if v:
            print(f'  - {k}: {v}')


if __name__ == '__main__':
    main()
