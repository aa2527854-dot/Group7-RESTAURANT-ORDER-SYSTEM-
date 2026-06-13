class Order:
    def __init__(self, order_id, customer_name):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = []

    def add_item(self, menu_item):
        self.items.append(menu_item)

    def remove_item(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                self.items.remove(item)
                return item

        return None

    def total(self):
        total_price = 0

        for item in self.items:
            total_price += item.price

        return total_price

    def summary(self):
        return (
            self.order_id,
            self.customer_name,
            self.total(),
            len(self.items)
        )
