filename = input("Enter the filename: ")
try:
    with open(filename, "r") as file:
        content = file.read()
        print("File content:")
        print(content)

except FileNotFoundError:
    print("Error: File not found. Please check the filename.")
