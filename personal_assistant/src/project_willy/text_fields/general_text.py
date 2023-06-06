
class GeneralText:

    START = ['start', 'hello', 'hi', '',]
    CONTINUE = ['', 'continue']
    EXIT = ['exit', 'close']
    
    start_message = \
    '\n{:^40}\n{:^40}\n'.format('---HELLO---', '-'*40)+\
    '|{:^38}|\n'.format("I'M WILLY ASSISTANT v0.9.*")+\
    '|{:^38}|\n{:^40}\n'.format("NICE TO MEET YOU!", '-'*40)
    
    start_input_message = 'Enter "start" to begin!\n>>> '
    hello_message = '\nHow can I help you?'
    exit_message = '\nleaving so soon? Okay...\n'
    wrong_input_message = '\nHmm.. Somesing wrong. Try again.\n'
    continue_input_message = 'Press enter to continue.\n>>> '
