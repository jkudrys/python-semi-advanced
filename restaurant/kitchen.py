from time import sleep, time, ctime


class Kitchen:

    def __init__(self, manager):
        self.manager = manager

    def prepare_meal(self, order):
        msg = f'Kitchen: Start preparing <{order.order_name}> at {ctime(time())}'
        # print(msg)
        self.print_to_file('kitchen.log', msg + '\n')
        sleep(3)
        self.meal_ready(order)

    def meal_ready(self, order):
        order.meal_ready_time = time()
        msg = f'Kitchen: <{order.order_name}> prepared at {ctime(time())}'
        self.manager.meal_ready(order)
        # print(msg)
        self.print_to_file('kitchen.log', msg + '\n')

    def print_to_file(self, filename, message):
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(message)
