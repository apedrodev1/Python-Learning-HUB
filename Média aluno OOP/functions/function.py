import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def fill_marks(self):
    while True:
        try:
            qtd_marks = int(input('Quantas notas deseja inserir? '))
            if qtd_marks > 0:
                break
            else: 
                print('Por favor, insira um número inteiro positivo.')

        except ValueError: 
            print ('Por favor, insira um número válido.')
    
    for i in range(1, qtd_marks + 1):
        while True: 
            try:
                grade = float(input(f'Digite a nota {i} de {self.name}: ')) #trocar nota para outro nome mark confudiria, achar sinonimo
                if 0 <= grade <= 10:
                    self.marks.append(grade)
                    break

                else:
                     print("Por favor, insira um número entre 0 e 10.")

            except ValueError:
                print("Por favor, insira um número válido.")



    self.final_mark = self.calculate_media_arithmetic()  
    self.condition = self.check_condition()