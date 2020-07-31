##!/usr/bin/env python3

""" The __init__ method, which should take an argument, name. It should initialise self.name to be the argument, and self.items to be an empty list.
The add_item method, which should append a dictionary representing an item to the store's items property. The dictionary should have keys name and price.
The stock_price method, which should add up each item price inside self.items to come up with a total, and return that. """


class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
        
        
    def add_item(self, name, price):
        item = {"name": name, "price": price}
        self.items.append(item)

    def stock_price(self):
        total_price = 0
        for item in self.items:
            total_price += item['price']
        return total_price


# Initialize the object
store = Store("General Store")

# Add Items to the Inventory
store.add_item('Copy', 10)
store.add_item('Soft Drikns', 45)

print(store.stock_price())
