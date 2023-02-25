from pathlib import Path
import shutil

list_doc = ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx']
list_image = ['.jpeg', '.png', '.jpg', '.svg', '.JPG']
list_music = ['.mp3', '.ogg', '.wav', '.amr']
list_video = ['.avi', '.mp4', '.mov', '.mkv']
list_zip = ['.zip', '.gz', '.tar']
list_other = list_doc + list_image + list_music + list_video + list_zip
list_name_folder = ['Documents', 'Images', 'Musics', 'Videos', 'Archives', 'Others']


def file_remove(file_ob, path):
    """
    We transfer files by folder.

    ---------
    :param:
    :return:
    """

    way_console = Path(main(path))
    if file_ob.suffix in list_zip:
        files_unpack(way_console, file_ob)
    elif file_ob.suffix in list_doc:
        new_folder = way_console.joinpath(list_name_folder[0])
        try:
            shutil.move(file_ob, new_folder)
        except shutil.Error:
            file_ob.replace(file_ob)
    elif file_ob.suffix in list_image:
        new_folder = way_console.joinpath(list_name_folder[1])
        try:
            shutil.move(file_ob, new_folder)
        except shutil.Error:
            file_ob.replace(file_ob)
    elif file_ob.suffix in list_music:
        new_folder = way_console.joinpath(list_name_folder[2])
        try:
            shutil.move(file_ob, new_folder)
        except shutil.Error:
            file_ob.replace(file_ob)
    elif file_ob.suffix in list_video:
        new_folder = way_console.joinpath(list_name_folder[3])
        try:
            shutil.move(file_ob, new_folder)
        except shutil.Error:
            file_ob.replace(file_ob)
    else:
        new_folder = way_console.joinpath(list_name_folder[5])
        try:
            shutil.move(file_ob, new_folder)
        except shutil.Error:
            file_ob.replace(file_ob)


def files_unpack(way_console, file_ob):
    """
    We unpack the archive.

    ---------
    :param:
    :return:
    """

    folder_archive = way_console.joinpath(list_name_folder[4])
    shutil.unpack_archive(file_ob, folder_archive)
    file_ob.unlink()


def folder_create(way_consoles):
    """
    We create folders by groups.

    ---------
    :param:
    :return:
    """

    new_folders(list_name_folder[0], way_consoles)
    new_folders(list_name_folder[1], way_consoles)
    new_folders(list_name_folder[2], way_consoles)
    new_folders(list_name_folder[3], way_consoles)
    new_folders(list_name_folder[4], way_consoles)
    new_folders(list_name_folder[5], way_consoles)


def folders_dell(way_consoles):
    """
    Delete folders.

    ---------
    :param:
    :return:
    """

    for folder in way_consoles.glob('*'):
        if folder.name not in list_name_folder:
            shutil.rmtree(folder)


def out_folders(name_folder):
    """
    The function displays the name of the folder that was created.

    ---------
    :param:
    :return:
    """

    print('')
    print('-------------------------------------------------------')
    print(f'The {name_folder} folder contains the following files: ')
    print('')


def out_files(path_folders, folders):
    """
    The function displays the name of the files that were transferred.

    ---------
    :param:
    :return:
    """

    for folder in path_folders.joinpath(folders).glob('*'):
        print(folder.name)


def list_of_files(way_consoles):
    """
    func

    :param way_consoles:
    :return:
    """

    out_folders(list_name_folder[0])
    out_files(way_consoles, list_name_folder[0])

    out_folders(list_name_folder[1])
    out_files(way_consoles, list_name_folder[1])

    out_folders(list_name_folder[2])
    out_files(way_consoles, list_name_folder[2])

    out_folders(list_name_folder[3])
    out_files(way_consoles, list_name_folder[3])

    out_folders(list_name_folder[4])
    out_files(way_consoles, list_name_folder[4])

    out_folders(list_name_folder[5])
    out_files(way_consoles, list_name_folder[5])


def main(path):
    """
    Рахуємо шлях до папки.

    Параметры
    ---------
    :param:
    :return:
    """

    try:
        return path
    except IndexError:  # Ошибку IndexError (аргументы не передали) "переводим" в
        return 'qwerty'  # неправильный путь и в дальнейшем выводим сообщение что "Введен неверный путь к папке"


def new_folders(name_folder, way_consoles):
    """
    Створюємо папки якщо їх нема.

    Параметры
    ---------
    :param:
    :return:
    """

    document_folder = way_consoles / name_folder
    if not document_folder.is_dir():
        Path(document_folder).mkdir()


def translate(name):
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ !#$%&'()*+,-./:;<=>?@[\]^`{|}~"

    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t",
                   "u", "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g", '_', '_',
                   '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
                   '_', '_', '_', '_', '_', '_', '_', '_', '_')

    TRANS = {}

    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()

    new_name = name.translate(TRANS)
    return new_name


def normalize(way_consoles):
    """
    Змінюємо назву файлів та папок.

    Параметры
    ---------
    :param:
    :return:
    """

    for element in way_consoles.rglob('*/*'):
        if element.is_file():
            file_suffix = element.suffix
            new_file = translate(str(element.stem))
            rez_name = ''.join([new_file, file_suffix])
            element.replace(element.parent / rez_name)
        elif element.is_dir():
            new_file = translate(str(element.stem))
            element.replace(element.parent / new_file)


def parsing(way_console, path):
    """
    Рекурсивно проходимось по папкам та передаєм файли у функцію file_remove.

    Параметры
    ---------
    :param:
    :return:
    """

    for file_ob in way_console.glob('*'):
        if file_ob.is_file():
            file_remove(file_ob, path)
        elif file_ob.is_dir():
            parsing(file_ob, path)


def run():
    input_path = input('Enter the path to the folder: ')
    way_console = Path(main(input_path))
    if way_console.is_dir():
        folder_create(way_console)
        parsing(way_console, input_path)
        folders_dell(way_console)
        normalize(way_console)
        list_of_files(way_console)
    else:
        print('Invalid folder path entered')
        print('Please enter the correct path!')


if __name__ == '__main__':
    run()
