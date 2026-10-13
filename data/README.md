# Data sources

No data files are stored in this repository. The notebooks read the files directly from the sources below.

| Data | Source | Used in | License / terms |
|---|---|---|---|
| ATP tour-level matches 1973–2026, weekly ATP rankings 1973–2025 | Jeff Sackmann, [tennis_atp](https://github.com/JeffSackmann/tennis_atp), read through the public mirror [Aneeshers/tennis-sackmann-archive](https://github.com/Aneeshers/tennis-sackmann-archive) (snapshot of June 2026) | Notebooks 1–3, pilot script | CC BY-NC-SA 4.0 — non-commercial use, cite Jeff Sackmann |
| Premier League 2025–26 results (380 matches) | [datasets/football-datasets](https://github.com/datasets/football-datasets) (`season-2526.csv`), cross-checked with [openfootball/football.json](https://github.com/openfootball/football.json) | Notebook 3 | See each repository |

## Processing choices

- Tennis: tour-level main-draw matches only (Grand Slams, Masters 1000, ATP 500/250, ATP Finals). Davis Cup ties, the Next Gen Finals exhibition and walkovers are removed. 164,894 matches among 4,263 players for 1973–2025.
- Official ranking: the last ATP ranking published in each calendar year (e.g. 29 December 2025). Ranking points for the year-end ranking are available from 1996 on; earlier years have ranks only.
- Football: the league table computed from the 380 results matches the official 2025–26 final table exactly.
