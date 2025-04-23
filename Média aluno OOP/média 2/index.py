#modulos:

from src.functions.parameters import get_main_parameters
from src.functions.main_function import process_students
from src.functions.loop_control import ask_to_retry


print("🎓 Bem-vindo ao Sistema de Cálculo de Médias 🎓\n")

def main():
    while True:
            students_quantity, way_to_calculate, passing_grade, weights = get_main_parameters() 
            students_list = process_students(students_quantity, way_to_calculate, passing_grade, weights)
        # Futuras funcionalidades
        # export_data(students_list)
        # enviar para email
        # imprimir resultados na tela
        # editar notas e alunos via ID

            print(students_list)

            retry = input("\n🔁 Deseja rodar o programa novamente? (s/n): ").lower() #usar a funcao
            if retry != 's':
                print("\n👋 Programa finalizado. Até a próxima!")
                break

if __name__ == "__main__":
    main()
