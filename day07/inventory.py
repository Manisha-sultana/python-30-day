inventory = {
    "laptop": {
        "price": 50000,
        "stock": 5
    },
    "mouse": {
        "price": 500,
        "stock": 2
    },
    "keyboard": {
        "price": 1500,
        "stock": 0
    }
}

for product, details in inventory.items():
    if details["stock"] <= 2:
        print("Low stock:", product)