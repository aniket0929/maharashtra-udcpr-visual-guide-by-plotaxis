"""
UDCPR Visual Guide - CHAPTER 9 LESSON SUITE
Package: scripts/ch09_lessons/
Export: CH09_LESSONS (List of 5 modular lesson dictionaries for Chapter 9: Requirements of Parts of Buildings)
"""

from .lesson_9_1_room_dimensions_heights import lesson_data as l9_1
from .lesson_9_2_basements_ramps_podiums import lesson_data as l9_2
from .lesson_9_3_lighting_ventilation_shafts import lesson_data as l9_3
from .lesson_9_4_exits_staircases_occupant_load import lesson_data as l9_4
from .lesson_9_5_refuge_areas_fire_safety_amenities import lesson_data as l9_5

CH09_LESSONS = [
    l9_1,
    l9_2,
    l9_3,
    l9_4,
    l9_5
]
