"""检查中文小说正文中的标点和风格问题, 附带修复建议。

检查项:
  - 章节标题合法性 (硬错误)
  - 中文字数 (硬警告, 越界需处理)
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

# 项目根目录 (skill 所在)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

# 默认扫描目录 (相对路径, 相对于当前工作目录)
# 用法: python scripts/check_dash.py            -> 扫描 ./06-chapter-drafts
#       python scripts/check_dash.py my_drafts  -> 扫描 ./my_drafts
DEFAULT_FOLDER = '06-chapter-drafts'
FOLDER = DEFAULT_FOLDER

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

# 全角左/右引号 (供 fix_dash 复用)
FULL_WIDTH_QUOTE_LEFT = '\u201c'
FULL_WIDTH_QUOTE_RIGHT = '\u201d'

# Markdown 结构标记 - 这些在正文里是不不允许的
MD_BOLD_RE = re.compile(r'\*\*[^*]+\*\*|__[^_]+__')
MD_ITALIC_RE = re.compile(r'(?<!\*)\*[^*]+\*(?!\*)|(?<!_)_[^_]+_(?!_)')
MD_HEADER_RE = re.compile(r'(?m)^#{1,6}\s+\S')
MD_LIST_RE = re.compile(r'(?m)^\s*[-*+]\s+\S|^\s*\d+\.\s+\S|^\s*-\s*\[\s*[xX ]\s*\]\s+\S')
MD_BLOCKQUOTE_RE = re.compile(r'(?m)^>\s+\S')
MD_CODE_SPAN_RE = re.compile(r'`[^`\n]+`')
MD_HR_RE = re.compile(r'(?m)^[-*_]{3,}$')

# 章节标题正则: 第N章"title"
TITLE_RE = re.compile(
    r'^第[\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341\u767e\u5343\u96f6\u3007\u4e24]+章["\u201c][^"\u201d]+["\u201d]$'
)

# 中文字符
CN_CHAR_RE = re.compile(r'[\u4e00-\u9fff]')

# 语义判断词
TONE_WORDS = '啊哦呀呢嘛吧唉哼嘿哈呵嗯呜'
TRANSITION_WORDS = '但可却然而不过只是可惜'
EXAMPLE_WORDS = '如比如例如即也就是'

# 密度预算 (per chapter, 约 3000 字)
BUDGET_DASH = 6
BUDGET_ELLIPSIS = 6
BUDGET_QUOTE = 30

# 字数阈值
MIN_CHARS = 1500
IDEAL_MIN_CHARS = 2500
IDEAL_MAX_CHARS = 3500
MAX_CHARS = 5000

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


def count_chinese_chars(s: str) -> int:
    """统计中文字符数."""
    return len(CN_CHAR_RE.findall(s))


def check_title(s: str) -> tuple[bool, str]:
    """检查第一行是否为合法的章节标题.

    返回: (is_valid, message)
    """
    if not s.strip():
        return False, '文件为空, 缺少章节标题'
    first_line = s.lstrip('\n').split('\n', 1)[0].rstrip()
    if not first_line:
        return False, '第一行为空, 缺少章节标题'
    if TITLE_RE.match(first_line):
        return True, first_line
    if not first_line.startswith('第'):
        return False, f'第一行不以"第"开头, 当前: {first_line!r}'
    if '章' not in first_line:
        return False, f'第一行缺少"章"字, 当前: {first_line!r}'
    if re.match(r'^第\d+章', first_line):
        return False, f'第N章必须使用中文数字, 当前: {first_line!r}'
    if first_line.lstrip().startswith('#'):
        return False, f'第一行不能是 Markdown 标题, 当前: {first_line!r}'
    if '"' not in first_line and '\u201c' not in first_line:
        return False, f'标题必须用全角引号包裹, 当前: {first_line!r}'
    if first_line.endswith(('。', '，', '；', '：', '!', '?', '！', '？')):
        return False, f'标题末尾不能有标点, 当前: {first_line!r}'
    return False, f'标题格式不符合 第N章"title", 当前: {first_line!r}'


def word_count_status(cnt: int) -> str:
    """根据中文字数返回状态字符串."""
    if cnt < MIN_CHARS:
        return f'过短 (低于 {MIN_CHARS})'
    if cnt > MAX_CHARS:
        return f'超长 (超过 {MAX_CHARS})'
    if cnt < IDEAL_MIN_CHARS:
        return f'可接受 (低于理想 {IDEAL_MIN_CHARS})'
    if cnt > IDEAL_MAX_CHARS:
        return f'可接受 (高于理想 {IDEAL_MAX_CHARS})'
    return 'OK (理想范围)'


def check_file(path: str, filename: str) -> tuple[list[str], dict]:
    with open(path, 'r', encoding='utf-8') as fp:
        s = fp.read()

    issues: list[str] = []
    stats = {
        'dash_count': 0,
        'ellipsis_count': 0,
        'quote_count': 0,
        'md_marks': 0,
        'title_ok': False,
        'cn_chars': 0,
    }

    # 章节标题检查 (硬错误, 不允许 exception)
    title_ok, title_msg = check_title(s)
    stats['title_ok'] = title_ok
    if not title_ok:
        issues.insert(0, f'  [HARD ERROR] 章节标题: {title_msg}')
        issues.insert(1, f'    期望格式: 第N章"title" (N 为中文数字, 如 第一章"雨夜来客")')
        issues.insert(2, '')

    # 中文字数
    stats['cn_chars'] = count_chinese_chars(s)

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

    # 字数警告
    cn = stats['cn_chars']
    if cn < MIN_CHARS or cn > MAX_CHARS:
        issues.append('')
        issues.append(f'  [HARD WARNING] 字数 {cn} {word_count_status(cn)}')
        issues.append(f'    处理: 拆分章节 (过长) 或合并相邻章节 (过短), 记录到 decisions-log.md')

    # 标题状态汇总
    if not stats['title_ok']:
        issues.append('')
        issues.append('  [HARD ERROR] 章节标题无效, 必须在 Punctuation Sweep 之前修复')

    return issues, stats


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
    print(f'{"文件":<30} {"标题":<4} {"字数":>5} {"破折号":>6} {"省略号":>6} {"引号":>6} {"MD":>4}')
    for f, s in all_stats:
        flag = ''
        if not s['title_ok']:
            flag = ' [ERR]'
        elif s['cn_chars'] < MIN_CHARS or s['cn_chars'] > MAX_CHARS:
            flag = ' [!LEN]'
        elif s['dash_count'] > BUDGET_DASH or s['ellipsis_count'] > BUDGET_ELLIPSIS or s['quote_count'] > BUDGET_QUOTE or s['md_marks'] > 0:
            flag = ' [!]'
        title_status = 'OK' if s['title_ok'] else 'NO'
        print(f'{f:<30} {title_status:<4} {s["cn_chars"]:>5} {s["dash_count"]:>6} {s["ellipsis_count"]:>6} {s["quote_count"]:>6} {s["md_marks"]:>4}{flag}')

    return 0


if __name__ == '__main__':
    sys.exit(main())
