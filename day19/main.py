import argparse
import csv
import logging
import sys
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "Personal Expense Tracker"))

from errors import InvalidAmountError, InvalidDateError
from storage import load_expenses, save_expenses

LOG_FILE = Path(__file__).parent / "expenses.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def validate_expense(amount, expense_date):
    if amount <= 0:
        raise InvalidAmountError("Amount must be greater than zero.")

    try:
        datetime.strptime(expense_date, "%Y-%m-%d")
    except ValueError as error:
        raise InvalidDateError(
            "Date must use YYYY-MM-DD format."
        ) from error


def add_expense(args):
    try:
        validate_expense(args.amount, args.date)

        expenses = load_expenses()
        next_id = max(
            (expense["id"] for expense in expenses),
            default=0,
        ) + 1

        expense = {
            "id": next_id,
            "amount": args.amount,
            "category": args.category,
            "date": args.date,
            "note": args.note,
        }

        expenses.append(expense)
        save_expenses(expenses)

        logging.info("Added expense ID %s", next_id)
        print(f"Expense added successfully. ID: {next_id}")

    except (InvalidAmountError, InvalidDateError) as error:
        logging.warning("Invalid expense: %s", error)
        print(f"Error: {error}")


def list_expenses(args):
    expenses = load_expenses()

    if args.month:
        expenses = [
            expense for expense in expenses
            if expense["date"].startswith(args.month)
        ]

    if not expenses:
        print("No expenses found.")
        return

    for expense in expenses:
        print(
            f'ID: {expense["id"]} | '
            f'{expense["date"]} | '
            f'{expense["category"]} | '
            f'Rs. {expense["amount"]:.2f} | '
            f'{expense["note"]}'
        )


def show_summary(args):
    expenses = load_expenses()

    if args.month:
        expenses = [
            expense for expense in expenses
            if expense["date"].startswith(args.month)
        ]

    if not expenses:
        print("No expenses to summarize.")
        return

    total = sum(expense["amount"] for expense in expenses)
    print(f"Total spending: Rs. {total:.2f}")

    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        category_totals[category] = (
            category_totals.get(category, 0) + expense["amount"]
        )

    for category, amount in category_totals.items():
        print(f"{category}: Rs. {amount:.2f}")


def delete_expense(args):
    expenses = load_expenses()
    remaining = [
        expense for expense in expenses
        if expense["id"] != args.id
    ]

    if len(remaining) == len(expenses):
        print("Expense ID not found.")
        return

    save_expenses(remaining)
    logging.info("Deleted expense ID %s", args.id)
    print("Expense deleted successfully.")


def export_expenses(args):
    expenses = load_expenses()
    output_file = Path(args.file)

    with open(output_file, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["id", "amount", "category", "date", "note"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)

    logging.info("Exported expenses to %s", output_file)
    print(f"Expenses exported to {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Personal Expense Tracker"
    )
    commands = parser.add_subparsers(dest="command", required=True)

    add_parser = commands.add_parser("add")
    add_parser.add_argument("--amount", type=float, required=True)
    add_parser.add_argument("--category", required=True)
    add_parser.add_argument("--date", default=date.today().isoformat())
    add_parser.add_argument("--note", default="")
    add_parser.set_defaults(func=add_expense)

    list_parser = commands.add_parser("list")
    list_parser.add_argument("--month", help="Filter by YYYY-MM")
    list_parser.set_defaults(func=list_expenses)

    summary_parser = commands.add_parser("summary")
    summary_parser.add_argument("--month", help="Filter by YYYY-MM")
    summary_parser.set_defaults(func=show_summary)

    delete_parser = commands.add_parser("delete")
    delete_parser.add_argument("--id", type=int, required=True)
    delete_parser.set_defaults(func=delete_expense)

    export_parser = commands.add_parser("export")
    export_parser.add_argument(
        "--file", default="expenses.csv"
    )
    export_parser.set_defaults(func=export_expenses)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()