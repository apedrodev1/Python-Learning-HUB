from functions.function import calculate_media, check_condition

class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []
        self.final_mark = 0
        self.condition = ''

    # PODE SER FUNCTION STANDALONE 
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
            self.final_mark = calculate_media(self.marks)
            self.condition = check_condition(self.final_mark)
        except ValueError:
            print("Por favor, insira um número válido.")