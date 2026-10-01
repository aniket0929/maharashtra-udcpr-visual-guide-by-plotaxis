import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('ucpr_real.md', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

print("Analyzing amended markers...")

# Let's search for any '#' that looks like an amendment marker (not a markdown heading #)
# Markdown headings start with # at line start.
# Amendment markers typically look like (#), <sup>(#)</sup>, <sup>#</sup>, *#, (#*)
amend_patterns = [
    (r'<sup>\s*\(?#\)?\s*</sup>', 'sup_hash'),
    (r'\(\s*#\s*\)', 'paren_hash'),
    (r'\(#\*\)', 'hash_star'),
    (r'\*#', 'star_hash'),
]

matches_by_section = {
    'toc': [],         # lines 172 to 670
    'body': [],        # lines 671 to 15470 (approx end of appendices)
    'appendices': [],  # forms/appendices
    'govt_orders': []  # lines > 16000
}

all_amend_matches = []

for idx, line in enumerate(lines):
    line_num = idx + 1
    # Strip markdown header prefix if any to avoid matching markdown hashes
    line_content = re.sub(r'^#+\s*', '', line)
    
    # Check if there is an amendment marker in this line
    found = False
    for pat, pat_name in amend_patterns:
        if re.search(pat, line_content):
            found = True
            break
            
    if found:
        # Determine region
        if line_num < 671:
            region = 'toc'
        elif line_num <= 13280:
            region = 'body' # Chapters 1 to 15
        elif line_num <= 16000:
            region = 'appendices'
        else:
            region = 'govt_orders'
            
        all_amend_matches.append({
            'line': line_num,
            'region': region,
            'is_heading': line.strip().startswith('#'),
            'text': line.strip()
        })

print(f"Total lines containing amendment marker (#): {len(all_amend_matches)}")
regions_count = {}
for m in all_amend_matches:
    regions_count[m['region']] = regions_count.get(m['region'], 0) + 1
print("Breakdown by region:", regions_count)

# Let's inspect unique regulations / clauses marked with (#) in the body
clause_matches = []
clause_re = re.compile(r'(\d+\.\d+(?:\.\d+)*(?:\s*\([a-z0-9]+\))?)')

print("\n--- Sample of Amended Headings / Clauses in Body ---")
count_body_headings = 0
for m in all_amend_matches:
    if m['region'] == 'body' and m['is_heading']:
        count_body_headings += 1
        if count_body_headings <= 25:
            print(f"L{m['line']}: {m['text']}")

print(f"Total amended headings in body (Chapters 1-15): {count_body_headings}")
