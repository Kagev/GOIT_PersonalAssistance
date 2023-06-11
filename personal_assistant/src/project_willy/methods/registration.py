import hashlib
import os
import json
import getpass


class Registration:
    def __init__(self):
        self.password = None
        self.username = None
        self.salt = None
        self.users = []

    def load_user(self):
        try:
            with open("users.json", "r") as file:
                self.users = json.load(file)
                if not isinstance(self.users, list):
                    self.users = []  # Initialize as an empty list if the loaded data is not a list
        except (FileNotFoundError, json.JSONDecodeError):
            self.users = []

    def save_user(self):
        with open("users.json", "a") as file:
            user_data = {
                'username': self.username,
                'salt': self.salt.hex(),
                'key': self.key.hex()
            }
            json.dump(user_data, file)
            file.write('\n')

    def registration_user(self):
        self.load_user()

        print("Enter your login name")
        self.username = input(">>>: ")
        print("Enter your password")
        self.password = getpass.getpass(prompt='Password: ', stream=None)
        print("Enter your pass for confirm ")
        confirm_password = getpass.getpass(prompt='Password: ', stream=None)

        if self.password != confirm_password:
            print("Your passwords do not match!")
            return

        for user in self.users:
            if user['username'] == self.username:
                print("User already exists")
                return

        self.salt = os.urandom(32)
        self.key = hashlib.pbkdf2_hmac('sha256', self.password.encode('utf-8'), self.salt, 100000)

        user_data = {
            'username': self.username,
            'salt': self.salt.hex(),
            'key': self.key.hex()
        }

        self.users.append(user_data)
        self.save_user()

        print("Registration successful.")


if __name__ == "__main__":
    registration = Registration()
    registration.registration_user()
