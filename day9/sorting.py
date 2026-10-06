#bubble sort 
numbers = [5, 2, 8, 1, 3]

for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):

        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)

#insertion sort
numbers = [5, 2, 8, 1, 3]

for i in range(1, len(numbers)):
    key = numbers[i]
    j = i - 1

    while j >= 0 and numbers[j] > key:
        numbers[j + 1] = numbers[j]
        j -= 1

    numbers[j + 1] = key

print(numbers)


#sorted()
numbers = [5, 2, 8, 1, 3]

print(sorted(numbers))