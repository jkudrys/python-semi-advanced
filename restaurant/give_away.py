from time import sleep, time, ctime

class GiveAway:

    def __init__(self, manager):
        self.manager = manager

    def call_customer(self, order):
        msg = f'Give away: Customer called for <{order.order_name}> at {ctime(time())}'
        self.print_to_file('give_away.log', msg + '\n')
        # print(msg)
        sleep(2)
        self.customer_collected_order(order)

    def customer_collected_order(self, order):
        order.collected_time = time()
        msg = f'Give away: <{order.order_name}> collected at {ctime(time())}'
        self.manager.customer_collected_order(order)
        self.print_to_file('give_away.log', msg + '\n')
        # print(msg)

    def print_to_file(self, filename, message):
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(message)
