number = int(input("Enter a number: "))

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
    
    
    #Nested loop
    for number in range(1, 11):
    print(f"\nTable of {number}")

    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")