from ..functions.validations import validate_quantity, validate_calculation_type, validate_weights, validate_grade #funcoes de validacao de entrada

def get_main_parameters():
    # Inicializa a lista de pesos das notas
    weights_marks = []



    # Valida a quantidade de alunos
    while True:
        user_input = input('First things first! How many students would you like to calculate grades for? ')
        students_quantity = validate_quantity(user_input)
        if students_quantity is not None:
            break
        print('❌ Please enter a valid positive integer.')



    # Valida o tipo de cálculo (aritmético ou ponderado)
    while True:
        calc_type_input = input(
            'Would you like to use arithmetic or weighted average? (Enter 0 for arithmetic and 1 for weighted): '
        )
        calculation_type = validate_calculation_type(calc_type_input)
        if calculation_type is not None:
            break
        print("❌ Please enter 0 or 1.")    


    # Se o cálculo for ponderado, solicita os pesos
    if calculation_type == "1":
        while True:
            weights_input = input('Enter the weights for each grade, separated by spaces (e.g., 2 3 1): ') 
            weights_marks = validate_weights(weights_input)  
            if weights_marks is not None:
                break  # Se os pesos são válidos, sai do loop.
            print('❌ Invalid input. Please enter a list of numbers between 0 and 10.')



    # Valida a nota mínima para aprovação
    while True:
        passing_input = input("Enter the minimum passing grade (0 to 10): ")
        passing_grade = validate_grade(passing_input)
        if passing_grade is not None:
            break
        print("❌ Invalid input. Please enter a number between 0 and 10.")



    # Retorna os parâmetros para serem usados na função student_process
    return students_quantity, calculation_type, passing_grade, weights_marks
