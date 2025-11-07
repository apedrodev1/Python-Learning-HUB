"""
Provides utility functions for controlling the application loop and UI.

This module includes functions for clearing the terminal screen
and managing the "run again" prompt at the end of the main loop.
"""

import os
from . ..utils.input_handler import get_valid_input
from . ..utils.validations import validate_yes_no

def clear_screen():
    """
    Clears the terminal screen.
    
    Checks the operating system name ('nt' for Windows, else POSIX)
    and executes the appropriate clear command ('cls' or 'clear').
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def ask_to_retry():
    """
    Asks the user if they want to run the program again.

    This function will loop until a valid 'y' (yes) or 'n' (no)
    is entered. It prints a goodbye message if 'n' is chosen.

    Returns:
        bool: True if the user wants to retry ('y'),
              False if the user wants to quit ('n').
    """
        
    retry, _ = get_valid_input( # This fuction does a While loop
        "\n🔁 Do you want to run the program again? (y/n): ",
        validate_yes_no  
    )
    
    if retry == 'y':
        clear_screen()
        return True
    elif retry == 'n':
        print("\n👋 Program finished. See you next time!")
        return False