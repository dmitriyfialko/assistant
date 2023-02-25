from notes_class import Notes
from user_interface import TableView, RowView
import time


NOTES = Notes()


def input_control(input_text: str, minimum=3, maximum=1000) -> str:
    """Функция проверяет минимальное и максимальное колличество символов ввода
    Возвращает строку"""
    while True:
        if (s := input(f'{input_text}\n>>>')) and len(s) < minimum:
            print(f'You entered less than {minimum} characters. Please re-enter')
        elif len(s) > maximum:
            print(f'You entered more than {maximum} characters. Please re-enter')
        else:
            return s


def add_note_commands():
    """Функция добавления заметки"""
    title = input_control('Specify the subject of the note', maximum=150)
    text = input_control('Enter the text of the note')
    teg = []
    while True:
        in_teg = input(f'Do you want to add tags to your note?\nYes - Y, No - N\n>>>').lower()
        if in_teg == 'y':
            teg_str = input_control('Enter tags separated by commas', minimum=4)
            teg_list = teg_str.split(',')
            for item in teg_list:
                teg.append(item.strip().lower())
            break
        elif in_teg == 'n':
            break
        else:
            print(f'You must enter Y or N')
    NOTES.add_notes(title=title, text=text, tag=teg)
    return RowView(f'Note added')


def search_note_command():
    """Функция поиска по заметкам"""
    search_str = input_control('Enter search text', maximum=50)
    list_id = NOTES.search(search_str=search_str)
    if list_id:
        field_names = ['id', 'Title', 'Text', 'tag', 'Date of change']
        rows = []
        for id_note in list_id:
            note = NOTES.get(id_note)
            rows.append([
                id_note,
                note['title'],
                note['text'],
                ', '.join([a for a in note['tag']]),
                time.strftime('%d-%m-%Y', time.gmtime(note['time']))
            ])
        return TableView(field_names, rows)
    return RowView(f'No notes found for your request')


def paginator(id_list: list, n=10):
    """Функция создаёт итератор по 'n' записям заметок из списка id_list
    [(id, title, text, tag, time), ...]"""
    if id_list:
        i = 0
        lst = []
        while True:
            note = NOTES.get(id_list[i])
            lst.append(
                (
                    id_list[i],
                    note['title'],
                    note['text'],
                    note['tag'],
                    time.strftime('%d-%m-%Y', time.gmtime(note['time']))
                )
            )
            i += 1
            if i == n:
                yield lst
                lst = []
                n += n
            if len(id_list) == i:
                if lst:
                    yield lst
                break


def show_notes_command():
    """Выодит все заметки постранично"""
    field_names = ['id', 'Title', 'Text', 'tag', 'Date of change']
    rows = []
    if NOTES:
        next_flag = False
        for notes in paginator([a for a in NOTES.keys()], n=10):
            for id_note, title, text, teg, date in notes:
                rows.append([id_note, title, text, ', '.join(teg), date])
            table = TableView(field_names, rows)
            print(table.show_info())
            if next_flag := input(f'Type "next" to view the next page of notes, '
                                  f'or any character to stop browsing.\n').lower() == 'next':
                continue
        if next_flag:
            return RowView('this is the last page with notes')
        return RowView(' ')
    return RowView('Notes not yet created')


def add_title_note(id_note):
    title = input_control('Specify a new note subject', maximum=150)
    NOTES.edit_notes(notes_id=id_note, title=title)
    print(f'Note subject changed')


def add_text_note(id_note):
    text = input_control('Enter new note text', maximum=150)
    NOTES.edit_notes(notes_id=id_note, text=text)
    print(f'Note text changed')


def add_tag_note(id_note):
    tag = NOTES[id_note]['tag']
    tag_str = input_control('Enter the tags you want to add separated by commas', minimum=4)
    tag_list = tag_str.split(',')
    for item in tag_list:
        tag.append(item.strip().lower())
    NOTES.edit_notes(notes_id=id_note, tag=tag, adding_tags=True)
    print(f'Tags added')


def replace_tag_note(id_note):
    tag = []
    tag_str = input_control('Enter new tags separated by commas, '
                            'or leave the field blank to remove all tags.', minimum=4)
    if tag_str:
        tag_list = tag_str.split(',')
        for item in tag_list:
            tag.append(item.strip().lower())
    NOTES.edit_notes(notes_id=id_note, tag=tag, adding_tags=False)
    print(f'Tags changed')


def edit_note_command():
    """Функция редактирования заметок"""
    id_note = input(f'Specify a note ID to edit, or type "show notes" to see all note IDs.\n')
    if id_note.lower() in ['show notes', 'show note', 'show', 'shownote']:
        return show_notes_command()
    try:
        id_note = int(id_note)
    except ValueError:
        return RowView(f'There are no notes with this ID. ID must be only a number\n'
                       f'Use the "show notes" command to find out the note id')
    if NOTES.get(id_note, None):
        field_names = ['command', 'description']
        rows = [['title', 'Title editing command'],
                ['text', 'Text editing command'],
                ['tag', 'Command for adding tags'],
                ['r-tag', 'Command to replace or remove tags'],
                ['stop', 'Command to exit note editing']]
        table = TableView(field_names, rows)
        com_d = {
            'title': add_title_note,
            'text': add_text_note,
            'tag': add_tag_note,
            'r-tag': replace_tag_note
        }
        while True:
            edit_com = input(f'Choose what to edit in a note\n{table.show_info()}\n>>> ')
            if edit_com.lower() == 'stop':
                break
            if edit_com.lower() in list(com_d.keys()):
                com_d[edit_com.lower()](id_note)
                while True:
                    yn = input(f'Do you want to continue editing this note?\n'
                               f'Yes - Y, No - N >>>').lower()
                    if yn in ['y', 'n']:
                        break
                    print(f'You must enter Y or N')
                if yn == 'n':
                    break
            else:
                print(f'There is no such command. You must enter the command from the table below')
        return RowView('Note editing completed')
    else:
        return RowView('There are no notes with this ID.\n'
                       'Use the "show notes" command to find out the note id')


def del_note_command():
    """Функция удаления заметок"""
    id_note = input(f'Specify the note ID to delete, or type "show notes" to see all note IDs.\n')
    if id_note.lower() in ['show notes', 'show note', 'show', 'shownote']:
        return show_notes_command()
    try:
        id_note = int(id_note)
        if NOTES.delete_by_id(notes_id=id_note):
            return RowView('Note removed')
        else:
            return RowView(f'There are no notes with this ID\n'
                           f'Use the "show notes" command to find out the note id')
    except ValueError:
        return RowView(f'There are no notes with this ID. ID must be only a number\n'
                       f'Use the "show notes" command to find out the note id')


COMMAND_NOTES = {
    'add note': add_note_commands,
    'find note': search_note_command,
    'show notes': show_notes_command,
    'edit note': edit_note_command,
    'delete note': del_note_command
}
