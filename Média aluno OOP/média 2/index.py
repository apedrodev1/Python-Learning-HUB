#modulos:

from src.functions.parameters import get_main_parameters
from src.functions.main_function import process_students
from src.functions.show_students import display_students
from src.functions.loop_control import ask_to_retry


print("🎓 Bem-vindo ao Sistema de Cálculo de Médias 🎓\n")

def main():
    while True:
            students_quantity, way_to_calculate, passing_grade, weights = get_main_parameters() 
            students_list = process_students(students_quantity, way_to_calculate, passing_grade, weights)
            display_students(students_list)
            
            if not ask_to_retry():
                 break
        
        
        # Futuras funcionalidades

        # editar notas e alunos via ID
        # export_data(students_list)
        # enviar para email
        
        


if __name__ == "__main__":
    main()
