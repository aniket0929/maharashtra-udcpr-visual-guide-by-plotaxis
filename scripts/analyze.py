import re

with open('ucpr_real.md', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")

# Search for chapters
chapter_re = re.compile(r'^(#+\s*)?CHAPTER\s*[-–—:]?\s*(\d+)', re.IGNORECASE)
found_chapters = []
for idx, line in enumerate(lines):
    clean = line.strip()
    m = chapter_re.match(clean)
    if m:
        next_line = lines[idx+1].strip() if idx+1 < len(lines) else ""
        next_line2 = lines[idx+2].strip() if idx+2 < len(lines) else ""
        found_chapters.append((idx+1, clean, next_line, next_line2))

print(f"\nFound {len(found_chapters)} Chapter occurrences:")
for ch in found_chapters:
    print(f"Line {ch[0]}: {ch[1]} | {ch[2]} | {ch[3]}")
