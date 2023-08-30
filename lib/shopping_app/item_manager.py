from tabulate import tabulate
from itertools import groupby
from item import Item


def items_list(self):   # Returns all Item instances owned by yourself.
    items = [item for item in Item.item_all() if item.owner == self]
    return items

def pick_items(self, number, quantity):   # Returns Item instances corresponding to the given number and quantity.
    items = filter(lambda num: num["number"] == number, _stock(self))
    items = list(items)
    if len(items) == 0:
        return []
    elif len(items[0]["items"]) < quantity:
        return []
    else:
        return items[0]["items"][0:quantity]

def show_items(self):   # Outputs the stock status of Item instances owned by yourself in a table format with columns ["Number", "Item Name", "Price", "Quantity"].
    table_data = []
    for stock in _stock(self):
        table_data.append([stock['number'], stock['label']['name'], stock['label']['price'], len(stock['items'])])
    print(tabulate(table_data, headers=["Number", "Item Name", "Price", "Quantity"], tablefmt="grid"))    # Using the tabulate module to output the results in a table format.
    #the code provided from the page isn't properly displaying the table with the added items in cart contents before completing the purchase


def _stock(self):   # Returns the stock status of Item instances owned by yourself.
    item_ls = self.items_list()
    item_ls.sort(key=lambda m: m.name)
    group_list = []
    for key, group in groupby(item_ls, key=lambda m: m.name):   # Classify by Item#name, which returns the same value for Item instances.
        group_list.append(list(group))
    stock = []
    for index, item in enumerate(group_list):
        stock.append({"number": index, "label": {"name": item[0].name, "price": item[0].price}, "items": item})   # The items list contains categorized Item instances.
    return stock
