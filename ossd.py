class MenuItem:
    def __init__(self, name, item_type, price):
        self.name = name
        self.item_type = item_type
        self.price = price


class CoffeeShop:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu
        self.orders = []

    def addOrder(self, item):
        for menu_item in self.menu:
            if menu_item.name == item:
                self.orders.append(item)
                return "Order added!"
        return "This item is currently unavailable!"

    def fulfillOrder(self):
        if self.orders:
            item = self.orders.pop(0)
            return f"The {item} is ready!"
        return "All orders have been fulfilled!"

    def listOrders(self):
        return self.orders

    def dueAmount(self):
        total_amount = 0.0
        for item in self.orders:
            for menu_item in self.menu:
                if menu_item.name == item:
                    total_amount += menu_item.price
        return total_amount

    def cheapestItem(self):
        cheapest_price = float('inf')
        cheapest_item = ""
        for menu_item in self.menu:
            if menu_item.price < cheapest_price:
                cheapest_price = menu_item.price
                cheapest_item = menu_item.name
        return cheapest_item

    def drinksOnly(self):
        drinks = []
        for menu_item in self.menu:
            if menu_item.item_type == "drink":
                drinks.append(menu_item.name)
        return drinks

    def foodOnly(self):
        food = []
        for menu_item in self.menu:
            if menu_item.item_type == "food":
                food.append(menu_item.name)
        return food


# Creating menu items
menu_items = [
    MenuItem("cinnamon roll", "food", 1.2),
    MenuItem("iced coffee", "drink", 0.97),
    MenuItem("lemonade", "drink", 1.5),
    MenuItem("tuna sandwich", "food", 4.5),
    MenuItem("ham and cheese sandwich", "food", 3.8),
    MenuItem("bacon and egg sandwich", "food", 4.25),
    MenuItem("orange juice", "drink", 1.8),
    MenuItem("cranberry juice", "drink", 2.1),
    MenuItem("pineapple juice", "drink", 2.5),
]

# Creating a coffee shop
tcs = CoffeeShop("The Coffee Shop", menu_items)

# Adding orders
print(tcs.addOrder("hot cocoa"))  # Expected output: "This item is currently unavailable!"
print(tcs.addOrder("iced tea"))  # Expected output: "This item is currently unavailable!"
print(tcs.addOrder("cinnamon roll"))  # Expected output: "Order added!"
print(tcs.addOrder("iced coffee"))  # Expected output: "Order added!"

# Listing orders
print(tcs.listOrders())  # Expected output: ["cinnamon roll", "iced coffee"]

# Due amount
print(tcs.dueAmount())  # Expected output: 2.17

# Fulfilling orders
print(tcs.fulfillOrder())  # Expected output: "The cinnamon roll is ready!"
print(tcs.fulfillOrder())  # Expected output: "The iced coffee is ready!"
print(tcs.fulfillOrder())  # Expected output: "All orders have been fulfilled!"

# Listing orders
print(tcs.listOrders())  # Expected output: []

# Due amount
print(tcs.dueAmount())  # Expected output: 0.0

