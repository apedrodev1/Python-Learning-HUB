from src.classes.Student import Student
# from ..functions.show_students import display_students ver depois, introduzir no final da funcao 
from ..functions.validations import (
    validate_grade,
    validate_names, 
    validate_quantity
)

def process_students(students_quantity, way_to_calculate, passing_grade, weights):
    '''
    Receives the name and grades (and weights, if the average is weighted),
    and creates a Student object from the Student class.

    Args:
        students_quantity (int): Number of students to process.
        way_to_calculate (str): Calculation method ("1" for weighted).
        passing_grade (float): Minimum average required to pass.
        weights (list): List of weights for grades if weighted average is chosen.

    Returns:
        list: A list containing all processed Student objects.
    '''

    # Defines if the calculation will be weighted based on the user's choice
    is_weighted = True if way_to_calculate == "1" else False

    # List to store all Student objects
    student_list = []

    # Loop to process each student
    for i in range(students_quantity):
        student_id = i+1 
        print(f"\n📘 Student {i+1}")

        # Validation of the student's name
        while True:
            name_input = input("Enter student's name: ")
            name, error = validate_names(name_input)
            if error:
                print(f'❌ {error}')
            else:
                break

        # Validation and input of grades
        marks = []

        # Define the number of grades based on the calculation type
        if is_weighted:
            num_marks = len(weights)  # If weighted, the number of grades must match the weights
        else:
            # If arithmetic, ask the user how many grades will be entered
            while True:
                marks_input = input("How many grades will be entered? ")
                num_marks, error = validate_quantity(marks_input)  # Uses validation to ensure a positive integer
                if error:
                    print(f'❌ {error}')
                else:
                    break

        # Loop to receive the student's grades
        for j in range(num_marks):
            while True:
                mark_input = input(f"Enter grade {j+1}: ")
                mark, error = validate_grade(mark_input)  # Validates if the grade is between 0 and 10
                if error: 
                    print(f'❌ {error}')
                else:
                    marks.append(mark)
                    break

        # Creates the Student object with the provided data
        student = Student(student_id, name, passing_grade, weights if is_weighted else [], is_weighted)
        student.add_marks(marks)         # Adds grades to the student
        student.check_condition()        # Checks if the student passed based on the average

        # Adds the student to the main list
        student_list.append(student)

    # Returns the list with all processed students
    return student_list
