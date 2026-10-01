"""
UDCPR FROM SCRATCH - CHAPTER 14 FULL LESSON BUILDER (MODULAR ORCHESTRATOR)
Executes building of all 7 comprehensive Drawing Sheet lessons for Chapter 14: Special Schemes.
Each lesson module resides in `scripts/ch14_lessons/` for clarity and modularity.
"""

import os
import sys

# Ensure current script folder is on sys.path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from generate_lessons import create_lesson_page
from ch14_lessons import CH14_LESSONS

sys.stdout.reconfigure(encoding='utf-8')

def build_all_ch14():
    print("==================================================================")
    print(f"🏗️  BUILDING COMPLETE CHAPTER 14 CURRICULUM ({len(CH14_LESSONS)} MODULAR LESSONS)")
    print("==================================================================")
    for idx, lesson in enumerate(CH14_LESSONS, 1):
        print(f"[{idx}/{len(CH14_LESSONS)}] Generating {lesson['clause']} - {lesson['title']}...")
        create_lesson_page(lesson)
    print("==================================================================")
    print("🎉 CHAPTER 14 LESSON SUITE SUCCESSFULLY GENERATED!")
    print("==================================================================")

if __name__ == '__main__':
    build_all_ch14()
