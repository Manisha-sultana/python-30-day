import random


def guessing_game():
    secret_number = random.randint(1, 10)
    attempts = 0

    print("Guess a number between 1 and 10")

    while True:
        user_input = input("Enter your guess: ")

        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(user_input)
        attempts += 1

        if guess == secret_number:
            print("Congratulations! You guessed correctly.")
            print(f"Attempts: {attempts}")
            break
        elif guess < secret_number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")


if __name__ == "__main__":
    guessing_game()