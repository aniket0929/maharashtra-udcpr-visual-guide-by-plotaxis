import glob
import re
import os

files = glob.glob('**/*.html', recursive=True)
print(f"Reordering navbars across {len(files)} files...")

updated_count = 0

for f in files:
    if f == 'govt-orders.html':
        continue
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()

    m = re.search(r'<ul class="nav-menu">(.*?)</ul>', content, re.DOTALL)
    if not m:
        continue

    menu_body = m.group(1)
    # Find all <li>...</li> items
    items = re.findall(r'<li class="nav-item">.*?</li>', menu_body, re.DOTALL)

    cat_map = {}
    for it in items:
        clean_it = it.strip()
        if 'glossary.html' in clean_it:
            cat_map['glossary'] = clean_it
        elif '/chapters/' in clean_it:
            cat_map['chapters'] = clean_it
        elif '/topics/' in clean_it:
            cat_map['topics'] = clean_it
        elif 'formulas.html' in clean_it:
            cat_map['formulas'] = clean_it
        elif 'amendments.html' in clean_it:
            cat_map['amendments'] = clean_it

    # Defaults if missing
    if 'glossary' not in cat_map:
        cat_map['glossary'] = '<li class="nav-item"><a href="/glossary.html">Glossary</a></li>'
    if 'chapters' not in cat_map:
        cat_map['chapters'] = '<li class="nav-item"><a href="/chapters/">Chapters</a></li>'
    if 'topics' not in cat_map:
        cat_map['topics'] = '<li class="nav-item"><a href="/topics/">Topics</a></li>'
    if 'formulas' not in cat_map:
        cat_map['formulas'] = '<li class="nav-item"><a href="/formulas.html">Formulas</a></li>'
    if 'amendments' not in cat_map:
        cat_map['amendments'] = '<li class="nav-item"><a href="/amendments.html">Amendments (#)</a></li>'

    # Target sequence: 1. Glossary, 2. Chapters, 3. Topics, 4. Formulas, 5. Amendments
    ordered = [
        cat_map['glossary'],
        cat_map['chapters'],
        cat_map['topics'],
        cat_map['formulas'],
        cat_map['amendments']
    ]

    new_menu = '<ul class="nav-menu">\n        ' + '\n        '.join(ordered) + '\n      </ul>'

    old_ul = m.group(0)
    if old_ul != new_menu:
        content = content[:m.start()] + new_menu + content[m.end():]
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(content)
        updated_count += 1

print(f"Successfully reordered navbars in {updated_count} files.")
