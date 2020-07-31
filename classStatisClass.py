##!/usr/bin/env python3

""" The franchise method, which takes in a store as argument. It should return a new Store object, with a name equal to the argument + " - franchise".
The store_details method, which alsotakes in a store as argument.It should return a string representing the argument. """


class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        # total = 0
        # for item in self.items:
        #     total += int(item['price'])
        # return total
        return sum([int(item['price']) for item in self.items])

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        return cls(f"{store.name} - franchise")

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'

        return f"{store.name}, total stock price: {store.stock_price()}"
        # return store.name+", total stock price: "+str(store.stock_price())


store = Store('Test')

store2 = Store('Amazon')
store2.add_item('Keyboard', '160')

print(Store.franchise(store).name)
print(Store.franchise(store2).name)

print(Store.store_details(store))
print(Store.store_details(store2))