from src.classes.Student import Student
from ..functions.validations import validate_grade, validate_names

def process_students(students_quantity, way_to_calculate, passing_grade, weights): 
    is_weighted = True if way_to_calculate == "1" else False

    student_list = []

    for i in range(students_quantity):
        print(f"\n📘 Student {i+1}")

        # Validação do nome
        while True:
            name = input("Enter student name: ")
            if validate_names(name):  # Valida se o nome contém apenas letras
                break
            else:
                print("❌ Invalid name. Please enter a valid name (letters only).")

        # Validação das notas
        marks = []
        num_marks = len(weights) if is_weighted else int(input("How many grades will be entered? "))

        for j in range(num_marks):
            while True:
                mark_input = input(f"Enter grade {j+1}: ")
                mark = validate_grade(mark_input)  # Valida se a nota está entre 0 e 10
                if mark is not None:
                    marks.append(mark)
                    break
                else:
                    print("❌ Invalid grade. Please enter a valid number between 0 and 10.")

        # Criando o estudante com as notas e pesos
        student = Student(name, passing_grade, weights if is_weighted else [], is_weighted)
        student.add_marks(marks)  # Adiciona as notas ao estudante
        student.check_condition()  # Verifica a condição do aluno (se passou ou não)

        student_list.append(student)

    return student_list
