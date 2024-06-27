from contact_manager import ContactManager

def main():
    manager = ContactManager("contacts.json")
    
    while True:
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Update Contact")
        print("4. View Contacts")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            manager.add_contact(name, phone, email)
        elif choice == '2':
            name = input("Enter name to delete: ")
            manager.delete_contact(name)
        elif choice == '3':
            name = input("Enter name to update: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            manager.update_contact(name, phone, email)
        elif choice == '4':
            contacts = manager.view_contacts()
            for contact in contacts:
                print(contact)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
