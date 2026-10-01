import re
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

os.makedirs('data', exist_ok=True)

with open('ucpr_real.md', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
total_lines = len(lines)
print(f"Read ucpr_real.md: {total_lines} lines.")

# ==========================================
# 1. BUILD GLOSSARY (141 Definitions from Reg 1.3)
# ==========================================
print("\n--- 1. Extracting Glossary Definitions (1.3) ---")

def_lines = lines[686:1185] # Lines 687 to 1185
raw_defs = []
curr_num = None
curr_title = ""
curr_body = []

for idx, line in enumerate(def_lines):
    line_str = line.strip()
    # Match patterns like: **1 Act** - means ... or **14 Authority means :** or **1.3.1 ...**
    m = re.match(r'^\*\*(\d+)\s+([^*]+)\*\*(.*)', line_str)
    if m:
        if curr_num is not None:
            raw_defs.append({
                'num': curr_num,
                'title': curr_title,
                'text': '\n'.join(curr_body).strip()
            })
        curr_num = int(m.group(1))
        curr_title = m.group(2).strip(' -:')
        after = m.group(3).strip(' -:')
        curr_body = [after] if after else []
    else:
        if curr_num is not None:
            # Filter out running page markers like UDCPR-2020 or pure page numbers
            if not re.match(r'^(UDCPR[- ]?2020|\d+|[IVXLCDM]+)$', line_str, re.IGNORECASE):
                curr_body.append(line_str)

if curr_num is not None:
    raw_defs.append({
        'num': curr_num,
        'title': curr_title,
        'text': '\n'.join(curr_body).strip()
    })

print(f"Extracted {len(raw_defs)} raw definitions from Reg. 1.3.")

# Categorization mapping helper
def categorize_term(title, body):
    t = title.lower()
    b = body.lower()
    if any(k in t for k in ['fsi', 'floor space', 'built up', 'carpet', 'tenement', 'dwelling', 'basic fsi']):
        return "FSI & Density"
    if any(k in t for k in ['setback', 'margin', 'height', 'access', 'road', 'street', 'curb', 'frontage', 'corridor', 'depth of site']):
        return "Setbacks, Height & Roads"
    if any(k in t for k in ['amenity', 'open space', 'cluster', 'group housing', 'row housing', 'plot', 'net plot', 'site']):
        return "Land Layout & Zoning"
    if any(k in t for k in ['fire', 'refuge', 'smoke', 'exit', 'escape', 'alarm']):
        return "Fire & Life Safety"
    if any(k in t for k in ['parking', 'garage', 'ramp']):
        return "Parking & Vehicles"
    if any(k in t for k in ['balcony', 'chajja', 'canopy', 'porch', 'plinth', 'podium', 'terrace', 'stair', 'lift', 'room height', 'habitable', 'kitchen', 'water closet', 'loft', 'mezzanine', 'basement', 'cellar', 'atrium']):
        return "Building Components"
    if any(k in t for k in ['act', 'authority', 'applicant', 'owner', 'architect', 'engineer', 'supervisor', 'permit', 'permission', 'development rights', 'annual statements', 'non-conforming', 'unsafe']):
        return "Procedures & Governance"
    if any(k in t for k in ['solar', 'photovoltaic', 'grey water', 'water course', 'energy efficient']):
        return "Sustainability & Environment"
    return "General Regulations"

# Plain language summaries for top terms to aid student understanding
def get_plain_summary(num, title, body):
    summaries = {
        1: "The statutory parent legislation: Maharashtra Regional & Town Planning Act, 1966.",
        7: "Statutory mandatory open land reserved in layouts for civic amenities like schools, parks, health clubs, and utilities.",
        8: "Ready Reckoner rates published annually by the government, used to compute land value, premium FSI fees, and development charges.",
        10: "Clear unobstructed vehicular and pedestrian approach to any plot or structure.",
        16: "Horizontal cantilevered projection with a parapet/handrail, open on at least one side, serving a room.",
        17: "The fundamental base Floor Space Index allowed on a plot as a matter of right before purchasing premium FSI or loading TDR.",
        18: "Lower storey below ground level, permitted strictly for non-habitable uses like parking, HVAC, transformers, and storage.",
        21: "Total area covered by a building on all floors, including internal walls and structural columns.",
        23: "Vertical clearance measured from the average surrounding road/ground crest to the top structural roof slab or terrace parapet.",
        25: "Net usable floor area inside an apartment/shop, excluding external walls, service shafts, and exclusive balconies (matches RERA definition).",
        29: "High-density core city or historic Gaothan areas with special relaxed setbacks and higher density rules.",
        31: "Statutory Gaothan / Old core areas marked on Development Plans with tailored setback and FSI regulations.",
        40: "Legal rights granted to a landowner or developer to carry out construction up to the maximum permissible building potential.",
        63: "Floor Space Index: The ratio of total covered built-up area across all floors divided by the gross or net plot area.",
        66: "Mandatory clear setback space between the front boundary of the plot (facing the road) and the exterior wall of the building.",
        70: "A development scheme consisting of two or more independent residential buildings or blocks on a single large layout plot.",
        72: "Any room designed for human occupation (bedrooms, living rooms, study) requiring statutory light, ventilation, and minimum height.",
        74: "Any building exceeding 15 meters in height (or 24 meters in certain provisions), triggering strict fire tower and 6m all-round setbacks.",
        76: "Statutory 10% recreational green open space required for any layout or subdivision on plots measuring 0.4 hectares (4,000 sq.m) or more.",
        85: "Unobstructed clear buffer spaces required between the sides and rear of a building and the respective plot boundaries.",
        90: "The final usable plot area for FSI calculations after deducting DP road widening, public reservations, and statutory amenity surrenders.",
        96: "Statutorily sized vehicular stall (e.g. 2.5m x 5.0m for cars) with designated driveway access and turning radius.",
        99: "The elevated base masonry platform of a building measured from ground level, designed to protect habitable floors from water logging.",
        103: "An extended structural platform (often 1 to 3 storeys high) covering a larger footprint than the tower above, predominantly used for multi-level parking.",
        105: "A fire-resistant cantilevered balcony or protected floor designated as a safe gathering refuge point for occupants during a high-rise fire.",
        131: "An independent dwelling unit designed for occupancy by a single family or household.",
        133: "Transferable Development Rights: Credit issued as a Development Rights Certificate (DRC) when land is surrendered for public reservations or roads."
    }
    if num in summaries:
        return summaries[num]
    # General fallback clean summary
    first_sentence = body.split('.')[0] if '.' in body else body[:140]
    first_sentence = re.sub(r'\s+', ' ', first_sentence).strip()
    return f"{title}: {first_sentence}."

glossary_items = []
for d in raw_defs:
    num = d['num']
    title = d['title']
    body = d['text']
    category = categorize_term(title, body)
    plain_summary = get_plain_summary(num, title, body)
    
    # Check if amended
    has_amend = bool(re.search(r'(\(\s*#\s*\)|<sup>\s*\(?#\)?\s*</sup>)', body))
    
    # Related clauses mapping
    related = []
    if category == "FSI & Density":
        related = ["Reg. 3.9", "Reg. 6.3", "Reg. 7.1", "Table 6-A"]
    elif category == "Setbacks, Height & Roads":
        related = ["Reg. 6.1", "Reg. 6.2", "Table 6-C", "Table 6-E"]
    elif category == "Parking & Vehicles":
        related = ["Reg. 8.1", "Reg. 8.2", "Table 8-1"]
    elif category == "Land Layout & Zoning":
        related = ["Reg. 3.1", "Reg. 3.4", "Reg. 3.5", "Reg. 3.8"]
    elif category == "Fire & Life Safety":
        related = ["Reg. 9.28", "Reg. 9.29", "Reg. 13.1"]
    else:
        related = ["Reg. 1.0", "Reg. 2.1"]
        
    glossary_items.append({
        'id': num,
        'term': title,
        'clause_ref': f"Reg. 1.3({num})",
        'category': category,
        'plain_summary': plain_summary,
        'statutory_definition': body,
        'related_clauses': related,
        'is_amended': has_amend
    })

with open('data/glossary.json', 'w', encoding='utf-8') as f:
    json.dump(glossary_items, f, indent=2, ensure_ascii=False)

print(f"Saved {len(glossary_items)} definitions to data/glossary.json")

