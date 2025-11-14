"""
Handles user input for application parameters.

This module gathers configuration settings (like calculation type,
passing grade, and weights) and encapsulates them into a Classroom object.
"""

from ...utils.input_handler import get_valid_input
from ...utils.validations import (
    validate_quantity,
    validate_calculation_type,
    validate_grade,
    validate_weights,
    validate_quantity_min_2,
    validate_names
)
# Importamos a classe para poder instanciá-la aqui
from ...classes.Classroom import Classroom

def get_app_parameters():
    """
    Prompts the user for necessary parameters to set up the Classroom
    and the data entry session.

    Returns:
        tuple: (
            classroom (Classroom): The configured Classroom object.
            students_quantity (int): Number of students to insert.
            number_of_marks (int): Number of marks per student (for Arithmetic/Median).
        )
    """
    print("\n--- ⚙️  Configuration Setup ⚙️  ---")

    # 1. Get Classroom Name (Optional, but good for the object)
    # We can validate it just like a student name for simplicity
    name_input, _ = get_valid_input("Enter the Classroom Name: ", validate_names)
    
    # 2. How many students to add?
    students_qty_str, _ = get_valid_input(
        "How many students do you want to add? ", 
        validate_quantity
    )
    students_quantity = int(students_qty_str)

    # 3. Calculation Method
    print("\nChoose calculation type:")
    print("0: Arithmetic Mean (Média Aritmética)")
    print("1: Weighted Mean (Média Ponderada)")
    print("2: Median (Mediana)")
    
    calc_type, _ = get_valid_input("Type the number of option: ", validate_calculation_type)

    # 4. Passing Grade
    passing_grade_str, _ = get_valid_input(
        "Enter the passing grade (0-10): ", 
        validate_grade
    )
    passing_grade = float(passing_grade_str)

    # 5. Specific Logic for Weights vs Quantity
    weights = []
    number_of_marks = 0

    if calc_type == '1':  # Weighted
        print("\n⚖️  Weighted Average Selected.")
        print("Enter weights separated by space (e.g., '2 3 5'). Sum must be 10.")
        while True:
            w_input = input("Weights: ")
            w_list, error = validate_weights(w_input)
            if error:
                print(f"❌ {error}")
            else:
                weights = w_list
                break
        # In weighted, number of marks = number of weights
        number_of_marks = len(weights)
        
    else:  # Arithmetic or Median
        qty_marks_str, _ = get_valid_input(
            "How many grades per student? (min 2): ", 
            validate_quantity_min_2
        )
        number_of_marks = int(qty_marks_str)

    # --- INSTANTIATING THE CLASSROOM ---
    # Agora criamos o objeto que detém as regras
    classroom = Classroom(
        name=name_input,
        passing_grade=passing_grade,
        calc_type=calc_type,
        weights=weights
    )

    return classroom, students_quantity, number_of_marks