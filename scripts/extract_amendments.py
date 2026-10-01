import re
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

with open('ucpr_real.md', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

# Track all occurrences of (#)
# Look for "(#)", "( # )", "<sup>(#)</sup>", "<sup>#</sup>", " # " in TOC or headings
amend_re = re.compile(r'(\(\s*#\s*\)|<sup>\s*\(?#\)?\s*</sup>|#(?:\s+|$))')

# Let's track:
# 1. In TOC (lines 172 to 650)
# 2. In Main Chapters (lines 671 to 13280)
# 3. In Appendices / Schedules (lines 13281 to 16000)
# 4. In Govt Orders / Marathi appendix (lines > 16000)

toc_amendments = []
body_amendments = []
appendices_amendments = []
orders_amendments = []

curr_clause = "Unknown"
curr_chapter = "Unknown"

for idx, line in enumerate(lines):
    line_num = idx + 1
    clean = line.strip()
    
    # Update chapter
    m_ch = re.search(r'CHAPTER\s*[-–—:]?\s*(\d+)', clean, re.IGNORECASE)
    if m_ch:
        curr_chapter = f"Chapter {m_ch.group(1)}"
        
    # Update clause if line is a heading with a regulation number
    m_cl = re.search(r'^(?:#+\s*)?(\d+\.\d+(?:\.\d+)*)', clean)
    if m_cl:
        curr_clause = m_cl.group(1)
        
    # Check for (#) or <sup>(#)</sup>
    # Also check for # in TOC table rows
    if line_num <= 650:
        if '#' in clean:
            # Check if it's the TOC entry
            toc_amendments.append({
                'line': line_num,
                'text': clean
            })
    elif line_num <= 13281:
        if re.search(r'(\(\s*#\s*\)|<sup>\s*\(?#\)?\s*</sup>)', clean):
            body_amendments.append({
                'line': line_num,
                'chapter': curr_chapter,
                'clause': curr_clause,
                'is_heading': clean.startswith('#'),
                'text': clean
            })
    elif line_num <= 16000:
        if re.search(r'(\(\s*#\s*\)|<sup>\s*\(?#\)?\s*</sup>)', clean):
            appendices_amendments.append({
                'line': line_num,
                'text': clean
            })
    else:
        if re.search(r'(\(\s*#\s*\)|<sup>\s*\(?#\)?\s*</sup>)', clean):
            orders_amendments.append({
                'line': line_num,
                'text': clean
            })

print(f"TOC entries with #: {len(toc_amendments)}")
print(f"Body (Ch 1-15) entries with (#): {len(body_amendments)}")
print(f"Appendices entries with (#): {len(appendices_amendments)}")
print(f"Orders entries with (#): {len(orders_amendments)}")

print("\n--- TOC items with # ---")
for t in toc_amendments:
    print(f"L{t['line']}: {t['text']}")

print("\n--- Body items with (#) (first 30) ---")
for b in body_amendments[:30]:
    print(f"L{b['line']} [{b['chapter']} | {b['clause']}]: {b['text'][:90]}")

