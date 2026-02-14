import json
from pathlib import Path

DATA_FILE = Path("library_system_data.json")


def load_data():
    if DATA_FILE.exists():
        try:
            return json.loads(DATA_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass
    return {"books": {}, "members": {}, "next_book_id": 1}


def save_data(data):
    DATA_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")


def add_book(data):
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    try:
        copies = int(input("Number of copies: "))
    except ValueError:
        print("Invalid number")
        return
    if copies <= 0:
        print("Copies must be at least 1")
        return

    book_id = str(data["next_book_id"])
    data["next_book_id"] += 1
    data["books"][book_id] = {
        "title": title,
        "author": author,
        "copies": copies,
        "available": copies,
        "borrowed_by": [],
    }
    print(f"Book added with ID {book_id}")


def register_member(data):
    member_id = input("Member ID: ").strip()
    name = input("Member name: ").strip()
    if not member_id or not name:
        print("Member ID and name are required")
        return
    if member_id in data["members"]:
        print("Member already exists")
        return
    data["members"][member_id] = {"name": name, "borrowed": []}
    print("Member registered")


def list_books(data):
    books = data["books"]
    if not books:
        print("No books in library")
        return
    print("ID | Title | Author | Available/Total")
    print("-" * 70)
    for book_id, book in sorted(books.items(), key=lambda x: int(x[0])):
        print(f"{book_id} | {book['title']} | {book['author']} | {book['available']}/{book['copies']}")


def borrow_book(data):
    member_id = input("Member ID: ").strip()
    book_id = input("Book ID: ").strip()

    if member_id not in data["members"]:
        print("Member not found")
        return
    if book_id not in data["books"]:
        print("Book not found")
        return

    member = data["members"][member_id]
    book = data["books"][book_id]

    if book["available"] <= 0:
        print("No copies available")
        return
    if book_id in member["borrowed"]:
        print("Member already borrowed this book")
        return

    member["borrowed"].append(book_id)
    book["borrowed_by"].append(member_id)
    book["available"] -= 1
    print("Book borrowed")


def return_book(data):
    member_id = input("Member ID: ").strip()
    book_id = input("Book ID: ").strip()

    if member_id not in data["members"] or book_id not in data["books"]:
        print("Member or book not found")
        return

    member = data["members"][member_id]
    book = data["books"][book_id]

    if book_id not in member["borrowed"]:
        print("This member does not have that book")
        return

    member["borrowed"].remove(book_id)
    if member_id in book["borrowed_by"]:
        book["borrowed_by"].remove(member_id)
    book["available"] += 1
    print("Book returned")


def member_report(data):
    member_id = input("Member ID: ").strip()
    if member_id not in data["members"]:
        print("Member not found")
        return

    member = data["members"][member_id]
    print(f"Member: {member['name']} ({member_id})")
    if not member["borrowed"]:
        print("No borrowed books")
        return

    print("Borrowed books:")
    for book_id in member["borrowed"]:
        book = data["books"].get(book_id)
        if book:
            print(f"{book_id}: {book['title']} by {book['author']}")


def menu():
    data = load_data()
    while True:
        print("\nLibrary System")
        print("1. Add book")
        print("2. Register member")
        print("3. List books")
        print("4. Borrow book")
        print("5. Return book")
        print("6. Member report")
        print("7. Save")
        print("8. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            add_book(data)
        elif choice == "2":
            register_member(data)
        elif choice == "3":
            list_books(data)
        elif choice == "4":
            borrow_book(data)
        elif choice == "5":
            return_book(data)
        elif choice == "6":
            member_report(data)
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
