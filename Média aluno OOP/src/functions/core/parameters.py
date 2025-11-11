"""
Handles the initial parameter setup for the application.

This module is responsible for the user-facing workflow of gathering
the initial batch of settings (like student quantity, average type,
and passing grade) and persisting them to the database using the
repository.
"""

import json
import os
from ...utils.validations import (
    validate_quantity,
    validate_calculation_type,
    validate_weights,
    validate_grade,
    validate_quantity_min_2
)


def get_app_parameters(repo):
    """
    Prompts the user for classroom settings and saves them to the DB.

    This function acts as a setup wizard. It checks if the classroom
    configuration (calc_type, passing_grade, weights) already exists
    in the database.
    
    - If NOT exists (New DB): It asks the user for the rules, saves
      them to the 'classroom_config' table, and then asks for the
      number of students to add immediately.
    - If exists (Existing DB): It skips the rule setup.

    Args:
        repo (Repository): The repository instance to interact with the DB.

    Returns:
        tuple: A tuple containing:
            (students_quantity (int),
             way_to_calculate (str),
             passing_grade (float),
             weights (list),
             number_of_marks (int))
    """
    # 1. Get context (Classroom Name) 
    classroom_name = os.path.basename(repo.db_manager.db_path)

    # 2. Check if config already exists in DB
    current_calc_type = repo.get_classroom_config("calc_type")
    
    # Default values (will be overwritten if not found in DB)
    weights = []
    number_of_marks = 0
    
    # --- Scenario A: Configuration already exists (Load mode) ---
    if current_calc_type is not None:
        # We just need to read them to return to the main flow
        # (The repository already has them, but index.py expects returns here for now)
        way_to_calculate = current_calc_type
        passing_grade = float(repo.get_classroom_config("passing_grade"))
        weights = json.loads(repo.get_classroom_config("weights_marks"))
        number_of_marks = len(weights)
        
        # We don't ask to add students automatically when loading.
        # We return 0 so the main loop simply shows the menu.
        return 0, way_to_calculate, passing_grade, weights, number_of_marks

    # --- Scenario B: Configuration does NOT exist (New DB mode) ---
    
    print(f"\n⚙️  Setting up rules for classroom: {classroom_name}")

    # 1. Calculation Type
    while True:
        calc_type_input = input(
            'Would you like to use arithmetic or weighted average? '
            '(Enter 0 for arithmetic, 1 for weighted, 2 for median): '
        )
        way_to_calculate, error = validate_calculation_type(calc_type_input)
        if error:
            print(f"❌ {error}")
        else:
            break

    # 2. Weights or Number of Marks
    if way_to_calculate == "1":
        while True:
            weights_input = input(
                'Enter the weights for each grade, separated by spaces (e.g., 2 3 1 4). '
                'The total must equal 10: '
            )
            weights, error = validate_weights(weights_input)
            if error:
                print(f"❌ {error}")
            else:
                number_of_marks = len(weights)
                break
    else:
        # For arithmetic (0) or median (2), we create "dummy" weights of 1.0
        # to define the structure of the grades in the DB.
        while True:
            marks_input = input(f"How many grades will the students in '{classroom_name}' have? ")
            number_of_marks, error = validate_quantity_min_2(marks_input)
            if error:
                print(f"❌ {error}")
            else:
                weights = [1.0] * number_of_marks
                break

    # 3. Passing Grade
    while True:
        passing_input = input("Enter the minimum passing grade (0 to 10): ")
        passing_grade, error = validate_grade(passing_input)
        if error:
            print(f"❌ {error}")
        else:
            break

    # 4. Save Configuration to DB 
    print("💾 Saving classroom configuration...")
    try:
        repo.set_classroom_config("calc_type", way_to_calculate)
        repo.set_classroom_config("passing_grade", str(passing_grade))
        repo.set_classroom_config("weights_marks", json.dumps(weights))
        print("✅ Configuration saved successfully.")
    except Exception as e:
        print(f"❌ Error saving configuration: {e}")

    # 5. Ask for initial students (only for new setup)
    while True:
        user_input = input(f'\nHow many students do you want to add to {classroom_name} now? ')
        students_quantity, error = validate_quantity(user_input)
        if error:
            print(f"❌ {error}")
        else:
            break

    return students_quantity, way_to_calculate, passing_grade, weights, number_of_marks