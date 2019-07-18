from oop.sports import Player, Game, Arena


def print_lower_case(string):
    print(string.lower())


def print_upper_case(string):
    print(string.upper())


def print_mod_string(string, modifier):
    print(modifier(string))


def to_lower_case(string):
    return string.lower()


if __name__ == '__main__':
    arena = Arena()

    player1 = Player('Player1', 10)
    player2 = Player('Player2', 11)
    player3 = Player('Player3', 11)

    game1 = Game(player1, player2, 1)
    game2 = Game(player1, player3, 2)
    game3 = Game(player2, player3, 1)
    game4 = Game(player1, player2, 2)
    game5 = Game(player1, player3, 2)
    game6 = Game(player2, player3, 1)

    arena.add_game(game1)
    arena.add_game(game2)
    arena.add_game(game3)
    arena.add_game(game4)
    arena.add_game(game5)
    arena.add_game(game6)

    for p in arena.standing:
        print(p.name)

    print()
    print(arena.standing[0].name)

    print(player1 == player1)
    print(player1 == player2)

    print(player1.__hash__())
    print(player2.__hash__())

    print_upper_case('Hello')
    print_lower_case('Hello')

    print_mod_string('Hello', lambda x: x.lower())
    print_mod_string('Hello', to_lower_case)

