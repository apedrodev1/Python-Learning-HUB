"""
Handles the initial parameter setup for the application.

This module is responsible for the user-facing workflow of gathering
the initial batch of settings (like student quantity, average type,
and passing grade) before the main processing begins.
"""

from . ..utils.validations import  (
    validate_quantity,
    validate_calculation_type,
    validate_weights,
    validate_grade,
    validate_quantity_min_2
)

def get_main_parameters():
    """
    Prompts the user to input the main parameters for the session.

    This function runs an interactive console prompt to gather:
    1.  The total number of new students to add.
    2.  The calculation type (0 for arithmetic, 1 for weighted).
    3.  The list of weights (if weighted) or the number of marks (if arithmetic).
    4.  The minimum passing grade.

    It validates each input and re-prompts on error.

    Returns:
        tuple: A tuple containing the following five values:
            (students_quantity (int),
             way_to_calculate (str),
             passing_grade (float),
             weights (list),
             number_of_marks (int or None))
    """

    weights = []
    number_of_marks = None

    # Validate the number of students
    while True:
        user_input = input('First things first! How many students would you like to calculate grades for? ')
        students_quantity, error = validate_quantity(user_input)
        if error:
            print(f"❌ {error}")
        else:
            break

    # Validate the type of average calculation
    while True:
        calc_type_input = input('Would you like to use arithmetic or weighted average? (Enter 0 for arithmetic mean, 1 for weighted mean and 2 for median): ')
        way_to_calculate, error = validate_calculation_type(calc_type_input)
        if error:
            print(f"❌ {error}")
        else:
            break

    # If weighted, request the weights
    if way_to_calculate == "1":
        while True:
            weights_input = input('Enter the weights for each grade, separated by spaces (e.g., 2 3 1 4). The total must equal 10: ')
            weights, error = validate_weights(weights_input)
            if error:
                print(f"❌ {error}")
            else:
                break
    else:
        # If arithmetic, ask for the number of grades per student
        while True:
            marks_input = input("How many grades will each student have? ")
            number_of_marks, error = validate_quantity_min_2(marks_input)
            if error:
                print(f"❌ {error}")
            else:
                break

    # Validate the passing grade
    while True:
        passing_input = input("Enter the minimum passing grade (0 to 10): ")
        passing_grade, error = validate_grade(passing_input)
        if error:
            print(f"❌ {error}")
        else:
            break

    return students_quantity, way_to_calculate, passing_grade, weights, number_of_marks