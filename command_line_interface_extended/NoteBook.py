from collections import UserDict, UserList
from datetime import datetime

class Note(UserDict):
    def add_tag(self, tag: str) -> None:
        if tag:
            self.data['tag'] = list(tag.split(' '))

    def add_note(self, note: str) -> None:
        self.data['notes'] = note
        self.data['date_of_change'] = str(datetime.now())

    


class NotesBook(UserList):

    def add_record(self, record: Note) -> None:
        self.append(record)

    def search_note_by_tag(self, search_tag: str) -> str:
        search_note = ''
        for record in self:
            if search_tag in record['tag']:
                search_note += record['notes'] + '\n'

        return search_note

a = Note()
a.add_tag('as sd df')
a.add_note('asdffrfdsf')


c = NotesBook()
c.add_record(a)
c.search_note_by_tag('as')
