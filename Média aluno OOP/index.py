import os   
from src.functions.parameters import get_main_parameters
from src.functions.main_function import process_students
from src.functions.data.manage_students import edit_student_edits
from src.functions.export.export_wrapper import export_students 
from src.functions.loop_control import ask_to_retry
from src.functions.show_students import display_students    
from src.bd.repository import StudentRepository     

# --- BD PATH ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
DB_PATH = os.path.join(BASE_DIR, 'src', 'bd', 'banco_de_dados.db') 
# ---------------------------------------------------------

print("🎓 Welcome to the Grade Calculation System 🎓\n")

def main():
         """
         Main function that controls the flow of the program. It requests initial parameters, 
         processes the students' data, and displays the results.
         """
    
         try:
              # Try to create the repository instance.
              # Create the table if not exists already.
              repo = StudentRepository(DB_PATH) 
         except Exception as e:
              print(f"❌ Critical error! to connect to the database: {e}")
              print("Finalizing the program...")
              return  # finish the program if DB connection fails
         # --------------------------------------------------

    # --- INDENTATION FIX ---
    # This entire 'try...finally' block was moved one level to the left.
    # It must be aligned with the 'try' block above, not nested inside its 'except'.
         try:
              # --- Main Loop of the Program ---
              while True:
                       # Get the main parameters from the user (number of students, type of average, etc.)
                       students_quantity, way_to_calculate, passing_grade, weights, number_of_marks = get_main_parameters()

                       # Process the students' data and get the list of Student objects
                       process_students(
                            students_quantity,
                            way_to_calculate,
                            passing_grade, 
                            weights,
                            number_of_marks,
                            repository=repo     
                       )
                       
                       # SELECT ALL (DQL)
                       students_list = repo.get_all_students() 
                       
                       # Show the student's list.
                       display_students(students_list) 

                       # RUD (without Create) - Edit students
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