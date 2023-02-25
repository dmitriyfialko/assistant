from collections import UserDict
import time
import pickle


class Notes(UserDict):
    """Клас хранит notes

    реализует доступ к хранению изменению и поиску заметок
    Структура (словарь словарей):
    {id: {'title': 'title text',
          'tag': [tag1, tag2],
          'text': 'text',
          'time': 'unix time'}
    }"""

    def __init__(self):
        super().__init__()
        self.__unpacking_notes()

    def __unpacking_notes(self):
        """Распаковует сохранённый класс Notes из файла 'notes.pic'
        Если файл существует, переопределяет self"""
        try:
            with open('notes.pic', 'rb') as f:
                self.data = pickle.load(f).data
        except FileNotFoundError:
            pass

    def __packing_notes(self):
        """Сохраняет класс AddressBook в файл 'address_book.pic'"""
        with open('notes.pic', 'wb') as f:
            pickle.dump(self, f)

    def __last_id(self) -> int:
        """Возвращает последний из имеющихся id"""
        if self.data:
            list_id = [i for i in self.data.keys()]
            list_id.sort()
            return list_id[-1]
        return 0

    def add_notes(self, title: str, text: str, tag: list):
        """Метод добавляет заметку
        :param title: строка заголовка заметки (str)
        :param text: текст заметки (str)
        :param tag: список тегов (обязательно list, иначе генерирует ValueError"""
        if type(tag) is not list:
            raise ValueError('"tag" argument must be a list')
        new_id = self.__last_id() + 1
        self.data[new_id] = {
            'title': title,
            'text': text,
            'tag': tag,
            'time': time.time()
        }
        self.__packing_notes()

    def delete_by_id(self, notes_id):
        """Удаляет заметку по ключу и возвращает удалённую заметку
        Если заметка не найдена, возвращает None"""
        notes = self.data.pop(notes_id, None)
        if notes:
            self.__packing_notes()
        return notes

    def edit_notes(self, notes_id, title=None, text=None, tag=None, adding_tags=True):
        """
        Вносит изменения в заметку по id
        :param notes_id: обязательный параметр, если нет id в self.data генерирует KeyError
        :param title: если не указан не изменяется (str)
        :param text: если не указан не изменяется (str)
        :param tag: если не указан не изменяется (обязательно list, иначе генерирует ValueError
        :param adding_tags: если True теги добавляются, если False теги заменяются новым списком
        :return: возвращает отредактированый notes, если изменения внесены успешно
        """
        notes = self.data[notes_id]
        if title:
            notes['title'] = title
        if text:
            notes['text'] = text
        if tag is not None:
            if type(tag) is not list:
                raise ValueError('"tag" argument must be a list')
            if adding_tags:
                notes['tag'] += tag
            else:
                notes['tag'] = tag
        notes['time'] = time.time()
        self.data[notes_id] = notes
        self.__packing_notes()
        return notes

    def search(self, search_str: str, n=10) -> list:
        """
        Осуществляет поиск по notes. Возвращается список с n-количеством id (Пример: [2, 8, 11, 3, 5])
        :param search_str: строка поиска
        :param n: указывает на максимальное количество заметок для вывода
        :return: список с n-количеством id

        Поиск осуществляется в следующем приоритете:
        вхождение в title, tag вхождение в search_str, вхождение в title по отдельным словам search_str,
        вхождение в text, вхождение в text по отдельным словам search_str,
        """
        list_id = []
        # вхождение в title
        for n_id, notes in self.data.items():
            if len(list_id) == n:
                return list_id
            if n_id not in list_id and search_str.lower() in notes['title'].lower():
                list_id.append(n_id)
        # tag вхождение в search_str
        for n_id, notes in self.data.items():
            if len(list_id) == n:
                return list_id
            for tag in notes['tag']:
                if n_id not in list_id and tag.lower() in search_str.lower():
                    list_id.append(n_id)
                    break
        # вхождение в title по отдельным словам search_str
        if len(search_list := search_str.split()) > 0:
            for item in search_list:
                item.strip().strip(',').strip('.').strip('!').strip('?')
                if len(item) >= 3:
                    for n_id, notes in self.data.items():
                        if len(list_id) == n:
                            return list_id
                        if n_id not in list_id and item.lower() in notes['title'].lower():
                            list_id.append(n_id)
        # вхождение в text
        for n_id, notes in self.data.items():
            if len(list_id) == n:
                return list_id
            if n_id not in list_id and search_str.lower() in notes['text'].lower():
                list_id.append(n_id)
        # вхождение в text по отдельным словам search_str
        if len(search_list := search_str.split()) > 0:
            for item in search_list:
                item.strip().strip(',').strip('.').strip('!').strip('?')
                if len(item) >= 3:
                    for n_id, notes in self.data.items():
                        if len(list_id) == n:
                            return list_id
                        if n_id not in list_id and item.lower() in notes['text'].lower():
                            list_id.append(n_id)
        return list_id
