class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []
        self.final_mark = 0
        self.condition = ''

    
    def fillMarks(self):
        try:
            qtd_marks = int(input('Quantas notas deseja inserir? '))
            i = 0
            for _ in range(qtd_marks):
                i += 1 
                while True:
                    #remover os inputs apos entrada dos dados - fazer
                    try:
                        nota = float(input(f'Digite a nota {i} de {self.name}: '))
                        self.marks.append(nota)
                        break
                    except ValueError:
                        print("Por favor, insira um número válido.")
            self.calcMedia()  
        except ValueError:
            print("Por favor, insira um número válido.")    


    def calcMedia(self):
        if self.marks:
            self.final_mark = sum(self.marks) / len(self.marks)

            if self.final_mark >= 7:
                self.condition = 'Aprovado'
            else:
                self.condition = 'Reprovado'

            return self.condition
        else:
            print('Nenhuma nota foi inserida.')
            return None
