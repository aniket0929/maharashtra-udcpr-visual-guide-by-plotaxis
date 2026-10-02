"""
UDCPR Visual Guide - CHAPTER 14 LESSON PACKAGE
Exports all 7 modular lessons covering Chapter 14: Special Schemes (Regulations 14.1 to 14.13).
"""

from .lesson_14_1_integrated_townships import lesson_data as lesson_14_1
from .lesson_14_2_transit_oriented_development import lesson_data as lesson_14_2
from .lesson_14_3_affordable_housing_pmay import lesson_data as lesson_14_3
from .lesson_14_4_heritage_conservation_tdr import lesson_data as lesson_14_4
from .lesson_14_5_slum_rehabilitation_srs import lesson_data as lesson_14_5
from .lesson_14_6_urban_renewal_clusters import lesson_data as lesson_14_6
from .lesson_14_7_special_industrial_logistics import lesson_data as lesson_14_7

CH14_LESSONS = [
    lesson_14_1,
    lesson_14_2,
    lesson_14_3,
    lesson_14_4,
    lesson_14_5,
    lesson_14_6,
    lesson_14_7
]

__all__ = ['CH14_LESSONS']
