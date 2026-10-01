import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('ucpr_real.md', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")

# 1. Lines containing '|' but not starting or ending with '|'
stray_pipe_lines = []
for idx, line in enumerate(lines):
    clean = line.strip()
    if '|' in clean:
        if not (clean.startswith('|') and clean.endswith('|')):
            stray_pipe_lines.append((idx + 1, clean))

print(f"\nLines with stray '|' (not properly enclosed): {len(stray_pipe_lines)}")
for lnum, txt in stray_pipe_lines[:15]:
    print(f"  L{lnum}: {txt}")

# 2. Check for tables split across pages
# Look for a table ending, followed within 1-5 lines of page headers (like 'UDCPR-2020', Roman numerals, page numbers, horizontal rules), followed by another table row starting with '|'
split_tables = []
for idx in range(len(lines) - 5):
    l1 = lines[idx].strip()
    if l1.startswith('|') and l1.endswith('|'):
        # Check if next line is NOT a table line
        l_next = lines[idx + 1].strip()
        if not (l_next.startswith('|') and l_next.endswith('|')):
            # Check lines idx+1 to idx+6 to see if table resumes
            for offset in range(1, 8):
                if idx + offset < len(lines):
                    cand = lines[idx + offset].strip()
                    if cand.startswith('|') and cand.endswith('|'):
                        between = [lines[idx + k].strip() for k in range(1, offset) if lines[idx + k].strip()]
                        # If the text between is just page numbers, UDCPR headers, etc.
                        is_page_break = all(
                            re.match(r'^(UDCPR[- ]?2020|\d+|[IVXLCDM]+|icon:.*|logo:.*)$', b, re.IGNORECASE) or b == ''
                            for b in between
                        )
                        if is_page_break and len(between) > 0:
                            split_tables.append((idx + 1, idx + offset + 1, between, l1, cand))
                        break

print(f"\nTables split across page breaks: {len(split_tables)}")
for st in split_tables[:10]:
    print(f"  Split between L{st[0]} and L{st[1]}: intermediary = {st[2]}")
    print(f"    Pre:  {st[3][:60]}")
    print(f"    Post: {st[4][:60]}")

# 3. Check for HTML tables
html_tables = [idx + 1 for idx, l in enumerate(lines) if '<table' in l.lower()]
print(f"\nHTML <table> tags found: {len(html_tables)}")

# 4. Check for broken math / formulas / corrupted characters
corrupted_chars = []
for idx, l in enumerate(lines):
    # Check for replacement characters \ufffd or weird OCR patterns
    if '\ufffd' in l or '' in l:
        corrupted_chars.append((idx + 1, l.strip()))

print(f"\nLines with unicode replacement character ( / \\ufffd): {len(corrupted_chars)}")
for cc in corrupted_chars[:10]:
    print(f"  L{cc[0]}: {cc[1][:80]}")

