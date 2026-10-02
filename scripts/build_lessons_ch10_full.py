"""
UDCPR Visual Guide - CHAPTER 10 FULL LESSON BUILDER (MODULAR ORCHESTRATOR)
Executes building of all 7 comprehensive Drawing Sheet lessons for Chapter 10: City Specific Regulations.
Each lesson module resides in `scripts/ch10_lessons/` for clarity and modularity.
"""

import os
import sys

# Ensure current script folder is on sys.path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from generate_lessons import create_lesson_page
from ch10_lessons import CH10_LESSONS

sys.stdout.reconfigure(encoding='utf-8')

def build_all_ch10():
    print("==================================================================")
    print(f"🏗️  BUILDING COMPLETE CHAPTER 10 CURRICULUM ({len(CH10_LESSONS)} MODULAR LESSONS)")
    print("==================================================================")
    for idx, lesson in enumerate(CH10_LESSONS, 1):
        print(f"[{idx}/{len(CH10_LESSONS)}] Generating {lesson['clause']} - {lesson['title']}...")
        create_lesson_page(lesson)
    print("==================================================================")
    print("🎉 CHAPTER 10 LESSON SUITE SUCCESSFULLY GENERATED!")
    print("==================================================================")

if __name__ == '__main__':
    build_all_ch10()
