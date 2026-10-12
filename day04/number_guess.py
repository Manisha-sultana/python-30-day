secret_number = 7
attempts = 5

for attempt in range(1, attempts + 1):
    guess = int(input("Guess the number(1-10) : "))

    if guess == secret_number:
        print("Congratulations! You guessed correctly.")
        break
    elif guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")

    if attempt == attempts:
        print("Game over! The correct number was", secret_number)