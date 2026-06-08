"""修复中文小说正文中的标点问题 (精简版)。

处理范围:
  - 句末多余逗号 (。，/！，/？，/；，/：，)
  - 行首逗号
  - 破折号:
      1. 行首破折号 -> 跳过 (Markdown 列表标记)
      2. 末尾破折号 -> 删除
      3. 引号前的破折号 -> 删除
      4. 中间破折号 -> 删除 (默认)
  - 省略号: 标准化为 ……; 超出预算时删除最早的
  - 章节标题 / 字数: 警告, 不自动修复

已移除 (不再需要):
  - 引号修复 (半角转全角 / 嵌套处理)
"""

import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

from check_dash import (
    BUDGET_DASH,
    BUDGET_ELLIPSIS,
    DASH_CHARS,
    DASH_RE,
    DASH_BEFORE_QUOTE_RE,
    ELLIPSIS_RE,
    LINE_START_DASH_RE,
    TRAILING_DASH_RE,
    CN_CHAR_RE,
    MIN_CHARS,
    MAX_CHARS,
    IDEAL_MIN_CHARS,
    IDEAL_MAX_CHARS,
    check_title,
    word_count_status,
)

DEFAULT_FOLDER = '06-chapter-drafts'
FOLDER = DEFAULT_FOLDER


def fix_dash_in_text(s: str) -> tuple[str, dict]:
    """对单段文本执行破折号修复, 返回 (新文本, 统计)."""
    stats = {
        'trailing_deleted': 0,
        'before_quote_deleted': 0,
        'middle_deleted': 0,
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

    # 重新找行首位置
    line_start_positions = {m.start(1) for m in LINE_START_DASH_RE.finditer(s)}

    # 中间破折号 -> 删除
    out_parts = []
    last = 0
    for m in DASH_RE.finditer(s):
        if m.start() in line_start_positions:
            continue
        out_parts.append(s[last:m.start()])
        stats['middle_deleted'] += 1
        out_parts.append('')  # 删除
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

    matches = list(ELLIPSIS_RE.finditer(s))
    if not matches:
        return s, stats

    # 标准化
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

    # 超出预算 -> 删除最早的
    total = stats['kept'] + stats['normalized']
    if total > BUDGET_ELLIPSIS:
        positions = [m.start() for m in re.finditer(r'……', s)]
        excess = total - BUDGET_ELLIPSIS
        for pos in reversed(positions[:excess]):
            s = s[:pos] + s[pos + 2:]
        stats['deleted_over_budget'] = excess

    return s, stats


def fix_punct_in_text(s: str) -> tuple[str, int]:
    """原有标点修复."""
    diff = 0
    pairs = [
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


def count_chinese_chars(s: str) -> int:
    return len(CN_CHAR_RE.findall(s))


def main() -> int:
    global FOLDER
    if len(sys.argv) > 1:
        FOLDER = sys.argv[1]

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

        # 标题检查 (硬错误, 不自动修复)
        title_ok, title_msg = check_title(original)
        if not title_ok:
            title_errors.append((f, title_msg))

        # 字数检查 (警告, 不处理)
        cn = count_chinese_chars(original)
        if cn < MIN_CHARS or cn > MAX_CHARS:
            length_errors.append((f, cn))

        s, punct_diff = fix_punct_in_text(original)
        s, dash_stats = fix_dash_in_text(s)
        s, ellipsis_stats = fix_ellipsis_in_text(s)

        if s == original:
            continue

        with open(p, 'w', encoding='utf-8') as fp:
            fp.write(s)

        total_punct += punct_diff

        chapter_stats = {
            'dash': dash_stats,
            'ellipsis': ellipsis_stats,
            'density': {
                'dashes': count_dashes(s),
                'ellipsis': count_ellipsis(s),
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

    if title_errors:
        print('\n[HARD ERROR] 以下文件缺少合法章节标题, 必须在 Punctuation Sweep 之前修复:')
        for f, msg in title_errors:
            print(f'  - {f}: {msg}')
        print('  期望格式: 第N章"title" (N 为中文数字, 如 第一章"雨夜来客")')

    if length_errors:
        print('\n[HARD WARNING] 以下文件字数越界, 需要拆分或合并:')
        for f, cnt in length_errors:
            print(f'  - {f}: {cnt} 字 ({word_count_status(cnt)})')
        print(f'  目标: {IDEAL_MIN_CHARS}-{IDEAL_MAX_CHARS} (理想), {MIN_CHARS}-{MAX_CHARS} (允许范围)')

    print(f'\n总计标点修复: {total_punct} 字符')

    # 密度总览
    if all_chapter_stats:
        print('\n=== 修复后密度总览 ===')
        print(f'{"文件":<30} {"字数":>5} {"破折号":>6} {"省略号":>6} {"状态":>8}')
        for f, cs in all_chapter_stats:
            d = cs['density']
            over = (d['dashes'] > BUDGET_DASH
                    or d['ellipsis'] > BUDGET_ELLIPSIS
                    or d['cn_chars'] < MIN_CHARS
                    or d['cn_chars'] > MAX_CHARS)
            status = '[!] 超出' if over else 'OK'
            print(f'{f:<30} {d["cn_chars"]:>5} {d["dashes"]:>6} {d["ellipsis"]:>6} {status:>8}')

    return 0


if __name__ == '__main__':
    sys.exit(main())
