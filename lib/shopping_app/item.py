class Item:
    instances = []

    def __init__(self, name, price, owner):
        self.name = name
        self.price = price
        self.owner = owner
        Item.instances.append(self)

    def label(self):
        return {"name": self.name, "price": self.price}

    @staticmethod
    def item_all():
        return Item.instances
