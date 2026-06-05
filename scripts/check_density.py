"""对 06-chapter-drafts 下的每个 .md 做手工密度审计, 含字数检查。

检查项:
- 中文字数 (Chinese characters, CJK Unified Ideographs)
- 章节标题合法性
- 破折号 (——/—/–/―/--)
- 省略号 (……/.../。。/…)
- 引号 (""/''/全角)
- Markdown 结构痕迹 (#, **, *, -, >, `, ---)
- 半角逗号/句号/问号/感叹号残留
- 行首逗号
- 双逗号
- 句末多余逗号

字数阈值 (per chapter):
- 最小: MIN_CHARS
- 理想: 2500-3500
- 最大: MAX_CHARS
"""

import os
import re
import sys

# 项目根目录 (skill 所在)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

# 默认扫描目录 (相对路径, 相对于当前工作目录)
# 用法: python scripts/check_density.py            -> 扫描 ./06-chapter-drafts
#       python scripts/check_density.py my_drafts  -> 扫描 ./my_drafts
DEFAULT_FOLDER = '06-chapter-drafts'
FOLDER = DEFAULT_FOLDER

# 字数阈值
MIN_CHARS = 1500
IDEAL_MIN_CHARS = 2500
IDEAL_MAX_CHARS = 3500
MAX_CHARS = 5000

CN_CHAR = r'[\u4e00-\u9fff]'

# 章节标题正则: 第N章"title"
TITLE_RE = re.compile(
    r'^第[\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341\u767e\u5343\u96f6\u3007\u4e24]+章["\u201c][^"\u201d]+["\u201d]$'
)

# 破折号
DASH_PATTERNS = {
    '破折号em—': r'—',
    '破折号en–': r'–',
    '破折号horiz―': r'―',
    '全角——': r'——',
    '全角――': r'――',
    '连续--': r'--',
}
# 省略号
ELLIPSIS_PATTERNS = {
    '中文省略号……': r'……',
    '英文省略号...': r'\.\.\.',
    '单点…': r'\u2026',
    '双句号。。': r'。。',
}
# 引号
QUOTE_PATTERNS = {
    '全角双引""': r'[\u201c\u201d]',
    '全角单引号': r'[\u2018\u2019]',
    '半角双引': r'"',
    '半角单引': r"'",
}
# Markdown
MD_PATTERNS = {
    'MD标题#': r'(?m)^#{1,6}\s',
    'MD加粗**': r'\*\*[^*]+\*\*',
    'MD斜体*': r'(?<!\*)\*[^*]+\*(?!\*)',
    'MD下划_': r'(?<!_)_[^_]+_(?!_)',
    'MD列表-': r'(?m)^\s*[-*]\s',
    'MD列表1.': r'(?m)^\s*\d+\.\s',
    'MD引用>': r'(?m)^\s*>',
    'MD代码`': r'`[^`]+`',
    'MD分隔---': r'(?m)^-{3,}$',
}
# 其他
OTHER = {
    '半角逗号,': r',',
    '半角句号.': r'(?<![\d])\.(?![\d])',
    '半角问号?': r'\?',
    '半角感叹!': r'!',
    '行首逗号': r'(?m)^\s*，',
    '双逗号，，': r'，，',
    '句末逗。,': r'。，',
}


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
        return f'[!] 过短 (低于 {MIN_CHARS})'
    if cnt > MAX_CHARS:
        return f'[!] 超长 (超过 {MAX_CHARS})'
    if cnt < IDEAL_MIN_CHARS:
        return f'可接受 (低于理想 {IDEAL_MIN_CHARS})'
    if cnt > IDEAL_MAX_CHARS:
        return f'可接受 (高于理想 {IDEAL_MAX_CHARS})'
    return 'OK (理想范围)'


def main():
    global FOLDER
    if len(sys.argv) > 1:
        FOLDER = sys.argv[1]

    if not os.path.isdir(FOLDER):
        print(f'[!] 目录不存在: {FOLDER}')
        return 1

    files = [f for f in sorted(os.listdir(FOLDER)) if f.endswith('.md')]
    if not files:
        print(f'[!] {FOLDER} 下没有 .md 文件')
        return 1

    over_budget_files = []

    for f in files:
        path = os.path.join(FOLDER, f)
        with open(path, 'r', encoding='utf-8') as fp:
            s = fp.read()

        cn_chars = len(re.findall(CN_CHAR, s))

        print(f'\n=== {f} ===')
        print(f'  中文字数: {cn_chars}  {word_count_status(cn_chars)}')
        print(f'  字符总数: {len(s)}')

        # 标题检查
        title_ok, title_msg = check_title(s)
        if not title_ok:
            print(f'  [HARD ERROR] 章节标题: {title_msg}')
            over_budget_files.append(f)
        else:
            print(f'  章节标题: {title_msg}')

        # 其他标记统计
        for name, pat in {**DASH_PATTERNS, **ELLIPSIS_PATTERNS, **QUOTE_PATTERNS, **MD_PATTERNS, **OTHER}.items():
            cnt = len(re.findall(pat, s))
            if cnt > 0:
                print(f'  {name}: {cnt}')

        # 字数越界提示
        if cn_chars < MIN_CHARS or cn_chars > MAX_CHARS:
            over_budget_files.append(f)

    # 总览
    print(f'\n=== 总览 ===')
    print(f'{"文件":<30} {"字数":>6} {"状态":<25} {"标题":<6}')
    for f in files:
        path = os.path.join(FOLDER, f)
        with open(path, 'r', encoding='utf-8') as fp:
            s = fp.read()
        cn = len(re.findall(CN_CHAR, s))
        title_ok, _ = check_title(s)
        title_status = 'OK' if title_ok else 'NO'
        print(f'{f:<30} {cn:>6} {word_count_status(cn):<25} {title_status:<6}')

    if over_budget_files:
        print(f'\n[!] 警告: {len(over_budget_files)} 个文件存在硬错误或字数越界, 必须在 Micro-Repair 之前修复:')
        for f in over_budget_files:
            print(f'    - {f}')

    return 0


if __name__ == '__main__':
    sys.exit(main())
