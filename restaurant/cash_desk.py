from time import ctime, time

class CashDesk:

    def __init__(self, manager):
        self.manager = manager

    def print_to_file(self, filename, message):
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(message)

    def new_order(self, order):
        msg = f'Cash desk: New order <{order.order_name}> send to manager at {ctime(time())}'
        # print(msg)
        self.print_to_file('cash_desk.log', msg + '\n')
        self.manager.new_order(order)
