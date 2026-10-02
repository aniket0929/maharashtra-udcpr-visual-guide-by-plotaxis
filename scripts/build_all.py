"""
UDCPR Visual Guide - MASTER BUILD PIPELINE
Rebuilds the entire site data layer, pages, and executes statutory verification from ucpr_real.md.

Usage:
    python scripts/build_all.py
"""

import subprocess
import sys
import time

sys.stdout.reconfigure(encoding='utf-8')

steps = [
    ("Step 1: Heading Tree & Structural Extraction", "python scripts/build_heading_tree.py"),
    ("Step 2: Build Complete Glossary (141 Definitions)", "python scripts/build_glossary.py"),
    ("Step 3: Build Master Formulas & Interactive Engines", "python scripts/build_formulas.py"),
    ("Step 4: Build Amendments & Clarifications (#) Tracker", "python scripts/build_amendments.py"),
    ("Step 5: Build Government Orders & Gazette Chronology", "python scripts/build_govt_orders.py"),
    ("Step 6: Generate Full Chapter 1 Blueprint Lessons (Reg 1.0 - 1.10)", "python scripts/build_lessons_ch01_full.py"),
    ("Step 7: Generate Full Chapter 2 Blueprint Lessons (Reg 2.1 - 2.15)", "python scripts/build_lessons_ch02_full.py"),
    ("Step 8: Generate Full Chapter 3 Blueprint Lessons (Reg 3.1 - 3.13)", "python scripts/build_lessons_ch03_full.py"),
    ("Step 9: Generate Full Chapter 4 Blueprint Lessons (Reg 4.1 - 4.27)", "python scripts/build_lessons_ch04_full.py"),
    ("Step 10: Generate Full Chapter 5 Blueprint Lessons (Reg 5.1 - 5.12)", "python scripts/build_lessons_ch05_full.py"),
    ("Step 11: Generate Full Chapter 6 Blueprint Lessons (Reg 6.1 - 6.15)", "python scripts/build_lessons_ch06_full.py"),
    ("Step 12: Generate Full Chapter 7 Blueprint Lessons (Reg 7.1 - 7.13)", "python scripts/build_lessons_ch07_full.py"),
    ("Step 13: Generate Full Chapter 8 Blueprint Lessons (Reg 8.1 - 8.2)", "python scripts/build_lessons_ch08_full.py"),
    ("Step 14: Generate Full Chapter 9 Blueprint Lessons (Reg 9.1 - 9.33)", "python scripts/build_lessons_ch09_full.py"),
    ("Step 15: Generate Full Chapter 10 Blueprint Lessons (Reg 10.1 - 10.16)", "python scripts/build_lessons_ch10_full.py"),
    ("Step 16: Generate Full Chapter 11 Blueprint Lessons (Reg 11.1 - 11.3)", "python scripts/build_lessons_ch11_full.py"),
    ("Step 17: Generate Full Chapter 12 Blueprint Lessons (Reg 12.1 - 12.7)", "python scripts/build_lessons_ch12_full.py"),
    ("Step 18: Generate Full Chapter 13 Blueprint Lessons (Reg 13.1 - 13.6)", "python scripts/build_lessons_ch13_full.py"),
    ("Step 19: Generate Full Chapter 14 Blueprint Lessons (Reg 14.1 - 14.13)", "python scripts/build_lessons_ch14_full.py"),
    ("Step 20: Generate Full Chapter 15 Blueprint Lessons (Reg 15.1 - 15.4 & App-M)", "python scripts/build_lessons_ch15_full.py"),
    ("Step 21: Build 7 Interactive CAD Practice Workbenches", "python scripts/build_all_topics.py"),
    ("Step 22: Run Automated Statutory Verification Audit", "python scripts/generate_verification_report.py"),
    ("Step 23: Run Link Integrity & Semantic Structure Audit", "python scripts/audit_links.py")
]

print("================================================================")
print("🚀 STARTING FULL UDCPR Visual Guide BUILD PIPELINE")
print("================================================================\n")

start_time = time.time()

for idx, (title, cmd) in enumerate(steps, 1):
    print(f"[{idx}/{len(steps)}] {title}...")
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding='utf-8')
    if res.returncode != 0:
        print(f"❌ FAILED: {title}")
        print(res.stderr)
        sys.exit(1)
    else:
        # Print first 2 lines of output
        lines = [l for l in res.stdout.strip().splitlines() if l.strip()]
        for l in lines[:2]:
            print(f"    ✓ {l}")

duration = time.time() - start_time
print("\n================================================================")
print(f"🎉 BUILD PIPELINE COMPLETED IN {duration:.2f}s")
print("Site is ready for local preview or static deployment.")
print("================================================================\n")
