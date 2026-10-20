# Data sources

No data files are stored in this repository. The notebooks read the files directly from the sources below.

| Data | Source | Used in | License / terms |
|---|---|---|---|
| ATP tour-level matches 1973–2026, weekly ATP rankings 1973–2025 | Jeff Sackmann, [tennis_atp](https://github.com/JeffSackmann/tennis_atp), read through the public mirror [Aneeshers/tennis-sackmann-archive](https://github.com/Aneeshers/tennis-sackmann-archive) (snapshot of June 2026) | Notebooks 1–4, pilot script | CC BY-NC-SA 4.0 — non-commercial use, cite Jeff Sackmann |
| Premier League 2025–26 (380 matches) | [datasets/football-datasets](https://github.com/datasets/football-datasets), cross-checked with [openfootball/football.json](https://github.com/openfootball/football.json) | Notebooks 3–4 | See repository |
| NFL 2025 regular season (272 games) | [nflverse/nfldata](https://github.com/nflverse/nfldata) | Notebook 4 | See repository |
| NBA 2025–26 regular season (1,230 games) | [sportsdataverse/hoopR-nba-data](https://github.com/sportsdataverse/hoopR-nba-data) | Notebook 4 | See repository |
| NHL 2025–26 regular season (1,312 games) | [sportsdataverse/fastRhockey-nhl-data](https://github.com/sportsdataverse/fastRhockey-nhl-data); official points from [Wikipedia, 2025–26 NHL season](https://en.wikipedia.org/wiki/2025%E2%80%9326_NHL_season) | Notebook 4 | See repository |
| UFC fights 1994–2026 (8,816 decided fights) | [Greco1899/scrape_ufc_stats](https://github.com/Greco1899/scrape_ufc_stats) (scraped from UFCStats) | Notebook 4 | See repository |

## Processing choices

- Tennis: tour-level main-draw matches only (Grand Slams, Masters 1000, ATP 500/250, ATP Finals, 2024 Olympics). Davis Cup ties, the Next Gen Finals exhibition and walkovers are removed. 164,894 matches among 4,263 players for 1973–2025.
- Official ranking: the last ATP ranking published in each calendar year (e.g. 29 December 2025). Ranking points for the year-end ranking are available from 1996 on.
- Leagues: a draw or tie adds a directed edge of weight 0.5 in each direction. The Premier League table computed from the results matches the official 2025–26 table exactly.
- Boxing: no open, downloadable dataset of professional results was found.
