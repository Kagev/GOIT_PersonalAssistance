import hashlib
import os
import pathlib
import json
import getpass


class Authorization:
    def __init__(self):
        self.users = {}
        self.key = None
        self.password = None
        self.identifier = None
        self.salt = None
        self.max_attempts = 5

    def load_users(self):
        try:
            data_folder = pathlib.Path(__file__).resolve().parent.parent / 'data'
            file_path = data_folder.joinpath('users.json')
            with open(file_path, "r") as file:
                self.users = json.load(file)
                if not isinstance(self.users, dict):
                    self.users = {}  # Initialize as an empty dictionary if the loaded data is not a dictionary
            return True
        except (FileNotFoundError, json.JSONDecodeError):
            self.users = {}
            return False

    def login(self):
        print("Enter your login name (email, phone number, or username)")
        self.identifier = input(">>>: ")

        for user_data in self.users.values():
            if (
                self.identifier.upper() == user_data['username'].upper()
                or self.identifier.lower() == user_data['email'].lower()
                or self.identifier == user_data['phone']
            ):
                self.user_data = user_data

                for attempt in range(self.max_attempts):
                    print(f"Hello {self.identifier}! Enter your password")
                    self.password = getpass.getpass("Password: ")

                    self.salt = os.urandom(32)
                    self.salt = bytes.fromhex(self.user_data['salt'])
                    self.key = bytes.fromhex(self.user_data['key'])
                    new_key = hashlib.pbkdf2_hmac(
                        'sha256', self.password.encode('utf-8'), self.salt, 100000
                    )

                    if self.key == new_key:
                        print('Login successful')
                        print(f'{self.user_data["username"]}, your personal assistant "Willy" welcomes you')
                        break
                    else:
                        print('Invalid password. Please try again.')
                else:
                    print('Exceeded maximum number of login attempts.')
                break
        else:
            print("User not found")


if __name__ == "__main__":
    authorization = Authorization()
    if authorization.load_user():
        authorization.login()
    else:
        print("Failed to load user data. Please check the data file.")
