
class MenuItem:
    def __init__(self, name, price, category, stock=0):
        self.name = name
        self.price = price
        self.category = category
        self._stock = stock

    def prepare_time(self):
        return 0

    def restock(self, amount):
        self._stock += amount

    def get_stock(self):
        return self._stock

    def display(self):
        print(
            f"{self.name} | "
            f"{self.price} SAR | "
            f"Stock: {self._stock}"
        )


class Food(MenuItem):
    def __init__(self, name, price, stock=0):
        super().__init__(name, price, "Food", stock)

    def prepare_time(self):
        return 10


class Drink(MenuItem):
    def __init__(self, name, price, stock=0):
        super().__init__(name, price, "Drink", stock)

    def prepare_time(self):
        return 2
    
def display(self):
    print(
        f"{self.name} | "
        f"{self.price} SAR | "
        f"Stock: {self._stock}"
    )
