# Modules imported
from src.functions.parameters import get_main_parameters
from src.functions.main_function import process_students
from src.functions.show_students import display_students
from src.functions.edit_data.edit_student import edit_student_data 
from src.functions.loop_control import ask_to_retry

print("🎓 Welcome to the Grade Calculation System 🎓\n")

def main():
    """
    Main function that controls the flow of the program. It requests initial parameters, 
    processes the students' data, and displays the results.
    """
    
    while True:
        # Get the main parameters from the user (number of students, type of average, etc.)
        students_quantity, way_to_calculate, passing_grade, weights, number_of_marks = get_main_parameters()

        # Process the students' data
        students_list = process_students(
            students_quantity,
            way_to_calculate,
            passing_grade,
            weights,
            number_of_marks
        )

        # Display the students' report
        display_students(students_list)
        
        # Ask to edit one or mutiples students
        edit_student_data(students_list)

        # Ask the user if they want to run the program again
        if not ask_to_retry():
            break

    # Future features:
    # - Export data to formats like CSV, JSON, or XML
    # - test_validations.py
    # - Send the results via email
    # - Add graphs or other types of reports
    

if __name__ == "__main__":
    main()
