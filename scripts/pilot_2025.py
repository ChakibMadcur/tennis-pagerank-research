"""
Tennis PageRank pilot — 2025 ATP season
=======================================

What this script does
1. Builds a graph of the 2025 ATP tour-level season (arrow = loser -> winner).
2. Runs PageRank and compares it with the ATP year-end ranking.
3. Prints basic network-science measures (degree, clustering, components, ...).
4. Uses the 2025 rankings to predict Jan-May 2026 matches and compares accuracy.

Setup (one time)
    git clone --depth 1 https://github.com/Aneeshers/tennis-sackmann-archive.git
    pip install pandas networkx scipy

Run
    python pilot_2025.py

Data: Jeff Sackmann / Tennis Abstract, CC BY-NC-SA 4.0 (academic use, cite him).
"""

import numpy as np
import pandas as pd
import networkx as nx
from scipy.stats import kendalltau, spearmanr

DATA = "tennis-sackmann-archive/atp/"   # folder with the ATP csv files


# ---------- 1. Load matches -------------------------------------------------
def load_matches(filename):
    df = pd.read_csv(DATA + filename)
    df = df[df.tourney_level != "D"]                              # drop Davis Cup
    df = df[~df.score.astype(str).str.contains("W/O", na=False)]  # drop walkovers
    return df

m25 = load_matches("atp_matches_2025.csv")
m26 = load_matches("atp_matches_2026.csv")
print(f"2025 matches used: {len(m25)}   |   2026 matches available: {len(m26)}")

names = dict(zip(m25.winner_id, m25.winner_name))
names.update(dict(zip(m25.loser_id, m25.loser_name)))


# ---------- 2. Build the graph (loser -> winner) -----------------------------
G = nx.DiGraph()
for winner, loser in zip(m25.winner_id, m25.loser_id):
    if G.has_edge(loser, winner):
        G[loser][winner]["weight"] += 1        # repeated wins make the arrow heavier
    else:
        G.add_edge(loser, winner, weight=1)

pagerank = nx.pagerank(G, alpha=0.85, weight="weight")   # alpha 0.85 = teleport 0.15


# ---------- 3. Network-science measures -------------------------------------
UG = G.to_undirected()
degrees = np.array([d for _, d in UG.degree()])
largest_scc = max(nx.strongly_connected_components(G), key=len)

print("\nNETWORK")
print(f"  players (nodes):            {G.number_of_nodes()}")
print(f"  directed edges:             {G.number_of_edges()}")
print(f"  mean / max opponents:       {degrees.mean():.1f} / {degrees.max()}")
print(f"  players with <=3 opponents: {100 * np.mean(degrees <= 3):.0f}%")
print(f"  largest strongly connected: {100 * len(largest_scc) / G.number_of_nodes():.0f}% of players")
print(f"  average clustering:         {nx.average_clustering(UG):.2f}")
print(f"  degree assortativity:       {nx.degree_assortativity_coefficient(UG):.2f}")


# ---------- 4. Compare with the ATP year-end ranking ------------------------
rk = pd.read_csv(DATA + "atp_rankings_20s.csv")
last_2025 = rk[rk.ranking_date <= 20251231].ranking_date.max()
year_end = rk[rk.ranking_date == last_2025]
atp_rank = dict(zip(year_end.player, year_end["rank"]))

order = sorted(G.nodes(), key=lambda p: -pagerank[p])
pr_rank = {p: i + 1 for i, p in enumerate(order)}

print(f"\nTOP 10 BY PAGERANK vs ATP year-end rank ({last_2025})")
for p in order[:10]:
    print(f"  {pr_rank[p]:>2}. {names[p]:<28} ATP {atp_rank.get(p)}")

top100 = [p for p in G.nodes() if atp_rank.get(p, 999) <= 100]
tau, _ = kendalltau([atp_rank[p] for p in top100], [pr_rank[p] for p in top100])
rho, _ = spearmanr([atp_rank[p] for p in top100], [pr_rank[p] for p in top100])
overlap = len(set(order[:10]) & {p for p, r in atp_rank.items() if r <= 10})
print(f"\n  Kendall tau (ATP top 100): {tau:.2f}   Spearman: {rho:.2f}   Top-10 overlap: {overlap}/10")


# ---------- 5. Predict Jan-May 2026 matches ---------------------------------
wins = m25.winner_id.value_counts()
losses = m25.loser_id.value_counts()
win_rate = {p: wins.get(p, 0) / (wins.get(p, 0) + losses.get(p, 0)) for p in G.nodes()}

def elo_ratings(df, k=32):
    """Very simple Elo: everyone starts at 1500, one season only."""
    r = {}
    for _, m in df.sort_values(["tourney_date", "match_num"]).iterrows():
        a, b = r.get(m.winner_id, 1500), r.get(m.loser_id, 1500)
        expected = 1 / (1 + 10 ** ((b - a) / 400))
        r[m.winner_id], r[m.loser_id] = a + k * (1 - expected), b - k * (1 - expected)
    return r

elo = elo_ratings(m25)

test = m26[m26.winner_id.isin(pagerank) & m26.loser_id.isin(pagerank)
           & m26.winner_id.isin(atp_rank) & m26.loser_id.isin(atp_rank)
           & m26.winner_rank.notna() & m26.loser_rank.notna()]

def accuracy(score, higher_is_better=True):
    s = [(score[w] > score[l]) if higher_is_better else (score[w] < score[l])
         for w, l in zip(test.winner_id, test.loser_id)]
    return np.mean(s)

print(f"\nPREDICTING {len(test)} MATCHES FROM JAN-MAY 2026 (share of winners picked)")
print(f"  PageRank 2025:              {accuracy(pagerank):.1%}")
print(f"  Win rate 2025:              {accuracy(win_rate):.1%}")
print(f"  Elo 2025 (simple):          {accuracy(elo):.1%}")
print(f"  ATP rank, frozen end 2025:  {accuracy(atp_rank, higher_is_better=False):.1%}")
print(f"  ATP rank, live at match:    {np.mean(test.winner_rank < test.loser_rank):.1%}")
