from imports import UserList, UserDict, datetime
from methods.errors import NotesError

class Notes(UserDict):
    def __init__(self) -> None:
        UserDict.__init__(self)
        self.data = {
            'tags': None,
            'notes': None,
            'date_of_change': None
        }

    def add_tags(self, user_input: str) -> None:
        if user_input.strip():
            new_tags = user_input.strip().split()
            if len(new_tags) == 1:
                tags = new_tags
            if len(new_tags) >= 2:
                _set = set(new_tags)
                tags = [i for i in _set]
            self.data['tags'] = tags  
        else:
            raise NotesError

    def add_text(self, user_input: str) -> None:
        text = user_input.strip()
        if len(text) > 300:
            raise NotesError
        self.data['notes'] = text

    def create_notes(self) -> None:
        if self.data['tags'] != None and self.data['notes'] != None:
            self.data['date_of_change'] = datetime.now()

    def notes_info(self) -> str:
        result = 'Notes:\n\n'
        if self.data['tags'] != None:
            result += f"Tags: {', '.join(self.data['tags'])}\n"
        else:
            result += 'tags: empty\n'
        if self.data['notes'] != None:
            result += f"Text: {self.data['notes']}\n"
        else:
            result += 'Text: empty\n'
        return result

class NotesBook(UserList):
    def __init__(self) -> None:
        UserList.__init__(self)

    def add_notes(self, notes: Notes) -> None:
        self.data.append(notes)

    def delete_notes(self, notes: Notes)-> None:
        self.data.remove(notes)

    def clear(self) -> None:
        self.data.clear()

    def find_notes(self, user_input: str) -> dict:
        result = {}
        count = 1
        search_tags = user_input.strip().split()
        for notes in self.data:
            for tag in search_tags:
                if tag.lower() in ''.join(notes['tags']).lower():
                    result.update({count: notes})
                    count += 1
        if result.values():
            return result
