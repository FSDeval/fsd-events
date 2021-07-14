# fsd-events

Compilation of events occurring in Tesla FSD videos.

FSD9 so far seems to be an improvement over FSD8.2. Since the release of FSD9, drivers on average intervene once every 3-4 minutes, compared to once every 2-3 minutes for 8.2.

## Status

version | videos | drivers | length | events | interventions | time between events | time between interventions
--- | --- | --- | --- | --- | --- | --- | --- 
Overall | 56 | 10 | 14:18:23 | 490 | 313 | 1m45s | 2m44s
8.1 | 2 | 1 | 0:49:30 | 23 | 11 | 2m9s | 4m30s
8.2 | 28 | 9 | 8:20:49 | 323 | 216 | 1m33s | 2m19s
9.0 | 26 | 10 | 5:08:04 | 144 | 86 | 2m8s | 3m34s

## Contributing

Criteria to include videos:
- Mostly 1x, uncut footage
- Driver shares their thoughts, observations and reactions
    - Driver shares when they press the accelerator
    - No music
- Central display clearly visible, especially speed gauge and FSD indicator

## Codes

We record three kinds of events: disengagements (D), interventions (I) and any kind of
inappropriate or wrong behavior (W).

Note that when we report statistics on interventions, we include both disengagements (D) and interventions (I).

Whenever possible, we further break down these events as follows.

### Disengagements

Code | Description
--- | ---
D-C | car disengages FSD
D-D | driver disengages FSD (by braking or moving the steering wheel)

### Interventions

Code | Description
--- | ---
I-DIS | driver increases speed using throttle on RHS of steering wheel
I-DRS | driver reduces speed using throttle on RHS of steering wheel
I-GAS | driver taps accelerator or taps stalk
I-FLC | driver forces lane change by tapping on turn signal

### Wrong behavior

Code | Description
--- | ---
W-2FAST | car drives too quickly
W-AVOID | car causes other driver or pedestrian to maneuver to avoid collision
W-BLINK | car activates spurious blinker
W-BUS | car drives into bus only lane
W-CLI | car changes lane in intersection
W-CWWAY | car drives into incoming lane
W-DPL | car drives in parking lane
W-DRUNK | car acts drunk
W-MT | car misses turn
W-MUST | car drives straight through in a turn-only lane
W-PWWAY | car partially drives into incoming lane
W-RED | car crosses on red
W-SA | car stops abruptly
W-SWL | car crosses solid white line
W-TWL | car drives into wrong lane (of correct direction)
W-YSLOW | car slows down unnecessarily
W-YSTOP | car stops unnecessarily
