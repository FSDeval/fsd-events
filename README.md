# fsd-events

Compilation of events occurring in Tesla FSD videos.

FSD9 so far seems to be an improvement over FSD8.2 -- on average, since the release of FSD9 drivers intervene once every 3-4 minutes, compared to once every 2-3 minutes for 8.2.

## Status

version | videos | drivers | length | events | interventions | time between events | time between interventions
--- | --- | --- | --- | --- | --- | --- | --- 
Overall | 56 | 10 | 14:18:23 | 490 | 312 | 1m45s | 2m45s
8.1 | 2 | 1 | 0:49:30 | 23 | 11 | 2m9s | 4m30s
8.2 | 28 | 9 | 8:20:49 | 323 | 215 | 1m33s | 2m19s
9.0 | 26 | 10 | 5:08:04 | 144 | 86 | 2m8s | 3m34s

## Contributing

Criteria to include videos:
- Mostly 1x, uncut footage
- Driver shares their thoughts, observations and reactions
    - Driver shares when they press the accelerator
    - No music
- Central display clearly visible, especially speed gauge and FSD indicator

## Codes

Codes | Importance | Description
--- | --- | ---
2FAST | 1 | car does not slow down to speed limit
AVOID | 1 | car causes other drivers or pedestrians to maneuver to avoid collision
CWWAY | 1 | car drives into incoming lane
D | 1 | disengagement (not clear whether CD or DD)
CD | 1 | car disengages
DD | 1 | driver disengages
RED | 1 | car crosses on red
GAS | 2 | driver taps accelerator
FLC | 2 | driver forces lane change
PWWAY | 2 | car partially drives into incoming lane
YSLOW | 2 | car slows down unnecessarily
YSTOP | 2 | car stops unnecessarily
TWL | 2 | car drives into wrong lane (of correct direction)
BLINK | 3 | car activates spurious blinker
BUS | 3 | car drives into bus only lane
CLI | 3 | car changes lane in intersection
DIS | 3 | driver increases speed
DPL | 3 | car drives in parking lane
DRS | 3 | driver reduces speed
MT | 3 | car misses turn
MUST | 3 | car drives straight through in a turn-only lane
SA | 3 | car stops abruptly
SWL | 3 | car crosses solid white line
DRUNK | 3 | car acts drunk
