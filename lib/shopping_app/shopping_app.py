from customer import Customer
from item import Item
from seller import Seller
from item_manager import *

seller = Seller("DIC Store")
for i in range(10):
    Item("CPU", 40830, seller)
    Item("Memory", 13880, seller)
    Item("Motherboard", 28980, seller)
    Item("Power Unit", 8980, seller)
    Item("PC Case", 8727, seller)
    Item("3.5-inch HDD", 10980, seller)
    Item("2.5-inch SSD", 13370, seller)
    Item("M.2 SSD", 12980, seller)
    Item("CPU Cooler", 13400, seller)
    Item("Graphics Card", 23800, seller)

print("🤖 Please tell me your name")
customer = Customer(input())

print("🏧 Please enter the amount to charge into your wallet")
customer.wallet.deposit(int(input()))

print("🛍️ Starting shopping")
end_shopping = False
while not end_shopping:
    print("📜 Item List")
    seller.show_items()

    print("️️⛏ Please enter the item number")
    number = int(input())

    print("⛏ Please enter the item quantity")
    quantity = int(input())

    items = seller.pick_items(number, quantity)
    for item in items:
        customer.cart.add(item)
    print("🛒 Cart Contents")
    customer.cart.show_items()
    print(f"🤑 Total Amount: {customer.cart.total_amount()}")

    print("😭 Do you want to end shopping? (yes/no)")
    end_shopping = input() == "yes"

print("💸 Do you want to confirm the purchase? (yes/no)")
if input() == "yes":
    customer.cart.check_out()

print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈ Results ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
print(f"️🛍️ ️{customer.name}'s belongings")
customer.show_items()
print(f"😱👛 {customer.name}'s Wallet Balance: {customer.wallet.balance}")

print(f"📦 {seller.name}'s Inventory Status")
seller.show_items()
print(f"😻👛 {seller.name}'s Wallet Balance: {seller.wallet.balance}")

print("🛒 Cart Contents")
customer.cart.show_items()
print(f"🌚 Total Amount: {customer.cart.total_amount()}")

print("🎉 End")
