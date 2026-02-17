# DEBUGGING ASSIGNMENT
# This file contains MANY intentional errors.
# The program should manage a list of products and print summary information.
# Fix all errors so the program runs correctly and produces logical output.

def calculate_total_price(products):
    total = 0
    for item in products:
        total = total + item["price"]
    return total


def apply_discount(price, discount):
    if discount > 1:
        discount = discount / 100
    return price - (price * discount)


def update_stock(products, product_name, amount):
    for product in products:
        if product["name"] == product_name:
            product["stock"] -= amount
    return product


def get_average_price(products):
    total = calculate_total_price(products)
    return total / len(products)


def print_products(products):
    for i in range(len(products)):
        print(products[i]["name"], "-", products[i]["price"], "-", products[i]["stock"])


products = [
    {"name": "Pencil", "price": 0.99, "stock": 100},
    {"name": "Notebook", "price": 2.50, "stock": 50},
    {"name": "Backpack", "price": 25, "stock": 20},
    {"name": "Marker", "price": 1.5, "stock": 40}
]


print("Product list:")
print_products(products)


print("Applying discount...")
discounted = apply_discount(10, 20)
print("Discounted price:", discounted)


print("Updating stock...")
update_stock(products, "Notebook", 5)
print(products)


average = get_average_price(products)
print("Average price:", average)


choice = input("Enter product name to buy: ")
quantity = input("Enter quantity: ")

for product in products:
    if product["name"] == choice:
        if int(quantity) <= product["stock"]:
            product["stock"] = product["stock"] - int(quantity)
            print("Purchase successful")
        else:
            print("Not enough stock")

count = 0
while count < len(products):
    print(products[count]["name"])
    count = count + 1

print("Done")
