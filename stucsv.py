import csv

with open('students.csv', "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "grade"])
    writer.writerow(["Alice", "A"])
    writer.writerow(["Bob", "B"])

with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

with open("students.csv", "r") as f:
    reader = csv.reader(f)
    print(f'Total rows: {sum(1 for row in reader)}')