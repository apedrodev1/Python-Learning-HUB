
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def fill_marks(self):
    try:
        qtd_marks = int(input('Quantas notas deseja inserir? '))
        for i in range(1, qtd_marks + 1):
            while True:
                try:
                    nota = float(input(f'Digite a nota {i} de {self.name}: '))
                    self.marks.append(nota)
                    break
                except ValueError:
                    print("Por favor, insira um número válido.")
        self.final_mark = self.calculate_media_arithmetic()  
        self.condition = self.check_condition()  
    except ValueError:
        print("Por favor, insira um número válido.")
