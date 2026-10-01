"""
UDCPR FROM SCRATCH - CHAPTER 13 LESSON PACKAGE
Exports all 4 modular lessons covering Chapter 13: Special Provisions for Certain Buildings (Regulations 13.0 to 13.6).
"""

from .lesson_13_1_barrier_free_access import lesson_data as lesson_13_1
from .lesson_13_2_solar_and_rainwater_harvesting import lesson_data as lesson_13_2
from .lesson_13_3_grey_water_and_solid_waste import lesson_data as lesson_13_3
from .lesson_13_4_disaster_fire_towers_electrical import lesson_data as lesson_13_4

CH13_LESSONS = [
    lesson_13_1,
    lesson_13_2,
    lesson_13_3,
    lesson_13_4
]

__all__ = ['CH13_LESSONS']
