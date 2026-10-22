import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "expenses.json"


def load_expenses():
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_expenses(expenses):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)