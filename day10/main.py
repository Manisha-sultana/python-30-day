students = []

subjects = ["Math", "Science", "English", "Computer", "Hindi"]


# -----------------------------
# Helper Functions
# -----------------------------

def get_number(prompt, minimum=None, maximum=None):
    while True:
        try:
            value = int(input(prompt))

            if minimum is not None and value < minimum:
                print(f"Value {minimum} se kam nahi hona chahiye.")
                continue

            if maximum is not None and value > maximum:
                print(f"Value {maximum} se zyada nahi hona chahiye.")
                continue

            return value

        except ValueError:
            print("Please valid number enter karo.")


# -----------------------------
# Add Student
# -----------------------------

def add_student():
    print("\n--- Add Student ---")

    roll = get_number("Enter roll number: ", 1)

    # Duplicate roll number check
    for student in students:
        if student["roll"] == roll:
            print("This roll number already exists!")
            return

    name = input("Enter student name: ").strip()

    while name == "":
        print("Name empty nahi ho sakta.")
        name = input("Enter student name: ").strip()

    marks = []

    for subject in subjects:
        mark = get_number(
            f"Enter marks for {subject} (0-100): ",
            0,
            100
        )
        marks.append(mark)

    student = {
        "roll": roll,
        "name": name,
        "marks": marks
    }

    students.append(student)

    print("Student added successfully!")


# -----------------------------
# View Students
# -----------------------------

def view_students():
    print("\n--- All Students ---")

    if not students:
        print("No student records found.")
        return

    for student in students:
        total = sum(student["marks"])
        average = total / len(student["marks"])

        print("\nRoll Number:", student["roll"])
        print("Name:", student["name"])
        print("Marks:", student["marks"])
        print("Total:", total)
        print("Average:", round(average, 2))


# -----------------------------
# Search Student
# -----------------------------

def search_student():
    print("\n--- Search Student ---")
    print("1. Search by Roll Number")
    print("2. Search by Name")

    choice = input("Enter choice: ")

    if choice == "1":
        roll = get_number("Enter roll number: ")

        found = False

        for student in students:
            if student["roll"] == roll:
                print("\nStudent Found!")
                print("Roll:", student["roll"])
                print("Name:", student["name"])
                print("Marks:", student["marks"])
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "2":
        name = input("Enter student name: ").strip().lower()

        found = False

        for student in students:
            if student["name"].lower() == name:
                print("\nStudent Found!")
                print("Roll:", student["roll"])
                print("Name:", student["name"])
                print("Marks:", student["marks"])
                found = True

        if not found:
            print("Student not found.")

    else:
        print("Invalid choice.")


# -----------------------------
# Update Student
# -----------------------------

def update_student():
    print("\n--- Update Student ---")

    roll = get_number("Enter roll number to update: ")

    for student in students:

        if student["roll"] == roll:

            print("Student found:", student["name"])

            new_name = input(
                "Enter new name (press Enter to keep old name): "
            ).strip()

            if new_name:
                student["name"] = new_name

            print("\nEnter new marks:")

            new_marks = []

            for subject in subjects:
                mark = get_number(
                    f"Enter marks for {subject} (0-100): ",
                    0,
                    100
                )
                new_marks.append(mark)

            student["marks"] = new_marks

            print("Student updated successfully!")
            return

    print("Student not found.")


# -----------------------------
# Delete Student
# -----------------------------

def delete_student():
    print("\n--- Delete Student ---")

    roll = get_number("Enter roll number to delete: ")

    for student in students:

        if student["roll"] == roll:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


# -----------------------------
# Get Grade
# -----------------------------

def get_grade(average):

    # Grade boundaries are an implementation choice
    if average >= 90:
        return "A"

    elif average >= 80:
        return "B"

    elif average >= 70:
        return "C"

    elif average >= 60:
        return "D"

    else:
        return "F"


# -----------------------------
# Reports
# -----------------------------

def reports():
    print("\n--- Reports ---")

    if not students:
        print("No student records available.")
        return

    # Class Topper
    topper = max(
        students,
        key=lambda student: sum(student["marks"]) / len(student["marks"])
    )

    topper_average = sum(topper["marks"]) / len(topper["marks"])

    print("\n1. Class Topper")
    print("Name:", topper["name"])
    print("Roll:", topper["roll"])
    print("Average:", round(topper_average, 2))

    # Subject-wise Average
    print("\n2. Subject-wise Average")

    for i in range(len(subjects)):

        total = 0

        for student in students:
            total += student["marks"][i]

        average = total / len(students)

        print(subjects[i], ":", round(average, 2))

    # Grade Distribution
    print("\n3. Grade Distribution")

    grades = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "F": 0
    }

    for student in students:

        average = sum(student["marks"]) / len(student["marks"])

        grade = get_grade(average)

        grades[grade] += 1

    for grade, count in grades.items():
        print("Grade", grade, ":", count, "student(s)")


# -----------------------------
# Sort Students
# -----------------------------

def sort_students():
    print("\n--- Sort Students ---")

    if not students:
        print("No student records available.")
        return

    print("1. Sort by Roll Number")
    print("2. Sort by Name")
    print("3. Sort by Average Marks")

    choice = input("Enter choice: ")

    if choice == "1":

        result = sorted(
            students,
            key=lambda student: student["roll"]
        )

    elif choice == "2":

        result = sorted(
            students,
            key=lambda student: student["name"].lower()
        )

    elif choice == "3":

        result = sorted(
            students,
            key=lambda student: sum(student["marks"]) / len(student["marks"]),
            reverse=True
        )

    else:
        print("Invalid choice.")
        return

    print("\n--- Sorted Students ---")

    for student in result:

        average = sum(student["marks"]) / len(student["marks"])

        print(
            "Roll:",
            student["roll"],
            "| Name:",
            student["name"],
            "| Average:",
            round(average, 2)
        )


# -----------------------------
# Main Menu
# -----------------------------

def main():

    while True:

        print("\n================================")
        print("     STUDENT RECORDS MANAGER")
        print("================================")

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Reports")
        print("7. Sort Students")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            reports()

        elif choice == "7":
            sort_students()

        elif choice == "8":
            print("Thank you for using Student Records Manager!")
            break

        else:
            print("Invalid choice! Please select 1-8.")


# Start Program
main()