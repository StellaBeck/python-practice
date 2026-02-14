import json
from datetime import datetime
from pathlib import Path

DATA_FILE = Path("expense_analyzer_data.json")


def load_data():
    if DATA_FILE.exists():
        try:
            return json.loads(DATA_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return []
    return []


def save_data(records):
    DATA_FILE.write_text(json.dumps(records, indent=2), encoding="utf-8")


def valid_date(text):
    try:
        datetime.strptime(text, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def add_expense(records):
    date = input("Date (YYYY-MM-DD): ").strip()
    if not valid_date(date):
        print("Invalid date format")
        return
    category = input("Category: ").strip().lower()
    note = input("Note: ").strip()
    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Invalid amount")
        return
    if amount <= 0:
        print("Amount must be greater than 0")
        return
    records.append({"date": date, "category": category, "amount": amount, "note": note})
    print("Expense added")


def list_expenses(records):
    if not records:
        print("No expenses")
        return
    print("Date | Category | Amount | Note")
    print("-" * 70)
    for item in sorted(records, key=lambda x: x["date"]):
        print(f"{item['date']} | {item['category']} | {item['amount']:.2f} | {item['note']}")


def totals_by_category(records):
    if not records:
        print("No expenses")
        return
    totals = {}
    for item in records:
        totals[item["category"]] = totals.get(item["category"], 0.0) + item["amount"]
    print("Category totals")
    print("-" * 24)
    for category, total in sorted(totals.items(), key=lambda x: x[1], reverse=True):
        print(f"{category}: {total:.2f}")


def monthly_summary(records):
    if not records:
        print("No expenses")
        return
    monthly = {}
    for item in records:
        month = item["date"][:7]
        monthly[month] = monthly.get(month, 0.0) + item["amount"]
    print("Monthly totals")
    print("-" * 24)
    for month in sorted(monthly):
        print(f"{month}: {monthly[month]:.2f}")


def highest_expense(records):
    if not records:
        print("No expenses")
        return
    top = max(records, key=lambda x: x["amount"])
    print("Highest expense")
    print(f"Date: {top['date']}")
    print(f"Category: {top['category']}")
    print(f"Amount: {top['amount']:.2f}")
    print(f"Note: {top['note']}")


def menu():
    records = load_data()
    while True:
        print("\nExpense Analyzer")
        print("1. Add expense")
        print("2. List expenses")
        print("3. Totals by category")
        print("4. Monthly summary")
        print("5. Highest expense")
        print("6. Save")
        print("7. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            add_expense(records)
        elif choice == "2":
            list_expenses(records)
        elif choice == "3":
            totals_by_category(records)
        elif choice == "4":
            monthly_summary(records)
        elif choice == "5":
            highest_expense(records)
        elif choice == "6":
            save_data(records)
            print("Saved")
        elif choice == "7":
            save_data(records)
            print("Saved and exiting")
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    menu()
