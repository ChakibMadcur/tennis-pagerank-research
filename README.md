# Weighted PageRank and Official Rankings in Tennis and Other Sports

**Chakib Madcur** · MS Computer Science, Roosevelt University · Research project, Fall 2026 – Spring 2027 · Advisor: Prof. Evgeny Dantsin

Each season is turned into a **directed network**: every player or team is a node and every match is a **link from the loser to the winner**, weighted by the number of wins. Competitors are ranked with **weighted PageRank (WPR)**, and the result is compared with the **official rankings** in three ways: how well correlated the two rankings are, which one better predicts the next season's matches, and what their differences reveal about each ranking rule. The data cover five decades of men's (ATP, 1973–2025) and women's (WTA, 1984–2025) professional tennis, international football, the Premier League, the NBA, the NHL and the NFL.

## Everything in this repository

| What | Link |
|---|---|
| **Paper, third draft (PDF)**, November 2026 | [paper/paper.pdf](paper/paper.pdf) |
| Paper source (LaTeX, opens in Overleaf) | [paper/paper.tex](paper/paper.tex) · [paper/references.bib](paper/references.bib) · [paper/figures/](paper/figures) |
| **Title and abstract** (one page) | [abstracts/abstract_and_title.pdf](abstracts/abstract_and_title.pdf) · [LaTeX](abstracts/abstract_and_title.tex) |
| NetSci / NERCCS one-page abstract with figure | [abstracts/netsci_one_page.pdf](abstracts/netsci_one_page.pdf) · [LaTeX](abstracts/netsci_one_page.tex) · [figure.pdf](abstracts/figure.pdf) |
| SDSS two-page extended abstract (anonymous, for review) | [abstracts/sdss_extended_abstract_blinded.pdf](abstracts/sdss_extended_abstract_blinded.pdf) · [LaTeX](abstracts/sdss_extended_abstract_blinded.tex) |
| All abstract versions as text (main, short, long, plain-language, bio) | [abstracts/abstract_texts.py](abstracts/abstract_texts.py) |
| **Conference submission kit** (titles, abstracts, author details, deadlines, which file to send where) | [docs/Conference_Submission_Kit.pdf](docs/Conference_Submission_Kit.pdf) · [Word](docs/Conference_Submission_Kit.docx) |
| CST presentation: slides and talk script | [docs/Presentation_Slides.pdf](docs/Presentation_Slides.pdf) · [docs/Presentation_Script.pdf](docs/Presentation_Script.pdf) |
| Notebook 1 · directed network, link weights, WPR program (2025) | [notebooks/01_weighted_pagerank_2025.ipynb](notebooks/01_weighted_pagerank_2025.ipynb) |
| Notebook 2 · head-to-head wins, top 10/50/100, 2015 vs 2025, Elo, equal ATP points | [notebooks/02_head_to_head_top_n_elo.ipynb](notebooks/02_head_to_head_top_n_elo.ipynb) |
| Notebook 3 · history 1973–2025, Premier League | [notebooks/03_cosine_history_premier_league.ipynb](notebooks/03_cosine_history_premier_league.ipynb) |
| Notebook 4 · NFL, NBA, NHL, UFC | [notebooks/04_standard_vs_weighted_other_sports.ipynb](notebooks/04_standard_vs_weighted_other_sports.ipynb) |
| Notebook 5 · the #100-beats-#1 experiment, who gains and loses (incl. location), women's tennis, table by sport | [notebooks/05_weighted_vs_standard_upsets_sports.ipynb](notebooks/05_weighted_vs_standard_upsets_sports.ipynb) |
| Notebook 6 · percentage of match results consistent with each ranking (1973–2025, men and women) | [notebooks/06_percent_consistent_with_ranking.ipynb](notebooks/06_percent_consistent_with_ranking.ipynb) |
| **Notebook 7 · which ranking predicts better: last season's official ranking vs last season's WPR, on the next season's matches** (tennis 1974–2026 and five other competitions) | [notebooks/07_prediction_official_vs_pagerank.ipynb](notebooks/07_prediction_official_vs_pagerank.ipynb) |
| Earlier results section (27 Oct 2026; superseded by the third draft) | [paper/new_section/section.pdf](paper/new_section/section.pdf) |
| Where to present and publish (conference and journal guide, October) | [docs/Conference_and_Journal_Guide.pdf](docs/Conference_and_Journal_Guide.pdf) |
| First feasibility test (September 2026) | [scripts/pilot_2025.py](scripts/pilot_2025.py) |
| Half page on the Elo rating | [docs/Elo_Rating_in_Tennis.docx](docs/Elo_Rating_in_Tennis.docx) |
| All references with links | [REFERENCES.md](REFERENCES.md) |
| Data sources and licenses | [data/README.md](data/README.md) |

Notes on earlier notebooks: Notebooks 1 and 2 used node weights; from Notebook 3 on there are no node weights (every player has the same restart probability, only links are weighted). Notebooks 3–6 also contain comparisons with standard (unweighted) PageRank and cosine similarity; these were exploratory and are **not part of the paper**, which compares only the official ranking and weighted PageRank, with Spearman's rank correlation as the one coefficient.

## Main results so far (third draft)

- **Well correlated.** Mean Spearman correlation between WPR and the official year-end ranking (top 100): 0.885 for men (1973–2025) and 0.907 for women (1984–2025); 0.88–0.96 in the leagues and 0.95 in international football. It was lower under the ATP's 1973–1989 averaging system (0.85) than under the best-of system since 1990 (0.91), and lowest in 2020 when the rankings were frozen (0.71).
- **Equal predictability (Notebook 7).** Last season's ranking predicts this season's matches: men 64.4% (ATP) vs 64.5% (WPR) over 52 seasons; the official ranking was better before 1990, WPR slightly better since 1991 (21 of 35 seasons). Women: WTA 65.0% vs WPR 64.5% (WTA better in 33 of 41 seasons). The two rankings pick the same winner in about 9 matches of 10. Other sports (one season each): small differences in both directions.
- **Consistency with the season's results (Notebook 6).** Of the matches between two top-100 players, 67.1% agree with the ATP order and 66.4% with the WPR order (women 69.4% vs 68.6%); tied among the top 10 and top 20. The order that fits one season best predicts the next season worse, so the next-season test is the fair one.
- **One upset.** If the 2025 ATP #100 beats Alcaraz or Sinner, he gains 64 or 61 places under WPR but 12 under ATP points. The value of a win follows the beaten player's score divided by his number of losses.
- **Who loses under WPR.** Players whose ATP points come from one deep run, from Challenger events, or from weaker regional fields (South American players: −2 places on average).
- **Prior work.** Weighted PageRank in tennis is not new (Radicchi 2011; Dingle et al. 2013). What is new here is the systematic comparison with the official rankings over five decades and across sports, the predictability test, and the explanation of the disagreements.

## How to run

**Google Colab (no installation):** open [colab.research.google.com](https://colab.research.google.com), choose *Upload*, select a notebook from `notebooks/`, then *Runtime → Run all*. The notebooks download the data themselves.

**On your own computer:**
```bash
pip install -r requirements.txt
jupyter notebook notebooks/
```

**Paper:** upload the `paper/` folder to [Overleaf](https://www.overleaf.com) (*New project → Upload project*) and compile with pdfLaTeX, or run `pdflatex paper && bibtex paper && pdflatex paper && pdflatex paper` inside `paper/`.

## Data

Tennis: Jeff Sackmann, [tennis_atp](https://github.com/JeffSackmann/tennis_atp) and [tennis_wta](https://github.com/JeffSackmann/tennis_wta) (CC BY-NC-SA 4.0). Other sports: see [data/README.md](data/README.md). No data files are stored in this repository, except one small list: [data/fifa_ranking_2024_07_18.csv](data/fifa_ranking_2024_07_18.csv).
