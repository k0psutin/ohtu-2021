from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or
from querybuilder import QueryBuilder

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)
    """
    matcher = All(
        And(PlaysIn("PHI"), HasFewerThan(5,"goals"))
    )
    """
    query = QueryBuilder()
    m1 = (
    query
    .playsIn("PHI")
    .hasAtLeast(10, "assists")
    .hasFewerThan(5, "goals")
    .build()
)

    m2 = (
    query
    .playsIn("EDM")
    .hasAtLeast(40, "points")
    .build()
    )
    """
    matcher = Or(And(
    PlaysIn("PHI"),HasAtLeast(10,"assists"),HasFewerThan(5,"goals")),
    And(PlaysIn("EDM"),HasAtLeast(40,"points"))
    )
    """


    matcher = query.oneOf(m1, m2).build()
    
    #matcher = And()

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
