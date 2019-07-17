from time import time, ctime


class Order:

    def __init__(self, order_name):
        self.order_name = order_name
        self.order_time = time()
        self.meal_ready_time = 0
        self.collected_time = 0

    def __str__(self) -> str:
        return f' *** {self.order_name}, collected at: {ctime(self.meal_ready_time)}, ' \
               f'delivered at: {ctime(self.collected_time)} ***\n'
