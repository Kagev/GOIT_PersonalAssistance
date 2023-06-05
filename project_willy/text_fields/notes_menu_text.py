
class NotesMenuText:
    options_message = \
    '\n{:^40}\n{:^40}\n'.format('---NOTES MENU---', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('1. ADD NEW NOTES', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('2. CHANGE EXISTS NOTES', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('3. SHOW NOTES', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('4. CLEAR NOTES BOOK', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('0. RETURN TO MAIN MENU', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('EXIT', '-'*40)
    input_message = 'You are in "NOTES MENU". Choose one of the options.\n>>> '
    clear_successful_message = '\nThe notes book has been cleared successfully!\n'
    clear_input = 'Are you sure? Enter "y" to continue.\n>>> '

class AddNotesMenuText:
    options_message = \
    '\n{:^40}\n{:^40}\n'.format('---ADD NOTES MENU---', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('0. RETURN TO NOTES MENU', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('EXIT', '-'*40)
    tags_input_message = 'Input tags for notes, please.\n>>> '
    text_input_message = 'Input text of notes, please.\n>>> '
    add_successful_message = '\nNotes has been successfully added to notes book!\n'

class ChangeNotesMenuText:
    options_message = \
    '\n{:^40}\n{:^40}\n'.format('---CHANGE NOTES MENU---', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('1. CHANGE TAGS', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('2. CHANGE NOTES TEXT', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('3. DELETE NOTES', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('0. RETURN TO NOTES MENU', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('EXIT', '-'*40)
    tags_input_message = 'Input some tags to begin.\n>>> '
    input_message = 'You are in "CHANGE NOTES MENU". Choose one of the options.\n>>> '
    tags_input_message = 'Input tags for notes, please.\n>>> '
    text_input_message = 'Input text of notes, please.\n>>> '
    empty_notes_book_message = '\nNotes book is empty. Nothing to look at.\n'
    notes_indx_input_message = 'Input number of one of notes to change.\n>>> '
    delete_input = 'Are you sure? Enter "y" to continue.\n>>> '
    delete_successful_message = '\nThe notes has been deleted successfully!\n'
    no_matches_message = '\nNo matches. Try again\n'
    premenu_options_message = \
    '\n{:^40}\n{:^40}\n'.format('---CHANGE NOTES PREMENU---', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('0. RETURN TO MAIN MENU', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('EXIT', '-'*40)

    submenu_options_message = \
    '\n{:^40}\n{:^40}\n'.format('---CHANGE NOTES SUBMENU---', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('0. RETURN TO CHANGE NOTES MENU', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('EXIT', '-'*40)

class ShowNotesMenuText:
    options_message = \
    '\n{:^40}\n{:^40}\n'.format('---SHOW NOTES MENU---', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('1. FIND NOTES', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('2. SORT ALL BY A-Z', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('3. SORT ALL BY DATE', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('4. DEBUG INFO', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('0. RETURN TO NOTES MENU', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('EXIT', '-'*40)
    input_message = 'You are in "SHOW NOTES MENU". Choose one of the options.\n>>> '
    search_input_message = 'Enter tags to find notes.\n>>> '
    no_matches_message = '\nNo matches. Try again\n'
    empty_notes_book_message = '\nNotes book is empty. Nothing to look at.\n'
    
    submenu_options_message = \
    '\n{:^40}\n{:^40}\n'.format('---SHOW NOTES SUBMENU---', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('0. RETURN TO SHOW NOTES MENU', '-'*40)+\
    '|{:^38}|\n{:^40}\n'.format('EXIT', '-'*40)
 