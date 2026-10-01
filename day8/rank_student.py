names = ["Rahul", "Aman", "Priya", "Neha"]
marks = [80, 95, 90, 95]

result = sorted(zip(names, marks), key=lambda student: (-student[1], student[0]))

print(result)