import json
from datetime import datetime
from pathlib import Path

DATA_FILE = Path("banking_console_data.json")


def load_data():
    if DATA_FILE.exists():
        try:
            return json.loads(DATA_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass
    return {"accounts": {}, "next_id": 1}


def save_data(data):
    DATA_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")


def now_text():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def add_transaction(account, entry):
    account["history"].append(f"{now_text()} | {entry}")


def create_account(data):
    name = input("Account holder name: ").strip()
    if not name:
        print("Name is required")
        return
    account_id = str(data["next_id"])
    data["next_id"] += 1
    data["accounts"][account_id] = {
        "name": name,
        "balance": 0.0,
        "history": [],
    }
    add_transaction(data["accounts"][account_id], "Account created")
    print(f"Account created with ID {account_id}")


def get_account(data, prompt):
    account_id = input(prompt).strip()
    account = data["accounts"].get(account_id)
    if not account:
        print("Account not found")
        return None, None
    return account_id, account


def deposit(data):
    account_id, account = get_account(data, "Account ID: ")
    if not account:
        return
    try:
        amount = float(input("Deposit amount: "))
    except ValueError:
        print("Invalid amount")
        return
    if amount <= 0:
        print("Amount must be positive")
        return
    account["balance"] += amount
    add_transaction(account, f"Deposit {amount:.2f}")
    print(f"New balance: {account['balance']:.2f}")


def withdraw(data):
    account_id, account = get_account(data, "Account ID: ")
    if not account:
        return
    try:
        amount = float(input("Withdraw amount: "))
    except ValueError:
        print("Invalid amount")
        return
    if amount <= 0:
        print("Amount must be positive")
        return
    if amount > account["balance"]:
        print("Insufficient balance")
        return
    account["balance"] -= amount
    add_transaction(account, f"Withdraw {amount:.2f}")
    print(f"New balance: {account['balance']:.2f}")


def transfer(data):
    from_id, from_acc = get_account(data, "From account ID: ")
    if not from_acc:
        return
    to_id, to_acc = get_account(data, "To account ID: ")
    if not to_acc:
        return
    if from_id == to_id:
        print("Cannot transfer to the same account")
        return
    try:
        amount = float(input("Transfer amount: "))
    except ValueError:
        print("Invalid amount")
        return
    if amount <= 0:
        print("Amount must be positive")
        return
    if amount > from_acc["balance"]:
        print("Insufficient balance")
        return

    from_acc["balance"] -= amount
    to_acc["balance"] += amount
    add_transaction(from_acc, f"Transfer out {amount:.2f} to {to_id}")
    add_transaction(to_acc, f"Transfer in {amount:.2f} from {from_id}")
    print("Transfer completed")


def show_accounts(data):
    accounts = data["accounts"]
    if not accounts:
        print("No accounts")
        return
    print("ID | Name | Balance")
    print("-" * 40)
    for account_id, account in sorted(accounts.items(), key=lambda x: int(x[0])):
        print(f"{account_id} | {account['name']} | {account['balance']:.2f}")


def statement(data):
    account_id, account = get_account(data, "Account ID: ")
    if not account:
        return
    print(f"Statement for {account['name']} ({account_id})")
    print(f"Current balance: {account['balance']:.2f}")
    print("History:")
    if not account["history"]:
        print("No transactions")
        return
    for entry in account["history"][-15:]:
        print(entry)


def menu():
    data = load_data()
    while True:
        print("\nBanking Console")
        print("1. Create account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Show accounts")
        print("6. Statement")
        print("7. Save")
        print("8. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            create_account(data)
        elif choice == "2":
            deposit(data)
        elif choice == "3":
            withdraw(data)
        elif choice == "4":
            transfer(data)
        elif choice == "5":
            show_accounts(data)
        elif choice == "6":
            statement(data)
        elif choice == "7":
            save_data(data)
            print("Saved")
        elif choice == "8":
            save_data(data)
            print("Saved and exiting")
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    menu()
