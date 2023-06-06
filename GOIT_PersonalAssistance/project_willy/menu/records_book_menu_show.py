
from methods.data import RECORDS_BOOK
from methods.records_book_methods import Name
from methods.menu_general_methods import General
from methods.errors_processing import error_handler

from text_fields.general_text import GeneralText
from text_fields.records_book_menu_show_text import ShowRecordsMenuText


class ShowRecordsMenu(General):
# OPTIONS
    def __init__(self) -> None:
        self.MENU_OPTIONS = {
        '1': self.option_find_record,            
        '2': self.option_show_record,
        '3': self.option_show_all,
        '4': self.option_debug,
        '0': self.option_return_to_previous,
        'exit': self.option_exit_from_cli,
        }
        self.SUBMENU_OPTIONS = {
        '0': self.option_return_to_previous,
        'exit': self.option_exit_from_cli,
        }
        self.record = None
        self.__call__()

# MAIN CALL
    @error_handler
    def __call__(self) -> None:
        if not RECORDS_BOOK.data:
            print(ShowRecordsMenuText.empty_records_book_message)
            input(GeneralText.continue_input_message)
            return # to record book menu
        else:
            while True:
                print(ShowRecordsMenuText.options_message)
                user_input = input(ShowRecordsMenuText.input_message)
                if not self.options_handler(user_input, self.MENU_OPTIONS):
                    print(GeneralText.wrong_input_message)

# FIND RECORD
    @error_handler
    def option_find_record(self) -> None:
        print(ShowRecordsMenuText.submenu_options_message)
        while True:
            user_input = input(ShowRecordsMenuText.search_input_message)
            self.options_handler(user_input, self.SUBMENU_OPTIONS)
            if self.find_and_show_record(user_input):
                return # to show records menu

    @error_handler
    def find_and_show_record(self, user_input) -> None:
        if RECORDS_BOOK.find_record(user_input):
            print(RECORDS_BOOK.find_record(user_input))
            input(GeneralText.continue_input_message)
            return True
        print(ShowRecordsMenuText.no_matches_message)

# SHOW RECORD
    @error_handler
    def option_show_record(self) -> None:
        print(ShowRecordsMenuText.submenu_options_message)
        while True:
            user_input = input(ShowRecordsMenuText.record_input_message)
            self.options_handler(user_input, self.SUBMENU_OPTIONS)
            if self.get_and_show_record(user_input):
                return # to show records menu
    
    @error_handler
    def get_and_show_record(self, user_input) -> None:
        self.record = RECORDS_BOOK.get_record(Name(user_input))
        print(self.record.show_record())
        input(GeneralText.continue_input_message)
        return True

# SHOW ALL
    @error_handler
    def option_show_all(self) -> None:
        print(RECORDS_BOOK.show_records())
        input(GeneralText.continue_input_message)

# DEBUG
    @error_handler
    def option_debug(self) -> None:
        print(RECORDS_BOOK.data)
        input(GeneralText.continue_input_message)
