"""
Main entry point for the Student Grade Calculation System.

This script initializes the application, connects to the database,
and runs the main user interaction loop. It orchestrates the flow
of the program, calling functions for parameter setup, student
processing, editing, and exporting.
"""
 
from src.db.db_manager import DatabaseManager
from src.functions.core.parameters import get_main_parameters
from src.functions.core.main_function import process_students
from src.functions.data.student_selector import prompt_for_selection
from src.functions.export.export_wrapper import export_students 
from src.functions.core.loop_control import ask_to_retry
from src.functions.core.show_students import display_students 


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
    
    repo = None
    is_new_db = False

    try:
        # Initializing the repository
        repo, is_new_db = setup_repository()
    
        # Verifies if the user has left
        if repo is None:
            print("\n👋 Program finished.")
            return #Finish main()
        
    except Exception as e:
        print(f"❌ Critical error! to connect to the database: {e}")
        print("Finalizing the program...")
        return # Finish the program if setup_repository fail


    # SELECT ALL students from the database
    students_list = repo.get_all_students() 

    # Sort list alphabetically by name
    students_list.sort(key=lambda s: s.name)


    # --- Main Loop of the Program ---
    try:
        if is_new_db:
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

        while True:
                 
            # Show the complete, updated student list
            display_students(students_list) 

            # Run the edit/delete/update workflow
            prompt_for_selection(students_list, repo) 
            
            # Ask if the User wants to export the data
            export_students(students_list)

            # Ask the user if they want to run the program again
            if not ask_to_retry():
                break
    
    finally:
        # --- Close DB conection ---
        repo.close()
    # ---------------------------------------

if __name__ == "__main__":
    main()