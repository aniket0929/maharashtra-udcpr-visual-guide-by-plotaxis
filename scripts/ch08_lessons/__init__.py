"""
UDCPR FROM SCRATCH - CHAPTER 8 LESSON SUITE
Package: scripts/ch08_lessons/
Export: CH08_LESSONS (List of 4 modular lesson dictionaries for Chapter 8: Parking, Loading and Unloading Spaces)
"""

from .lesson_8_1_parking_standards_dimensions import lesson_data as l8_1
from .lesson_8_2_loading_spaces_marginal_parking import lesson_data as l8_2
from .lesson_8_3_off_street_parking_matrix import lesson_data as l8_3
from .lesson_8_4_city_multipliers_penalties import lesson_data as l8_4

CH08_LESSONS = [
    l8_1,
    l8_2,
    l8_3,
    l8_4
]
