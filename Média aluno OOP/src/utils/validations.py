"""
A utility module containing validation functions for user input.

These functions are designed to be used by the console UI layer.
They all follow a standard pattern: they accept a string input
and return a (value, None) tuple on success, or a (None, error_message)
tuple on failure.
"""

# --- Base Functions (Internal) ---

def _validate_integer_range(value_str, min_val=None, max_val=None, error_msg="Invalid input. Please enter a whole number."):
    """Base function to validate integers in an optional range."""
    try:
        value = int(value_str)
        if min_val is not None and value < min_val:
            # Use the specific error message or a generic one
            return None, error_msg or f"Value must be at least {min_val}."
        if max_val is not None and value > max_val:
            # Use the specific error message or a generic one
            return None, error_msg or f"Value must be no more than {max_val}."
        return value, None # Success
    except ValueError:
        # Use the specific error message or a generic one
        return None, error_msg or "Invalid input. Please enter a whole number."

def _validate_float_range(value_str, min_val=None, max_val=None, error_msg="Invalid input. Please enter a number."):
    """Base function to validate floats in an optional range."""
    try:
        value = float(value_str)
        if min_val is not None and value < min_val:
            # Use the specific error message or a generic one
            return None, error_msg or f"Value must be at least {min_val}."
        if max_val is not None and value > max_val:
            # Use the specific error message or a generic one
            return None, error_msg or f"Value must be no more than {max_val}."
        return value, None
    except ValueError:
        # Use the specific error message or a generic one
        return None, error_msg or "Invalid input. Please enter a number."

def _validate_allowed_options(value_str, options, error_msg="Invalid option."):
    """Base function to validate if the input is in a list of options."""
    cleaned_val = value_str.strip().lower()
    if cleaned_val in options:
        return cleaned_val, None
    return None, error_msg

# --- Number Validations (Specific) ---

def validate_quantity(input_quantity):
    """Validates if the input is a positive integer (>= 1)."""
    return _validate_integer_range(
        input_quantity,
        min_val=1,
        error_msg="Number must be greater than zero."
    )

def validate_quantity_min_2(value_str):
    """Validates if the input is an integer greater than or equal to 2."""
    return _validate_integer_range(
        value_str,
        min_val=2,
        error_msg="The number of grades must be at least 2."
    )

def validate_id(input_id):
    """Validates if the input is a non-negative integer (ID >= 0)."""
    return _validate_integer_range(
        input_id,
        min_val=0,
        error_msg="ID must be 0 or greater."
    )

def validate_grade(input_grade):
    """Validates if the grade is a number between 0 and 10."""
    return _validate_float_range(
        input_grade,
        min_val=0.0,
        max_val=10.0,
        error_msg="Please enter a number between 0 and 10."
    )

def validate_weights(input_str):
    """Validates a list of weights (sum must be 10)."""
    try:
        weights = list(map(float, input_str.strip().split()))
        if not weights:
            return None, "Weights cannot be empty."
        if any(w <= 0 for w in weights):
            return None, "All weights must be greater than zero."
        # Use round() to avoid float precision issues
        if round(sum(weights), 5) != 10:
            return None, "The total weight must equal 10."
        return weights, None
    except ValueError:
        return None, "All weights must be numeric."

# --- Text/Option Validations ---

def validate_names(name):
    """Validates if the name contains only letters and spaces."""
    cleaned = name.strip().capitalize()
    if cleaned and cleaned.replace(" ", "").isalpha():
        return cleaned, None
    return None, "Name must contain only letters and spaces."

def validate_yes_no(input_value):
    """Validates a 'y' or 'n' input."""
    return _validate_allowed_options(
        input_value,
        options=["y", "n"],
        error_msg="Please enter only 'y' for yes or 'n' for no."
    )

def validate_calculation_type(input_type):
    """Validates the calculation type (0, 1, or 2)."""
    return _validate_allowed_options(
        input_type,
        options=["0", "1", "2"], # Already including the future median
        error_msg="Please enter 0 (Arithmetic), 1 (Weighted), or 2 (Median)."
    )