"""
UDCPR Visual Guide - CHAPTER 15 FULL LESSON BUILDER (MODULAR ORCHESTRATOR)
Executes building of all 3 comprehensive Drawing Sheet lessons for Chapter 15: Regulations for Special Activities / Plans.
Each lesson module resides in `scripts/ch15_lessons/` for clarity and modularity.
"""

import os
import sys

# Ensure current script folder is on sys.path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from generate_lessons import create_lesson_page
from ch15_lessons import CH15_LESSONS

sys.stdout.reconfigure(encoding='utf-8')

def build_all_ch15():
    print("==================================================================")
    print(f"🏗️  BUILDING COMPLETE CHAPTER 15 CURRICULUM ({len(CH15_LESSONS)} MODULAR LESSONS)")
    print("==================================================================")
    for idx, lesson in enumerate(CH15_LESSONS, 1):
        print(f"[{idx}/{len(CH15_LESSONS)}] Generating {lesson['clause']} - {lesson['title']}...")
        create_lesson_page(lesson)
    print("==================================================================")
    print("🎉 CHAPTER 15 LESSON SUITE SUCCESSFULLY GENERATED!")
    print("==================================================================")

if __name__ == '__main__':
    build_all_ch15()
