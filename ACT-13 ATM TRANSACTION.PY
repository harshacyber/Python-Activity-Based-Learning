balance = 5000

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = int(input("Enter deposit amount: "))
        balance = balance + amount
        print("Amount deposited")

    elif choice == 2:
        amount = int(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance = balance - amount
            print("Collect your money")
        else:
            print("Insufficient balance")

    elif choice == 3:
        print("Balance:", balance)

    elif choice == 4:
        break

    else:
        print("Invalid choice")