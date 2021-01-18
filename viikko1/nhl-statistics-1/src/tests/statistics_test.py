import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_returns_correct_player(self):
        self.assertEqual(self.statistics.search("Kurri").name, "Kurri")
        
    def test_search_returns_none_if_not_found(self):
        self.assertEqual(self.statistics.search("Jaajo"), None)
        
    def test_team_returns_correct_list_of_players(self):
        teams = self.statistics.team("EDM")
        correct = False
        
        for player in teams:
            correct = (player.team == "EDM")
            
        self.assertTrue(correct)
        
    def test_top_scorers_return_correct_highscore(self):
        self.assertEqual(self.statistics.top_scorers(1)[0].name, "Gretzky")
        