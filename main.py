def calculate_total_price(products):
    total = 0
    for item in products:
        total = total + item["price"]
    return total


def apply_discount(price, discount):
    if discount > 1:
        discount = discount / 100
    return price - price * discount


def update_stock(products, product_name, amount):
    if isinstance(amount, str):
        amount = int(amount) if amount.isdigit() else 0

    for product in products:
        if product["name"] == product_name:
            product["stock"] = product["stock"] - amount


def get_average_price(products):
    total = calculate_total_price(products)
    return total / len(products)


def print_products(products):
    for i in range(len(products)):
        print(products[i]["name"], "-", products[i]["price"], "-", products[i].get("stock", "N/A"))


products = [
    {"name": "Pencil", "price": 0.99, "stock": 100},
    {"name": "Notebook", "price": 2.50, "stock": 50},
    {"name": "Backpack", "price": 25, "stock": 20},
    {"name": "Marker", "price": 1.5}
]


print("Product list:")
print_products(products)


print("Applying discount...")
discounted = apply_discount(100, 20)
print("Discounted price:", discounted)


print("Updating stock...")
update_stock(products, "Notebook", "5")
print(products)


average = get_average_price(products)
print("Average price:", average)


choice = input("Enter product name to buy: ")
quantity_input = input("Enter quantity: ")

if isinstance(quantity_input, str):
    try:
        quantity = int(quantity_input)
    except ValueError:
        quantity = 0
else:
    quantity = quantity_input

for product in products:
    if product["name"] == choice:
        if quantity <= product["stock"]:
            product["stock"] = product["stock"] - quantity
            print("Purchase successful")
        else:
            print("Not enough stock")


count = 0
while count < len(products):
    print(products[count]["name"])
    count = count + 1


print("Done")
