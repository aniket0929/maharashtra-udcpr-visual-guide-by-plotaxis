import re
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

with open('ucpr_real.md', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

lines = text.splitlines()
total_lines = len(lines)
print(f"Total lines in ucpr_real.md: {total_lines}")

# 1. Look for where the Government Orders / Marathi appendix begins
# We look for lines containing Marathi unicode range (\u0900-\u097F) or headers mentioning orders / parishishta
marathi_lines = []
for idx, l in enumerate(lines):
    if re.search(r'[\u0900-\u097F]', l):
        marathi_lines.append(idx + 1)

print(f"Total lines containing Devanagari script: {len(marathi_lines)}")
if marathi_lines:
    print(f"First Devanagari line: L{marathi_lines[0]}: {lines[marathi_lines[0]-1]}")
    # find where clusters of Marathi begin
    for i in range(len(marathi_lines)):
        line_num = marathi_lines[i]
        # check if this is the start of the massive Marathi appendix
        if line_num > 14000:
            print(f"Post-appendices Devanagari at line {line_num}: {lines[line_num-1][:100]}")
            break

# Let's inspect headers between 15000 and the end
print("\n--- Headers from line 15000 onwards ---")
for idx in range(15000, len(lines)):
    line = lines[idx]
    if line.startswith('#'):
        print(f"L{idx+1}: {line[:100]}")
