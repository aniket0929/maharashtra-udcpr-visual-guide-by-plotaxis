import json

with open('scripts/udcpr_heading_tree.json', 'r', encoding='utf-8') as f:
    tree = json.load(f)

for ch in tree[:5]:
    print(f"\n==========================================")
    print(f"Chapter {ch['chapter']}: {ch['title']} (Lines {ch['start_line']} - {ch['end_line']})")
    print(f"Total headings: {len(ch['sections'])}, (#) occurrences: {ch['amended_count']}")
    print(f"==========================================")
    for s in ch['sections']:
        am = " [AMENDED (#)]" if s['has_amend_marker'] else ""
        print(f"  L{s['line']} (h{s['level']}) {s['title']}{am}")
