# Weighted PageRank in Professional Tennis

**Chakib Madcur** · MS Computer Science, Roosevelt University · Research project, Fall 2026 – Spring 2027

Each ATP season is turned into a directed graph: every player is a node and every match is an arrow from the loser to the winner. Players are ranked with a **weighted PageRank** (edge weight = number of wins over that opponent, node weight = matches won), and the result is compared with the **official ATP ranking**, with **Elo**, through history (1973–2025), and on a football league (Premier League 2025–26).

## Everything in this repository

| What | Link |
|---|---|
| Paper, first draft (PDF) | [paper/paper.pdf](paper/paper.pdf) |
| Paper source (LaTeX, opens in Overleaf) | [paper/paper.tex](paper/paper.tex) · [paper/references.bib](paper/references.bib) · [paper/figures/](paper/figures) |
| Notebook 1 · directed graph, weights, weighted PageRank program (2025) | [notebooks/01_weighted_pagerank_2025.ipynb](notebooks/01_weighted_pagerank_2025.ipynb) |
| Notebook 2 · head-to-head wins, top 10/50/100, 2015 vs 2025, Elo, equal ATP points | [notebooks/02_head_to_head_top_n_elo.ipynb](notebooks/02_head_to_head_top_n_elo.ipynb) |
| Notebook 3 · cosine similarity vs Euclidean, history 1973–2025, Premier League | [notebooks/03_cosine_history_premier_league.ipynb](notebooks/03_cosine_history_premier_league.ipynb) |
| First feasibility test (September 2026, plain PageRank) | [scripts/pilot_2025.py](scripts/pilot_2025.py) |
| Half page on the Elo rating (for the paper) | [docs/Elo_Rating_in_Tennis.docx](docs/Elo_Rating_in_Tennis.docx) |
| All references with links | [REFERENCES.md](REFERENCES.md) |
| Data sources and licenses | [data/README.md](data/README.md) |

## Main results so far

- **PageRank and ATP agree strongly.** Cosine similarity between the two score vectors is 0.97–0.99 for the ATP top 10, 50 and 100 (2015 and 2025), against a random baseline of 0.35–0.78.
- **Agreement depends on the ATP rules.** Mean Spearman 0.86 under the 1973–1989 averaging system, 0.91 under the best-of system since 1990, and a drop to 0.71 in 2020 (COVID-19 ranking rules).
- **PageRank separates players with equal ATP points**, e.g. Nakashima (29th) and Tsitsipas (46th), both on 1,380 points in 2025.
- **Premier League 2025–26:** PageRank nearly reproduces the final table (Spearman 0.97) and ranks Manchester City above champions Arsenal because of City's results against the top six.

## How to run

**Google Colab (no installation):** open [colab.research.google.com](https://colab.research.google.com), choose *Upload*, select a notebook from `notebooks/`, then *Runtime → Run all*. The notebooks download the data themselves.

**On your own computer:**
```bash
pip install -r requirements.txt
jupyter notebook notebooks/
```

**Paper:** upload the `paper/` folder to [Overleaf](https://www.overleaf.com) (*New project → Upload project*) and compile with pdfLaTeX, or run `pdflatex paper && bibtex paper && pdflatex paper && pdflatex paper` inside `paper/`.

## Data

Tennis data: Jeff Sackmann, [tennis_atp](https://github.com/JeffSackmann/tennis_atp) (CC BY-NC-SA 4.0), read from a public mirror. Football data: [datasets/football-datasets](https://github.com/datasets/football-datasets). No data files are stored in this repository; see [data/README.md](data/README.md).
