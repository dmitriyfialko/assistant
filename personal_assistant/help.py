from user_interface import HelpTable


def all_commands():
    """
    Функция показывает все возможные команды.

    :return: 'Enter new command.'
    """

    help_list = [
        ('Add a birthday to an existing contact', 'add birthday'),
        ('Add a new phone number to an existing contact', 'add phone'),
        ('Add an address to an existing contact', 'add address'),
        ('Add notes', 'add note'),
        ('Add an email address to an existing contact', 'add email'),
        ('Change the address of an existing contact', 'change address'),
        ('Change the birthday of an existing contact', 'change birthday'),
        ('Change the phone number of an existing contact', 'change phone'),
        ('Change the mailbox of an existing contact', 'change email'),
        ('Close program and save data', 'close'),
        ('Close program and save data', 'good bye'),
        ('Command table', 'help'),
        ('Create a new contact with the following fields', 'add contact'),
        ('Delete an address from an existing contact', 'delete address'),
        ('Delete an existing contact', 'delete contact'),
        ("Delete an existing contact's mailbox", 'delete email'),
        ('Delete notes', 'delete note'),
        ('Delete the birthday of an existing contact', 'delete birthday'),
        ('Delete the phone number of an existing contact', 'delete phone'),
        ('Edit notes', 'edit note'),
        ('Exit the program and save the data', 'exit'),
        ('File sorting', 'sort'),
        ('Find notes', 'find note'),
        ('Greeting', 'hello'),
        ('List users whose birthday is in N days', 'birthday list'),
        ('Look up a phone number based on the name of an existing contact', 'phone'),
        ('Search contact', 'search'),
        ('Shows how many days are left until the birthday', 'birthday contact'),
        ('View all contacts', 'show all contacts'),
        ('View notes', 'show notes'),
        ]
    table_header = ['DESCRIPTION', 'COMMAND']

    table = HelpTable(headers=table_header, rows=help_list)
    return table

