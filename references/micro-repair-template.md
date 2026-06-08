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
- Punctuation fixes left to user (with reason):
- Punctuation sweep signed off:

## Quality Self-Check (质量自检 — mandatory)

These checks MUST be completed before Micro-Repair proceeds. Each check is a pass/fail gate.

### Q1. Show vs Tell
- Direct emotion statements found ("他很紧张", "她感到害怕"): (none / list them)
- All converted to action/detail/sensory: (yes / no — if no, list remaining)

### Q2. AI-tone Filter
- Banned transition words found ("就在这时", "与此同时"): (none / count / list)
- Banned thought phrases found ("他心想", "不知为何", "莫名的"): (none / count / list)
- Banned metaphor phrases found ("仿佛", "宛如"): (none / count / list)
- Banned empty descriptions found ("说不出的", "格外", "异常"): (none / count / list)
- Banned dialogue tags found ("他说道", "回答道"): (none / count / list)
- All removed or rewritten: (yes / no)

### Q3. Voice Differentiation
- Characters appearing in this chapter:
- Voice test: can you tell who is speaking without the name tag? (yes / no — if no, specify which character)

### Q4. Sensory Details
- Sensory details in first scene paragraph: (count, must be ≥ 1)
- Total sensory details in chapter: (count, must be ≥ 2 per 500 words)
- Details are specific/concrete (not abstract adjectives): (yes / no)

### Q5. Sentence Rhythm
- Consecutive sentences of similar length (>3): (none / count / location)
- Short sentences (≤8 chars) per paragraph: (count, must be ≥ 1)

### Q5b. Pronoun Density (代词密度)
- Paragraphs with ≥3 consecutive same-pronoun starts ("他/她/它"): (none / list paragraph numbers)
- Total "他" count in chapter:
- Total "她" count in chapter:
- Pronouns replaced with omission/name/identity/action: (count)

### Q6. Dialogue Quality
- Max consecutive dialogue-only exchanges: (count, must be ≤ 5)
- Dialogue with subtext vs direct info-dump: (ratio or notes)
- Setting explained through dialogue: (yes = fail / no = pass)
- Dialogue tags minimized (action replaces "他说"): (yes / no)

### Q7. Scene Transitions
- New scenes start with concrete sensory detail (not "第二天早上"): (yes / no)
- Time jumps marked with concrete detail (not abstract words): (yes / no)

### Q8. Concrete Specificity
- Vague nouns found ("武器", "食物", "很多人"): (none / list)
- Vague adverbs found ("格外", "异常", "慢慢地"): (none / list)
- All replaced with concrete specifics: (yes / no)

## Style Density Check (mandatory)
- Word count (Chinese characters):
- Dash count (all variants):      budget ≤ 6, ideal ≤ 3
- Ellipsis count (`……` only):   budget ≤ 6, ideal ≤ 3
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
- Quality self-check passed: (yes / no — if no, which checks failed)
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