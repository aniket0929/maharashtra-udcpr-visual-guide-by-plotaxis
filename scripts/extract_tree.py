import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('ucpr_real.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

total_lines = len(lines)

# 1. Heading extraction
heading_re = re.compile(r'^(#+)\s*(.*)')
raw_headings = []
for idx, line in enumerate(lines):
    line_str = line.strip()
    m = heading_re.match(line_str)
    if m:
        raw_headings.append({
            'line': idx + 1,
            'level': len(m.group(1)),
            'text': m.group(2).strip()
        })

print(f"Total markdown headings: {len(raw_headings)}")

# Heading count by level
level_counts = {}
for h in raw_headings:
    level_counts[h['level']] = level_counts.get(h['level'], 0) + 1
print("Headings by level:", level_counts)

# Let's inspect chapters
chapters = []
chapter_ranges = []

# Regex to detect chapter headers
ch_pattern = re.compile(r'^CHAPTER\s*[-–—:]?\s*(\d+)\s*(.*)', re.IGNORECASE)

for i, h in enumerate(raw_headings):
    m = ch_pattern.match(h['text'])
    if m:
        ch_num = int(m.group(1))
        ch_title = m.group(2).strip(' -–—:')
        # Check if next heading or line has the title if ch_title is empty
        if not ch_title and i + 1 < len(raw_headings):
            next_h = raw_headings[i+1]
            if next_h['line'] == h['line'] + 1 or next_h['line'] == h['line'] + 2:
                ch_title = next_h['text'].strip(' -–—:')
        chapters.append({
            'number': ch_num,
            'line': h['line'],
            'title': ch_title
        })

for i in range(len(chapters)):
    start_line = chapters[i]['line']
    end_line = chapters[i+1]['line'] - 1 if i + 1 < len(chapters) else 13281
    chapter_ranges.append({
        'chapter': chapters[i]['number'],
        'title': chapters[i]['title'],
        'start_line': start_line,
        'end_line': end_line
    })

# Add Appendices range and Marathi orders range
# Find where Appendix A starts
appendix_start = 13282
orders_start = None
for idx, l in enumerate(lines):
    if idx > 15000 and ('आदेश क्र.' in l or 'महाराष्ट्र शासन नगर विकास विभाग' in l):
        orders_start = idx + 1
        break

print("\n--- Chapters Found ---")
for cr in chapter_ranges:
    print(f"Chapter {cr['chapter']:2d}: {cr['title']} (Lines {cr['start_line']} - {cr['end_line']})")

print(f"\nAppendices start around line {appendix_start}")
print(f"Government Orders (Marathi) start around line {orders_start}")
