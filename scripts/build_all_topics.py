"""
UDCPR FROM SCRATCH - MASTER TOPICS BUILDER
Executes generation of all 7 CAD-driven interactive practice workbenches.
"""

import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

def main():
    import build_topic_dev_potential
    import build_topic_setbacks_margins
    import build_topic_parking
    import build_topic_layout_subdivision
    import build_topic_fire_safety
    import build_topic_tdr_credit
    import build_topic_redevelopment

    build_topic_dev_potential.main()
    build_topic_setbacks_margins.main()
    build_topic_parking.main()
    build_topic_layout_subdivision.main()
    build_topic_fire_safety.main()
    build_topic_tdr_credit.main()
    build_topic_redevelopment.main()
    print("✓ Successfully rebuilt all 7 CAD interactive practice workbenches.")

if __name__ == '__main__':
    main()
