numbers = [1, 2, 3, 4, 5]

# Loop
result = []

for n in numbers:
    result.append(n * 2)

# Comprehension
result = [n ** 2 for n in numbers]

print(result)