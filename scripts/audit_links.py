import os
import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

html_files = glob.glob('**/*.html', recursive=True)
print(f"Auditing {len(html_files)} HTML files for link integrity...\n")

broken = []
total_links = 0

for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
    for hr in hrefs:
        if hr.startswith('http') or hr.startswith('#') or hr.startswith('mailto:'):
            continue
        total_links += 1
        clean = hr.split('#')[0]
        if clean in ['/', '']:
            target = 'index.html'
        elif clean.startswith('/'):
            target = clean.lstrip('/')
            if target.endswith('/'):
                target += 'index.html'
            elif not os.path.splitext(target)[1]:
                target = os.path.join(target, 'index.html')
        else:
            curr_dir = os.path.dirname(hf)
            target = os.path.normpath(os.path.join(curr_dir, clean))
            if os.path.isdir(target):
                target = os.path.join(target, 'index.html')

        if not os.path.exists(target):
            broken.append((hf, hr, target))

print(f"Total internal links checked: {total_links}")
print(f"Broken links count: {len(broken)}")
if broken:
    for b in broken:
        print(f"  In {b[0]}: '{b[1]}' -> unresolved '{b[2]}'")
else:
    print("ALL internal links 100% RESOLVED and VALID!")
