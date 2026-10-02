import glob
import re

files = glob.glob('**/*.html', recursive=True)
patterns = {}
for f in files:
    if f == 'govt-orders.html':
        continue
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    m = re.search(r'<ul class="nav-menu">(.*?)</ul>', c, re.DOTALL)
    if m:
        menu_text = m.group(1).strip()
        # simplify by removing active class
        norm = re.sub(r'\s+class="active"', '', menu_text)
        norm = re.sub(r'\s+', ' ', norm)
        patterns.setdefault(norm, []).append(f)

print(f"Total patterns found: {len(patterns)}")
for i, (p, flist) in enumerate(patterns.items()):
    print(f"--- Pattern {i+1} ({len(flist)} files, e.g. {flist[0]}) ---")
    print(p[:200])
