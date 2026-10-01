"""
UDCPR FROM SCRATCH - CHAPTER 11 FULL LESSON BUILDER (MODULAR ORCHESTRATOR)
Executes building of all 4 comprehensive Drawing Sheet lessons for Chapter 11: Acquisition of Reserved Sites & TDR.
Each lesson module resides in `scripts/ch11_lessons/` for clarity and modularity.
"""

import os
import sys

# Ensure current script folder is on sys.path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from generate_lessons import create_lesson_page
from ch11_lessons import CH11_LESSONS

sys.stdout.reconfigure(encoding='utf-8')

def build_all_ch11():
    print("==================================================================")
    print(f"🏗️  BUILDING COMPLETE CHAPTER 11 CURRICULUM ({len(CH11_LESSONS)} MODULAR LESSONS)")
    print("==================================================================")
    for idx, lesson in enumerate(CH11_LESSONS, 1):
        print(f"[{idx}/{len(CH11_LESSONS)}] Generating {lesson['clause']} - {lesson['title']}...")
        create_lesson_page(lesson)
    print("==================================================================")
    print("🎉 CHAPTER 11 LESSON SUITE SUCCESSFULLY GENERATED!")
    print("==================================================================")

if __name__ == '__main__':
    build_all_ch11()
