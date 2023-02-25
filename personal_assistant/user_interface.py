from abc import abstractmethod, ABC
from prettytable import PrettyTable
from tabulate import tabulate


class UserInterface(ABC):
    @abstractmethod
    def show_info(self):
        pass


class RowView(UserInterface):
    """Выводит инфомацию в виде строк"""

    def __init__(self, text):
        self.text = text
        self.__color = 'default'
        self.color_dict = {'red': '\033[31m',
                           'blue': '\033[34m',
                           'green': '\033[32m',
                           'yellow': '\033[33m',
                           'default': '\033[0m'}

    def color_settings(self, color='default'):
        if color in self.color_dict.items():
            self.__color = color

    def show_info(self):
        return f'{self.color_dict[self.__color]}{self.text}'


class TableView(UserInterface):
    """Выводит инфомацию в виде таблицы
    при помощи PrettyTable"""

    def __init__(self, fields: list, rows: list):
        self.fields = fields
        self.rows = rows

    def show_info(self):
        table = PrettyTable()
        table.field_names = self.fields
        table.add_rows(self.rows)
        return table.get_string()


class HelpTable(UserInterface):
    """Выводит инфомацию в виде таблицы
        при помощи 'tabulate'"""

    def __init__(self, headers, rows):
        self.headers = headers
        self.rows = rows
        self.format = 'pipe'
        self.showindex = 'always'

    def change_settings(self, format_=None, showindex_=None):
        if format_:
            self.format = format_
        if showindex_:
            self.showindex = showindex_

    def show_info(self):
        return tabulate(self.rows, headers=self.headers, tablefmt=self.format, showindex=self.showindex)
