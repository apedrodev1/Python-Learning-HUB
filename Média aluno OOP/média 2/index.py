#modulos
from src.functions.parameters import get_main_parameters
from src.functions.main_function import process_students
#from src.functions.exporter import export_data


print("🎓 Bem-vindo ao Sistema de Cálculo de Médias 🎓\n")

def main():
    students_quantity, way_to_calculate, passing_grade, weights = get_main_parameters() ##crashando ao passar argumentos
    students_list = process_students(students_quantity, way_to_calculate, passing_grade, weights)
    
#funcao export_data export_data(students_list)
#funcao enviar para o email 
#funcao imprimir na tela




if __name__ == "__main__":
    main()








(input(print('Deseja rodar de novo')))

#if no mensagem de fim do programa  


