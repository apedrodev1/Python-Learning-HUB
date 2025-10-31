from src.classes.Student import Student
from ..functions.show_students import display_students
from ..utils.helpers import generate_student_ids
from ..functions.validations import (
    validate_grade,
    validate_names, 
    validate_quantity
)

def process_students(students_quantity, way_to_calculate, passing_grade, weights, number_of_marks):
    '''
    Processes student data and returns a list of Student objects.

    Args:
        students_quantity (int): Number of students to process.
        way_to_calculate (str): Calculation method ("1" for weighted).
        passing_grade (float): Minimum average required to pass.
        weights (list): List of weights for grades if weighted average is chosen.
        number_of_marks(int): total of marks per student, if arithmetic is chosen.

    Returns:
        list: A list containing all processed Student objects.
    '''

    is_weighted = way_to_calculate == "1"
    student_list = []

        # Initialize the ID generator
    id_generator = generate_student_ids(start=1)

    for _ in range(students_quantity): 
        
        # Call the ID generator for first time
        student_id = next(id_generator) 

        print(f"\n📘 Student {student_id}")

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
        marks = []
        for j in range(num_marks):
            while True:
                mark_input = input(f"Enter grade {j + 1}: ")
                mark, error = validate_grade(mark_input)
                if error: 
                    print(f'❌ {error}')
                else:
                    marks.append(mark)
                    break

        # Create and process Student
        student = Student(student_id, name, passing_grade, weights if is_weighted else [], is_weighted)
        try:
            student.marks = marks
        except ValueError as e:
            print(f'❌ Unexpected error {e}')
            
        student_list.append(student)

    display_students(student_list) 

    return student_list