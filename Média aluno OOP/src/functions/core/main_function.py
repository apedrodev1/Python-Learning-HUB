"""
Handles the core logic for processing and creating new students.

This module is responsible for the user-facing workflow of gathering
student data (name, grades), instantiating Student objects, 
applying Classroom rules, and persisting them via the repository.
"""

from ...utils.validations import (
    validate_grade,
    validate_names
)
from ...classes.Student import Student

def process_students(classroom, students_quantity, number_of_marks, repository):
    """
    Gathers data for new students, calculates their results using the 
    Classroom context, and saves them.

    Iterates 'students_quantity' times. For each student, it:
    1. Prompts for name and grades.
    2. Instantiates a Student object.
    3. Asks the Classroom to calculate the student's average and condition.
    4. Passes the fully processed Student object to the repository.

    Args:
        classroom (Classroom): The context object containing rules (weights, calc_type).
        students_quantity (int): The total number of new students to process.
        number_of_marks (int): The number of grades to ask for (only used if 
                               classroom is NOT weighted).
        repository (Repository): The repository object for database access.

    Returns:
        None
    """

    # 1. Determine exactly how many grades to ask for based on the Classroom
    # If the classroom is weighted, the number of grades MUST match the weights.
    if classroom.calc_type == "1":  # Weighted
        num_marks_to_collect = len(classroom.weights)
    else:
        # Arithmetic ("0") or Median ("2")
        num_marks_to_collect = number_of_marks

    for i in range(students_quantity): 
        print(f"\n📘 Inserting Student {i+1} of {students_quantity}")
    
        # 2. Get and Validate Name
        while True:  # Talvez refatorar usando o utils/input_helpers.py
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
        
        # 4. Create and Process the Student Object (OOP Logic)
        try:
            # Instantiate the Dumb Class
            # ID is None because it hasn't been saved to DB yet
            new_student = Student(student_id=None, name=name)
            
            # Set the marks (The Student class will validade the list)
            new_student.marks = marks_input_list
            
            # The Magic: Classroom applies the rules to the Student
            classroom.calculate_student(new_student)
            
            # 5. Save to Repository
            # We pass the full object. The repository will handle extracting
            # name, marks, average, and condition to save to SQLite.
            repository.add_student(new_student)
            
            print(f"✅ Student {new_student.name} saved! "
                  f"(Avg: {new_student.final_average} - {new_student.condition})")
        
        except Exception as e:
            print(f'❌ Unexpected error saving student {name}: {e}')