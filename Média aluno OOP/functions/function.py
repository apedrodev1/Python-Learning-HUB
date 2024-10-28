import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def fill_marks(self):
        try:
            qtd_marks = int(input('Quantas notas deseja inserir? ')) #letra entra tbm, rever 
            for i in range(1, qtd_marks + 1):
                while True:
                    try:
                        nota = float(input(f'Digite a nota {i} de {self.name}: ')) #valores negativos entram, criar verificacao 
                        self.marks.append(nota)
                        break
                    except ValueError:
                        print("Por favor, insira um número válido.")
            self.final_mark = calculate_media_arithmetic(self.marks)
            self.condition = check_condition(self.final_mark)
        except ValueError:
            print("Por favor, insira um número válido.")
            
# MPODE SER MÉTODO NA CLASSE STUDENT
def calculate_media_arithmetic(marks):
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