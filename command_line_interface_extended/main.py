from menu import MainMenu
from text_fields import GeneralText


# ----------ENTER TO MAIN MENU----------
def main() -> None:
    
    print(GeneralText.start_message)
    
    while True:
        user_input = input(GeneralText.start_input_message)
        if user_input in GeneralText.EXIT:
            print(GeneralText.exit_message)
            return
        elif user_input in GeneralText.START:
            MainMenu()
        else:
            print(GeneralText.wrong_input_message)


# ----------ENTRY POINT----------
if __name__ == '__main__':
    main()
