"""
UDCPR FROM SCRATCH - CHAPTER 11 LESSON PACKAGE
Exports all 4 modular lessons covering Chapter 11: Acquisition of Reserved Sites & TDR (Regulations 11.0 to 11.3).
"""

from .lesson_11_1_accommodation_reservation import lesson_data as lesson_11_1
from .lesson_11_2_tdr_generation_amenities import lesson_data as lesson_11_2
from .lesson_11_3_tdr_utilisation_indexation import lesson_data as lesson_11_3
from .lesson_11_4_reservation_credit_certificate import lesson_data as lesson_11_4

CH11_LESSONS = [
    lesson_11_1,
    lesson_11_2,
    lesson_11_3,
    lesson_11_4
]

__all__ = ['CH11_LESSONS']
