import glob
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

files = glob.glob('**/*.html', recursive=True)
print(f"Auditing UI consistency across {len(files)} HTML files...\n")

issues = {
    'missing_viewport': [],
    'missing_fonts': [],
    'missing_css_blueprint': [],
    'missing_css_components': [],
    'missing_sheet_container': [],
    'missing_corner_ticks': [],
    'missing_disclaimer': [],
    'missing_nav': [],
    'navbar_order_mismatch': [],
    'missing_search_btn': [],
    'missing_search_modal': [],
    'missing_footer': [],
    'missing_js_app': [],
    'missing_js_search': []
}

expected_nav_order = ['glossary.html', '/chapters/', '/topics/', 'formulas.html', 'amendments.html']

for f in files:
    if f == 'govt-orders.html':
        continue # redirect file
    
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()

    # 1. Viewport
    if 'name="viewport"' not in content:
        issues['missing_viewport'].append(f)

    # 2. Fonts
    if 'fonts.googleapis.com' not in content:
        issues['missing_fonts'].append(f)

    # 3. CSS
    if 'blueprint.css' not in content:
        issues['missing_css_blueprint'].append(f)
    if 'components.css' not in content:
        issues['missing_css_components'].append(f)

    # 4. Sheet container
    if 'class="sheet"' not in content:
        issues['missing_sheet_container'].append(f)

    # 5. Corner ticks
    if 'corner-tick' not in content:
        issues['missing_corner_ticks'].append(f)

    # 6. Disclaimer
    if 'disclaimer-strip' not in content and 'DISCLAIMER:' not in content:
        issues['missing_disclaimer'].append(f)

    # 7. Navigation
    m_nav = re.search(r'<ul class="nav-menu">(.*?)</ul>', content, re.DOTALL)
    if not m_nav:
        issues['missing_nav'].append(f)
    else:
        nav_html = m_nav.group(1)
        items = re.findall(r'href="([^"]+)"', nav_html)
        # Check order of items
        # Each item should map to our 5 categories
        matched_cats = []
        for h in items:
            for exp in expected_nav_order:
                if exp in h:
                    matched_cats.append(exp)
                    break
        if matched_cats != expected_nav_order:
            issues['navbar_order_mismatch'].append((f, matched_cats))

    # 8. Search button
    if 'openSearchModal()' not in content:
        issues['missing_search_btn'].append(f)

    # 9. Search modal backdrop
    if 'search-modal-backdrop' not in content:
        issues['missing_search_modal'].append(f)

    # 10. Footer
    if 'class="sheet-footer"' not in content:
        issues['missing_footer'].append(f)

    # 11. Scripts
    if 'app.js' not in content:
        issues['missing_js_app'].append(f)
    if 'search.js' not in content:
        issues['missing_js_search'].append(f)

total_issues = 0
for k, v in issues.items():
    if v:
        total_issues += len(v)
        print(f"❌ {k.upper()} ({len(v)} occurrences):")
        for item in v[:5]:
            print(f"   - {item}")
        if len(v) > 5:
            print(f"   ... and {len(v) - 5} more")
    else:
        print(f"✅ {k.upper()}: 100% Consistent across all pages")

print(f"\n--- AUDIT SUMMARY: {total_issues} total discrepancies found ---")
