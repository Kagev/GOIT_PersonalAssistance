
from methods.file_operations_methods import FileOperations
from methods.records_book_methods import RecordsBook
from methods.notes_methods import NotesBook

def create_or_restore_records_book() -> RecordsBook:
    if FileOperations.AUTOSAVE_PATH.is_file():
        records_book, notes_book = FileOperations.import_from_pickle(FileOperations.AUTOSAVE_PATH)
        result = records_book
    else:
        result = RecordsBook()
    return result

def create_or_restore_notes_book() -> NotesBook:
    if FileOperations.AUTOSAVE_PATH.is_file():
        records_book, notes_book = FileOperations.import_from_pickle(FileOperations.AUTOSAVE_PATH)
        result = notes_book
    else:
        result = NotesBook()
    return result

def autosave():
    FileOperations.autosave_to_pickle(FileOperations.AUTOSAVE_PATH, RECORDS_BOOK, NOTES_BOOK)

RECORDS_BOOK = create_or_restore_records_book()
NOTES_BOOK = create_or_restore_notes_book()
