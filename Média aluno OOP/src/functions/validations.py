def validate_quantity(input_quantity):
    try:
        value = int(input_quantity)
        if value > 0:
            return value, None
        return None, "Number must be greater than zero."
    except ValueError:
        return None, "Please enter a valid positive integer."


def validate_calculation_type(input_type):
    if input_type in ["0", "1"]:
        return input_type, None
    return None, "Please enter 0 for arithmetic or 1 for weighted."


def validate_weights(input_str):
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



def validate_grade(input_grade):
    try:
        value = float(input_grade)
        if 0 <= value <= 10:
            return value, None
        return None, "Please enter a number between 0 and 10."
    except ValueError:
        return None, "Please enter a valid number between 0 and 10."
    

def validate_names(name):
    cleaned = name.strip().capitalize()
    if cleaned.replace(" ", "").isalpha():
        return cleaned, None
    return None, "Name must contain only letters and spaces."