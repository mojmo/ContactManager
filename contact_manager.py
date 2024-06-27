import json
from utils import load_json, write_json

class ContactManager:
    def __init__(self, filepath):
        self.filepath = filepath
        self.contacts = load_json(filepath)

    def add_contact(self, name, phone, email):
        if name in self.contacts:
            print("Contact already exists.")
        else:
            self.contacts[name] = {"phone": phone, "email": email}
            write_json(self.filepath, self.contacts)
            print("Contact added successfully.")
