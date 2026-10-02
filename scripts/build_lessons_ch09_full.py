"""
UDCPR Visual Guide - CHAPTER 9 FULL LESSON BUILDER (MODULAR ORCHESTRATOR)
Executes building of all 5 comprehensive Drawing Sheet lessons for Chapter 9: Requirements of Parts of Buildings.
Each lesson module resides in `scripts/ch09_lessons/` for clarity and modularity.
"""

import os
import sys

# Ensure current script folder is on sys.path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from generate_lessons import create_lesson_page
from ch09_lessons import CH09_LESSONS

sys.stdout.reconfigure(encoding='utf-8')

def build_all_ch09():
    print("==================================================================")
    print(f"🏗️  BUILDING COMPLETE CHAPTER 9 CURRICULUM ({len(CH09_LESSONS)} MODULAR LESSONS)")
    print("==================================================================")
    for idx, lesson in enumerate(CH09_LESSONS, 1):
        print(f"[{idx}/{len(CH09_LESSONS)}] Generating {lesson['clause']} - {lesson['title']}...")
        create_lesson_page(lesson)
    print("==================================================================")
    print("🎉 CHAPTER 9 LESSON SUITE SUCCESSFULLY GENERATED!")
    print("==================================================================")

if __name__ == '__main__':
    build_all_ch09()
