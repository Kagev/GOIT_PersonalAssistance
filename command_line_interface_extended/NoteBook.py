from collections import UserDict, UserList
from datetime import datetime


class NotesBook(UserList):

    def add_record(self, tag: str, notes: str) -> None:
        record = {'tag': tag,
                  'notes': notes,
                  'date_of_change': datetime.now()}
        self.append(record)

    def search_note_by_tag(self, search_tag: str) -> str:
        search_note = ''
        for record in self:
            if search_tag in record['tag']:
                search_note += record['notes'] + '\n'

        return search_note


c = NotesBook()
c.add_record('as sd df', 'asdfsdfsd')
c.add_record('as ed rfdf fr', 'sdeffgthtyhyhy')
print(c.search_note_by_tag('as'))


