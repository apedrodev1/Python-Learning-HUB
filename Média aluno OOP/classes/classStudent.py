class Student:
    def __init__(self, name, passing_mark):
        self.name = name
        self.passing_mark = passing_mark
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
        return 'Aprovado' if self.final_mark >= self.passing_mark else 'Reprovado'
