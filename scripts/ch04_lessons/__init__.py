"""
UDCPR FROM SCRATCH - CHAPTER 4 LESSON SUITE
Package: scripts/ch04_lessons/
Export: CH04_LESSONS (List of 6 modular lesson dictionaries for Chapter 4)
"""

from .lesson_4_1_residential_zones import lesson_data as l4_1
from .lesson_4_2_commercial_industrial import lesson_data as l4_2
from .lesson_4_3_industrial_conversion import lesson_data as l4_3
from .lesson_4_4_agricultural_zone import lesson_data as l4_4
from .lesson_4_5_protection_and_special_zones import lesson_data as l4_5
from .lesson_4_6_public_semi_public_dp_reservations import lesson_data as l4_6

CH04_LESSONS = [
    l4_1,
    l4_2,
    l4_3,
    l4_4,
    l4_5,
    l4_6
]
