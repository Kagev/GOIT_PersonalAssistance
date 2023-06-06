
from methods.data import RECORDS_BOOK, autosave

from methods.imports import Path

from methods.records_book_methods import RecordsBook
from methods.file_operations_methods import FileOperations
from methods.menu_general_methods import General
from methods.errors_processing import error_handler

from text_fields.general_text import GeneralText
from text_fields.records_book_menu_import_text import ImportMenuText


class ImportMenu(General):
# OPTIONS
    def __init__(self) -> None:
        self.MENU_OPTIONS = {
        '0': self.option_return_to_previous,
        'exit': self.option_exit_from_cli,
        }
        self.__call__()

# MAIN CALL
    @error_handler
    def __call__(self) -> None:
        print(ImportMenuText.options_message)
        while True:
            user_input = input(ImportMenuText.input_message)
            self.options_handler(user_input, self.MENU_OPTIONS)
            if self.import_records_book_from_pickle(user_input):
                return # to previous menu

    @error_handler
    def import_records_book_from_pickle(self, path_from_user: str) -> None:
        path_for_import = Path(path_from_user)
        if path_for_import.is_file():
            imported_records_book = FileOperations.import_from_pickle(path_for_import)
            if isinstance(imported_records_book, RecordsBook):
                RECORDS_BOOK.update(imported_records_book)
                autosave()
                print(ImportMenuText.import_records_book_successful_message)
                input(GeneralText.continue_input_message)
                return True
            else:
                print(ImportMenuText.invalid_file_message)
        else:
            print(ImportMenuText.file_not_exists_message)
