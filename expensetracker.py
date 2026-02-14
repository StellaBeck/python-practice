import csv
from datetime import date
import json
import os

FILENAME = "expenses.csv"

def add_expense():
    category = input("Category: ")
    amount = float(input("Amount: "))
    with open(FILENAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date.today(), category, amount])
    print("✅ Expense added!")

def show_expenses():
    if not os.path.exists(FILENAME):
        print("No expenses recorded yet.")
        return
    total = 0
    with open(FILENAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            total += float(row[2])
    print(f"💰 Total = {total}")

def export_to_json():
    data = []
    with open(FILENAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            data.append({"date": row[0], "category": row[1], "amount": float(row[2])})
    with open("expenses.json", "w") as jf:
        json.dump(data, jf, indent=4)
    print("✅ Exported to expenses.json")

def main():
    while True:
        print("\n1. Add  2. Show  3. Export JSON  4. Exit")
        c = input("Choose: ")
        if c == "1": add_expense()
        elif c == "2": show_expenses()
        elif c == "3": export_to_json()
        elif c == "4": break
        else: print("❌ Invalid option")

def monthly_total(month):
    total = 0
    with open(FILENAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0].startswith(month):  # e.g. "2025-10"
                total += float(row[2])
    print(f"📅 Total for {month}: {total}")

def category_totals():
    totals = {}
    with open(FILENAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            cat = row[1]
            amt = float(row[2])
            totals[cat] = totals.get(cat, 0) + amt
    for c, t in totals.items():
        print(f"{c}: {t}")

def show_sorted_expenses():
    if not os.path.exists(FILENAME):
        print("⚠️ No expenses yet!")
        return
    with open(FILENAME, "r") as f:
        reader = csv.reader(f)
        expenses = list(reader)
    expenses.sort(key=lambda x: float(x[2]), reverse=True)
    for e in expenses:
        print(e)

def export_large(threshold):
    data = []
    with open(FILENAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if float(row[2]) > threshold:
                data.append({"date": row[0], "category": row[1], "amount": float(row[2])})
    with open("large_expenses.json", "w") as jf:
        json.dump(data, jf, indent=4)
    print("✅ Exported to large_expenses.json")

main()

