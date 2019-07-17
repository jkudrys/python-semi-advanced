import unittest
from oop.sports import *


class TestGame(unittest.TestCase):

    def test_white_differs_from_black(self):
        white = Player("Jan Kowalski", 1200)
        black = Player("Jan Nowak", 1200)

        game = Game(white, black, 1)

        self.assertEquals(game.white, white)
        self.assertEquals(game.black, black)
        self.assertNotEquals(game.white, game.black)

    def test_white_won_returns_correct_value(self):
        white = Player("Jan Kowalski", 1200)
        black = Player("Jan Nowak", 1200)

        game = Game(white, black, 1)

        self.assertTrue(game.whiteWon())

    def test_black_won_returns_correct_value(self):
        white = Player("Jan Kowalski", 1200)
        black = Player("Jan Nowak", 1200)

        game = Game(white, black, 2)

        self.assertTrue(game.blackWon())
