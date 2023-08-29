from ownable import Ownable

class Cart(Ownable):
    from item_manager import show_items

    def __init__(self, owner):
        self.set_owner(owner)
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def check_out(self):
        if self.owner.wallet.balance < self.total_amount():
            pass
        # Requirements
        #   - The purchase amount of each item in the cart (Cart#items) should be transferred from the cart owner's wallet to the item owner's wallet.
        #   - Ownership of all items in the cart (Cart#items) should be transferred to the cart owner.
        #   - The cart's contents (Cart#items) should be emptied.
        # Hints
        #   - Cart owner's wallet ==> self.owner.wallet
        #   - Item owner's wallet ==> item.owner.wallet
        #   - Transferring money ==> Withdraw that amount from (？) and deposit it into (？)
        #   - Transferring ownership of items ==> Change the owner (item.owner = ?)
