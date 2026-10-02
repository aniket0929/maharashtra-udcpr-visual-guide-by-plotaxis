import os
import re

def audit_discrepancies():
    print("=== SEARCHING EXCLUSIVELY FOR OUTDATED STATS & LABELS ===")
    
    for root, dirs, files in os.walk('.'):
        if '.git' in root or 'node_modules' in root or 'scripts' in root:
            continue
        for file in sorted(files):
            if file.endswith('.html') or file.endswith('.js'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()

                # Stat boxes
                boxes = re.findall(r'<div class="stat-box">[\s\S]*?<span class="stat-label">([^<]+)</span>[\s\S]*?<span class="stat-value">([^<]+)</span>', content)
                if boxes:
                    print(f"\n[STAT-BOXES in {path}]:")
                    for label, val in boxes:
                        print(f"  {label.strip()} -> {val.strip()}")

                # Specific outdated strings
                patterns = [
                    (r'\b52\s+clarif[a-z]*', 'Outdated 52 clarifications'),
                    (r'\b9\s+master\s+calc[a-z]*', 'Outdated 9 master calculators'),
                    (r'\b9\s+master\s+formula[a-z]*', 'Outdated 9 master formulas'),
                    (r'\b9\s+statutory\s+formula[a-z]*', 'Outdated 9 statutory formulas'),
                    (r'\b9\s+engines?\b', 'Outdated 9 engines'),
                    (r'\b79\s+amend[a-z]*', 'Outdated 79 amendments'),
                ]

                for pat, label in patterns:
                    for line_idx, line in enumerate(content.splitlines(), 1):
                        if re.search(pat, line, re.I):
                            print(f"[{label}] {path}:{line_idx}: {line.strip()[:100]}")

audit_discrepancies()
