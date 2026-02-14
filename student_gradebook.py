import json
from pathlib import Path

DATA_FILE = Path("gradebook_data.json")


def load_data():
    if DATA_FILE.exists():
        try:
            return json.loads(DATA_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {}
    return {}


def save_data(data):
    DATA_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")


def add_student(data):
    name = input("Student name: ").strip()
    if not name:
        print("Name cannot be empty")
        return
    if name in data:
        print("Student already exists")
        return
    data[name] = []
    print("Student added")


def add_score(data):
    name = input("Student name: ").strip()
    if name not in data:
        print("Student not found")
        return
    try:
        score = float(input("Score (0-100): "))
    except ValueError:
        print("Invalid score")
        return
    if score < 0 or score > 100:
        print("Score must be between 0 and 100")
        return
    data[name].append(score)
    print("Score added")


def calc_average(scores):
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def letter_grade(avg):
    if avg >= 90:
        return "A"
    if avg >= 80:
        return "B"
    if avg >= 70:
        return "C"
    if avg >= 60:
        return "D"
    return "F"


def student_report(data):
    name = input("Student name: ").strip()
    if name not in data:
        print("Student not found")
        return
    scores = data[name]
    avg = calc_average(scores)
    print(f"Scores: {scores}")
    print(f"Average: {avg:.2f}")
    print(f"Grade: {letter_grade(avg)}")


def class_report(data):
    if not data:
        print("No students found")
        return
    class_scores = []
    print("Name | Tests | Average | Grade")
    print("-" * 36)
    for name in sorted(data):
        scores = data[name]
        avg = calc_average(scores)
        class_scores.extend(scores)
        print(f"{name} | {len(scores)} | {avg:.2f} | {letter_grade(avg)}")
    class_avg = calc_average(class_scores)
    print("-" * 36)
    print(f"Class average: {class_avg:.2f}")


def remove_student(data):
    name = input("Student name: ").strip()
    if name in data:
        del data[name]
        print("Student removed")
    else:
        print("Student not found")


def menu():
    data = load_data()
    while True:
        print("\nGradebook Menu")
        print("1. Add student")
        print("2. Add score")
        print("3. Student report")
        print("4. Class report")
        print("5. Remove student")
        print("6. Save")
        print("7. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            add_student(data)
        elif choice == "2":
            add_score(data)
        elif choice == "3":
            student_report(data)
        elif choice == "4":
            class_report(data)
        elif choice == "5":
            remove_student(data)
        elif choice == "6":
            save_data(data)
            print("Saved")
        elif choice == "7":
            save_data(data)
            print("Saved and exiting")
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    menu()
