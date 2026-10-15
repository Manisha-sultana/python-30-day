import argparse
import secrets
import string


def generate_password(length, use_letters, use_digits, use_symbols):
    characters = ""

    if use_letters:
        characters += string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_symbols:
        characters += "!@#$%^&*()-_=+?"

    if not characters:
        raise ValueError("Select at least one character type.")

    return "".join(
        secrets.choice(characters) for _ in range(length)
    )


def main():
    parser = argparse.ArgumentParser(
        description="Generate a random password."
    )

    parser.add_argument("--length", type=int, default=12)
    parser.add_argument("--letters", action="store_true")
    parser.add_argument("--digits", action="store_true")
    parser.add_argument("--symbols", action="store_true")

    args = parser.parse_args()

    if args.length < 1:
        parser.error("--length must be at least 1")

    # If no type is selected, enable all three.
    if not (args.letters or args.digits or args.symbols):
        args.letters = args.digits = args.symbols = True

    password = generate_password(
        args.length,
        args.letters,
        args.digits,
        args.symbols
    )

    print("Generated password:", password)


if __name__ == "__main__":
    main()