"""
UDCPR Visual Guide - CHAPTER 4 FULL LESSON BUILDER (MODULAR ORCHESTRATOR)
Executes building of all 6 comprehensive Drawing Sheet lessons for Chapter 4: Land Use Classification & Permissible Uses.
Each lesson module resides in `scripts/ch04_lessons/` for clarity and modularity.
"""

import os
import sys

# Ensure current script folder is on sys.path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from generate_lessons import create_lesson_page
from ch04_lessons import CH04_LESSONS

sys.stdout.reconfigure(encoding='utf-8')

def build_all_ch04():
    print("==================================================================")
    print(f"🏗️  BUILDING COMPLETE CHAPTER 4 CURRICULUM ({len(CH04_LESSONS)} MODULAR LESSONS)")
    print("==================================================================")
    for idx, lesson in enumerate(CH04_LESSONS, 1):
        print(f"[{idx}/{len(CH04_LESSONS)}] Generating {lesson['clause']} - {lesson['title']}...")
        create_lesson_page(lesson)
    print("==================================================================")
    print("🎉 CHAPTER 4 LESSON SUITE SUCCESSFULLY GENERATED!")
    print("==================================================================")

if __name__ == '__main__':
    build_all_ch04()
