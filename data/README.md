# Data sources

The notebooks read the files directly from the sources below. The only file stored here is `fifa_ranking_2024_07_18.csv` (the full FIFA men's ranking of 18 July 2024, typed from the list published by GiveMeSport, used in Notebook 5).

| Data | Source | Used in | License / terms |
|---|---|---|---|
| ATP tour-level matches 1973–2026, weekly ATP rankings 1973–2025 | Jeff Sackmann, [tennis_atp](https://github.com/JeffSackmann/tennis_atp), read through the public mirror [Aneeshers/tennis-sackmann-archive](https://github.com/Aneeshers/tennis-sackmann-archive) (snapshot of June 2026) | Notebooks 1–7, pilot script | CC BY-NC-SA 4.0 — non-commercial use, cite Jeff Sackmann |
| Premier League 2024–25 and 2025–26 (380 matches each) | [datasets/football-datasets](https://github.com/datasets/football-datasets), cross-checked with [openfootball/football.json](https://github.com/openfootball/football.json) | Notebooks 3–5, 7 | See repository |
| NFL 2024 and 2025 regular seasons (272 games each) | [nflverse/nfldata](https://github.com/nflverse/nfldata) | Notebooks 4–5 | See repository |
| NBA 2024–25 and 2025–26 regular seasons (1,230 games each) | [sportsdataverse/hoopR-nba-data](https://github.com/sportsdataverse/hoopR-nba-data) | Notebooks 4–5, 7 | See repository |
| NHL 2024–25 and 2025–26 regular seasons (1,312 games each) | [sportsdataverse/fastRhockey-nhl-data](https://github.com/sportsdataverse/fastRhockey-nhl-data); official 2025–26 points from [Wikipedia, 2025–26 NHL season](https://en.wikipedia.org/wiki/2025%E2%80%9326_NHL_season); official 2024–25 points from the Stats Crew standings (statscrew.com), typed into Notebook 7 | Notebooks 4–5, 7 | See repository |
| UFC fights 1994–2026 (8,816 decided fights) | [Greco1899/scrape_ufc_stats](https://github.com/Greco1899/scrape_ufc_stats) (scraped from UFCStats) | Notebook 4 | See repository |
| WTA tour-level matches 1984–2026, weekly WTA rankings 1984–2025 | Jeff Sackmann, [tennis_wta](https://github.com/JeffSackmann/tennis_wta), read through the same mirror | Notebooks 5–7 | CC BY-NC-SA 4.0 — non-commercial use, cite Jeff Sackmann |
| International football results (men, 1872–2026) | Mart Jürisoo, [martj42/international_results](https://github.com/martj42/international_results) | Notebooks 5, 7 | See repository |
| FIFA men's ranking, 18 July 2024 (210 teams) | [GiveMeSport](https://www.givemesport.com/fifa-world-rankings/), stored in this folder | Notebooks 5, 7 | Public ranking list |

## Processing choices

- Tennis: tour-level main-draw matches only (Grand Slams, Masters 1000, ATP 500/250, ATP Finals, 2024 Olympics). Davis Cup ties and walkovers are removed. Notebooks 1–4 meant to remove the Next Gen Finals too, but the filter did not match because the dataset spells it "NextGen Finals"; Notebook 5 fixes this and also removes the Laver Cup (neither gives ranking points). With the fix: 164,745 matches for 1973–2025 (164,894 before); Spearman values change by at most 0.005.
- Women's tennis: tour-level events (Grand Slams, WTA tournaments of all tiers, Olympics, WTA Finals); ITF events, Billie Jean King Cup/Fed Cup, exhibitions and walkovers are removed. 101,500 matches for 1984–2025.
- International football: matches between FIFA members from 16 August 2018 (start of FIFA's Elo-based method) to 18 July 2024 for the network; a draw is half a win each way. Notebook 7 uses the FIFA ranking of 18 July 2024 and that network to predict all later matches (to November 2026).
- Prediction (Notebook 7): last season's year-end ranking and last season's WPR predict every match of the next season between two competitors ranked by both; 1 if the higher-ranked one won, 0 if not, 0.5 for a tie in a ranking. Draws are left out, and in the Premier League the three promoted teams are left out.
- Official ranking: the last ATP ranking published in each calendar year (e.g. 29 December 2025). Ranking points for the year-end ranking are available from 1996 on.
- Leagues: a draw or tie adds a directed edge of weight 0.5 in each direction. The Premier League table computed from the results matches the official 2025–26 table exactly.
- Boxing: no open, downloadable dataset of professional results was found.
