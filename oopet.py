import csv
from datetime import date
import json

class ExpenseTracker:
    def __init__(self, filename="expenses.csv"):
        self.filename = filename

    def add_expense(self, category, amount):
        with open(self.filename, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([date.today(), category, amount])
        print("✅ Expense added!")

    def load_expenses(self):
        expenses = []
        try:
            with open(self.filename, "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    expenses.append(Expense(row[0], row[1], float(row[2])))
        except FileNotFoundError:
            print("⚠️ No expenses yet.")
        return expenses

    def show_all(self):
        expenses = self.load_expenses()
        for e in expenses:
            print(e)

    def monthly_total(self, month):
        expenses = self.load_expenses()
        total = sum(e.amount for e in expenses if e.date.startswith(month))
        return total

    def summary_by_category(self):
        expenses = self.load_expenses()
        summary = {}
        for e in expenses:
            if e.category in summary:
                summary[e.category] += e.amount
            else:
                summary[e.category] = e.amount
        return summary
    
    def sort_by_amount(self):
        expenses = self.load_expenses()
        return sorted(expenses, key=lambda x: x.amount, reverse=True)
    
    def export_to_json(self, json_filename="expenses.json"):
        expenses = self.load_expenses()
        data = [{"date": e.date, "category": e.category, "amount": e.amount} for e in expenses]
        with open(json_filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"✅ Exported {len(data)}to {json_filename}!")
    
class Expense:
    def __init__(self, date, category, amount):
        self.date = date
        self.category = category
        self.amount = amount

    def __repr__(self):
        return f"{self.date} | {self.category} | {self.amount}"

def main():
    tracker = ExpenseTracker()

    while True:
        print("\n1. Add  2. Show  3. Exit")
        c = input("Choose: ")

        if c == "1":
            cat = input("Category: ")
            amt = float(input("Amount: "))
            tracker.add_expense(cat, amt)
        elif c == "2":
            tracker.show_all()
        elif c == "3":
            break
        else:
            print("❌ Invalid option")

main()
