class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []
        self.final_mark = 0
        self.condition = ''

    def calculate_media_arithmetic(self):
        if self.marks:
            return sum(self.marks) / len(self.marks)
        else:
            print('Nenhuma nota foi inserida.')
        return 0
    

    # def calculate_weighted_media(marks, weigthted_marks):
#     if marks:

    #formula media ponderada, recebendo os pesos como parametro, setar na class 
#         print('Nenhuma nota foi inserida.')
#         return 0
#     else: 

    
    def check_condition(self):
        return 'Aprovado' if self.final_mark >= 7 else 'Reprovado'
