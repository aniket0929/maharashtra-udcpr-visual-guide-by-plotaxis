"""
UDCPR Visual Guide - CHAPTER 12 LESSON PACKAGE
Exports all 4 modular lessons covering Chapter 12: Structural Safety, Water Supply, Drainage & Sanitary Requirements (Regulations 12.1 to 12.7).
"""

from .lesson_12_1_structural_services import lesson_data as lesson_12_1
from .lesson_12_2_water_supply_storage import lesson_data as lesson_12_2
from .lesson_12_3_drainage_institutional import lesson_data as lesson_12_3
from .lesson_12_4_commercial_transit_signs import lesson_data as lesson_12_4

CH12_LESSONS = [
    lesson_12_1,
    lesson_12_2,
    lesson_12_3,
    lesson_12_4
]

__all__ = ['CH12_LESSONS']
