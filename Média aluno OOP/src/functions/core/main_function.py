"""
Handles the core logic for processing and creating new students.

This module is responsible for the user-facing workflow of gathering
student data (name, grades) and persisting it to the database
via the repository.
"""

from ...utils.validations import (
    validate_grade,
    validate_names
)

def process_students(students_quantity, way_to_calculate, passing_grade, weights, number_of_marks, repository):
    """
    Gathers data for a specified number of new students and saves them.

    Iterates 'students_quantity' times, prompting the user for a name
    and the required number of grades. It validates this input
    and then uses the provided repository to create and save the
    raw student data directly to the database.

    Args:
        students_quantity (int): The total number of new students to process.
        way_to_calculate (str): The calculation method (used to determine grade count).
        passing_grade (float): Unused here (kept for signature compatibility).
        weights (list): List of weights (used to determine count if weighted).
        number_of_marks (int): The number of grades per student (if arithmetic).
        repository (Repository): The repository object for database access.

    Returns:
        None
    """

    # 1. Determine exactly how many grades to ask for
    # We do this once before the loop to keep logic clean.
    if way_to_calculate == "1":  # Weighted
        num_marks_to_collect = len(weights)
    else:
        # Arithmetic ("0") or Median ("2")
        num_marks_to_collect = number_of_marks

    for i in range(students_quantity): 
        print(f"\n📘 Inserting Student {i+1} of {students_quantity}")
    
        # 2. Get and Validate Name
        while True:
            name_input = input("Enter student's name: ")
            name, error = validate_names(name_input)
            if error:
                print(f'❌ {error}')
            else:
                break

        # 3. Get and Validate Grades
        marks_input_list = [] 
        for j in range(num_marks_to_collect):
            while True:
                mark_input = input(f"Enter grade {j + 1}: ")
                mark, error = validate_grade(mark_input)
                if error: 
                    print(f'❌ {error}')
                else:
                    marks_input_list.append(mark)
                    break
        
        # 4. Save directly to Repository (Phase 3 Logic)
        # We no longer create a Student object here. We pass raw data.
        # This avoids the "double validation" issue.
        try:
            repository.add_student(name, marks_input_list)
        
        except Exception as e:
            print(f'❌ Unexpected error saving student {name}: {e}')