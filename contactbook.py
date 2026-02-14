import json

FILENAME = "contacts.json"

# Load contacts
def load_contacts():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save contacts
def save_contacts(contacts):
    with open(FILENAME, "w") as f:
        json.dump(contacts, f, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    if not name or not phone:
        print("⚠️ Name and phone are required!")
        return

    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("✅ Contact added!")

def view_contacts(contacts):
    sorted_contacts = sorted(contacts, key=lambda x: x['name'].lower())
    for c in contacts:
        print(f"{c['name']} - {c['phone']} - {c['email']}")

def search_contact(contacts):
    keyword = input("Search name: ").lower()
    found = [c for c in contacts if keyword in c['name'].lower()]
    for c in found:
        print(f"{c['name']} - {c['phone']} - {c['email']}")
    if not found:
        print("❌ No match found.")

def main():
    contacts = load_contacts()
    while True:
        print("\n1. Add\n2. View\n3. Search\n4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            break
        else:
            print("Invalid choice!")


def delete(contacts):
    name = input("Name to delete: ")
    if not any(c['name'].lower() == name.lower() for c in contacts):
        print("❌ Contact not found.")
        return
    else:
        to_delete = [c for c in contacts if c['name'].lower() == name.lower()]
        print("Are you sure you want to delete these contacts?")
        for c in to_delete:
            print(f"{c['name']} - {c['phone']} - {c['email']}")
        confirm = input("Type 'yes' to confirm: ")
        if confirm.lower() != 'yes':
            contacts = [c for c in contacts if c['name'].lower() != name.lower()]
        else:
            print("Deletion cancelled.")
            return
    save_contacts(contacts)
    print("✅ Contact deleted!")

def update_contact(contacts):
    name = input("Enter name to update: ").lower()
    for c in contacts:
        if c["name"].lower() == name:
            print(f"Found: {c['name']} - {c['phone']} - {c['email']}")
            c["phone"] = input("New phone: ") or c["phone"]
            c["email"] = input("New email: ") or c["email"]
            save_contacts(contacts)
            print("✅ Contact updated!")
            return
    print("❌ Contact not found.")

main()
