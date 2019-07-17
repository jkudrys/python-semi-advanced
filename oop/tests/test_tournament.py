import unittest
from oop.sports import *


class TestTournament(unittest.TestCase):

    def test_arena_has_games(self):
        arena = Arena()
        self.assertIsInstance(arena.games, list)

    def test_standing_contains_all_players(self):
        arena = Arena()
        player1 = Player("Jan Kowalski", 1200)
        player2 = Player("Jan Nowak", 1200)
        player3 = Player("Jan Lewandowski", 1200)
        game1 = Game(player1, player2, 1)
        game2 = Game(player1, player3, 2)
        game3 = Game(player2, player3, 2)

        self.assertEquals(arena.standing[0], player3)