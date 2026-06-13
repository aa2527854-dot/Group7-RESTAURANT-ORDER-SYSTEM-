from Order import Order


class Restaurant:
    def __init__(self):
        self.menu = {}
        self.daily_orders = []
        self.unique_customers = set()

    def show_menu(self):
        print("\n----- MENU -----")

        for item in self.menu.values():
            item.display()

    def new_order(self, customer_name):
        order_id = len(self.daily_orders) + 1

        order = Order(order_id, customer_name)

        self.unique_customers.add(customer_name)

        return order

    def checkout(self, order):
        subtotal = order.total()

        vat = subtotal * 0.15

        final = subtotal + vat

        method = input(
            "Payment Method (cash/card/applepay): "
        ).lower()

        match method:

            case "cash":
                fee = 0
                print("Pay at the counter")

            case "card":
                fee = 1
                print("Insert card")

            case "applepay":
                fee = 0
                print("Tap your device")

            case _:
                print("Unknown method")
                return

        final += fee

        self.daily_orders.append(order)

        print("\n----- RECEIPT -----")
        print(f"Subtotal : {subtotal:.2f}")
        print(f"VAT      : {vat:.2f}")
        print(f"Total    : {final:.2f} SAR")

    def show_orders(self):
        print("\n----- TODAY ORDERS -----")

        for order in self.daily_orders:
            print(order.summary())

    def stats(self):
        total_sales = 0

        for order in self.daily_orders:
            total_sales += order.total()

        print("\n----- STATISTICS -----")
        print(f"Total Sales      : {total_sales:.2f}")
        print(f"Number Of Orders : {len(self.daily_orders)}")
        print(f"Unique Customers : {len(self.unique_customers)}")

        item_counter = {}

        for order in self.daily_orders:
            for item in order.items:

                if item.name in item_counter:
                    item_counter[item.name] += 1
                else:
                    item_counter[item.name] = 1

        if item_counter:
            most_ordered = max(
                item_counter,
                key=item_counter.get
            )

            print(
                f"Most Ordered Item : {most_ordered}"
            )

