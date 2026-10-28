# Weighted PageRank in Professional Tennis

**Chakib Madcur** · MS Computer Science, Roosevelt University · Research project, Fall 2026 – Spring 2027

Each season is turned into a **directed graph**: every player is a node and every match is a **directed edge from the loser to the winner**, weighted by the number of wins over that opponent. Players are ranked with **weighted PageRank (WPR)**, and the result is compared with the **official ATP ranking**, with **standard PageRank**, with **Elo**, through history (1973–2025), and in other sports (Premier League, NFL, NBA, NHL, UFC).

## Everything in this repository

| What | Link |
|---|---|
| Paper, second draft (PDF) | [paper/paper.pdf](paper/paper.pdf) |
| Paper source (LaTeX, opens in Overleaf) | [paper/paper.tex](paper/paper.tex) · [paper/references.bib](paper/references.bib) · [paper/figures/](paper/figures) |
| Notebook 1 · directed graph, edge weights, WPR program (2025) | [notebooks/01_weighted_pagerank_2025.ipynb](notebooks/01_weighted_pagerank_2025.ipynb) |
| Notebook 2 · head-to-head wins, top 10/50/100, 2015 vs 2025, Elo, equal ATP points | [notebooks/02_head_to_head_top_n_elo.ipynb](notebooks/02_head_to_head_top_n_elo.ipynb) |
| Notebook 3 · cosine similarity vs Euclidean, history 1973–2025, Premier League | [notebooks/03_cosine_history_premier_league.ipynb](notebooks/03_cosine_history_premier_league.ipynb) |
| Notebook 4 · standard PageRank vs WPR, Elo, NFL, NBA, NHL, UFC, match-importance weights | [notebooks/04_standard_vs_weighted_other_sports.ipynb](notebooks/04_standard_vs_weighted_other_sports.ipynb) |
| Notebook 5 · is WPR better than standard PageRank (1973–2025), the #100-beats-#1 experiment, who gains and loses (incl. location), women's tennis, table by sport and ranking style | [notebooks/05_weighted_vs_standard_upsets_sports.ipynb](notebooks/05_weighted_vs_standard_upsets_sports.ipynb) |
| New results section (written separately, 27 Oct 2026), with proposed title and abstract | [paper/new_section/section.pdf](paper/new_section/section.pdf) · [LaTeX](paper/new_section/section.tex) |
| Where to present and publish (conference and journal guide) | [docs/Conference_and_Journal_Guide.pdf](docs/Conference_and_Journal_Guide.pdf) |
| First feasibility test (September 2026, plain PageRank) | [scripts/pilot_2025.py](scripts/pilot_2025.py) |
| Half page on the Elo rating | [docs/Elo_Rating_in_Tennis.docx](docs/Elo_Rating_in_Tennis.docx) |
| All references with links | [REFERENCES.md](REFERENCES.md) |
| Data sources and licenses | [data/README.md](data/README.md) |

Notebooks 1 and 2 used node weights (matches won); from Notebook 3 on, as agreed on 14 October, there are **no node weights**: every player has the same restart probability and only the directed edges are weighted.

## Main results so far

- **WPR and the ATP ranking agree closely.** For the ATP top 10, 50 and 100 (2015 and 2025): Spearman 0.85–0.95, cosine 0.96–0.99, against a random cosine baseline of 0.38–0.78.
- **WPR agrees with the ATP more than standard PageRank** in all 30 seasons from 1996 to 2025 (cosine 0.963 vs 0.925). Standard PageRank ignores how many times a player won; in 2015 it ranks Wawrinka above Djokovic.
- **Agreement depends on the ATP rules:** mean Spearman 0.85 under the 1973–1989 averaging system, 0.91 under the best-of system since 1990, and 0.70 in 2020 (COVID-19 rules).
- **Other sports:** WPR is close to the final standings in the Premier League, NBA and NHL (0.88–0.96), differs more in the NFL, where teams meet only 45% of the possible opponents, and breaks down in the UFC, where one upset can move a fighter near the top.
- **Is WPR better? (Notebook 5, Spearman only)** WPR agrees with the official ranking slightly better than standard PageRank (men 0.885 vs 0.883, better in 34 of 53 seasons; women 0.904 vs 0.903, 31 of 42). For predicting next-season matches, WPR, standard PageRank and the ATP ranking are tied at about 64%; for women the WTA ranking is slightly better.
- **One upset:** if the ATP #100 beats the #1, he gains about 60 places in WPR but 12 in the ATP ranking. The value of a win is the beaten player's score divided by how often he loses.
- **Who loses under WPR:** players whose ATP points come from one deep run, from Challenger events, or from weaker regional fields (South American players: −2 places on average).
- **Across sports:** weighting by wins matters where the same opponents meet repeatedly (Premier League 0.96 vs 0.80) and hardly at all in tennis.
- **Prior work:** weighted PageRank in tennis is not new (Radicchi 2011; Dingle et al. 2013). What is new here is the side-by-side comparison of weighted and standard PageRank over 50+ seasons and across sports.

## How to run

**Google Colab (no installation):** open [colab.research.google.com](https://colab.research.google.com), choose *Upload*, select a notebook from `notebooks/`, then *Runtime → Run all*. The notebooks download the data themselves.

**On your own computer:**
```bash
pip install -r requirements.txt
jupyter notebook notebooks/
```

**Paper:** upload the `paper/` folder to [Overleaf](https://www.overleaf.com) (*New project → Upload project*) and compile with pdfLaTeX, or run `pdflatex paper && bibtex paper && pdflatex paper && pdflatex paper` inside `paper/`.

## Data

Tennis: Jeff Sackmann, [tennis_atp](https://github.com/JeffSackmann/tennis_atp) (CC BY-NC-SA 4.0). Other sports: see [data/README.md](data/README.md). No data files are stored in this repository, except one small list: [data/fifa_ranking_2024_07_18.csv](data/fifa_ranking_2024_07_18.csv).
