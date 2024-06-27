# ContactManager

## Purpose of the Project
The **ContactManager** is a simple yet effective Python mini-project designed to manage contact information. The primary goal is to provide users with a straightforward interface to add, delete, update, and view contacts, storing the data in a JSON file. This project serves as an excellent introduction to file handling, JSON operations, and basic CRUD (Create, Read, Update, Delete) functionalities in Python.

## Key Features
- **Add Contact**: Easily add a new contact by providing a name, phone number, and email address.
- **Delete Contact**: Remove an existing contact by specifying the name.
- **Update Contact**: Modify the details of an existing contact.
- **View Contacts**: Display all stored contacts with their details.

## Project Structure
The project is organized into three main files:

1. main.py: Handles user interaction and input, directing commands to the ContactManager class.
2. contact_manager.py: Contains the ContactManager class which manages the contact data.
3. utils.py: Provides utility functions for loading and writing JSON data.

## Usage
### Prerequisites
- Python 3.x

### Installation

1. Clone the repository:

```bash
git clone [<repository link>](https://github.com/mojmo/ContactManager.git)
```

2. Navigate to the project directory:

```bash
cd ContactManager
```

### Running the Project
Execute the main.py file to start the ContactManager:
```bash
python main.py
```

### Sample Interaction
```
1. Add Contact
2. Delete Contact
3. Update Contact
4. View Contacts
5. Exit
Choose an option: 1
Enter name: Mohamed Ahmed
Enter phone number: 0912345678
Enter email: mohamed.ahmed@example.com
Contact added successfully.
```

### JSON File
The contacts are stored in a file named contacts.json in the project directory. This file is created automatically if it doesn't exist.

## Contributors
[**Mugtaba Mohamed Abdalla Ibrahim**](https://github.com/mojmo/)  
[**Subaib Abdulhafeez Altyeb Ahmed**](https://github.com/suhaib8310/)
