import json
from datetime import datetime
from pathlib import Path

DATA_FILE = Path("task_planner_data.json")


def load_data():
    if DATA_FILE.exists():
        try:
            return json.loads(DATA_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass
    return {"tasks": [], "next_id": 1}


def save_data(data):
    DATA_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")


def valid_due_date(value):
    if not value:
        return True
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def add_task(data):
    title = input("Task title: ").strip()
    if not title:
        print("Title is required")
        return
    priority = input("Priority (low/medium/high): ").strip().lower()
    if priority not in {"low", "medium", "high"}:
        priority = "medium"
    due = input("Due date (YYYY-MM-DD or empty): ").strip()
    if not valid_due_date(due):
        print("Invalid due date")
        return
    tags = [tag.strip().lower() for tag in input("Tags separated by commas: ").split(",") if tag.strip()]

    task = {
        "id": data["next_id"],
        "title": title,
        "priority": priority,
        "due": due,
        "status": "todo",
        "tags": tags,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    data["tasks"].append(task)
    data["next_id"] += 1
    print(f"Task added with ID {task['id']}")


def list_tasks(data):
    tasks = data["tasks"]
    if not tasks:
        print("No tasks")
        return

    status_filter = input("Filter by status (todo/doing/done or empty): ").strip().lower()
    filtered = tasks
    if status_filter in {"todo", "doing", "done"}:
        filtered = [t for t in tasks if t["status"] == status_filter]

    priority_order = {"high": 0, "medium": 1, "low": 2}
    filtered = sorted(filtered, key=lambda t: (priority_order.get(t["priority"], 1), t["due"] or "9999-99-99"))

    print("ID | Title | Priority | Due | Status | Tags")
    print("-" * 90)
    for task in filtered:
        tags = ",".join(task["tags"]) if task["tags"] else "-"
        due = task["due"] if task["due"] else "-"
        print(f"{task['id']} | {task['title']} | {task['priority']} | {due} | {task['status']} | {tags}")


def find_task(data, task_id):
    for task in data["tasks"]:
        if task["id"] == task_id:
            return task
    return None


def update_status(data):
    try:
        task_id = int(input("Task ID: "))
    except ValueError:
        print("Invalid ID")
        return
    task = find_task(data, task_id)
    if not task:
        print("Task not found")
        return
    new_status = input("New status (todo/doing/done): ").strip().lower()
    if new_status not in {"todo", "doing", "done"}:
        print("Invalid status")
        return
    task["status"] = new_status
    print("Status updated")


def delete_task(data):
    try:
        task_id = int(input("Task ID to delete: "))
    except ValueError:
        print("Invalid ID")
        return
    before = len(data["tasks"])
    data["tasks"] = [t for t in data["tasks"] if t["id"] != task_id]
    if len(data["tasks"]) < before:
        print("Task deleted")
    else:
        print("Task not found")


def summary(data):
    tasks = data["tasks"]
    total = len(tasks)
    todo = sum(1 for t in tasks if t["status"] == "todo")
    doing = sum(1 for t in tasks if t["status"] == "doing")
    done = sum(1 for t in tasks if t["status"] == "done")
    print(f"Total: {total}")
    print(f"Todo: {todo}")
    print(f"Doing: {doing}")
    print(f"Done: {done}")


def menu():
    data = load_data()
    while True:
        print("\nTask Planner")
        print("1. Add task")
        print("2. List tasks")
        print("3. Update status")
        print("4. Delete task")
        print("5. Summary")
        print("6. Save")
        print("7. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            add_task(data)
        elif choice == "2":
            list_tasks(data)
        elif choice == "3":
            update_status(data)
        elif choice == "4":
            delete_task(data)
        elif choice == "5":
            summary(data)
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
