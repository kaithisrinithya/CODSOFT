# -------------------------------
# Simple Calculator with Exit
# -------------------------------

while True:
    print("\n===== CALCULATOR =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # Exit option
    if choice == "5":
        print("Exiting Calculator... Goodbye!")
        break

    # Check valid choice
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice! Try again.")
        continue

    # Take numbers
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Enter numbers only.")
        continue

    # Perform operations
    if choice == "1":
        print(f"Result: {num1} + {num2} = {num1 + num2}")

    elif choice == "2":
        print(f"Result: {num1} - {num2} = {num1 - num2}")

    elif choice == "3":
        print(f"Result: {num1} * {num2} = {num1 * num2}")

    elif choice == "4":
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
        else:
            print(f"Result: {num1} / {num2} = {num1 / num2}")
