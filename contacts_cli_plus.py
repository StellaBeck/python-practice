import json
from pathlib import Path

DATA_FILE = Path("contacts_cli_plus_data.json")


def load_data():
    if DATA_FILE.exists():
        try:
            return json.loads(DATA_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {}
    return {}


def save_data(contacts):
    DATA_FILE.write_text(json.dumps(contacts, indent=2), encoding="utf-8")


def add_contact(contacts):
    name = input("Name: ").strip()
    if not name:
        print("Name cannot be empty")
        return
    if name in contacts:
        print("Contact exists")
        return
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    city = input("City: ").strip()
    contacts[name] = {"phone": phone, "email": email, "city": city}
    print("Contact added")


def update_contact(contacts):
    name = input("Name to update: ").strip()
    if name not in contacts:
        print("Contact not found")
        return
    phone = input(f"Phone [{contacts[name]['phone']}]: ").strip()
    email = input(f"Email [{contacts[name]['email']}]: ").strip()
    city = input(f"City [{contacts[name]['city']}]: ").strip()
    if phone:
        contacts[name]["phone"] = phone
    if email:
        contacts[name]["email"] = email
    if city:
        contacts[name]["city"] = city
    print("Contact updated")


def search_contacts(contacts):
    term = input("Search by name/city: ").strip().lower()
    if not term:
        print("Search term is empty")
        return
    hits = []
    for name, info in contacts.items():
        if term in name.lower() or term in info["city"].lower():
            hits.append((name, info))
    if not hits:
        print("No matches")
        return
    for name, info in sorted(hits):
        print(f"{name} | {info['phone']} | {info['email']} | {info['city']}")


def delete_contact(contacts):
    name = input("Name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("Contact deleted")
    else:
        print("Contact not found")


def list_contacts(contacts):
    if not contacts:
        print("No contacts")
        return
    print("Name | Phone | Email | City")
    print("-" * 72)
    for name in sorted(contacts):
        info = contacts[name]
        print(f"{name} | {info['phone']} | {info['email']} | {info['city']}")


def menu():
    contacts = load_data()
    while True:
        print("\nContacts CLI Plus")
        print("1. Add contact")
        print("2. Update contact")
        print("3. Search contacts")
        print("4. Delete contact")
        print("5. List contacts")
        print("6. Save")
        print("7. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            update_contact(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            list_contacts(contacts)
        elif choice == "6":
            save_data(contacts)
            print("Saved")
        elif choice == "7":
            save_data(contacts)
            print("Saved and exiting")
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    menu()
