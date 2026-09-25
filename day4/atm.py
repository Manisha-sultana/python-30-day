balance = 5000

while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print(f"Your balance is: ₹{balance:.2f}")

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Deposit successful.")
        else:
            print("Enter a valid amount.")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Enter a valid amount.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print("Withdrawal successful.")

    elif choice == "4":
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice. Please try again.")