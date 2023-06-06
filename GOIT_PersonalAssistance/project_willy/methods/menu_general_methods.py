
from methods.errors import Return, ExitFromCLI

class General:

    def options_handler(self, user_command: str, options: dict) -> None:
        command = user_command.strip().lower()
        if command in options:
            options[command]()
            return True

    def option_return_to_previous(self) -> None:
        raise Return

    def option_exit_from_cli(self) -> None:
        raise ExitFromCLI
