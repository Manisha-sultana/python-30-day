from datetime import date


def calculate_age(birth_date):
    today = date.today()

    if birth_date > today:
        raise ValueError("Date of birth cannot be in the future.")

    years = today.year - birth_date.year

    if (today.month, today.day) < (
        birth_date.month, birth_date.day
    ):
        years -= 1

    last_birthday_year = birth_date.year + years

    try:
        last_birthday = birth_date.replace(
            year=last_birthday_year
        )
    except ValueError:
        # Handles February 29 in a non-leap year.
        last_birthday = date(last_birthday_year, 2, 28)

    months = (today.year - last_birthday.year) * 12
    months += today.month - last_birthday.month

    if today.day < last_birthday.day:
        months -= 1

    if today.day >= last_birthday.day:
        days = today.day - last_birthday.day
    else:
        previous_month = (
            today.month - 1 if today.month > 1 else 12
        )
        previous_year = (
            today.year if today.month > 1 else today.year - 1
        )
        days_in_previous_month = (
            date(today.year, today.month, 1)
            - date(previous_year, previous_month, 1)
        ).days if today.month > 1 else (
            date(today.year, 1, 1) - date(today.year - 1, 12, 1)
        ).days
        days = days_in_previous_month - last_birthday.day + today.day

    next_year = today.year
    try:
        next_birthday = birth_date.replace(year=next_year)
    except ValueError:
        next_birthday = date(next_year, 2, 28)

    if next_birthday <= today:
        try:
            next_birthday = birth_date.replace(year=next_year + 1)
        except ValueError:
            next_birthday = date(next_year + 1, 2, 28)

    days_left = (next_birthday - today).days

    return years, months, days, days_left


def main():
    try:
        dob_text = input("Enter DOB (YYYY-MM-DD): ")
        birth_date = date.fromisoformat(dob_text)

        years, months, days, days_left = calculate_age(birth_date)

        print(f"Age: {years} years, {months} months, {days} days")
        print(f"Days until next birthday: {days_left}")

    except ValueError as error:
        print("Invalid date:", error)


if __name__ == "__main__":
    main()