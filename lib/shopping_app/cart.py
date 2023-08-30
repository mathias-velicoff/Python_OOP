from ownable import Ownable
from item_manager import show_items


class Cart(Ownable):

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
            print("insufficient funds. Cannot complete the purchase")
            return
        #El precio de compra de todos los artículos del carrito se transfiere del monedero del propietario del carrito al monedero del propietario del artículo.
        for item in self.items:
            self.owner.wallet.withdraw(item.price)
            item.owner.wallet.deposit(item.price)

            # Transfer ownership of the item to the cart owner
            item.owner = self.owner

        #vaciar contenido del carrito
        self.items = []
        print("purchase completed successfully")

        # Requirements
        #   - The purchase amount of each item in the cart (Cart#items) should be transferred from the cart owner's wallet to the item owner's wallet.
        #   - Ownership of all items in the cart (Cart#items) should be transferred to the cart owner.
        #   - The cart's contents (Cart#items) should be emptied.
        # Hints
        #   - Cart owner's wallet ==> self.owner.wallet
        #   - Item owner's wallet ==> item.owner.wallet
        #   - Transferring money ==> Withdraw that amount from (？) and deposit it into (？)
        #   - Transferring ownership of items ==> Change the owner (item.owner = ?)
