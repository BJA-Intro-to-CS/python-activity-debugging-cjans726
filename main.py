# DEBUGGING ASSIGNMENT
# This file contains MANY intentional errors.
# The program should manage a list of products and print summary information.
# Fix all errors so the program runs correctly and produces logical output.

def calculate_total_price(products):
    total = 0
    for item in products:
        if isinstance(item.get("price"), (int, float)):
            total += item["price"]
    return total

def apply_discount(price, discount):
    if isinstance(discount, (int, float)) and discount > 1:
        discount = discount / 100
    
    if not isinstance(price, (int, float)):
        return None
    
    return price - price * discount

def update_stock(products, product_name, amount):
    for product in products:
        if product["name"] == product_name:
            if isinstance(amount, (int, float)) and isinstance(product["stock"], (int, float)):
                product["stock"] -= amount
                return product
    return None

def get_average_price(products):
    if not products:
        return 0
    total = calculate_total_price(products)
    return total / len(products)

def print_products(products):
    for i in range(len(products)):
        p = products[i]
        name = p.get("name", "???")
        price = p.get("price", "?")
        stock = p.get("stock", "?")
        print(f"{name} - ${price:.2f} - stock: {stock}")

products = [
    {"name": "Pencil",   "price": 0.99,  "stock": 100},
    {"name": "Notebook", "price": 2.50,  "stock": 50},
    {"name": "Backpack", "price": 25.0,  "stock": 20},
    {"name": "Marker",   "price": 1.50,  "stock": 75}
]

print("Product list:")
print_products(products)
print()

print("Applying discount...")
discounted = apply_discount(100, 20)
if discounted is not None:
    print(f"Discounted price: ${discounted:.2f}")
else:
    print("Can't apply discount: invalid price")
print()

print("Updating stock...")
updated = update_stock(products, "Notebook", 5)
if updated:
    print(f"Updated stock for {updated['name']}: {updated['stock']}")
else:
    print("Product not found")
print()

average = get_average_price(products)
print(f"Average price: ${average:.2f}")
print()

choice = input("Enter product name to buy: ").strip()
quantity_str = input("Enter quantity: ").strip()

try:
    quantity = int(quantity_str)
except ValueError:
    print("Invalid quantity: must be a whole number")
    quantity = 0

found = False
for product in products:
    if product["name"].lower() == choice.lower():
        found = True
        if isinstance(product["stock"], (int, float)) and quantity <= product["stock"]:
            product["stock"] -= quantity
            print(f"Purchase successful! New stock: {product['stock']}")
        else:
            print("Not enough stock or invalid stock value")
        break

if not found:
    print("Product not found")

print("All product names:")
count = 0
while count < len(products):
    print(products[count]["name"])
    count += 1

print("Done")

