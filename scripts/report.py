#!/usr/bin/env python3

"""
Report basic statistics on FSD videos.

Usage: ./scripts/report.py videos/*.json
"""

import json
import re
import sys
from collections import defaultdict
from datetime import timedelta


class Stats:
    def __init__(self, video_length=timedelta(), events=0, interventions=0, drivers=[], videos=0):
        self.video_length = video_length
        self.events = events
        self.interventions = interventions
        self.drivers = set(drivers)
        self.videos = videos
    def __add__(self, other):
        return Stats(
            self.video_length + other.video_length,
            self.events + other.events,
            self.interventions + other.interventions,
            self.drivers.union(other.drivers),
            self.videos + other.videos,
        )

def pretty_time_interval(n, ti):
    if n == 0:
        return "NA"
    h, m, s = 0, 0, int(ti.total_seconds() / n)
    ret = []
    if s >= 3600:
        h = s // 3600
        s = s % 3600
        ret.append(f"{h}h")
    if s >= 60:
        m = s // 60
        s = s % 60
        ret.append(f"{m}m")
    ret.append(f"{s}s")
    return "".join(ret)
    

def get_per_hour(stats):
    hours = stats.video_length.total_seconds() / 3600
    events_per_hour = int(stats.events / hours)
    interventions_per_hour = int(stats.interventions / hours)
    return (events_per_hour, interventions_per_hour)


def print_stats(stats, fsd_version=None, fout=sys.stdout):
    title = "videos" if not fsd_version else f"{fsd_version} videos"
    events_per_hour, interventions_per_hour = get_per_hour(stats)
    fout.write(f"Watched {stats.videos} {title} produced by {len(stats.drivers)} drivers and running for {stats.video_length}:\n")
    fout.write(f"- Observed {stats.events} events, i.e. about {events_per_hour} events per hour\n")
    fout.write(f"- Of those events, {stats.interventions} are interventions, i.e. about {interventions_per_hour} interventions per hour\n")


def print_stats_table(stats_list, fsd_versions, fout=sys.stdout):
    fout.write("version | videos | drivers | length | events | interventions | time between events | time between interventions\n")
    fout.write("--- | --- | --- | --- | --- | --- | --- | --- \n")
    for stats, fsd_version in zip(stats_list, fsd_versions):
        time_between_events = pretty_time_interval(stats.events, stats.video_length)
        time_between_interventions = pretty_time_interval(stats.interventions, stats.video_length)
        fout.write(f"{fsd_version} | {stats.videos} | {len(stats.drivers)} | {stats.video_length} | {stats.events} | {stats.interventions} | {time_between_events} | {time_between_interventions}\n")


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
        intervention_codes = set(["D", "D-C", "D-D", "I-GAS", "I-DIS", "I-DRS", "I-FLC",])
        return len(intervention_codes.intersection(set(event["codes"]))) > 0
    return list(filter(has_intervention_code, events))


if __name__ == '__main__':
    event_files = sys.argv[1:]
    total_stats = Stats()
    fsd_version_to_stats = defaultdict(Stats)
    for event_file in event_files:
        with open(event_file) as fin:
            try:
                d = json.load(fin)
                fsd_version = get_fsd_version(d["metadata"]["fsd-version"])
                fsd_version = str(fsd_version[0]) + "." + str(fsd_version[1])
                events = d["events"]
                interventions = get_interventions(events)
                driver = d["metadata"]["user"]
                stats = Stats(
                    get_video_length(d["metadata"]["video-length"]),
                    len(events),
                    len(interventions),
                    [driver],
                    1,
                )
                print(f"{event_file}: {driver} {fsd_version} {stats.video_length} {stats.events} {stats.interventions}")
                total_stats += stats
                fsd_version_to_stats[fsd_version] += stats
            except Exception as e:
                print(f"Failed to load: {event_file}: {e}")
    print_stats(total_stats)
    sorted_fsd_versions = sorted(fsd_version_to_stats.keys())
    for fsd_version in sorted_fsd_versions:
        stats = fsd_version_to_stats[fsd_version]
        print_stats(stats, fsd_version)
    print_stats_table(
        [total_stats] + [fsd_version_to_stats[fsd_version] for fsd_version in sorted_fsd_versions],
        ["Overall"] + sorted_fsd_versions,
    )
