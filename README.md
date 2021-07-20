# fsd-events

Compilation of events occurring in Tesla FSD videos.

FSD9 so far seems to be an improvement over FSD8.2. Since the release of FSD9, drivers on average intervene once every 3-4 minutes, compared to once every 2-3 minutes for 8.2.

## Status

version | videos | drivers | length | events | interventions | time between events | time between interventions
--- | --- | --- | --- | --- | --- | --- | --- 
Overall | 92 | 13 | 22:42:29 | 886 | 576 | 1m32s | 2m21s
7.7 | 1 | 1 | 0:18:19 | 28 | 24 | 39s | 45s
7.8 | 1 | 1 | 0:31:24 | 44 | 32 | 42s | 58s
7.9 | 1 | 1 | 0:10:00 | 8 | 7 | 1m15s | 1m25s
8.1 | 8 | 3 | 1:42:11 | 66 | 40 | 1m32s | 2m33s
8.2 | 37 | 10 | 9:37:38 | 371 | 249 | 1m33s | 2m19s
9.0 | 44 | 13 | 10:22:57 | 369 | 224 | 1m41s | 2m46s

## Methodology

### Video Selection

Criteria to include videos:
- Mostly 1x, uncut footage
- Driver shares their thoughts, observations and reactions
    - Driver shares when they press the accelerator
    - No music
- Central display clearly visible, especially speed gauge and FSD indicator

### Codes

We record three kinds of events: disengagements (D), interventions (I) and any kind of
inappropriate or wrong behavior (W).

Note that when we report statistics on interventions, we include both disengagements (D) and interventions (I).

Whenever possible, we further break down these events as follows.

#### Disengagements

Code | Description
--- | ---
D-C | car disengages FSD
D-D | driver disengages FSD (by braking or turning the steering wheel)

#### Interventions

Code | Description
--- | ---
I-FAST | driver increases speed using throttle on RHS of steering wheel
I-GAS | driver taps accelerator or uses stalk to tell car to proceed
I-SLOW | driver reduces speed using throttle on RHS of steering wheel
I-TURN | driver forces lane change by using turn signal

#### Wrong behavior

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

### Drivers

#### Match Requirements

User name | Youtube | Twitter
--- | --- | ---
AI Addict | [Channel](https://www.youtube.com/channel/UCnSt1nfVXyTyMbKhk-IaTJw/about) | -
Brandonee916 | [Brandonee916](https://www.youtube.com/c/Brandonee916/about) | [@brandonee916](https://twitter.com/brandonee916)
Chuck Cook | [Channel](https://www.youtube.com/channel/UCwdbsDtaMAh6QXvcbp08YzQ/about) | [@Chazman](https://twitter.com/chazman)
Dave Mac | [DMacTech](https://www.youtube.com/c/DMacTech/about) | [@CGDaveMac](https://twitter.com/CGDaveMac)
Dirty Tesla | [DirtyTesla](https://www.youtube.com/c/DirtyTesla/about) | [@DirtyTesla](https://twitter.com/DirtyTesla)
Frenchie | [Channel](https://www.youtube.com/channel/UCt8fkjhFgywzLGLVIz7Z7-g/about) | [@FrenchieEAP](https://twitter.com/FrenchieEAP)
James Locke | [pilotjc78](https://www.youtube.com/user/pilotjc78) | [@arctechinc](https://twitter.com/arctechinc)
Kim Paquette| [bimbels](https://www.youtube.com/user/bimbels/about) | [@kimpaquette](https://twitter.com/kimpaquette)
Nicholas Howard | [NicholasHoward](https://www.youtube.com/c/NicholasHoward/about) | -
oisiaa | [oisiaa](https://www.youtube.com/user/oisiaa/about) | -
TesLatino | [TesLatino](https://www.youtube.com/c/TesLatino/about) | [@TesLatino](https://twitter.com/TesLatino)
Tesla Owners Silicon Valley | [TeslaOwnersSiliconValley](https://www.youtube.com/c/TeslaOwnersSiliconValley/about) | [@teslaownersSV](https://twitter.com/teslaownersSV)
Trevor Mahlmann | [TrevorMahlmann](https://www.youtube.com/c/TrevorMahlmann/about) | [@TrevorMahlmann](https://twitter.com/TrevorMahlmann)

#### Don't Match Requirements

- [CMePrint](https://www.youtube.com/c/CMePrint/about): driver is silent
