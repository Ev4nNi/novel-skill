# Micro-Repair Template

After every chapter draft, fill this report and save it as `10-review/micro-reports/Chapter-XXX-repair.md`. The micro-repair is mandatory before starting the next chapter.

The first block of the report is the **Punctuation Sweep**, which is mandatory before any other micro-repair work.

````markdown
# Chapter XXX Micro-Repair

## Punctuation Sweep (mandatory, runs first)
- Sweep date:
- check_dash.py report reviewed by user:
- Punctuation issues found:
- Punctuation fixes applied:
  - trailing-dash deleted:
  - before-quote dash deleted:
  - middle-dash deleted (default, no replacement):
  - middle-dash replaced (semantic, requires prose-style-exception in decisions-log):
  - ellipsis normalized (3-dot `...` or `。。` -> `……`):
  - ellipsis deleted (over budget):
  - quote normalized (half-width -> full-width):
  - nested quote deleted:
  - quote deleted (over budget):
- Punctuation fixes left to user (with reason):
- Punctuation sweep signed off:

## Style Density Check (mandatory)
- Word count (Chinese characters):
- Dash count (all variants):      budget ≤ 6, ideal ≤ 3
- Ellipsis count (`……` only):   budget ≤ 6, ideal ≤ 3
- Quote count (dialogue + nested + scare):  budget ≤ 30, ideal ≤ 20
- Markdown structural marks in draft body: budget = 0
  - bold/italic/headers/lists/blockquotes/code spans found:
  - any found must be converted to natural prose before Micro-Repair proceeds
- Over budget? (yes/no):
  - if yes: prose-style-exception row appended to decisions-log.md, or chapter edited
- Word count within range? (yes/no):
  - target: 1500-5000 Chinese characters per chapter
  - if out of range: split chapter or merge with adjacent, log a chapter-length event
- Style density signed off:

## User Confirmation
- Draft reviewed:
- Continuity updates applied:
- Repair signed off:

## Draft Summary
- Chapter card reference:
- Draft file reference:
- Word count:
- POV character:

## Continuity Updates
- Character files updated:
- Worldbuilding files updated:
- Foreshadowing tracker updated:
- Reveals tracker updated:
- Timeline updated:
- Lore-index updated:

## Decisions Made
- Conflicts raised:
- Conflicts resolved:
- Skipped callbacks (with reason):
- Forwarded to next chapter:

## Progress Update
- progress.md updated:
- decisions-log.md updated:
````