from oop.exceptions import *


class Arena:
    def __init__(self):
        self.games = []
        self.standing = []

    def add_game(self, game):
        self.games.append(game)

    def calc_standing(self):
        stand = {}
        c = 0
        for game in self.games:
            stand[game.white.name] = 0
            stand[game.black.name] = 0
            c += 1
        print(stand)

        for game in self.games:
            if game.result == 1:
                stand[game.white.name] += 1
            if game.result == 2:
                stand[game.black.name] += 1
        print(stand)
        stand_list = list(stand.items())
        print(stand_list)
        sorted_list = sorted(stand_list, key=lambda x: x[1])
        print(sorted_list)



class Player:
    def __init__(self, name, rank=0):
        if len(name) < 3:
            raise NameToShort()
        if rank < 0:
            raise RankToLow()
        self.name = name
        self.ranking = rank

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
#
