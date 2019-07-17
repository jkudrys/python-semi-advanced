import unittest
from oop.sports import *


class TestPlayer(unittest.TestCase):

    def test_player_has_name(self):
        player = Player("Jan Kowalski", 1200)
        name = player.name


def test_player_has_ranking(self):
    player = Player("Jan Kowalski", 1200)
    ranking = player.ranking


def test_player_self_describes(self):
    player = Player("Jan Kowalski", 1200)
    description = player.description()

    self.assertEquals(description, f"My name is {player.name} and my ranking is {player.ranking}.")

