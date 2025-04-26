import os

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
    retry = input("\n🔁 Do you want to run the program again? (y/n): ").lower()
    if retry == 'y':
        clear_screen()
        return True
    elif retry == 'n':
        print("\n👋 Program finished. See you next time!")
        return False
    else:
        print("❌ Please type 'y' for yes or 'n' for no.")
          
    

  
    





