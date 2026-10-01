import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('ucpr_real.md', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

# Map lines to chapters and sections
reg_re = re.compile(r'^(?:#+\s*)?(\d+\.\d+(?:\.\d+)*)\s*(.*)')
ch_re = re.compile(r'CHAPTER\s*[-–—:]?\s*(\d+)', re.IGNORECASE)

curr_ch = "Chapter 1"
curr_reg = "General"
curr_reg_title = ""

amend_entries = []

# Scan body (lines 670 to 15564)
for idx in range(670, 15564):
    line_num = idx + 1
    raw = lines[idx]
    clean = raw.strip()
    
    m_ch = ch_re.search(clean)
    if m_ch:
        curr_ch = f"Chapter {m_ch.group(1)}"
        
    m_r = reg_re.match(clean)
    if m_r:
        curr_reg = m_r.group(1)
        curr_reg_title = m_r.group(2).strip(' -:')
        
    if re.search(r'(\(\s*#\s*\)|<sup>\s*\(?#\)?\s*</sup>)', clean):
        # Look ahead 1-5 lines for the citation if this is a heading or footnote
        citation = ""
        for look in range(max(0, idx - 2), min(len(lines), idx + 6)):
            l_cand = lines[look].strip()
            if re.search(r'(Clarification|Directive|Order|Letter|No\.|dt\.|vide)', l_cand, re.IGNORECASE) and '#' in l_cand:
                citation = l_cand
                break
        if not citation:
            citation = clean
            
        amend_entries.append({
            'line': line_num,
            'chapter': curr_ch,
            'clause': curr_reg,
            'clause_title': curr_reg_title or curr_reg,
            'text': clean,
            'citation': citation
        })

print(f"Captured {len(amend_entries)} amendment entries.")

# Group by distinct clause
grouped = {}
for e in amend_entries:
    c = e['clause']
    if c not in grouped:
        grouped[c] = {
            'clause': c,
            'title': e['clause_title'],
            'chapter': e['chapter'],
            'occurrences': []
        }
    grouped[c]['occurrences'].append({
        'line': e['line'],
        'text': e['text'],
        'citation': e['citation']
    })

print(f"Grouped into {len(grouped)} distinct clauses.")

# Format cleanly for amendments.json
amendments_list = []
for clause, item in sorted(grouped.items()):
    # Determine the primary clarification document
    citations = [occ['citation'] for occ in item['occurrences'] if occ['citation']]
    primary_citation = citations[0] if citations else "Government Clarification under Regulation 1.10"
    
    # Clean up citation text
    primary_citation = re.sub(r'[*_#<>/sup]+', '', primary_citation).strip()
    
    amendments_list.append({
        'clause': f"Reg. {clause}",
        'title': item['title'] or f"Regulation {clause}",
        'chapter': item['chapter'],
        'impact_summary': f"Clarifications and executive interpretations issued by the Urban Development Department regarding {item['title'] or clause}.",
        'citation': primary_citation,
        'occurrences_count': len(item['occurrences']),
        'line_numbers': [occ['line'] for occ in item['occurrences']],
        'raw_excerpts': [occ['text'] for occ in item['occurrences']]
    })

with open('data/amendments.json', 'w', encoding='utf-8') as f:
    json.dump(amendments_list, f, indent=2, ensure_ascii=False)

print(f"Saved {len(amendments_list)} clarified clauses to data/amendments.json")
