import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# MPODE SER MÉTODO NA CLASSE STUDENT
def calculate_media(marks):
    if marks:
        return sum(marks) / len(marks)
    else:
        print('Nenhuma nota foi inserida.')
        return 0
    


# def calculate_weighted_media(marks, weigthted_marks):
#     if marks:

    #formula media ponderada, recebendo os pesos como parametro, setar na class 
#         print('Nenhuma nota foi inserida.')
#         return 0
#     else: 

# MPODE SER MÉTODO NA CLASSE STUDENT
def check_condition(final_mark):
    return 'Aprovado' if final_mark >= 7 else 'Reprovado'