TITLE = "Weighted PageRank and Official Rankings in Tennis and Other Sports"
SHORT_TITLE = "PageRank and Official Rankings in Sports"
MAIN = ("Official sports rankings follow different rules: tournament points in tennis, an Elo-type rating in international football, "
        "and league tables in team sports. Using ideas from network science, I rank competitors "
        "with weighted PageRank on the directed network of match results, where every loser points to the winner and each link is weighted "
        "by the number of wins. I compare these PageRank rankings with the official rankings over five decades of men's and women's "
        "professional tennis, and in international football, the Premier League, the NBA, the NHL and the NFL. The two rankings are well "
        "correlated, so I focus on their differences. I compare their predictability by using each ranking at the end of one season to predict "
        "the winners of the next season's matches, and I examine where the rankings disagree: how much one upset of the world number one is "
        "worth, and which players gain or lose places depending on where and in which tournaments they play. The aim is to understand "
        "what each ranking rule rewards.")
SHORT = ("I compare official sports rankings with rankings computed by weighted PageRank on the network of match results, over five decades "
         "of professional tennis and in several other sports. I study how well correlated the two rankings are, which one better predicts "
         "the next season's matches, and what their differences reveal about each ranking rule.")
LONG = ("Sports rank their competitors with very different rules. Tennis gives points for each round reached in a tournament, international "
        "football uses an Elo-type rating, and team sports such as football, basketball, hockey and American football use league tables. "
        "These rules are set by each sport's organization, and none of them looks directly at the full set of results: who beat whom, and how "
        "strong the opponents were. In this project I use ideas from network science to build a ranking from the results alone. Every season "
        "becomes a directed network in which each loser points to the winner and each link is weighted by the number of wins, and I rank "
        "competitors with weighted PageRank, the algorithm originally used to rank web pages. I compare the PageRank rankings with the official "
        "rankings over five decades of men's and women's professional tennis, and in international football, the Premier League, the NBA, the NHL "
        "and the NFL. I measure how well correlated the two rankings are with Spearman's rank correlation, and I compare their predictability "
        "by using each ranking at the end of one season to predict the winners of the next season's matches and counting how often each one is "
        "right. I also study where the rankings disagree: how much a single upset of the world number one is worth under each ranking, and which "
        "players gain or lose places depending on the tournaments they enter and the region where they play. The goal is to understand what each "
        "official ranking rule rewards, and when a ranking based only on results tells a different story.")
PLAIN = ("Every sport has an official ranking, but each one follows its own rules. In professional tennis, for example, players earn points for "
         "how far they go in each tournament, and it does not matter who they beat along the way. My project asks a simple question: what would "
         "the rankings look like if they were based only on who beat whom? To answer it, I treat each season as a network. Every player or team "
         "is a point, and every match is an arrow from the loser to the winner. I then use PageRank, the method Google originally used to rank "
         "web pages, to score every competitor: a player scores highly by beating other players who score highly. I compare these rankings with "
         "the official ones over more than fifty years of men's and women's tennis and in other sports, including the NFL, the NBA, the NHL, the "
         "Premier League and international football. I look at three things: how similar the two rankings are, which one does a better job of "
         "predicting the next season's results, and where they disagree, for example how much one surprise win against the world number one is "
         "worth. The goal is to understand what each official ranking really rewards, and to offer a simple, transparent way to check it.")
KEYWORDS = ["PageRank", "network science", "ranking", "sports analytics", "tennis", "prediction", "directed weighted networks", "official rankings"]
BIO = ("Chakib Madcur is a Master of Science student in Computer Science at Roosevelt University in Chicago, graduating in May 2027. "
       "His research applies network science to sports rankings, under the supervision of Professor Evgeny Dantsin. A former three-year "
       "NCAA Division II men's tennis team captain, he combines experience as a competitor with data analysis to study what rankings reward.")
if __name__ == "__main__":
    for k in ["MAIN", "SHORT", "LONG", "PLAIN", "BIO"]:
        t = globals()[k]; print(k, len(t.split()), "words,", len(t), "characters")
