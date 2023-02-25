# Bot commands associated with ContactBook, Notes, Sort folders
import book_commands
import sort_folders
from help import all_commands
from notes_commands import COMMAND_NOTES


COMMANDS = {
    'hello': book_commands.hello_func,
    'exit': book_commands.exit_func,
    'close': book_commands.exit_func,
    'good bye': book_commands.exit_func,
    'add contact': book_commands.add_contact_func,
    'add phone': book_commands.add_phone_func,
    'add address': book_commands.add_address_func,
    'add email': book_commands.add_email_func,
    'add birthday': book_commands.add_birthday_func,
    'change phone': book_commands.change_phone_func,
    'change address': book_commands.change_address_func,
    'change email': book_commands.change_email_func,
    'change birthday': book_commands.change_birthday_func,
    'delete phone': book_commands.delete_phone_func,
    'delete address': book_commands.delete_address_func,
    'delete email': book_commands.delete_email_func,
    'delete birthday': book_commands.delete_birthday_func,
    'delete contact': book_commands.delete_contact_func,
    'help': all_commands,
    'show all contacts': book_commands.show_all_info,
    'phone': book_commands.phone,
    'birthday contact': book_commands.show_birthday,
    'birthday list': book_commands.list_birthday,
    'search': book_commands.find_contacts,
    'sort': sort_folders.run,
}

COMMANDS.update(COMMAND_NOTES)
