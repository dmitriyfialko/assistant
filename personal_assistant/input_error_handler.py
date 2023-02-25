"""
Декоратор обробки помилок.
"""
from user_interface import RowView


def input_error(func):
    """
    A decorator for handling errors that occur due to incorrect user input.

    Параметры
    ---------
    :param func: User input function.
    :return: Outputting the result of an input function or outputting an error with re-entry.
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as key_error:
            return RowView(key_error)
        except TypeError:
            return RowView("Wrong command type")
        except IndexError:
            return RowView("Input name and phone number")
        except ValueError as exception:
            return RowView(exception.args[0])
        except Exception as ex_error:
            return RowView(ex_error)

    return wrapper
