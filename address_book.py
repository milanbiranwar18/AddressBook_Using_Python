import csv
import json
import logging

logging.basicConfig(filename="address_book.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


class Contact:
    """
    Class for constructor
    """

    def __init__(self, address_book_parameters_dict):
        self.first_name = address_book_parameters_dict.get("first_name")
        self.last_name = address_book_parameters_dict.get("last_name")
        self.address = address_book_parameters_dict.get("address")
        self.city = address_book_parameters_dict.get("city")
        self.state = address_book_parameters_dict.get("state")
        self.zip_code = address_book_parameters_dict.get("zip_code")
        self.mob_number = address_book_parameters_dict.get("mob_number")
        self.email = address_book_parameters_dict.get("email")

    def get_address_book_jsons_dict(self):
        try:
            return "{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(self.first_name, self.last_name,
                                                                                    self.address,
                                                                                    self.city, self.state,
                                                                                    self.zip_code, self.mob_number,
                                                                                    self.email)
        except Exception as e:
            logging.error(e)

    def get_address_book_dict(self):
        try:
            return {"First Name": self.first_name, "Last Name": self.last_name, "Address": self.address,
                    "City": self.city, "State": self.state, "Zip Code": self.zip_code, "Mobile Number": self.mob_number,
                    "Email": self.email}
        except Exception as e:
            logging.error(e)


class AddressBook:

    def __init__(self, address_book):
        self.address_book = address_book
        self.address_book_dict = {}

    def add_person(self, person):
        """
        Function for adding the person to the address book
        :param person: using person parameter as a string
        :return: will add person and person details in dictionary
        """
        try:
            self.address_book_dict.update({person.first_name: person})
        except Exception as e:
            logging.error(e)

    def get_person(self, first_name):
        """
        Function for get the person from dictionary
        :param first_name: using first_name parameter as a string
        :return: return details of person from dictionary
        """
        try:
            return self.address_book_dict.get(first_name)
        except Exception as e:
            logging.error(e)

    def update_person(self, person_data, person_dict):
        """
        Method to update the address book information
        :param person_data: using object for old information
        :param person_dict: using object for new information
        :return: will return updated address book information
        """
        try:
            person_data.address = person_dict.get("update_address")
            person_data.city = person_dict.get("update_city")
            person_data.state = person_dict.get("update_state")
            person_data.zip_code = person_dict.get("update_pin")
            person_data.mob_number = person_dict.get("update_phone")
            person_data.email = person_dict.get("update_email")
        except Exception as e:
            logging.error(e)

    def delete_person(self, person_name):
        """
        Function for deleting the person from address book dictionary
        :param person_name: using as a object to delete the person
        :return: will delete the person from address book dictionary
        """
        try:
            self.address_book_dict.pop(person_name, "Person name not exist")
        except Exception as e:
            logging.error(e)

    def display_names(self):
        """
        Function for person name
        :return: will return person name
        """
        try:
            if self.address_book_dict == {}:
                print("There is no person to display")
            else:
                for key, value in self.address_book_dict.items():
                    print(key)

        except Exception as e:
            logging.error(e)

    def display_contacts(self):
        """
        Function to address book
        :return: return address book
        """
        try:
            print("First Name \t\tLast Name \t\t\tAddress \t\tCity \tState \tZip Code \tMobile Number\t Email")
            for key, value in self.address_book_dict.items():
                print("\t{}\t\t\t{}\t\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}".format(value.first_name,
                                                                                              value.last_name,
                                                                                              value.address, value.city,
                                                                                              value.state,
                                                                                              value.zip_code,
                                                                                              value.mob_number,
                                                                                              value.email))
        except Exception as e:
            logging.error(e)

    def get_address_book_json_dict(self):
        """
        Function for getting data in json
        :return: return data in json
        """
        try:
            json_address_book_dict = {}
            for key, value in self.address_book_dict.items():
                json_address_book_dict.update({value.first_name: value.get_address_book_jsons_dict()})
            return json_address_book_dict
        except Exception as e:
            logging.error(e)

    def get_address_book_dict(self):
        """
        Function for getting data in csv
        :return: return data in csv
        """
        try:
            address_details_dict = {}
            for key, value in self.address_book_dict.items():
                address_details_dict.update({value.first_name: value.get_address_book_dict()})
            return address_details_dict
        except Exception as e:
            logging.error(e)


class MultipleAddressBook:
    def __init__(self):
        self.multi_address_book_dict = {}
        self.json_dict = {}
        self.csv_dit = {}

    def add_address_book(self, address_book_object):
        """
        Function to add address_book_object to address_book_dict dictionary
        """
        try:
            self.multi_address_book_dict.update({address_book_object.address_book: address_book_object})
        except Exception as e:
            logging.error(e)

    def get_address_book_object(self, address_book):
        """
        Function to get address_book_object
        """
        try:
            return self.multi_address_book_dict.get(address_book)
        except Exception as e:
            logging.error(e)

    def display_address_book_names(self):
        """
        Function to show address book names
        """
        try:
            for key, value in self.multi_address_book_dict.items():
                print(key)
        except Exception as e:
            logging.error(e)

    def delete_address_book(self, address_book):
        """
        Function to delete address_book
        """
        try:
            self.multi_address_book_dict.pop(address_book, "Address Book not present")
        except Exception as e:
            logging.error(e)

    def write_to_json_file(self):
        """
            Function to write Details to Json File
        """
        try:
            dict_json = {}
            for address_book, address_book_object in self.multi_address_book_dict.items():
                address_book_dictionary = address_book_object.get_address_book_json_dict()

                dict_json.update({address_book: address_book_dictionary})

                json_obj = json.dumps(dict_json, indent=4)
                with open("address_book.json", "w") as write_file:
                    write_file.write(json_obj)
        except Exception as e:
            logging.exception(e)

    def write_to_csv_file(self):
        """
        Function to write Details to csv File
        :return:
        """
        try:
            with open("address_book.csv", "w", newline='') as write_file:
                fieldnames = ['First Name', 'Last Name', 'Address', 'City', 'State', 'Zip Code', 'Mobile Number',
                              'Email']
                csv_writer = csv.DictWriter(write_file, fieldnames=fieldnames)
                csv_writer.writeheader()

                for address_book, address_book_object in self.multi_address_book_dict.items():
                    address_book_diction = address_book_object.get_address_book_dict()
                    for key, value in address_book_diction.items():
                        csv_writer.writerow(value)
        except Exception as e:
            logging.error(e)


def add_contact():
    """
    Function to add a contact
    """
    try:
        address_book_name = input("Enter Address Book name : ")
        address_book_object = multi_address_book.get_address_book_object(address_book_name)
        if not address_book_object:
            address_book_object = AddressBook(address_book_name)
            multi_address_book.add_address_book(address_book_object)
        first_name = input("Enter first name : ")
        if first_name == "":
            print("Please enter first name")
            return
        last_name = input("Enter last name : ")
        if last_name == "":
            print("Please enter last name")
            return
        address = input("Enter address : ")
        city = input("Enter city : ")
        state = input("Enter state : ")
        zip_code = int(input("Enter zip code : "))
        mob_number = int(input("Enter phone number : "))
        email = input("Enter email id : ")

        contact_parameters = {"first_name": first_name, "last_name": last_name, "address": address, "city": city,
                              "state": state, "zip_code": zip_code, "mob_number": mob_number, "email": email}
        contact = Contact(contact_parameters)

        address_book_object.add_person(contact)

        multi_address_book.write_to_json_file()
        multi_address_book.write_to_csv_file()

    except Exception as e:
        logging.exception(e)


def update_contact():
    """
    Function to update contact
    """
    try:
        address_book_name = input("Enter Address Book name : ")
        address_book_object = multi_address_book.get_address_book_object(address_book_name)
        name = input("Enter contact name to update : ")
        contact_object = address_book_object.get_person(name)
        if not contact_object:
            print("Contact not present")
        else:
            update_address = input("Enter new address to update : ")
            update_city = input("Enter new city to update : ")
            update_state = input("Enter new state to update : ")
            update_zip_code = int(input("Enter new zip code to update : "))
            update_phone = int(input("Enter new mobile number to update : "))
            update_email = input("Enter new email id to update : ")

            update_dict = {"update_address": update_address, "update_city": update_city, "update_state": update_state,
                           "update_pin": update_zip_code, "update_phone": update_phone,
                           "update_email": update_email}

            address_book_object.update_person(contact_object, update_dict)

        multi_address_book.write_to_json_file()
        multi_address_book.write_to_csv_file()

    except Exception as e:
        logging.exception(e)


def delete_contact():
    """
    Function to remove a contact
    """
    try:
        address_book_name = input("Enter Address Book name : ")
        address_book_object = multi_address_book.get_address_book_object(address_book_name)
        name = input("Enter first name to delete contact : ")
        address_book_object.delete_person(name)

        multi_address_book.write_to_json_file()
        multi_address_book.write_to_csv_file()

    except Exception as e:
        logging.error(e)


def display_names():
    """
    Function to display contacts
    """
    try:
        address_book_name = input("Enter Address Book name : ")
        address_book_object = multi_address_book.get_address_book_object(address_book_name)
        address_book_object.display_names()

        multi_address_book.write_to_json_file()
        multi_address_book.write_to_csv_file()

    except Exception as e:
        logging.error(e)


def display_contacts():
    """
    Function to display all contacts in address book
    """
    try:
        address_book_name = input("Enter Address Book name : ")
        address_book_object = multi_address_book.get_address_book_object(address_book_name)
        address_book_object.display_contacts()

        multi_address_book.write_to_json_file()
        multi_address_book.write_to_csv_file()
    except Exception as e:
        logging.error(e)


def display_address_book_names():
    """
    Function to display address book names
    """
    try:
        multi_address_book.display_address_book_names()

        multi_address_book.write_to_json_file()
        multi_address_book.write_to_csv_file()
    except Exception as e:
        logging.error(e)


def delete_address_book():
    """
    Function to delete address book
    """
    try:
        address_book_name = input("Enter Address Book name : ")
        multi_address_book.delete_address_book(address_book_name)

        multi_address_book.write_to_json_file()
        multi_address_book.write_to_csv_file()
    except Exception as e:
        logging.error(e)


def read_from_json_file():
    """
    Function for json file to read data
    """
    with open("address_book.json", "r") as read_file:
        json_object = json.load(read_file)
        print(json_object)


def write_to_json_file():
    """
    Function for json file to write data
    """
    multi_address_book.write_to_json_file()


def write_to_csv_file():
    """
    Function to write contact information to a json file
    """
    multi_address_book.write_to_csv_file()


def read_from_csv_file():
    with open("address_book.csv", "r") as read_file:
        csv_reader = csv.DictReader(read_file)
        for i in csv_reader:
            print(i)


if __name__ == '__main__':
    multi_address_book = MultipleAddressBook()

    while True:
        choice = int(input("Enter 1 to add person\n"
                           "Enter 2 to Update person\n"
                           "Enter 3 to Delete person\n"
                           "Enter 4 to see all person in address book\n"
                           "Enter 5 to check person details \n"
                           "Enter 6 to Display address book names\n"
                           "Enter 7 to Delete an Address Book\n"
                           "Enter 8 to write data to json file\n"
                           "Enter 9 to read data from json file\n"
                           "Enter 10 to write data to csv file\n"
                           "Enter 11 to read data from csv file\n"
                           "0. Enter 0 to Exit\n"
                           "Enter any number : "))

        options = {1: add_contact,
                   2: update_contact,
                   3: delete_contact,
                   4: display_names,
                   5: display_contacts,
                   6: display_address_book_names,
                   7: delete_address_book,
                   8: write_to_json_file,
                   9: read_from_json_file,
                   10: write_to_csv_file,
                   11: read_from_csv_file
                   }
        if choice == 0:
            break
        else:
            options.get(choice)()
