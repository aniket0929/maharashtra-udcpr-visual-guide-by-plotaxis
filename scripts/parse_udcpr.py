import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('ucpr_real.md', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

total_lines = len(lines)
print(f"Total lines: {total_lines}")

# 1. Inspect headings
# Markdown headers: lines starting with #
headings = []
for idx, line in enumerate(lines):
    line_str = line.strip()
    if line_str.startswith('#'):
        m = re.match(r'^(#+)\s*(.*)', line_str)
        if m:
            level = len(m.group(1))
            text = m.group(2).strip()
            headings.append({
                'line': idx + 1,
                'level': level,
                'raw': line_str,
                'text': text
            })

print(f"Total markdown headings (#): {len(headings)}")

# 2. Inspect Chapters
chapters = []
curr_ch = None
for h in headings:
    m = re.search(r'CHAPTER\s*[-–—:]?\s*(\d+)(.*)', h['text'], re.IGNORECASE)
    if m:
        ch_num = int(m.group(1))
        ch_title = m.group(2).strip(' -–—:')
        curr_ch = {'number': ch_num, 'line': h['line'], 'title': ch_title, 'subheadings': []}
        chapters.append(curr_ch)

print(f"\nChapters identified: {len(chapters)}")
for ch in chapters:
    print(f"  Chapter {ch['number']} (Line {ch['line']}): {ch['title']}")

# 3. Amended clauses (#)
# Check both in headings and in general text:
# Notice that (#) can appear as `(#)`, `<sup>(#)</sup>`, `<sup>#</sup>`, `(#*)`, `*#`, etc.
amended_in_headings = []
amended_in_text = []

# Pattern for amended marker
# The prompt says: "(#)" in headings and text marks amended clauses. Capture every one.
amend_pattern = re.compile(r'(\( ?# ?\)|<sup>\s*\(?#\)?\s*</sup>|#\))')

for idx, line in enumerate(lines):
    if amend_pattern.search(line):
        is_heading = line.strip().startswith('#')
        entry = {'line': idx + 1, 'text': line.strip(), 'is_heading': is_heading}
        amended_in_text.append(entry)
        if is_heading:
            amended_in_headings.append(entry)

print(f"\nAmended markers found:")
print(f"  Total lines with amended marker: {len(amended_in_text)}")
print(f"  Headings with amended marker: {len(amended_in_headings)}")

# 4. Definitions in 1.3
# Let's find Section 1.3 and its boundary (where does 1.4 start?)
line_1_3 = None
line_1_4 = None
for h in headings:
    if '1.3' in h['text'] and 'DEFINITION' in h['text'].upper():
        line_1_3 = h['line']
    elif '1.4' in h['text'] and 'APPLICABILITY' in h['text'].upper():
        line_1_4 = h['line']

print(f"\nSection 1.3 starts at line: {line_1_3}, ends before line 1.4: {line_1_4}")

# Let's analyze how definitions are formatted in Section 1.3
def_lines = lines[line_1_3 - 1 : line_1_4 - 1]
# Check how individual definitions are numbered or headed (e.g., 1.3.1, 1.3.2 or 1., 2. or bold terms)
defs_found = []
# Match numbered patterns like "1.3.1 Term", "### 1.3.1", or "1. Term", "**1. Term**"
for idx, l in enumerate(def_lines):
    full_line_num = line_1_3 + idx
    # Check patterns
    # Often in UDCPR it is 1.3.1 or 1. or (1) or bold
    m1 = re.match(r'^(?:###?\s*)?(\d+\.\d+(?:\.\d+)?)\s+(.*)', l.strip())
    m2 = re.match(r'^(?:###?\s*)?\*\*(\d+(?:\.\d+)?)\s*(.*?)\*\*', l.strip())
    m3 = re.match(r'^\*\*(\d+)\.\s*(.*?)\*\*', l.strip())
    # Let's inspect raw lines
    if '###' in l or '**' in l or re.match(r'^\d+\.', l.strip()):
        pass

