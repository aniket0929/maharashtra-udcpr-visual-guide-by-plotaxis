"""
UDCPR Visual Guide - CHAPTER 8 FULL LESSON BUILDER (MODULAR ORCHESTRATOR)
Executes building of all 4 comprehensive Drawing Sheet lessons for Chapter 8: Parking, Loading and Unloading Spaces.
Each lesson module resides in `scripts/ch08_lessons/` for clarity and modularity.
"""

import os
import sys

# Ensure current script folder is on sys.path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from generate_lessons import create_lesson_page
from ch08_lessons import CH08_LESSONS

sys.stdout.reconfigure(encoding='utf-8')

def build_all_ch08():
    print("==================================================================")
    print(f"🏗️  BUILDING COMPLETE CHAPTER 8 CURRICULUM ({len(CH08_LESSONS)} MODULAR LESSONS)")
    print("==================================================================")
    for idx, lesson in enumerate(CH08_LESSONS, 1):
        print(f"[{idx}/{len(CH08_LESSONS)}] Generating {lesson['clause']} - {lesson['title']}...")
        create_lesson_page(lesson)
    print("==================================================================")
    print("🎉 CHAPTER 8 LESSON SUITE SUCCESSFULLY GENERATED!")
    print("==================================================================")

if __name__ == '__main__':
    build_all_ch08()
