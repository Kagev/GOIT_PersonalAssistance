
from imports import sys

from methods.errors import NameError, PhoneError, EmailError, BirthdayError, ExitFromCLI, NotesError

from text_fields.errors_text import ErrorsText

def error_handler(func) -> str:
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except IndexError:
            print(ErrorsText.index_error_message)
        except KeyError:
            print(ErrorsText.key_error_message)
        except TypeError:
            print(ErrorsText.type_error_message)
        except ValueError:
            print(ErrorsText.value_error_message)
        except NameError:
            print(ErrorsText.name_error_message)
        except PhoneError:
            print(ErrorsText.phone_error_message)
        except EmailError:
            print(ErrorsText.email_error_message)
        except BirthdayError:
            print(ErrorsText.birthday_error_message)
        except NotesError:
            print(ErrorsText.notes_error_message)
        except ExitFromCLI:
            print(ErrorsText.exit_message)
            sys.exit()
        else:
            return result
    return wrapper
