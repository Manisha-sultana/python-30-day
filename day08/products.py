products = [
    {"name": "Laptop", "price": 50000, "category": "Electronics"},
    {"name": "Mouse", "price": 500, "category": "Electronics"},
    {"name": "Chair", "price": 3000, "category": "Furniture"},
]
result = []
for p in products:
    if p["price"] < 5000:
        result.append(p)

print(result)