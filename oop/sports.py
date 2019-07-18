from oop.exceptions import *


class Arena:
    def __init__(self):
        self.games = []
        self.standing = []

    def add_game(self, game):
        self.games.append(game)
        self.calc_standing()

    def calc_standing(self):
        players = []
        stands = []
        for game in self.games:
            if game.white not in players:
                players.append(game.white)
                stands.append(0)
            if game.black not in players:
                players.append(game.black)
                stands.append(0)

        for game in self.games:
            if game.result == 1:
                stands[players.index(game.white)] += 1
            if game.result == 2:
                stands[players.index(game.black)] += 1

        sorted_stands = sorted(list(zip(players, stands)), key=lambda x: x[1])
        self.standing = [i for i, v in reversed(sorted_stands)]


class Player:
    def __init__(self, name, rank=0):
        if len(name) < 3:
            raise NameToShort()
        if rank < 0:
            raise RankToLow()
        self.__name = name
        self.ranking = rank

    def __eq__(self, other):
        if not isinstance(other, Player):
            return False
        return self.name == other.name

    @property
    def name(self):
        return self.__name

    def __hash__(self):
        res = 0
        for letter in self.name:
            res += ord(letter)
            res *= 31
        return res

    def description(self):
        return f'My name is {self.name} and my ranking is {self.ranking}.'


class Game:
    def __init__(self, white, black, result):
        if result not in [1, 2]:
            raise WrongResult()
        self.white = white
        self.black = black
        self.result = result

    def white_won(self):
        return self.result == 1

    def black_won(self):
        return self.result == 2
