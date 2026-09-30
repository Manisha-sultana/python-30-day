phonebook = {}

phonebook["Manisha"] = "9876543210"
phonebook["Rahul"] = "9876501234"

print(phonebook)

name = input("Enter name to search: ")

if name in phonebook:
    print("Phone:", phonebook[name])
else:
    print("Contact not found")