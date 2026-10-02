"""
UDCPR Visual Guide - CHAPTER 3 FULL LESSON BUILDER (MODULAR ORCHESTRATOR)
Executes building of all 6 comprehensive Drawing Sheet lessons for Chapter 3: General Land Development Requirements.
Each lesson module resides in `scripts/ch03_lessons/` for clarity and modularity.
"""

import os
import sys

# Ensure current script folder is on sys.path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from generate_lessons import create_lesson_page
from ch03_lessons import CH03_LESSONS

sys.stdout.reconfigure(encoding='utf-8')

def build_all_ch03():
    print("==================================================================")
    print(f"🏗️  BUILDING COMPLETE CHAPTER 3 CURRICULUM ({len(CH03_LESSONS)} MODULAR LESSONS)")
    print("==================================================================")
    for idx, lesson in enumerate(CH03_LESSONS, 1):
        print(f"[{idx}/{len(CH03_LESSONS)}] Generating {lesson['clause']} - {lesson['title']}...")
        create_lesson_page(lesson)
    print("==================================================================")
    print("🎉 CHAPTER 3 LESSON SUITE SUCCESSFULLY GENERATED!")
    print("==================================================================")

if __name__ == '__main__':
    build_all_ch03()
