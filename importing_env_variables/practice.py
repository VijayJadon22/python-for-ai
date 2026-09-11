def calculate_total(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]

    print(f"The total price of the grocery is {total}")


grocery_list = [
    {"name": "slipper", "price": 100, "quantity": 3},
    {"name": "socks", "price": 15, "quantity": 6},
    {"name": "bedsheet", "price": 350, "quantity": 2},
]

calculate_total(grocery_list)

#formatted by Ruff extension