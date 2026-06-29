import json
import os

FILE_NAME = "contacts.json"

# -------------------------------
# File Handling
# -------------------------------

def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

# -------------------------------
# Display Functions
# -------------------------------

def show_contacts(contacts):
    print("\n------ CONTACT LIST ------")
    if not contacts:
        print("No contacts found.\n")
        return

    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
    print()

def show_full_contact(contact):
    print("\n--- Contact Details ---")
    print(f"Name   : {contact['name']}")
    print(f"Phone  : {contact['phone']}")
    print(f"Email  : {contact['email']}")
    print(f"Address: {contact['address']}")
    print()

# -------------------------------
# Core Features
# -------------------------------

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    save_contacts(contacts)
    print("Contact added successfully!\n")

def search_contact(contacts):
    key = input("Enter name or phone to search: ").lower()
    found = False

    for contact in contacts:
        if key in contact["name"].lower() or key in contact["phone"]:
            show_full_contact(contact)
            found = True

    if not found:
        print("No matching contact found.\n")

def update_contact(contacts):
    show_contacts(contacts)
    try:
        num = int(input("Enter contact number to update: "))
        if 1 <= num <= len(contacts):
            contact = contacts[num - 1]

            print("Leave blank to keep old value.")
            name = input(f"New name ({contact['name']}): ") or contact['name']
            phone = input(f"New phone ({contact['phone']}): ") or contact['phone']
            email = input(f"New email ({contact['email']}): ") or contact['email']
            address = input(f"New address ({contact['address']}): ") or contact['address']

            contacts[num - 1] = {
                "name": name,
                "phone": phone,
                "email": email,
                "address": address
            }

            save_contacts(contacts)
            print("Contact updated successfully!\n")
        else:
            print("Invalid number!\n")
    except:
        print("Invalid input!\n")

def delete_contact(contacts):
    show_contacts(contacts)
    try:
        num = int(input("Enter contact number to delete: "))
        if 1 <= num <= len(contacts):
            removed = contacts.pop(num - 1)
            save_contacts(contacts)
            print(f"Deleted contact: {removed['name']}\n")
        else:
            print("Invalid number!\n")
    except:
        print("Invalid input!\n")

# -------------------------------
# Main Program
# -------------------------------

def main():
    contacts = load_contacts()

    while True:
        print("===== CONTACT BOOK MENU =====")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        print("=============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Exiting Contact Book...")
            break
        else:
            print("Invalid choice! Try again.\n")

# Run program
if __name__ == "__main__":
    main()
