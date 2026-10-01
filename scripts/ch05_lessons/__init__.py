"""
UDCPR FROM SCRATCH - CHAPTER 5 LESSON SUITE
Package: scripts/ch05_lessons/
Export: CH05_LESSONS (List of 5 modular lesson dictionaries for Chapter 5)
"""

from .lesson_5_1_gaothan_expansion import lesson_data as l5_1
from .lesson_5_2_rp_amenity_infrastructure import lesson_data as l5_2
from .lesson_5_3_konkan_coastal_plans import lesson_data as l5_3
from .lesson_5_4_western_ghats_hill_stations import lesson_data as l5_4
from .lesson_5_5_special_regional_plans import lesson_data as l5_5

CH05_LESSONS = [
    l5_1,
    l5_2,
    l5_3,
    l5_4,
    l5_5
]
