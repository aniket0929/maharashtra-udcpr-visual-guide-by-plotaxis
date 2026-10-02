import json
import os
import re

def render_callout(item):
    return f"""
          <!-- In-Situ Statutory Clarification Callout -->
          <div class="clarification-callout" id="{item['anchor']}">
            <div class="callout-header">
              <div class="callout-badge-row">
                <span class="badge badge-clause">{item['clause']}</span>
                <span class="badge badge-amended">(#) Clarified</span>
                <span class="badge" style="background:var(--paper); color:var(--ink-soft); border:1px solid var(--line-strong);">{item['chapter']}</span>
              </div>
              <span class="callout-ref">📅 {item['order_ref']}</span>
            </div>

            <h4 class="callout-title">
              {item['title']}
            </h4>

            <div class="callout-grid">
              <div class="callout-pane">
                <div class="callout-label ambiguity">❓ The Practical Ambiguity / Dispute</div>
                <p style="margin:0; font-family:var(--sans);">{item['ambiguity']}</p>
              </div>

              <div class="callout-pane">
                <div class="callout-label ruling">⚖️ Statutory Govt Ruling (Sec. 154 MRTP)</div>
                <p style="margin:0; font-family:var(--sans);">{item['ruling']}</p>
              </div>

              <div class="callout-pane-full">
                <div class="callout-label takeaway">📐 Practical Takeaway for Architects &amp; Students</div>
                <p style="margin:0; font-family:var(--sans); font-weight:500;">{item['takeaway']}</p>
              </div>
            </div>
          </div>
"""

def inject_into_file(filepath, injections):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False
    for target_pattern, item in injections:
        anchor_id = item['anchor']
        if f'id="{anchor_id}"' in content:
            print(f"Anchor {anchor_id} already exists in {filepath}. Skipping.")
            continue

        callout_html = render_callout(item)
        
        # Search for target pattern
        match = re.search(target_pattern, content, re.DOTALL)
        if match:
            # Insert after the matched block or at the match position
            insert_pos = match.end()
            content = content[:insert_pos] + "\n" + callout_html + content[insert_pos:]
            modified = True
            print(f"Injected {anchor_id} into {filepath}")
        else:
            print(f"Warning: pattern '{target_pattern}' not found in {filepath}")

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully updated {filepath}")

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    clarifications_path = os.path.join(base_dir, 'data', 'clarifications.json')
    with open(clarifications_path, 'r', encoding='utf-8') as f:
        items = json.load(f)

    items_by_id = {it['id']: it for it in items}

    # 1. Chapter 14
    ch14_path = os.path.join(base_dir, 'chapters', 'ch14.html')
    inject_into_file(ch14_path, [
        (r'reg-14-3-affordable-housing-and-pmay\.html.*?</div>\s*</div>', items_by_id['clarification-14-4-1']),
        (r'reg-14-6-urban-renewal-cluster-redevelopment\.html.*?</div>\s*</div>', items_by_id['clarification-14-8-7']),
    ])

    # 2. Chapter 6
    ch06_path = os.path.join(base_dir, 'chapters', 'ch06.html')
    inject_into_file(ch06_path, [
        (r'reg-6-1-fsi-stacking-and-building-potential\.html.*?</div>', items_by_id['clarification-6-3-xiv']),
        (r'reg-6-1-fsi-stacking-and-building-potential\.html.*?</div>', items_by_id['clarification-6-3-xii']),
        (r'reg-6-2-front-setbacks-and-street-alignments\.html.*?</div>', items_by_id['clarification-6-2-3-a']),
        (r'reg-6-2-3-side-rear-margins-and-h5-rule\.html.*?</div>', items_by_id['clarification-6-2-3-b']),
    ])

    # 3. Chapter 2
    ch02_path = os.path.join(base_dir, 'chapters', 'ch02.html')
    inject_into_file(ch02_path, [
        (r'reg-2-2-fees-and-charges\.html.*?</div>', items_by_id['clarification-2-2-12']),
        (r'reg-2-2-fees-and-charges\.html.*?</div>', items_by_id['clarification-2-2-13-transfer']),
        (r'reg-2-2-fees-and-charges\.html.*?</div>', items_by_id['clarification-2-2-13-pline']),
        (r'reg-2-2-fees-and-charges\.html.*?</div>', items_by_id['clarification-2-2-14']),
        (r'reg-2-6-commencement-and-occupancy\.html.*?</div>', items_by_id['clarification-2-7-1']),
    ])

    # 4. Chapter 3
    ch03_path = os.path.join(base_dir, 'chapters', 'ch03.html')
    inject_into_file(ch03_path, [
        (r'reg-3-3-internal-layout-roads\.html.*?</div>', items_by_id['clarification-3-3-8-b']),
    ])

    # 5. Chapter 4
    ch04_path = os.path.join(base_dir, 'chapters', 'ch04.html')
    inject_into_file(ch04_path, [
        (r'reg-4-8-1-industrial-to-residential-conversion\.html.*?</div>', items_by_id['clarification-4-8-1-xvi']),
        (r'reg-4-11-agricultural-and-green-zone\.html.*?</div>', items_by_id['clarification-4-11-ix']),
    ])

    # 6. Chapter 9
    ch09_path = os.path.join(base_dir, 'chapters', 'ch09.html')
    inject_into_file(ch09_path, [
        (r'reg-9-11-basements-podiums-and-vehicular-ramps\.html.*?</div>', items_by_id['clarification-9-13']),
        (r'reg-9-28-exit-requirements-and-staircases\.html.*?</div>', items_by_id['clarification-9-27-1']),
        (r'reg-9-28-exit-requirements-and-staircases\.html.*?</div>', items_by_id['clarification-9-28-8']),
    ])

    # 7. Chapter 10
    ch10_path = os.path.join(base_dir, 'chapters', 'ch10.html')
    inject_into_file(ch10_path, [
        (r'reg-10-3-nagpur-nmc-and-nmrda\.html.*?</div>\s*</div>', items_by_id['clarification-10-4-1']),
    ])

    # 8. Chapter 11
    ch11_path = os.path.join(base_dir, 'chapters', 'ch11.html')
    inject_into_file(ch11_path, [
        (r'reg-11-2-6-tdr-utilisation-indexation-and-restrictions\.html.*?</div>\s*</div>', items_by_id['clarification-11-2-6']),
    ])

    # 9. Chapter 15
    ch15_path = os.path.join(base_dir, 'chapters', 'ch15.html')
    inject_into_file(ch15_path, [
        (r'reg-15-3-local-area-plans-and-street-design\.html.*?</div>\s*</div>', items_by_id['clarification-c-7']),
    ])

if __name__ == '__main__':
    main()
