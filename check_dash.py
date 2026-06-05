"""检查中文小说正文中的标点问题, 附带修复建议。

检查项:
  - 各种破折号残留 (em-dash — / en-dash – / horizontal bar ― / 全角 —— / 连续 --)
  - 双逗号 (，,)
  - 句末多余逗号
  - 行首逗号

对每个破折号, 给出修复建议 (删除 / 改为 , / 改为 ; / 改为 :)。

只扫描 06-chapter-drafts 下的 .md 文件, 不修改文件。
"""

import os
import re

FOLDER = r'd:\programproject\novels\悬疑小说\06-chapter-drafts'

DASH_RE = re.compile(r'(——|――|—|–|―)')
LINE_START_DASH_RE = re.compile(r'(?m)^\s*(——|――|—|–|―)\s')
TRAILING_DASH_RE = re.compile(r'(——|――|—|–|―)\s*$')
DASH_BEFORE_QUOTE_RE = re.compile(r'(——|――|—|–|―)(["\u201d\u2019])')

TONE_WORDS = '啊哦呀呢嘛吧唉哼嘿哈呵嗯呜'
TRANSITION_WORDS = '但可却然而不过只是可惜'
EXAMPLE_WORDS = '如比如例如即也就是'


def suggest_fix(dash: str, before: str, after: str, is_line_start: bool, is_trailing: bool, is_before_quote: bool) -> tuple[str, str]:
    """返回 (动作, 替换符号) 动作: delete / replace / skip."""
    if is_line_start:
        return 'skip', dash
    if is_trailing:
        return 'delete', ''
    if is_before_quote:
        return 'delete', ''
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
    return 'replace', '，'


def make_snippet(s: str, pos: int, length: int = 30) -> str:
    start = max(0, pos - length)
    end = min(len(s), pos + length)
    snippet = s[start:end].replace('\n', ' ')
    if start > 0:
        snippet = '...' + snippet
    if end < len(s):
        snippet = snippet + '...'
    return snippet


def check_file(path: str, filename: str) -> list[str]:
    with open(path, 'r', encoding='utf-8') as fp:
        s = fp.read()

    issues: list[str] = []

    # 行首位置
    line_start_positions = {m.start(1) for m in LINE_START_DASH_RE.finditer(s)}

    # 破折号逐个分析
    for m in DASH_RE.finditer(s):
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
            suggestion = f'删除 ({"末尾" if is_trailing else "引号前"})'
        else:
            suggestion = f'改为 "{repl}"'
        snippet = make_snippet(s, pos)
        issues.append(f'  破折号 {dash!r} @ 偏移 {pos}: {suggestion}\n    上下文: {snippet}')

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

    return issues


def main() -> None:
    total = 0
    for f in sorted(os.listdir(FOLDER)):
        if not f.endswith('.md'):
            continue
        p = os.path.join(FOLDER, f)
        issues = check_file(p, f)
        if issues:
            print(f'\n[{f}] {len(issues)} 个问题:')
            for line in issues:
                print(line)
            total += len(issues)
    print(f'\n共发现 {total} 个问题')


if __name__ == '__main__':
    main()
