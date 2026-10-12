bill = float(input("Enter total bill: "))1
people = int(input("Enter number of people: "))
tip_percentage = float(input("Enter tip percentage: "))

tip = bill * tip_percentage / 100
total_amount = bill + tip
amount_per_person = total_amount / people

print(f"Tip amount: {tip:.2f}")
print(f"Total amount: {total_amount:.2f}")
print(f"Amount per person: {amount_per_person:.2f}")