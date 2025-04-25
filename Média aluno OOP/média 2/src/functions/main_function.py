from src.classes.Student import Student
from ..functions.validations import (
    validate_grade,
    validate_names, 
    validate_quantity
)


def process_students(students_quantity, way_to_calculate, passing_grade, weights): 
    # Define se o cálculo será ponderado com base na escolha do usuário
    is_weighted = True if way_to_calculate == "1" else False

    # Lista para armazenar todos os objetos Student
    student_list = []

    # Loop para processar todos os estudantes
    for i in range(students_quantity):
        print(f"\n📘 Student {i+1}")

        # Validação do nome do estudante
        while True:
            name_input = input("Enter student name: ")
            name, error = validate_names(name_input)
            if error:
                print(f'❌ {error}')
            else:
                break


        # Validação e entrada das notas
        marks = []

        # Define a quantidade de notas com base no tipo de cálculo
        if is_weighted:
            num_marks = len(weights)  # Se for ponderado, o número de notas deve bater com os pesos
        else:
            # Se for aritmético, pergunta ao usuário quantas notas deseja inserir
            while True:
                marks_input = input("How many grades will be entered? ")
                num_marks, error = validate_quantity(marks_input)  # Usa validação para garantir número inteiro positivo
                if error:
                    print(f'❌ {error}')
                else:
                    break

        # Loop para receber as notas do estudante
        for j in range(num_marks):
            while True:
                mark_input = input(f"Enter grade {j+1}: ")
                mark, error = validate_grade(mark_input)  # Valida se a nota está entre 0 e 10
                if error: 
                    print(f'❌ {error}')
                else:
                    marks.append(mark)
                    break

        
        print('📊 Notas armazenadas:', marks)
        # Cria o objeto Student com os dados fornecidos
        student = Student(name, passing_grade, weights if is_weighted else [], is_weighted)
        student.add_marks(marks)         # Adiciona as notas ao estudante
        student.check_condition()        # Verifica se o estudante passou com base na média

        # Adiciona o estudante à lista principal
        student_list.append(student)

    # Retorna a lista com todos os estudantes processados
    return student_list
