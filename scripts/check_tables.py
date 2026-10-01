import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('ucpr_real.md', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")

# We can find table blocks by finding consecutive lines starting with '|' (or having '|' separators)
# Let's track tables and look for anomalies.

tables = []
in_table = False
curr_table = []
start_line = 0

for idx, line in enumerate(lines):
    line_num = idx + 1
    stripped = line.strip()
    
    if stripped.startswith('|') and stripped.endswith('|'):
        if not in_table:
            in_table = True
            start_line = line_num
            curr_table = []
        curr_table.append((line_num, stripped))
    else:
        if in_table:
            # Table ended
            tables.append({
                'start': start_line,
                'end': line_num - 1,
                'rows': curr_table
            })
            in_table = False
            curr_table = []

if in_table:
    tables.append({
        'start': start_line,
        'end': len(lines),
        'rows': curr_table
    })

print(f"Total table blocks found: {len(tables)}")

# Analyze each table for integrity:
# 1. Separator line presence (e.g. |---|---|)
# 2. Consistent column count
# 3. Broken rows or column mismatch
# 4. Stray table rows nearby (e.g. separated by a blank line or page header)

table_issues = []

for t_idx, t in enumerate(tables):
    rows = t['rows']
    # Calculate column counts for each row
    col_counts = []
    has_separator = False
    separator_idx = -1
    
    for r_idx, (lnum, r_text) in enumerate(rows):
        # Count cells
        # A row like | a | b | has 2 cells, split by '|' gives ['', ' a ', ' b ', ''] -> len-2
        cells = [c.strip() for c in r_text.split('|')[1:-1]]
        col_counts.append((lnum, len(cells), cells))
        if all(re.match(r'^:?-+:?$', c) for c in cells) and len(cells) > 0:
            has_separator = True
            separator_idx = r_idx

    header_cols = col_counts[0][1] if col_counts else 0
    mismatches = []
    for lnum, c_len, cells in col_counts:
        if c_len != header_cols:
            mismatches.append((lnum, c_len, header_cols, cells))
            
    # Check if table has issues
    issues = []
    if not has_separator:
        issues.append("Missing markdown separator (|---|)")
    if mismatches:
        issues.append(f"Column count mismatch across rows: header has {header_cols} cols, but {len(mismatches)} rows have different counts (e.g. L{mismatches[0][0]} has {mismatches[0][1]} cols)")
    
    # Check for empty cells or suspicious single column table
    if header_cols <= 1:
        issues.append(f"Single-column table (often OCR/conversion artifact): {header_cols} col")
        
    if issues:
        table_issues.append({
            'table_idx': t_idx + 1,
            'start': t['start'],
            'end': t['end'],
            'row_count': len(rows),
            'header_cols': header_cols,
            'issues': issues,
            'sample_header': rows[0][1][:100],
            'mismatches': mismatches[:5]
        })

print(f"\nTables with potential issues/anomalies: {len(table_issues)}")
for ti in table_issues[:20]:
    print(f"\nTable #{ti['table_idx']} (Lines {ti['start']}-{ti['end']}, {ti['row_count']} rows):")
    print(f"  Header: {ti['sample_header']}")
    for iss in ti['issues']:
        print(f"  - Issue: {iss}")

