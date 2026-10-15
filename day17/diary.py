from datetime import datetime
from pathlib import Path

DIARY_FILE = Path("diary.txt")


def add_entry():
    entry = input("Write your diary entry: ").strip()

    if not entry:
        print("Entry cannot be empty.")
        return

    date_time = datetime.now().strftime("%Y-%m-%d %H:%M")

    with DIARY_FILE.open("a", encoding="utf-8") as file:
        file.write(f"[{date_time}] {entry}\n")

    print("Diary entry saved!")


def search_entries():
    keyword = input("Enter keyword to search: ").strip().lower()

    if not keyword:
        print("Keyword cannot be empty.")
        return

    if not DIARY_FILE.exists():
        print("No diary entries found.")
        return

    with DIARY_FILE.open("r", encoding="utf-8") as file:
        matches = [
            line.strip()
            for line in file
            if keyword in line.lower()
        ]

    if matches:
        for entry in matches:
            print(entry)
    else:
        print("No matching entries found.")


def main():
    while True:
        print("\n1. Add entry")
        print("2. Search entries")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_entry()
        elif choice == "2":
            search_entries()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()