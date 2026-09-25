marks = float(input("Enter your marks: "))xz
if marks < 0 or marks > 100:
    print("Invalid marks. Please enter marks between 0 and 100.")
elif marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")