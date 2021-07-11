#!/usr/bin/env python3

import argparse
import json
import sys

"""
Report basic statistics on FSD videos.

Usage: ./scripts/report.py videos/*.json
"""

if __name__ == '__main__':
    event_files = sys.argv[1:]
    print(f"From {len(event_files)} Tesla FSD videos")
    for event_file in event_files:
        with open(event_file) as fin:
            try:
                d = json.load(fin)
            except Exception as e:
                print(f"Failed to load: {event_file}: {e}")
