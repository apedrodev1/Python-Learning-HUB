"""
A utility module containing validation functions for user input.

These functions are designed to be used by the console UI layer.
They all follow a standard pattern: they accept a string input
and return a (value, None) tuple on success, or a (None, error_message)
tuple on failure.
"""

def validate_quantity(input_quantity):
    """
    Validates if the input is a positive integer.

    Args:
        input_quantity (str): The quantity input as a string.

    Returns:
        tuple: (int, None) if valid, (None, str) if invalid.
    """
    try:
        value = int(input_quantity)
        if value > 0:
            return value, None
        return None, "Number must be greater than zero."
    except ValueError:
        return None, "Please enter a valid positive integer."


def validate_id(input_id):
    """
    Validates if the input is a non-negative integer (ID).

    Args:
        input_id (str): The student's ID input as a string.

    Returns:
        tuple: (int, None) if valid, (None, str) if invalid.
    """
    try:
        value = int(input_id)
        if value >= 0:
            return value, None
        return None, "ID must be 0 or greater."
    except ValueError:
        return None, "Please enter a valid integer ID."


def validate_calculation_type(input_type):
    """
    Validates if the calculation type is either 0 (arithmetic) or 1 (weighted).

    Args:
        input_type (str): The type input as a string.

    Returns:
        tuple: (str, None) if valid, (None, str) if invalid.
    """
    if input_type in ["0", "1"]:
        return input_type, None
    return None, "Please enter 0 for arithmetic or 1 for weighted."


def validate_weights(input_str):
    """
    Validates numeric weights from a space-separated string.

    Checks if:
    1. The string is not empty.
    2. All inputs are numeric and > 0.
    3. The sum of all weights equals 10.

    Args:
        input_str (str): The weights input as a space-separated string.

    Returns:
        tuple: (list[float], None) if valid, (None, str) if invalid.
    """
    try:
        weights = list(map(float, input_str.strip().split()))
        if not weights:
            return None, "Weights cannot be empty."
        if any(w <= 0 for w in weights):
            return None, "All weights must be greater than zero."
        if sum(weights) != 10:
            return None, "The total weight must equal 10."
        return weights, None
    except ValueError:
        return None, "All weights must be numeric."


def validate_yes_no(input_value):
    """
    Validates a yes/no input. Accepts only 'y' or 'n'.

    Args:
        input_value (str): The user input.

    Returns:
        tuple: (str, None) if valid ('y' or 'n'), (None, str) if invalid.
    """
    input_value = input_value.strip().lower()
    if input_value in ["y", "n"]:
        return input_value, None
    return None, "Please enter only 'y' for yes or 'n' for no."


def validate_grade(input_grade):
    """
    Validates if the grade is a number between 0 and 10.

    Args:
        input_grade (str): The grade input as a string.

    Returns:
        tuple: (float, None) if valid, (None, str) if invalid.
    """
    try:
        value = float(input_grade)
        if 0 <= value <= 10:
            return value, None
        return None, "Please enter a number between 0 and 10."
    except ValueError:
        return None, "Please enter a valid number between 0 and 10."


def validate_names(name):
    """
    Validates if the name contains only letters and spaces.

    Args:
        name (str): The student's name input.

    Returns:
        tuple: (str, None) if valid (cleaned name), (None, str) if invalid.
    """
    cleaned = name.strip().capitalize()
    # Check if the name (with spaces removed) contains only letters
    if cleaned.replace(" ", "").isalpha():
        return cleaned, None
    return None, "Name must contain only letters and spaces."