from wallet import Wallet
from ownable import Ownable

class User(Ownable):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.wallet = Wallet(self)

    def show_items(self):
        from item_manager import show_items
