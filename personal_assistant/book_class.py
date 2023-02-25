import pickle
import sys
from collections import UserDict


class Field:
    """
    `Field` class, which is the parent for all fields,
    and is responsible for the logic common to all fields.
    """

    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Name(Field):
    """
    `Name` class, a mandatory field with a contact name.
    """


class Address(Field):
    """
    `Address` class, an optional field with a contact address info.
    """
    pass


class Phone(Field):
    """
    `Phone` class, an optional field with a contact phone numbers.
    """

    @Field.value.setter
    def value(self, new_value):
        self._value = new_value


class Email(Field):
    """
    `Email` class, an optional field with a contact email address.
    """

    @Field.value.setter
    def value(self, new_value):
        self._value = new_value


class Birthday(Field):
    """
    `Birthday` class, an optional field with a contact birthday info.
    """

    @Field.value.setter
    def value(self, value):
        self._value = value

    def __str__(self) -> str:
        return self._value.strftime("%d.%m.%Y")


class Record:
    """
    `Record` class, which is responsible for the logic of
    adding/deleting/editing optional fields and storing the required fields.
    """

    def __init__(self, name, address: object = None, phones: object = None, email: object = None,
                 birthday: object = None):
        self.name = Name(name)
        self.address = address if address else None
        self.phones = phones if phones else []
        self.email = email if email else None
        self.birthday = birthday if birthday else None

    def add_phone(self, phone):
        """
        Add phone to contact
        :param: phone
        """
        self.phones.append(Phone(phone))

    def get_phones(self):
        """
        Contact phones list
        """
        return [phone.value for phone in self.phones]

    def add_email(self, email):
        """
        Add email to contact
        :param email: email address
        """
        self.email = Email(email)

    def add_address(self, address):
        """
        Add address to contact
        :param address: contact address
        """
        self.address = Address(address)

    def add_birthday(self, birthday):
        """
        Add birthday to contact
        :param birthday: date
        """
        self.birthday = Birthday(birthday)

    def change_phone(self, phone, new_phone):
        """
        Change phone for contact
        :param phone: old phone number
        :param new_phone: new phone number
        """
        for item in self.phones:
            if item.value == phone:
                item.value = new_phone

    def change_email(self, new_email):
        """
        Change email for contact
        :param new_email: new email address
        """
        self.email = Email(new_email)

    def change_address(self, new_address):
        """
        Change address for contact
        :param new_address: new address
        """
        self.address = Address(new_address)

    def change_birthday(self, new_birthday):
        """
        Change birthday for contact
        :param new_birthday: new date
        """
        self.birthday = Birthday(new_birthday)

    def delete_phone(self, phone):
        """
        Delete phone for contact
        :param phone: phone to delete
        """
        for item in self.phones:
            if item.value == phone:
                self.phones.remove(item)

    def delete_email(self):
        """
        Delete email for contact
        """
        self.email = Email(None)

    def delete_address(self):
        """
        Delete address for contact
        """
        self.address = Address(None)

    def delete_birthday(self):
        """
        Delete birthday for contact
        """
        self.birthday = Birthday(None)

    def get_user_details(self):
        """
        The method converts phones and date to a list.

        Parameters
        ---------
        :param:
        :return: list res_list
        """

        show_phone = ''
        show_birthday = ''
        show_address = ''
        show_email = ''

        for phone in self.phones:
            show_phone += f"{phone.value}  "

        if self.birthday:
            show_birthday = self.birthday.value

        if self.address:
            show_address = self.address.value

        if self.email:
            show_email = self.email.value

        return self.name.value, show_phone, show_birthday, show_address, show_email


class ContactBook(UserDict):
    """
    `ContactBook` class, which is inherited from `UserDict`,
    and is responsible for the logic of searching for records in this class.
    """

    def __init__(self):
        super().__init__()
        self.address_book_load()

    def add_record(self, record):
        """
        Add record to contact book
        :param record: Record(name, phone, email, address, birthday)
        """
        self.data[record.name.value] = record

    def delete_contact(self, name):
        """
        Delete contact from contact book
        :param name: contact name
        """
        del self.data[name]

    def address_book_load(self):
        """
        The function loads the address book at startup.

        ---------
        :param:
        :return:
        """

        try:
            with open('dump.pickle', 'rb') as dump_file:
                self.data = pickle.load(dump_file)
        except FileNotFoundError:
            pass

    def address_book_save(self, archive_book):
        """
        The function saves the address book and ends the program.

        ---------
        :param:
        :return:
        """

        with open('dump.pickle', 'wb') as dump_file:
            pickle.dump(archive_book, dump_file)

        sys.exit()


CONTACTS = ContactBook()
