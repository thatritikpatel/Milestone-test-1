class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.order_items = []

    def add_item(self, order_item):
        self.order_items.append(order_item)