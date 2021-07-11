#!/usr/bin/env python3

"""
Report basic statistics on FSD videos.

Usage: ./scripts/report.py videos/*.json
"""

import argparse
from datetime import timedelta
import json
import re
import sys


# Return (major, minor, version_string?)
fsd_version_re = re.compile("(\\d+)[.](\\d+)(.+)?")
def get_fsd_version(s):
    m = fsd_version_re.match(s)
    major = int(m.group(1))
    minor = int(m.group(2))
    version_string = None if not m.group(3) else m.group(3).strip().replace('(', '').replace(')', '')
    return (major, minor, version_string)


def get_video_length(s):
    components = s.split(":")
    minutes, seconds = int(components[0]), int(components[1])
    return timedelta(minutes=minutes, seconds=seconds)


def get_interventions(events):
    def has_intervention_code(event):
        intervention_codes = set(["CD", "D", "DD",  "DIS", "DRS", "GAS",])
        return len(intervention_codes.intersection(set(event["codes"]))) > 0
    return list(filter(has_intervention_code, events))


if __name__ == '__main__':
    event_files = sys.argv[1:]
    total_video_length = timedelta()
    valid_event_files = []
    total_events = 0
    total_interventions = 0
    drivers = set()
    for event_file in event_files:
        with open(event_file) as fin:
            try:
                d = json.load(fin)
                fsd_version = get_fsd_version(d["metadata"]["fsd-version"])
                video_length = get_video_length(d["metadata"]["video-length"])
                events = d["events"]
                driver = d["metadata"]["user"]
                n_events = len(events)
                n_interventions = len(get_interventions(d["events"]))
                print(f"{event_file}: {driver} {fsd_version} {video_length} {n_events} {n_interventions}")
                total_video_length += video_length
                valid_event_files.append(event_file)
                total_events += n_events
                drivers.add(driver)
                total_interventions += n_interventions
            except Exception as e:
                print(f"Failed to load: {event_file}: {e}")
    float_total_video_hours = total_video_length.total_seconds() / 3600
    events_per_hour = int(total_events / float_total_video_hours)
    interventions_per_hour = int(total_interventions / float_total_video_hours)
    print(f"Watched {len(valid_event_files)} Tesla FSD videos produced by {len(drivers)} drivers and running for {total_video_length}:")
    print(f"- Observed {total_events} events, i.e. about {events_per_hour} events per hour")
    print(f"- Of those events, {total_interventions} are interventions, i.e. about {interventions_per_hour} interventions per hour")
