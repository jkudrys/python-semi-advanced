from restaurant.cash_desk import CashDesk
from restaurant.kitchen import Kitchen
from restaurant.give_away import GiveAway
from restaurant.manager import Manager

if __name__ == '__main__':

    cash_desk = CashDesk(None)
    kitchen = Kitchen(None)
    give_away = GiveAway(None)
    manager = Manager(cash_desk, kitchen, give_away)

    cash_desk.manager = manager
    kitchen.manager = manager
    give_away.manager = manager

    cash_desk.new_order("Burger")



