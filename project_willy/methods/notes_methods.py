from imports import UserList, UserDict

class Notes(UserDict):
    def __init__(self) -> None:
        UserDict.__init__(self)


class NotesBook(UserList):
    def __init__(self) -> None:
        UserList.__init__(self)
