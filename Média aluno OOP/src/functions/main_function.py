from src.classes.Student import Student
from ..functions.validations import (
    validate_grade,
    validate_names, 
    validate_quantity
)

def process_students(students_quantity, way_to_calculate, passing_grade, weights, number_of_marks, repository):
    '''
    Processes student data and returns a list of Student objects.

    Args:
        students_quantity (int): Number of students to process.
        way_to_calculate (str): Calculation method ("1" for weighted).
        passing_grade (float): Minimum average required to pass.
        weights (list): List of weights for grades if weighted average is chosen.
        number_of_marks(int): total of marks per student, if arithmetic is chosen.
        repository (Repository): The repository to update student data.

    Returns:
        None
    '''

    is_weighted = way_to_calculate == "1"

    for i in range(students_quantity): 
        print(f"\n📘 Inserting Student {i+1} of {students_quantity}")
      
        # Validate student name
        while True:
            name_input = input("Enter student's name: ")
            name, error = validate_names(name_input)
            if error:
                print(f'❌ {error}')
            else:
                break

        # Determine number of grades to collect
        if is_weighted:
            num_marks = len(weights)
        else:
            num_marks = number_of_marks

        # Collect grades
        marks_input_list = [] 
        for j in range(num_marks):
            while True:
                mark_input = input(f"Enter grade {j + 1}: ")
                mark, error = validate_grade(mark_input)
                if error: 
                    print(f'❌ {error}')
                else:
                    marks_input_list.append(mark)
                    break
        
        # This inner try/except block is correct and handles creation
        try:
            student = Student(
                student_id=None, # ID will be set by the DB
                name=name, 
                passing_grade=passing_grade, 
                weights_marks=weights if is_weighted else [], 
                is_weighted=is_weighted
            )
            
          
            student.marks = marks_input_list 
            repository.add_student(student)
        
        except ValueError as e:
            print(f'❌ Erro ao validar dados do aluno: {e}')
        except Exception as e:
            print(f'❌ Erro inesperado ao salvar aluno {name}: {e}')