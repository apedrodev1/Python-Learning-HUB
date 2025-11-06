"""
Main entry point for the Student Grade Calculation System.

This script initializes the application, connects to the database,
and runs the main user interaction loop. It orchestrates the flow
of the program, calling functions for parameter setup, student
processing, editing, and exporting.
"""

import os
from src.functions.parameters import get_main_parameters
from src.functions.main_function import process_students
from src.functions.data.manage_students import edit_student_edits
from src.functions.export.export_wrapper import export_students 
from src.functions.loop_control import ask_to_retry
from src.functions.show_students import display_students 
from src.db.repository import StudentRepository 

# --- Database Path Setup ---
# Get the absolute path of the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
# Create a reliable path to the database file
DB_PATH = os.path.join(BASE_DIR, 'src', 'db', 'db_files', 'banco_de_dados.db') 
# ---------------------------------------------------------

print("🎓 Welcome to the Grade Calculation System 🎓\n")

def main():
    """
    Runs the main application logic.

    This function handles:
    1.  Connecting to the database by initializing the StudentRepository.
    2.  Running the main loop (while True).
    3.  Orchestrating the calls to get parameters, process new students,
        display all students, manage edits, and handle exports.
    4.  Ensuring the database connection is closed properly on exit.
    """
    
    try:
        # Try to create the repository instance.
        # This also creates the tables if they don't exist.
        repo = StudentRepository(DB_PATH) 
    except Exception as e:
        print(f"❌ Critical error! to connect to the database: {e}")
        print("Finalizing the program...")
        return # finish the program if DB connection fails
    # --------------------------------------------------

    # This 'try...finally' block ensures that the database connection
    # is *always* closed when the program exits, even if an error occurs.
    try:
        # --- Main Loop of the Program ---
        while True:
            # Get the main parameters from the user
            students_quantity, way_to_calculate, passing_grade, weights, number_of_marks = get_main_parameters()

            # Process and add new students to the database
            process_students(
                students_quantity,
                way_to_calculate,
                passing_grade, 
                weights,
                number_of_marks,
                repository=repo 
            )
            
            # SELECT ALL students from the database
            students_list = repo.get_all_students() 

            # Sort list alphabetically by name
            students_list.sort(key=lambda s: s.name)
            
            # Show the complete, updated student list
            display_students(students_list) 

            # Run the edit/delete/update workflow
            edit_student_edits(students_list, repo) 
            
            # Ask if the User wants to export the data
            export_students(students_list)

            # Ask the user if they want to run the program again
            if not ask_to_retry():
                break
    
    finally:
        # --- Close DB conection ---
        print("\n👋 Closing database connection...")
        repo.close()
    # ---------------------------------------

if __name__ == "__main__":
    main()