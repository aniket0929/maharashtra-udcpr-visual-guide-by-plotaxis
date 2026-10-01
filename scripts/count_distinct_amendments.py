import re
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

with open('ucpr_real.md', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()

# Let's inspect TOC entries with '#'
toc_clauses = []
for idx in range(171, 650):
    line = lines[idx]
    if '#' in line:
        # Extract regulation number if present
        m = re.search(r'\|\s*(\d+(?:\.\d+)*(?:[A-Za-z0-9\.\s\(\)]*))\s*(?:\*|#|\+)', line)
        m2 = re.search(r'\|\s*([A-Za-z0-9\.\s\(\)\*#\+]+)\|', line)
        toc_clauses.append((idx + 1, line.strip()))

print(f"Total TOC rows with '#': {len(toc_clauses)}")

# Now scan body (lines 671 to 15564) for all clauses with (#)
# A clause can have (#) in its heading OR in a clarification note attached to it
# Let's track:
# - Heading with (#)
# - Clarification notes mentioning specific letters/orders
body_amended_clauses = {}
curr_reg = "General"

reg_heading_re = re.compile(r'^(?:#+\s*)?(\d+\.\d+(?:\.\d+)*)\s*(.*)')
clarif_re = re.compile(r'(\(\s*#\s*\)|<sup>\s*\(?#\)?\s*</sup>)')

for idx in range(670, 15564):
    line = lines[idx]
    m_h = reg_heading_re.match(line.strip())
    if m_h:
        curr_reg = m_h.group(1)
    
    if clarif_re.search(line):
        if curr_reg not in body_amended_clauses:
            body_amended_clauses[curr_reg] = []
        body_amended_clauses[curr_reg].append({
            'line': idx + 1,
            'text': line.strip()
        })

print(f"Total distinct regulations in body with (#) marker or clarification: {len(body_amended_clauses)}")
print("\nRegulations list:")
for reg, occurrences in sorted(body_amended_clauses.items()):
    print(f"  Reg {reg}: {len(occurrences)} occurrence(s), e.g. L{occurrences[0]['line']}: {occurrences[0]['text'][:80]}")

