"""统计中文小说章节的字数并输出状态。

用法:
  python scripts/count_chars.py                          # 默认 06-chapter-drafts/
  python scripts/count_chars.py <文件夹路径>             # 指定目录
  python scripts/count_chars.py --range 1 10             # 指定章节范围
  python scripts/count_chars.py --range 1 10 --folder 指定目录

字数标准:
  理想范围: 2500-3500
  允许范围: 1500-5000
  超出允许范围 = HARD WARNING
"""

import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
DEFAULT_FOLDER = os.path.join(PROJECT_ROOT, '06-chapter-drafts')

# 字数阈值 (与 check_dash.py 保持一致)
IDEAL_MIN = 2500
IDEAL_MAX = 3500
MIN_CHARS = 1500
MAX_CHARS = 5000

CN_CHAR_RE = re.compile(r'[\u4e00-\u9fff]')


def count_chinese_chars(text: str) -> int:
    return len(CN_CHAR_RE.findall(text))


def word_count_status(cnt: int) -> tuple[str, str]:
    if cnt < MIN_CHARS:
        return f'过短 (低于 {MIN_CHARS})', 'HARD WARNING'
    if cnt > MAX_CHARS:
        return f'超长 (超过 {MAX_CHARS})', 'HARD WARNING'
    if cnt < IDEAL_MIN:
        return f'可接受 (低于理想 {IDEAL_MIN})', 'WARN'
    if cnt > IDEAL_MAX:
        return f'可接受 (高于理想 {IDEAL_MAX})', 'WARN'
    return 'OK (理想范围)', 'OK'


def parse_args():
    folder = DEFAULT_FOLDER
    start = None
    end = None

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == '--folder' and i + 1 < len(args):
            folder = args[i + 1]
            i += 2
        elif args[i] == '--range' and i + 2 < len(args):
            start = int(args[i + 1])
            end = int(args[i + 2])
            i += 3
        else:
            # 兼容旧用法: 直接传文件夹路径
            folder = args[i]
            i += 1

    if not os.path.isdir(folder):
        print(f'[!] 目录不存在: {folder}')
        sys.exit(1)

    return folder, start, end


def find_chapters(folder: str, start: int | None = None, end: int | None = None):
    """找出目录下的章节文件并排序."""
    files = sorted(f for f in os.listdir(folder) if f.endswith('.md'))

    if start is None and end is None:
        return [(f, None) for f in files]

    results = []
    chapter_re = re.compile(r'Chapter-(\d+)\.md', re.IGNORECASE)
    for f in files:
        m = chapter_re.search(f)
        if m:
            num = int(m.group(1))
            if (start is None or num >= start) and (end is None or num <= end):
                results.append((f, num))

    # 按章节号排序
    results.sort(key=lambda x: x[1])
    return results


def main():
    folder, start, end = parse_args()

    chapters = find_chapters(folder, start, end)
    if not chapters:
        print(f'[!] {folder} 下没有找到匹配的章节文件')
        return

    total = 0
    ok_count = 0
    warn_count = 0
    hard_warn_count = 0

    print(f'\n{"文件":<25} {"字数":>6} {"状态":>15}')
    print('-' * 50)

    for filename, _ in chapters:
        filepath = os.path.join(folder, filename)
        content = open(filepath, encoding='utf-8').read()
        chars = count_chinese_chars(content)
        status, level = word_count_status(chars)

        if level == 'OK':
            ok_count += 1
        elif level == 'WARN':
            warn_count += 1
        else:
            hard_warn_count += 1

        total += chars
        print(f'{filename:<25} {chars:>6} {level:>15}  {status}')

    avg = total / len(chapters) if chapters else 0
    print('-' * 50)
    print(f'共 {len(chapters)} 章 | 总字数 {total} | 平均 {avg:.0f} 字/章')
    print(f'  OK: {ok_count}  |  WARN: {warn_count}  |  HARD WARNING: {hard_warn_count}')

    if hard_warn_count > 0:
        print(f'\n建议: 过短的章节考虑合并, 过长的章节考虑拆分')
    elif warn_count > 0:
        print(f'\n提示: 部分章节不在理想范围内 ({IDEAL_MIN}-{IDEAL_MAX}), 可接受但不推荐')
    else:
        print(f'\n所有章节字数均在理想范围内 ({IDEAL_MIN}-{IDEAL_MAX})')


if __name__ == '__main__':
    main()
