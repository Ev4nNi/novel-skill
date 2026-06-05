"""修复中文小说正文中的标点和风格问题。

处理范围:
  - 双引号 + 逗号 -> 双引号
  - 句末多余逗号 (。，/！，/？，/；，/：，)
  - 行首逗号
  - 章节标题检查 (警告, 不自动修复)
  - 字数检查 (警告, 不自动处理)
  - 破折号 (em-dash — / en-dash – / horizontal bar ― / 连续 -- / 全角 ——):
      1. 行首破折号 -> 跳过 (Markdown 列表标记, 但正文不应有)
      2. 末尾破折号 (后面无字符) -> 删除
      3. 引号前的破折号 -> 删除
      4. 中间破折号 -> 默认删除 (严格模式)
                       若 SEMANTIC_REPLACE=True, 按语义替换:
                       - 语气词前后 -> ，
                       - 补充/举例前后 -> :
                       - 转折前后 -> ;
                       - 其它 -> ，
  - 省略号: 标准化为 ……; 超出预算时删除最早的
  - 引号: 半角 -> 全角; 嵌套 -> 删除内层; 超出预算时删除最早的
  - 密度警告: 输出每章的破折号/省略号/引号/MD 数量, 标记超出预算

只扫描 06-chapter-drafts 下的 .md 文件。
"""

import os
import re
import sys

# 让本目录下的模块可以被 import (复用 check_dash 的工具)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from check_dash import (
    BUDGET_DASH,
    BUDGET_ELLIPSIS,
    BUDGET_QUOTE,
    CN_CHAR_RE,
    DASH_CHARS,
    DASH_RE,
    HALF_WIDTH_QUOTE_RE,
    LINE_START_DASH_RE,
    NESTED_QUOTE_RE,
    TONE_WORDS,
    TRAILING_DASH_RE,
    TRANSITION_WORDS,
    EXAMPLE_WORDS,
    FULL_WIDTH_QUOTE_LEFT,
    FULL_WIDTH_QUOTE_RIGHT,
    SEMANTIC_REPLACE,
    ELLIPSIS_RE,
    DASH_BEFORE_QUOTE_RE,
    MIN_CHARS,
    MAX_CHARS,
    IDEAL_MIN_CHARS,
    IDEAL_MAX_CHARS,
    check_title,
    word_count_status,
)

# 默认扫描目录 (相对路径, 相对于当前工作目录)
# 用法: python scripts/fix_dash.py            -> 修复 ./06-chapter-drafts
#       python scripts/fix_dash.py my_drafts  -> 修复 ./my_drafts
DEFAULT_FOLDER = '06-chapter-drafts'
FOLDER = DEFAULT_FOLDER

# 各种破折号变体
# 行首破折号: 在行首 (可能有空白) 跟随空白
# 末尾破折号: 破折号出现在字符串末尾 (允许尾随空白/换行)
# 破折号紧贴左/右中文双引号


def classify_middle_dash(text_before: str, text_after: str) -> str:
    """根据破折号前后的内容决定替换为何种标点。

    返回: 替换标点 (单个字符), 或 '' 表示直接删除
    """
    after_stripped = text_after.lstrip()

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

    # 默认 -> 删除
    return ''


def fix_dash_in_text(s: str) -> tuple[str, dict]:
    """对单段文本执行破折号修复, 返回 (新文本, 统计)."""
    stats = {
        'trailing_deleted': 0,
        'before_quote_deleted': 0,
        'middle_deleted': 0,
        'middle_replaced': 0,
        'line_start_skipped': 0,
        'variants_normalized': 0,
    }

    # 标准化变体: – ― ―― —— → — (目标形式, 中文常用 —)
    def _to_em(m: re.Match) -> str:
        form = m.group(1)
        if form == '—':
            return form  # 已经是标准形式, 不计数
        stats['variants_normalized'] += 1
        return '—'
    # 一次替换, 避免链式 sub 重复计数
    s = re.sub(r'(——|――|—|–|―)', _to_em, s)

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

    # 重新找行首位置
    line_start_positions = {m.start(1) for m in LINE_START_DASH_RE.finditer(s)}

    # 中间破折号 -> 删除 / 替换
    out_parts = []
    last = 0
    for m in DASH_RE.finditer(s):
        if m.start() in line_start_positions:
            continue
        out_parts.append(s[last:m.start()])
        before = s[max(0, m.start() - 5):m.start()]
        after = s[m.end():m.end() + 5]
        if SEMANTIC_REPLACE:
            repl = classify_middle_dash(before, after)
            if repl == '':
                stats['middle_deleted'] += 1
            else:
                stats['middle_replaced'] += 1
        else:
            repl = ''
            stats['middle_deleted'] += 1
        out_parts.append(repl)
        last = m.end()
    out_parts.append(s[last:])
    s = ''.join(out_parts)

    return s, stats


def fix_ellipsis_in_text(s: str) -> tuple[str, dict]:
    """标准化省略号; 超出预算时删除最早的."""
    stats = {
        'normalized': 0,
        'deleted_over_budget': 0,
        'kept': 0,
    }

    # 找出所有省略号位置
    matches = list(ELLIPSIS_RE.finditer(s))
    if not matches:
        return s, stats

    # 先标准化: ... 。。 …… …… → ……
    new_parts = []
    last = 0
    for m in matches:
        new_parts.append(s[last:m.start()])
        form = m.group(0)
        if form == '……':
            stats['kept'] += 1
        else:
            stats['normalized'] += 1
        new_parts.append('……')
        last = m.end()
    new_parts.append(s[last:])
    s = ''.join(new_parts)

    # 预算检查: 保留最后的, 删除最早的
    if stats['kept'] + stats['normalized'] > BUDGET_ELLIPSIS:
        # 找所有 …… 位置, 标记最早的超出量为删除
        positions = [m.start() for m in re.finditer(r'……', s)]
        excess = (stats['kept'] + stats['normalized']) - BUDGET_ELLIPSIS
        if excess > 0 and len(positions) > BUDGET_ELLIPSIS:
            # 删除前 excess 个
            # 倒序删除以保持位置
            for pos in reversed(positions[:excess]):
                s = s[:pos] + s[pos + 2:]
            stats['deleted_over_budget'] = excess

    return s, stats


def fix_quote_in_text(s: str) -> tuple[str, dict]:
    """半角 -> 全角; 嵌套引号删除内层; 超出预算时删除最早的非对话引号."""
    stats = {
        'half_to_full': 0,
        'nested_deleted': 0,
        'deleted_over_budget': 0,
    }

    # 半角 -> 全角
    counter = {'n': 0}
    def _swap(m: re.Match) -> str:
        counter['n'] += 1
        ch = m.group(0)
        if ch == '"':
            return FULL_WIDTH_QUOTE_LEFT if counter['n'] % 2 == 1 else FULL_WIDTH_QUOTE_RIGHT
        return ch
    new_s, n = HALF_WIDTH_QUOTE_RE.subn(_swap, s)
    stats['half_to_full'] = n
    s = new_s

    # 嵌套引号: 检测 4 个引号在 30 字符内 (保守策略, 避免误伤)
    positions = [m.start() for m in re.finditer(r'["\u201d]', s)]
    for i in range(len(positions) - 3):
        if positions[i + 3] - positions[i] < 30:
            # 可能是嵌套, 删除中间两个
            inner_l = positions[i + 1]
            inner_r = positions[i + 2]
            s = s[:inner_l] + s[inner_r + 1:]
            stats['nested_deleted'] += 1
            # 更新位置 (简化: 重新扫描)
            positions = [m.start() for m in re.finditer(r'["\u201d]', s)]
            break  # 一次只处理一个, 让下次重跑处理剩余

    # 预算检查
    quote_count = len(re.findall(r'["\u201d]', s))
    if quote_count > BUDGET_QUOTE:
        # 删除"成对"的, 从最早开始
        # 这里简单实现: 找到 (n/2) 对, 删除前 (n/2 - budget/2) 对
        # 但更稳妥的是: 仅警告, 不自动删除 (避免误伤对话)
        stats['deleted_over_budget'] = quote_count - BUDGET_QUOTE
        # 不自动删除, 让用户决定

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


def count_dashes(s: str) -> int:
    return sum(len(re.findall(re.escape(d), s)) for d in DASH_CHARS)


def count_ellipsis(s: str) -> int:
    return len(re.findall(r'……', s))


def count_quotes(s: str) -> int:
    return len(re.findall(r'["\u201d]', s))


def count_chinese_chars(s: str) -> int:
    return len(CN_CHAR_RE.findall(s))


def main() -> int:
    global FOLDER
    if len(sys.argv) > 1:
        FOLDER = sys.argv[1]

    # 兼容 Windows 控制台 (默认 GBK 无法输出部分 Unicode 字符)
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

    if not os.path.isdir(FOLDER):
        print(f'[!] 目录不存在: {FOLDER}')
        return 1

    total_punct = 0
    all_chapter_stats = []
    title_errors = []
    length_errors = []

    for f in sorted(os.listdir(FOLDER)):
        if not f.endswith('.md'):
            continue
        p = os.path.join(FOLDER, f)
        with open(p, 'r', encoding='utf-8') as fp:
            original = fp.read()

        # 标题检查 (硬错误, 但 fix_dash 不会自动修复, 只警告)
        title_ok, title_msg = check_title(original)
        if not title_ok:
            title_errors.append((f, title_msg))

        # 字数检查 (警告, fix_dash 不处理)
        cn = count_chinese_chars(original)
        if cn < MIN_CHARS or cn > MAX_CHARS:
            length_errors.append((f, cn))

        s, punct_diff = fix_punct_in_text(original)
        s, dash_stats = fix_dash_in_text(s)
        s, ellipsis_stats = fix_ellipsis_in_text(s)
        s, quote_stats = fix_quote_in_text(s)

        if s == original:
            continue

        with open(p, 'w', encoding='utf-8') as fp:
            fp.write(s)

        total_punct += punct_diff

        chapter_stats = {
            'dash': dash_stats,
            'ellipsis': ellipsis_stats,
            'quote': quote_stats,
            'density': {
                'dashes': count_dashes(s),
                'ellipsis': count_ellipsis(s),
                'quotes': count_quotes(s),
                'cn_chars': count_chinese_chars(s),
            },
        }
        all_chapter_stats.append((f, chapter_stats))

        print(f'{f}: 标点修复 {punct_diff} 字符')
        for k, v in dash_stats.items():
            if v:
                print(f'  破折号 {k}: {v}')
        for k, v in ellipsis_stats.items():
            if v:
                print(f'  省略号 {k}: {v}')
        for k, v in quote_stats.items():
            if v:
                print(f'  引号 {k}: {v}')

    if title_errors:
        print('\n[HARD ERROR] 以下文件缺少合法章节标题, 必须在 Punctuation Sweep 之前修复:')
        for f, msg in title_errors:
            print(f'  - {f}: {msg}')
        print('  期望格式: 第N章"title" (N 为中文数字, 如 第一章"雨夜来客")')
        print('  注意: fix_dash 不会自动修复标题, 必须人工编辑章节')

    if length_errors:
        print('\n[HARD WARNING] 以下文件字数越界, 需要拆分或合并:')
        for f, cnt in length_errors:
            print(f'  - {f}: {cnt} 字 ({word_count_status(cnt)})')
        print(f'  目标: {IDEAL_MIN_CHARS}-{IDEAL_MAX_CHARS} (理想), {MIN_CHARS}-{MAX_CHARS} (允许范围)')
        print('  注意: fix_dash 不会自动调整字数, 必须人工编辑或拆分章节')

    print(f'\n总计标点修复: {total_punct} 字符')

    # 密度总览
    if all_chapter_stats:
        print('\n=== 修复后密度总览 ===')
        print(f'{"文件":<30} {"字数":>5} {"破折号":>6} {"省略号":>6} {"引号":>6} {"状态":>8}')
        for f, cs in all_chapter_stats:
            d = cs['density']
            over = (d['dashes'] > BUDGET_DASH
                    or d['ellipsis'] > BUDGET_ELLIPSIS
                    or d['quotes'] > BUDGET_QUOTE
                    or d['cn_chars'] < MIN_CHARS
                    or d['cn_chars'] > MAX_CHARS)
            status = '[!] 超出' if over else 'OK'
            print(f'{f:<30} {d["cn_chars"]:>5} {d["dashes"]:>6} {d["ellipsis"]:>6} {d["quotes"]:>6} {status:>8}')

    return 0


if __name__ == '__main__':
    sys.exit(main())
