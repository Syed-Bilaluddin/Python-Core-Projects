import json

contacts = {}
try:
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
except FileNotFoundError:
    pass
while True:
    print("===== CONTACT MANAGER =====")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice. Please enter a number b/w 1-6.")
        continue

    match choice:
        case 1: 
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter e-mail: ")
            contact_id = str(len(contacts) + 1)

            contact = {
                "name":name,
                "phone no": phone,
                "email": email,
            }
            contacts[contact_id] = contact
            print("Contact added successfully")
            print(contact)
            with open("contacts.json", "w") as file:
                json.dump(contacts, file, indent=4)

        case 2:
            for contact_id, contact in contacts.items():
                print(f"ID: {contact_id}")
                print(f"Name: {contact["name"]}")
                print(f"Phone No: {contact["phone no"]}")
                print(f"Email: {contact["email"]}")
        case 3:
            search = input("Enter your search keyword: ")
            for contact_id, contact in contacts.items():
                if search.lower() in contact["name"].lower():
                    print(f"ID: {contact_id}")
                    print(f"Name: {contact["name"]}")
                    print(f"Phone No: {contact["phone no"]}")
                    print(f"Email: {contact["email"]}")
        case 4:
            updateID = input("Enter contact ID you want to update: ")
            if updateID in contacts:
                print("Contact found.")
                print(f"Name: {contacts[updateID]["name"]}")
                print(f"Phone No: {contacts[updateID]["phone no"]}")
                print(f"Email: {contacts[updateID]["email"]}")

                try:
                    update_choice = int(input("What you want to update?\n" \
                    "1. Name\n" \
                    "2. Phone No\n" \
                    "3. Email\n" \
                    "Choose: "))
                except ValueError:
                    print("Invalid choice. Please enter a number b/w 1-3.")
                    continue
                match update_choice:
                    case 1:
                        new_name = input("Enter new name: ")
                        contacts[updateID]["name"] = new_name
                        print(f"Updated Name: {new_name}")
                        print("Contact name updated successfully.")
                        with open("contacts.json", "w") as file:
                            json.dump(contacts, file, indent=4)
                    case 2:
                        new_phone = input("Enter new phone no: ")
                        contacts[updateID]["phone no"] = new_phone
                        print(f"Updated Phone Number: {new_phone}")
                        print("Phone number updated successfully.")
                        with open("contacts.json", "w") as file:
                            json.dump(contacts, file, indent=4)
                    case 3:
                        new_email = input("Enter new email: ")
                        contacts[updateID]["email"] = new_email
                        print(f"Updated Email: {new_email}")
                        print("Email updated successfully.")
                        with open("contacts.json", "w") as file:
                            json.dump(contacts, file, indent=4)
            else:
                print("Contact not found.")
        case 5:
            deleteID = input("Enter contact ID you want to delete: ")
            if deleteID in contacts:
                del contacts[deleteID]
                print("Contact deleted successfully.")
                with open("contacts.json", "w") as file:
                    json.dump(contacts, file, indent=4)
        case 6:
            break
