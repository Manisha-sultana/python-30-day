import csv

with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    students = list(reader)

with open("summary.csv", "w", newline="") as file:
    fieldnames = ["name", "total", "percentage", "result"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for student in students:
        math = int(student["math"])
        science = int(student["science"])
        english = int(student["english"])

        total = math + science + english
        percentage = total / 300 * 100

        if math >= 33 and science >= 33 and english >= 33:
            result = "Pass"
        else:
            result = "Fail"

        writer.writerow({
            "name": student["name"],
            "total": total,
            "percentage": round(percentage, 2),
            "result": result
        })

print("Summary CSV created successfully!")
