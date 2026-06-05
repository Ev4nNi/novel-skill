"""检查中文小说正文中的标点和风格问题, 附带修复建议。

检查项:
  - 各种破折号残留 (em-dash — / en-dash – / horizontal bar ― / 全角 —— / 连续 --)
  - 省略号格式 (... / 。。 / ……)
  - 引号格式 (半角 / 全角 / 嵌套)
  - 双逗号 (，,)
  - 句末多余逗号
  - 行首逗号
  - Markdown 结构标记 (**bold** / *italic* / # headers / - lists / > quotes / `code` / ---)
  - 破折号/省略号/引号 密度

对每个问题, 给出修复建议 (删除 / 改为 , / 改为 ; / 改为 : / 标准化)。

只扫描 06-chapter-drafts 下的 .md 文件, 不修改文件。
"""

import os
import re
import sys

FOLDER = r'd:\programproject\novels\悬疑小说\06-chapter-drafts'

# 各种破折号变体
DASH_CHARS = ['——', '――', '—', '–', '―']
DASH_RE = re.compile(r'(——|――|—|–|―)')

# 行首破折号: 在行首 (可能有空白) 跟随空白
LINE_START_DASH_RE = re.compile(r'(?m)^\s*(——|――|—|–|―)\s')

# 末尾破折号: 破折号出现在字符串末尾 (允许尾随空白/换行)
TRAILING_DASH_RE = re.compile(r'(——|――|—|–|―)\s*$')

# 破折号紧贴左/右中文双引号
DASH_BEFORE_QUOTE_RE = re.compile(r'(——|――|—|–|―)(["\u201d\u2019])')

# 省略号各种形式
ELLIPSIS_RE = re.compile(r'\.\.\.|。。|\u2026\u2026|……|\u2026')

# 半角引号
HALF_WIDTH_QUOTE_RE = re.compile(r'["\']')

# 嵌套引号检测 (一个引号对内嵌另一个引号对)
NESTED_QUOTE_RE = re.compile(r'["\u201c][^"\u201c]*["\u201d][^"\u201c]*["\u201d]')

# 全角引号配对 (用于统计)
FULL_WIDTH_QUOTE_RE = re.compile(r'["\u201d]')

# Markdown 结构标记 - 这些在正文里是不允许的
MD_BOLD_RE = re.compile(r'\*\*[^*]+\*\*|__[^_]+__')
MD_ITALIC_RE = re.compile(r'(?<!\*)\*[^*]+\*(?!\*)|(?<!_)_[^_]+_(?!_)')
MD_HEADER_RE = re.compile(r'(?m)^#{1,6}\s+\S')
MD_LIST_RE = re.compile(r'(?m)^\s*[-*+]\s+\S|^\s*\d+\.\s+\S|^\s*-\s*\[\s*[xX ]\s*\]\s+\S')
MD_BLOCKQUOTE_RE = re.compile(r'(?m)^>\s+\S')
MD_CODE_SPAN_RE = re.compile(r'`[^`\n]+`')
MD_HR_RE = re.compile(r'(?m)^[-*_]{3,}$')

# 语义判断词
TONE_WORDS = '啊哦呀呢嘛吧唉哼嘿哈呵嗯呜'
TRANSITION_WORDS = '但可却然而不过只是可惜'
EXAMPLE_WORDS = '如比如例如即也就是'

# 密度预算 (per chapter, 约 3000 字)
BUDGET_DASH = 6
BUDGET_ELLIPSIS = 6
BUDGET_QUOTE = 30

# 是否启用语义替换 (默认 False = 严格删除模式)
# 若改为 True, 中间破折号会按语义替换; False 则一律删除
SEMANTIC_REPLACE = False


def suggest_fix(dash: str, before: str, after: str, is_line_start: bool, is_trailing: bool, is_before_quote: bool) -> tuple[str, str]:
    """返回 (动作, 替换符号) 动作: delete / replace / skip."""
    if is_line_start:
        return 'skip', dash
    if is_trailing:
        return 'delete', ''
    if is_before_quote:
        return 'delete', ''
    if not SEMANTIC_REPLACE:
        return 'delete', ''
    # 语义替换 (仅在显式开启时)
    after_stripped = after.lstrip()
    if after_stripped and after_stripped[0] in TONE_WORDS:
        return 'replace', '，'
    if before and before[-1] in TONE_WORDS:
        return 'replace', '，'
    if after_stripped and after_stripped[0] in EXAMPLE_WORDS:
        return 'replace', ':'
    if before and before[-1] in EXAMPLE_WORDS:
        return 'replace', ':'
    if after_stripped and after_stripped[0] in TRANSITION_WORDS:
        return 'replace', '；'
    if before and before[-1] in TRANSITION_WORDS:
        return 'replace', '；'
    return 'delete', ''


def make_snippet(s: str, pos: int, length: int = 30) -> str:
    start = max(0, pos - length)
    end = min(len(s), pos + length)
    snippet = s[start:end].replace('\n', ' ')
    if start > 0:
        snippet = '...' + snippet
    if end < len(s):
        snippet = snippet + '...'
    return snippet


def count_dashes(s: str) -> int:
    """统计所有破折号变体的总数."""
    return sum(len(re.findall(re.escape(d), s)) for d in DASH_CHARS)


def count_ellipsis(s: str) -> int:
    """统计所有省略号 (规范化后)."""
    return len(ELLIPSIS_RE.findall(s))


def count_quotes(s: str) -> int:
    """统计所有引号配对数 (半角 + 全角)."""
    half = len(HALF_WIDTH_QUOTE_RE.findall(s))
    full = len(FULL_WIDTH_QUOTE_RE.findall(s))
    return (half + full) // 2


def check_file(path: str, filename: str) -> tuple[list[str], dict]:
    with open(path, 'r', encoding='utf-8') as fp:
        s = fp.read()

    issues: list[str] = []
    stats = {
        'dash_count': 0,
        'ellipsis_count': 0,
        'quote_count': 0,
        'md_marks': 0,
    }

    # 行首位置
    line_start_positions = {m.start(1) for m in LINE_START_DASH_RE.finditer(s)}

    # 破折号逐个分析
    for m in DASH_RE.finditer(s):
        stats['dash_count'] += 1
        pos = m.start()
        dash = m.group(1)
        before = s[max(0, pos - 5):pos]
        after = s[m.end():m.end() + 5]
        is_line_start = pos in line_start_positions
        is_trailing = bool(TRAILING_DASH_RE.match(dash + s[m.end():m.end() + 1]) or s[m.end():].strip() == '' and (s.rstrip().endswith(dash)))
        is_before_quote = bool(DASH_BEFORE_QUOTE_RE.match(s[pos:pos + 5]))

        action, repl = suggest_fix(dash, before, after, is_line_start, is_trailing, is_before_quote)
        if action == 'skip':
            suggestion = f'跳过 (行首 Markdown 标记)'
        elif action == 'delete':
            suggestion = f'删除 ({"末尾" if is_trailing else "引号前" if is_before_quote else "中间破折号 — 默认删除"})'
        else:
            suggestion = f'改为 "{repl}"'
        snippet = make_snippet(s, pos)
        issues.append(f'  破折号 {dash!r} @ 偏移 {pos}: {suggestion}\n    上下文: {snippet}')

    # 省略号
    for m in ELLIPSIS_RE.finditer(s):
        stats['ellipsis_count'] += 1
        pos = m.start()
        form = m.group(0)
        if form == '……':
            suggestion = f'保留 (标准 6-dot 形式), 但计入预算'
        else:
            suggestion = f'标准化为 ……'
        issues.append(f'  省略号 {form!r} @ 偏移 {pos}: {suggestion}\n    上下文: {make_snippet(s, pos)}')

    # 半角引号
    for m in HALF_WIDTH_QUOTE_RE.finditer(s):
        pos = m.start()
        issues.append(f'  半角引号 {m.group(0)!r} @ 偏移 {pos}: 改为全角\n    上下文: {make_snippet(s, pos)}')

    # 嵌套引号
    for m in NESTED_QUOTE_RE.finditer(s):
        pos = m.start()
        issues.append(f'  嵌套引号 @ 偏移 {pos}: 删除内层引号\n    上下文: {make_snippet(s, pos)}')

    # Markdown 结构标记
    for pattern, name in [
        (MD_BOLD_RE, 'bold'),
        (MD_ITALIC_RE, 'italic'),
        (MD_HEADER_RE, 'header'),
        (MD_LIST_RE, 'list'),
        (MD_BLOCKQUOTE_RE, 'blockquote'),
        (MD_CODE_SPAN_RE, 'code span'),
        (MD_HR_RE, 'horizontal rule'),
    ]:
        for m in pattern.finditer(s):
            stats['md_marks'] += 1
            pos = m.start()
            issues.append(f'  Markdown {name} @ 偏移 {pos}: 不允许出现在正文中, 改为自然散文\n    上下文: {make_snippet(s, pos)}')

    # 双逗号
    if '，，' in s:
        for m in re.finditer(r'，，+', s):
            issues.append(f'  双逗号 @ 偏移 {m.start()}: 改为单个 ，\n    上下文: {make_snippet(s, m.start())}')

    # 句末多余逗号
    for punct in ['。，', '！，', '？，', '；，', '：，']:
        if punct in s:
            for m in re.finditer(re.escape(punct), s):
                issues.append(f'  句末多余逗号 {punct!r} @ 偏移 {m.start()}: 删除逗号\n    上下文: {make_snippet(s, m.start())}')

    # 行首逗号
    for m in re.finditer(r'\n，', s):
        issues.append(f'  行首逗号 @ 偏移 {m.start() + 1}: 删除\n    上下文: {make_snippet(s, m.start() + 1)}')

    stats['quote_count'] = count_quotes(s)

    # 密度警告
    over_budget = []
    if stats['dash_count'] > BUDGET_DASH:
        over_budget.append(f'破折号 {stats["dash_count"]} > 预算 {BUDGET_DASH}')
    if stats['ellipsis_count'] > BUDGET_ELLIPSIS:
        over_budget.append(f'省略号 {stats["ellipsis_count"]} > 预算 {BUDGET_ELLIPSIS}')
    if stats['quote_count'] > BUDGET_QUOTE:
        over_budget.append(f'引号 {stats["quote_count"]} > 预算 {BUDGET_QUOTE}')
    if stats['md_marks'] > 0:
        over_budget.append(f'Markdown 结构标记 {stats["md_marks"]} > 预算 0')

    if over_budget:
        issues.append('')
        issues.append('  [!] 密度警告 (超出预算):')
        for w in over_budget:
            issues.append(f'    - {w}')
        issues.append('    处理: 编辑章节 或 在 decisions-log.md 添加 prose-style-exception 行')

    return issues, stats


def main() -> None:
    # 兼容 Windows 控制台 (默认 GBK 无法输出部分 Unicode 字符)
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
    total = 0
    all_stats = []
    for f in sorted(os.listdir(FOLDER)):
        if not f.endswith('.md'):
            continue
        p = os.path.join(FOLDER, f)
        issues, stats = check_file(p, f)
        all_stats.append((f, stats))
        if issues:
            print(f'\n[{f}] {len(issues)} 项报告:')
            for line in issues:
                print(line)
            total += len(issues)
    print(f'\n共发现 {total} 项问题')

    # 密度总览
    print('\n=== 密度总览 ===')
    print(f'{"文件":<30} {"破折号":>6} {"省略号":>6} {"引号":>6} {"MD":>4}')
    for f, s in all_stats:
        flag = ''
        if s['dash_count'] > BUDGET_DASH or s['ellipsis_count'] > BUDGET_ELLIPSIS or s['quote_count'] > BUDGET_QUOTE or s['md_marks'] > 0:
            flag = ' [!]'
        print(f'{f:<30} {s["dash_count"]:>6} {s["ellipsis_count"]:>6} {s["quote_count"]:>6} {s["md_marks"]:>4}{flag}')


if __name__ == '__main__':
    main()
