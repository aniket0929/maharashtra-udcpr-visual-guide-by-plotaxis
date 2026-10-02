"""
UDCPR Visual Guide - CHAPTER 3 LESSON MODULES PACKAGE
Exports all 6 modular lesson definitions for Chapter 3: General Land Development Requirements
"""

from .lesson_3_1_site_clearance import lesson_data as lesson_3_1
from .lesson_3_2_internal_roads import lesson_data as lesson_3_2
from .lesson_3_3_recreational_open_space import lesson_data as lesson_3_3
from .lesson_3_4_amenity_space import lesson_data as lesson_3_4
from .lesson_3_5_inclusive_housing import lesson_data as lesson_3_5
from .lesson_3_6_net_plot_computation import lesson_data as lesson_3_6

CH03_LESSONS = [
    lesson_3_1,
    lesson_3_2,
    lesson_3_3,
    lesson_3_4,
    lesson_3_5,
    lesson_3_6
]

__all__ = [
    'CH03_LESSONS',
    'lesson_3_1',
    'lesson_3_2',
    'lesson_3_3',
    'lesson_3_4',
    'lesson_3_5',
    'lesson_3_6'
]
