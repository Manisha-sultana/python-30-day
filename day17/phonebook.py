import json
from pathlib import Path

CONTACTS_FILE = Path("contacts.json")


def load_contacts():
    if not CONTACTS_FILE.exists():
        return {}

    with CONTACTS_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_contacts(contacts):
    with CONTACTS_FILE.open("w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=4)


def main():
    contacts = load_contacts()

    while True:
        print("\n1. Add contact")
        print("2. View contacts")
        print("3. Search contact")
        print("4. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()

            if not name or not phone:
                print("Name and phone are required.")
            else:
                contacts[name] = phone
                save_contacts(contacts)
                print("Contact saved.")

        elif choice == "2":
            if not contacts:
                print("No contacts saved.")
            else:
                for name, phone in contacts.items():
                    print(name, "-", phone)

        elif choice == "3":
            name = input("Name to search: ").strip()
            phone = contacts.get(name)

            if phone:
                print(name, "-", phone)
            else:
                print("Contact not found.")

        elif choice == "4":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()