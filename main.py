import os


def signup():
    username = input("Enter Username: ")
    if os.path.exists(f"{username}.txt"):
        print("Username Already exist.")
    else:
        password = input("Enter Password: ")
        print("Signed up!")
        budget = input("Enter your budget: ")

        with open(f"{username}.txt", "w") as f:
            f.write(f"{username}\n")
            f.write(f"{password}\n")
            f.write(f"Budget: {budget}\n")


def view_balance(username):
    try:
        with open(f"{username}.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("Budget:"):
                    balance = line.strip().split(":")[1].strip()
                    print(f"Your balance is: {balance}")
                    return float(balance)
    except FileNotFoundError:
        print("⚠️ User file not found.")
        return None


def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    try:
        with open(f"{username}.txt", "r") as f:
            lines = f.readlines()
            stored_username = lines[0].strip()
            stored_password = lines[1].strip()

            if username == stored_username and password == stored_password:
                print("✅ Login successful!")
                return True, username
            else:
                print("❌ Invalid username or password.")
                return False, None
    except FileNotFoundError:
        print("⚠️ User file not found.")
        return False, None


def add_balance(username):
    try:
        amount = float(input("Enter the amount to add to your balance: "))
        with open(f"{username}.txt", "r") as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            if line.startswith("Budget:"):
                current_balance = float(line.strip().split(":")[1].strip())
                new_balance = current_balance + amount
                lines[i] = f"Budget: {new_balance}\n"
                break

        with open(f"{username}.txt", "w") as f:
            f.writelines(lines)

        print(f"✅ Added {amount}. New balance: {new_balance}")
    except ValueError:
        print("⚠️ Please enter a valid number.")


def add_expense(username):
    try:
        amount = float(input("Enter expense amount: "))
        reason = input("Enter reason: ")
        date = input("Enter date (e.g. 2025-07-30): ")

        with open(f"{username}.txt", "r") as f:
            lines = f.readlines()

        for i in range(len(lines)):
            if lines[i].startswith("Budget:"):
                current = float(lines[i].split(":")[1].strip())
                if amount > current:
                    print("❌ Not enough balance.")
                    return
                updated = current - amount
                lines[i] = f"Budget: {updated:.2f}\n"
                break

        lines.append(f"Expense: {amount:.2f} | Reason: {reason} | Date: {date}\n")

        with open(f"{username}.txt", "w") as f:
            f.writelines(lines)

        print(f"✅ Expense of {amount} added. New balance: {updated:.2f}")
    except FileNotFoundError:
        print("❌ Invalid input.")


def view_expense(username):
    try:
        with open(f"{username}.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("Expense"):
                    show_expense = line.strip().split("|")
                    print(show_expense)
    except FileNotFoundError:
        print("⚠️ User file not found.")
        return None


# Main program
signup_or_login = int(input("1 - Signup\n2 - Login\nChoose option: "))

if signup_or_login == 1:
    signup()
elif signup_or_login == 2:
    success, username = login()
    if success:
        print("Welcome to your Budget Tracker!")
        while True:
            try:
                user_input = int(
                    input(
                        "\nEnter:\n 1 - Add Budget\n 2 - Add Expense\n 3 - View Balance\n 4 - View Expenses \n 5- Exit\nChoice: "
                    )
                )
                if user_input == 1:
                    add_balance(username)
                elif user_input == 2:
                    add_expense(username)
                elif user_input == 3:
                    view_balance(username)
                elif user_input == 4:
                    view_expense(username)
                elif user_input == 5:
                    print("Goodbye!")
                    break
                else:
                    print("❌ Invalid option, try again.")
            except ValueError:
                print("❌ Please enter a valid number.")
    else:
        print("Login failed. Please try again.")
else:
    print("❌ Invalid option. Choose 1 or 2.")
