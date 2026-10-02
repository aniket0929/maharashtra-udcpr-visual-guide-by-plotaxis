"""
UDCPR Visual Guide - CHAPTER 10 LESSON PACKAGE
Exports all 7 modular lessons covering Regulations 10.0 to 10.16 (City Specific Regulations).
"""

from .lesson_10_1_pune_pmc import lesson_data as lesson_10_1
from .lesson_10_2_thane_urban_corridors import lesson_data as lesson_10_2
from .lesson_10_3_thane_buffers_yeur import lesson_data as lesson_10_3
from .lesson_10_4_nagpur_nmc_nmrda import lesson_data as lesson_10_4
from .lesson_10_5_nashik_kolhapur import lesson_data as lesson_10_5
from .lesson_10_6_navi_mumbai_cidco import lesson_data as lesson_10_6
from .lesson_10_7_mmr_special_hubs import lesson_data as lesson_10_7

CH10_LESSONS = [
    lesson_10_1,
    lesson_10_2,
    lesson_10_3,
    lesson_10_4,
    lesson_10_5,
    lesson_10_6,
    lesson_10_7
]

__all__ = ['CH10_LESSONS']
