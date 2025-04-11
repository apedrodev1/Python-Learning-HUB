def get_main_parameters():
    weights = []

    students_quantity = int(input('First things first! How many students would you like to calculate grades for? '))
    
    calculation_type = input('Would you like to use arithmetic or weighted average? (Enter 0 for arithmetic and 1 for weighted): ').strip()

    if calculation_type == "1":
        weights_input = input('Enter the weights for each grade, separated by spaces (e.g., 2 3 1): ')
        weights = [int(w) for w in weights_input.split()]
    
    passing_grade = float(input('What is the minimum passing grade? '))

    return students_quantity, calculation_type, passing_grade, weights
