from player_stats import PlayerStats
from player_reader import PlayerReader

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorer_by_nationality("FIN")
    
    print("Suomalaiset pelaajat:")

    for player in players:
        print(player)


if __name__ == "__main__":
    main()
