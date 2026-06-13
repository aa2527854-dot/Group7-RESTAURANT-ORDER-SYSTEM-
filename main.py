from menuitem import Food , Drink
from restaurant import Restaurant


restaurant = Restaurant()

restaurant.menu["Kabsa"] = Food(
    "Kabsa",
    45,
    30
)

restaurant.menu["Shawarma"] = Food(
    "Shawarma",
    15,
    50
)

restaurant.menu["Mandi"] = Food(
    "Mandi",
    55,
    20
)

restaurant.menu["Karak"] = Drink(
    "Karak",
    8,
    100
)

restaurant.menu["Laban"] = Drink(
    "Laban",
    5,
    80
)

current_order = None

while True:

    print("\n===== RESTAURANT SYSTEM =====")
    print("1. Show Menu")
    print("2. New Order")
    print("3. Add Item")
    print("4. Remove Item")
    print("5. Checkout")
    print("6. Show Orders Today")
    print("7. Statistics")
    print("8. Exit")

    choice = input("Choose: ")

    match choice:

        case "1":
            restaurant.show_menu()

        case "2":
            customer_name = input(
                "Customer Name: "
            )

            current_order = restaurant.new_order(
                customer_name
            )

            print("Order Created")

        case "3":

            if current_order is None:
                print("Create Order First")
                continue

            item_name = input(
                "Item Name: "
            )

            item = restaurant.menu.get(item_name)

            if item is None:
                print("Item Not On Menu")

            elif item.get_stock() <= 0:
                print("Out Of Stock")

            else:
                current_order.add_item(item)

                item._stock -= 1

                print("Item Added")

        case "4":

            if current_order is None:
                print("Create Order First")
                continue

            item_name = input(
                "Item Name: "
            )

            removed_item = current_order.remove_item(
                item_name
            )

            if removed_item:
                removed_item._stock += 1
                print("Item Removed")
            else:
                print("Not In Order")

        case "5":

            if current_order is None:
                print("No Active Order")
                continue

            restaurant.checkout(current_order)

            current_order = None

        case "6":
            restaurant.show_orders()

        case "7":
            restaurant.stats()

        case "8":
            print("Goodbye")
            break

        case _:
            print("Invalid Choice")