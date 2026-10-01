"""
UDCPR FROM SCRATCH - CHAPTER 6 LESSON SUITE
Package: scripts/ch06_lessons/
Export: CH06_LESSONS (List of 6 modular lesson dictionaries for Chapter 6)
"""

from .lesson_6_1_fsi_stacking_tables import lesson_data as l6_1
from .lesson_6_2_ancillary_fsi import lesson_data as l6_2
from .lesson_6_3_front_road_setbacks import lesson_data as l6_3
from .lesson_6_4_side_rear_margins import lesson_data as l6_4
from .lesson_6_5_fire_driveways_projections import lesson_data as l6_5
from .lesson_6_6_height_caps_chowks import lesson_data as l6_6

CH06_LESSONS = [
    l6_1,
    l6_2,
    l6_3,
    l6_4,
    l6_5,
    l6_6
]
