import json
import os

with open('data/clarifications.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

missing = []
for it in items:
    rel_path = it['chapter_file'].lstrip('/')
    if not os.path.exists(rel_path):
        missing.append((it['clause'], 'File does not exist', rel_path))
        continue
    with open(rel_path, 'r', encoding='utf-8') as f_ch:
        content = f_ch.read()
    if f'id="{it["anchor"]}"' not in content:
        missing.append((it['clause'], it['anchor'], rel_path))

print(f"Total clarifications checked: {len(items)}")
if missing:
    print(f"FAILED: {len(missing)} anchors missing:")
    for m in missing:
        print(f"  {m[0]} -> anchor '{m[1]}' in {m[2]}")
else:
    print("SUCCESS: 100% of clarification anchors exist in their respective chapter files!")
