from oop.sports import Player, Game, Arena

if __name__ == '__main__':
    arena = Arena()

    player1 = Player('Player1', 10)
    player2 = Player('Player2', 11)
    player3 = Player('Player3', 11)

    game1 = Game(player1, player2, 1)
    game2 = Game(player1, player3, 1)
    game3 = Game(player3, player2, 1)

    arena.add_game(game1)
    arena.add_game(game2)
    arena.add_game(game3)

    arena.calc_standing()
