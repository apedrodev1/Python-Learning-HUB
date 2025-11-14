"""
Main entry point for the Student Grade Calculation System.

This script initializes the application, connects to the database,
and runs the main user interaction loop. It orchestrates the flow
of the program, calling functions for parameter setup, student
processing, editing, and exporting.
"""

from src.db.db_manager import setup_repository
from src.functions.core.parameters import get_app_parameters
from src.functions.core.main_function import process_students
from src.functions.data.student_selector import prompt_for_selection
from src.functions.export.export_wrapper import export_students 
from src.functions.core.loop_control import ask_to_retry
from src.functions.core.show_students import display_students 

# Importamos a classe para criar uma default caso carreguemos um DB existente
from src.classes.Classroom import Classroom 

print("🎓 Welcome to the Grade Calculation System 🎓\n")

def main():
    """
    Runs the main application logic using the new Classroom architecture.
    """
    
    # 1. Setup Repository
    # We assume setup_repository handles the initial connection logic
    try:
        # Initializing the repository
        repo, is_new_db = setup_repository()
        if repo is None:  # User chose to exit in the setup menu
            print("\n👋 Program finished.")
            return
    except Exception as e:
        print(f"❌ Critical error connecting to database: {e}")
        return

    # 2. Start the Context Manager block
    # This replaces the need for 'finally: repo.close()'
    # The repo (or its internal connection) will close automatically at the end of this block.
    with repo: 
        
        classroom = None
        
        # --- Scenario A: New Database ---
        if is_new_db:
            print("\n✨ New Database detected. Let's configure your Classroom.")
            # Get parameters returns the configured Classroom object
            classroom, students_qty, num_marks = get_app_parameters()
            
            # Process new students using the rules from 'classroom'
            process_students(classroom, students_qty, num_marks, repo)

        # --- Scenario B: Existing Database ---
        else:
            print("\nrz Existing Database loaded.")
            # TODO: In a future version, we should load Classroom config from DB.
            # For now, we create a default classroom or ask user for rules 
            # if we want to recalculate. 
            # Let's assume a default Arithmetic classroom for viewing:
            print("⚠️  Using default Arithmetic rules for viewing.")
            classroom = Classroom(name="Loaded Class", calc_type="0") 


        # 3. Main Interaction Loop
        while True:
            
            # --- Hydration Step (CRUCIAL) ---
            # 1. Get raw students from DB
            students_list = repo.get_all_students()
            
            # 2. If list is not empty, we MUST calculate their status based on current Classroom rules
            if students_list:
                for student in students_list:
                    classroom.calculate_student(student)
                
                # Sort alphabetically
                students_list.sort(key=lambda s: s.name)
            
            # --- Display & CRUD ---
            
            # Show the complete list (now populated with averages)
            display_students(students_list) 

            # Run the edit/delete/update workflow
            # Note: If we edit a student here, we might need to pass 'classroom' 
            # inside if we want immediate recalculation, or just rely on the loop re-hydrating.
            did_edit = prompt_for_selection(students_list, repo) 
            
            # Ask if the User wants to export the data
            export_students(students_list)

            # Ask to retry
            if not ask_to_retry():
                print("\n👋 Program finished. See you next time!")
                break
    
    # End of 'with repo': Connection is closed automatically here.

if __name__ == "__main__":
    main()