
from methods.imports import traceback
from methods.menu_general_methods import General
from methods.errors_processing import error_handler
from methods.clean_folder import main as clean_folder

from text_fields.main_menu_text import MainMenuText
from text_fields.general_text import GeneralText

from menu.records_book_menu_main import RecordsBookMenu
from menu.notes_menu_main import NotesMenu


class MainMenu(General):
# OPTIONS
    def __init__(self) -> None:
        self.MENU_OPTIONS = {
        '1': self.option_records_book_menu,
        '2': self.option_notes_menu,
        '3': self.option_clean_folder_tool,
        'call_stack': self.option_show_current_call_stack,
        'exit': self.option_exit_from_cli,
        }
        self.__call__()

# MAIN CALL
    @error_handler
    def __call__(self) -> None:
        while True:
            print(MainMenuText.options_message)
            user_input = input(MainMenuText.input_message)
            if not self.options_handler(user_input, self.MENU_OPTIONS):
                print(GeneralText.wrong_input_message)

# RECORDS BOOK
    def option_records_book_menu(self) -> None:
       RecordsBookMenu()
        
# NOTES MENU
    def option_notes_menu(self) -> None:
        NotesMenu()

#CLEAN FOLDER TOOL
    def option_clean_folder_tool(self) -> None:
        clean_folder()
        input(GeneralText.continue_input_message)

# SHOW CURRENT CALL STACK
    def option_show_current_call_stack(self) -> None:
        for line in traceback.format_stack():
            print(f'{line.strip()}\n')
        print(f'Number of calls: {len(traceback.format_stack())}\n')
        input(GeneralText.continue_input_message)