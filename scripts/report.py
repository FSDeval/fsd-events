#!/usr/bin/env python3

"""
Report basic statistics on FSD videos.

Usage: ./scripts/report.py videos/*.json
"""

import argparse
import json
import re
import sys


# Return (major, minor, version_string?)
version_re = re.compile("(\\d+)[.](\\d+)(.+)?")
def get_version(version):
    m = version_re.match(version)
    major = int(m.group(1))
    minor = int(m.group(2))
    version_string = None if not m.group(3) else m.group(3).strip().replace('(', '').replace(')', '')
    return (major, minor, version_string)


if __name__ == '__main__':
    event_files = sys.argv[1:]
    print(f"From {len(event_files)} Tesla FSD videos")
    for event_file in event_files:
        with open(event_file) as fin:
            try:
                d = json.load(fin)
                version = get_version(d["metadata"]["fsd-version"])
                print(f"{event_file}: {version}")
            except Exception as e:
                print(f"Failed to load: {event_file}: {e}")
