"""
UDCPR FROM SCRATCH - CHAPTER 15 LESSON PACKAGE
Exports all 3 modular lessons covering Chapter 15: Regulations for Special Activities / Plans (Regulations 15.1 to 15.4).
"""

from .lesson_15_1_quarrying_operations import lesson_data as lesson_15_1
from .lesson_15_2_telecom_mobile_towers import lesson_data as lesson_15_2
from .lesson_15_3_local_area_plans_street_design import lesson_data as lesson_15_3

CH15_LESSONS = [
    lesson_15_1,
    lesson_15_2,
    lesson_15_3
]

__all__ = ['CH15_LESSONS']
