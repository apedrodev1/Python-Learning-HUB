"""
Handles the core logic for processing and creating new students.

This module is responsible for the user-facing workflow of gathering
student data (name, grades) and persisting it to the database
via the repository.
"""

from src.classes.Student import Student
from ..functions.validations import (
    validate_grade,
    validate_names, 
    validate_quantity
)

def process_students(students_quantity, way_to_calculate, passing_grade, weights, number_of_marks, repository):
    """
    Gathers data for a specified number of new students and saves them.

    Iterates 'students_quantity' times, prompting the user for a name
    and the required number of grades. It validates this input
    and then uses the provided repository to create and save each
    new Student object to the database.

    Args:
        students_quantity (int): The total number of new students to process.
        way_to_calculate (str): The calculation method ("0" or "1").
        passing_grade (float): The minimum grade required to pass.
        weights (list): A list of weights (if 'is_weighted' is True).
        number_of_marks (int): The number of grades per student (if arithmetic).
        repository (StudentRepository): The repository object for database access.

    Returns:
        None
    """

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
        
        # Create the Student object and save it to the database
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
            print(f'❌ Error validating student data: {e}')
        except Exception as e:
            print(f'❌ Unexpected error saving student {name}: {e}')