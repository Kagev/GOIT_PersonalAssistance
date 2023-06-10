import hashlib
import os
import json
import getpass


class Authorization:

    def __init__(self):
        self.key = None
        self.password = None
        self.username = None
        self.salt = None
        self.users = {}

    def load_user(self):
        try:
            with open("users.json", "r") as file:
                for line in file:
                    user_data = json.loads(line)
                    if 'username' in user_data:
                        self.users[user_data['username']] = user_data
        except (FileNotFoundError, json.JSONDecodeError):
            self.users = {}

    def login(self):
        print("Enter your login name")
        self.username = input(">>>: ")

        if self.username not in self.users:
            print("User does not exist")
            return
        else:
            print("Enter your password")
            self.password = getpass.getpass(">>>: ")

        user_data = self.users[self.username]
        self.salt = bytes.fromhex(user_data['salt'])
        self.key = bytes.fromhex(user_data['key'])
        new_key = hashlib.pbkdf2_hmac('sha256', self.password.encode('utf-8'), self.salt, 100000)

        if self.key == new_key:
            print('Login successful')
        else:
            print('Invalid Login')


if __name__ == "__main__":
    authorization = Authorization()
    authorization.load_user()
    authorization.login()
