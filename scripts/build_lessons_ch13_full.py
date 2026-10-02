"""
UDCPR Visual Guide - CHAPTER 13 FULL LESSON BUILDER (MODULAR ORCHESTRATOR)
Executes building of all 4 comprehensive Drawing Sheet lessons for Chapter 13: Special Provisions for Certain Buildings.
Each lesson module resides in `scripts/ch13_lessons/` for clarity and modularity.
"""

import os
import sys

# Ensure current script folder is on sys.path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from generate_lessons import create_lesson_page
from ch13_lessons import CH13_LESSONS

sys.stdout.reconfigure(encoding='utf-8')

def build_all_ch13():
    print("==================================================================")
    print(f"🏗️  BUILDING COMPLETE CHAPTER 13 CURRICULUM ({len(CH13_LESSONS)} MODULAR LESSONS)")
    print("==================================================================")
    for idx, lesson in enumerate(CH13_LESSONS, 1):
        print(f"[{idx}/{len(CH13_LESSONS)}] Generating {lesson['clause']} - {lesson['title']}...")
        create_lesson_page(lesson)
    print("==================================================================")
    print("🎉 CHAPTER 13 LESSON SUITE SUCCESSFULLY GENERATED!")
    print("==================================================================")

if __name__ == '__main__':
    build_all_ch13()
