# src/functions/parameters.py

from ..functions.validations import (
    validate_quantity,
    validate_calculation_type,
    validate_weights,
    validate_grade
)

def get_main_parameters():
    weights = []

    # Validação da quantidade de alunos
    while True:
        user_input = input('First things first! How many students would you like to calculate grades for? ')
        students_quantity, error = validate_quantity(user_input)
        if error:
            print(f"❌ {error}")
        else:
            break

    # Validação do tipo de média
    while True:
        calc_type_input = input('Would you like to use arithmetic or weighted average? (Enter 0 for arithmetic and 1 for weighted): ')
        way_to_calculate, error = validate_calculation_type(calc_type_input)
        if error:
            print(f"❌ {error}")
        else:
            break

    # Se for ponderada, solicitar pesos
    if way_to_calculate == "1":
        while True:
            weights_input = input('Enter the weights for each grade, separated by spaces (e.g., 2 3 1). The sum of weights must be equal to 10: : ')
            weights, error = validate_weights(weights_input)
            if error:
                print(f"❌ {error}")
            else:
                break

    # Validação da nota de corte
    while True:
        passing_input = input("Enter the minimum passing grade (0 to 10): ")
        passing_grade, error = validate_grade(passing_input)
        if error:
            print(f"❌ {error}")
        else:
            break

    return students_quantity, way_to_calculate, passing_grade, weights
