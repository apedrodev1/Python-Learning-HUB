# Create this new file at: src/utils/input_handler.py

from typing import Callable, Tuple, Any

def get_valid_input(prompt: str, validation_func: Callable[[str], Tuple[Any, str | None]]) -> Tuple[Any, None]:
    """
    Continuously prompts the user until a valid input is provided.

    This function abstracts the common 'while True' validation loop.
    
    Args:
        prompt (str): The message to display to the user.
        validation_func (Callable): The function (from validations.py) 
                                    to use for validating the input.
                                    It must return (value, None) on success
                                    or (None, error_message) on failure.
    
    Returns:
        Tuple[Any, None]: A tuple containing the validated, cleaned value 
                          and None for the error (as success is guaranteed).
    """
    while True:
        user_input = input(prompt)
        value, error = validation_func(user_input)
        
        if error:
            print(f"❌ {error}")
        else:
            return value, None