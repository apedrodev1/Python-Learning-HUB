import os
from ..functions.validations import validate_yes_no

def clear_screen():
    '''
    Clears the terminal screen depending on the operating system.
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


def ask_to_retry():
    '''
    Asks the user if they want to run the program again.

    Returns:
        bool: True if the user wants to retry, False otherwise.
    '''
    while True:
        retry_input = input("\n🔁 Do you want to run the program again? (y/n): ")
        retry, error = validate_yes_no(retry_input)
        if error:
            print(f"❌ {error}")
        elif retry == 'y':
            clear_screen()
            return True
        elif retry == 'n':
            print("\n👋 Program finished. See you next time!")
            return False

  
    





