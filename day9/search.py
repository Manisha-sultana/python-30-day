numbers = [10, 20, 30, 40, 50]

target = 30

for i, number in enumerate(numbers):
    if number == target:
        print("Found at index:", i)
        break
else:
    print("Not found")