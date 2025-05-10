from ..functions.validations import (
    validate_quantity,
    validate_calculation_type,
    validate_weights,
    validate_grade
)

def get_main_parameters():
    """
    Requests the initial parameters:
    - Number of students
    - Type of calculation (arithmetic or weighted average)
    - Minimum passing grade
    - Number of grades per student (if arithmetic)
    - Weights (if weighted)

    Returns:
        tuple: (students_quantity, way_to_calculate, passing_grade, weights, number_of_marks)
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
        calc_type_input = input('Would you like to use arithmetic or weighted average? (Enter 0 for arithmetic and 1 for weighted): ')
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
            number_of_marks, error = validate_quantity(marks_input)
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
