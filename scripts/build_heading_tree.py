import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('ucpr_real.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Parse headings in each chapter
chapters_info = [
    (1, "ADMINISTRATION", 671, 1310),
    (2, "DEVELOPMENT PERMISSION AND COMMENCEMENT CERTIFICATE", 1311, 2067),
    (3, "GENERAL LAND DEVELOPMENT REQUIREMENTS", 2068, 2820),
    (4, "LAND USE CLASSIFICATION AND PERMISSIBLE USES", 2821, 3945),
    (5, "ADDITIONAL PROVISIONS FOR REGIONAL PLAN AREAS", 3946, 4757),
    (6, "GENERAL BUILDING REQUIREMENTS - SETBACK, MARGINAL DISTANCE, HEIGHT AND PERMISSIBLE FSI", 4758, 5365),
    (7, "HIGHER FSI FOR CERTAIN USES", 5366, 5966),
    (8, "PARKING, LOADING AND UNLOADING SPACES", 5967, 6171),
    (9, "REQUIREMENTS OF PART OF BUILDING", 6172, 6973),
    (10, "CITY SPECIFIC REGULATIONS", 6974, 8205),
    (11, "ACQUISITION AND DEVELOPMENT OF RESERVED SITES IN DEVELOPMENT PLANS", 8206, 8700),
    (12, "STRUCTURAL SAFETY, WATER SUPPLY, DRAINAGE AND SANITARY REQUIREMENTS, OUTDOOR DISPLAY AND OTHER SERVICES", 8701, 9038),
    (13, "SPECIAL PROVISIONS FOR CERTAIN BUILDINGS", 9039, 9424),
    (14, "SPECIAL SCHEMES", 9425, 13173),
    (15, "REGULATIONS FOR SPECIAL ACTIVITIES / PLANS", 13174, 13281),
    (16, "APPENDICES (A-M)", 13282, 15564),
    (17, "GOVERNMENT ORDERS (MARATHI APPENDIX)", 15565, len(lines))
]

tree = []

heading_re = re.compile(r'^(#+)\s*(.*)')
amend_re = re.compile(r'(\(\s*#\s*\)|<sup>\s*\(?#\)?\s*</sup>|#(?:\s+|$))')

for ch_num, ch_title, start_l, end_l in chapters_info:
    ch_obj = {
        'chapter': ch_num,
        'title': ch_title,
        'start_line': start_l,
        'end_line': end_l,
        'sections': [],
        'amended_count': 0
    }
    
    # Track sections in this chapter
    for l_idx in range(start_l - 1, end_l):
        line = lines[l_idx]
        m = heading_re.match(line.strip())
        if m:
            level = len(m.group(1))
            htext = m.group(2).strip()
            
            # Skip repeating chapter title headers
            if htext.upper().startswith("CHAPTER") or htext.upper() == ch_title:
                continue
                
            has_amend = bool(amend_re.search(htext))
            
            # Also check text inside the section for amendments
            ch_obj['sections'].append({
                'line': l_idx + 1,
                'level': level,
                'title': htext,
                'has_amend_marker': has_amend
            })
            
        if amend_re.search(line):
            ch_obj['amended_count'] += 1

    tree.append(ch_obj)

# Output summary
print("=== UDCPR-2020 HEADING TREE SUMMARY ===")
total_amended_lines = sum(c['amended_count'] for c in tree)
print(f"Total Sections / Headings in tree: {sum(len(c['sections']) for c in tree)}")
print(f"Total lines with (#) across all chapters: {total_amended_lines}")

for c in tree:
    print(f"\nChapter {c['chapter']}: {c['title']} (L{c['start_line']}-L{c['end_line']})")
    print(f"  Headings: {len(c['sections'])}, (#) occurrences in text: {c['amended_count']}")
    # print top level sections (level 2 or first 5)
    for s in c['sections'][:8]:
        amend_flag = " [AMENDED (#)]" if s['has_amend_marker'] else ""
        print(f"    L{s['line']} (h{s['level']}): {s['title'][:75]}{amend_flag}")
    if len(c['sections']) > 8:
        print(f"    ... and {len(c['sections']) - 8} more sections")

# Save full tree to JSON
with open('scripts/udcpr_heading_tree.json', 'w', encoding='utf-8') as f:
    json.dump(tree, f, indent=2, ensure_ascii=False)

print("\nSaved full heading tree to scripts/udcpr_heading_tree.json")
