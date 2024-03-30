from AddressBook import *
from abc import ABC, abstractmethod

class UserInterface(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def show(self, text):
        pass

    @abstractmethod
    def get_input(self, prompt):
        pass

class ConsoleUI(UserInterface):

    def start(self):
        print("*** Address Book ***")

    def show(self, text):
        print(text)

    def get_input(self, prompt):
        return input(prompt)



class Bot:

    def __init__(self, ui: UserInterface):
        self.book = AddressBook()
        self.ui = ui

    def handle(self, action):
        if action == 'add':
            name = self.ui.get_input("Name: ").strip()
            phones = Phone().value
            birth = Birthday().value
            email = self.ui.get_input("Email: ").strip()
            status = Status().value.strip()
            note = self.ui.get_input("Note: ")
            record = Record(name, phones, birth, email, status, note)
            return self.book.add(record)
        elif action == 'search':
            self.ui.show("There are following categories: \nName \nPhones \nBirthday \nEmail \nStatus \nNote")
            category = self.ui.get_input('Search category: ')
            pattern = self.ui.get_input('Search pattern: ')
            result = (self.book.search(pattern, category))
            for account in result:
                if account['birthday']:
                    birth = account['birthday'].strftime("%d/%m/%Y")
                    result = "_" * 50 + "\n" + f"Name: {account['name']} \nPhones: {', '.join(account['phones'])} \nBirthday: {birth} \nEmail: {account['email']} \nStatus: {account['status']} \nNote: {account['note']}\n" + "_" * 50
                    self.ui.show(result)
        elif action == 'edit':
            contact_name = self.ui.get_input('Contact name: ')
            parameter = self.ui.get_input('Which parameter to edit(name, phones, birthday, status, email, note): ').strip()
            new_value = self.ui.get_input("New Value: ")
            return self.book.edit(contact_name, parameter, new_value)
        elif action == 'remove':
            pattern = self.ui.get_input("Remove (contact name or phone): ")
            return self.book.remove(pattern)
        elif action == 'save':
            file_name = self.ui.get_input("File name: ")
            return self.book.save(file_name)
        elif action == 'load':
            file_name = self.ui.get_input("File name: ")
            return self.book.load(file_name)
        elif action == 'congratulate':
            self.ui.show(self.book.congratulate())
        elif action == 'view':
            self.ui.show(self.book)
        elif action == 'exit':
            pass
        else:
            self.ui.show("There is no such command!")

