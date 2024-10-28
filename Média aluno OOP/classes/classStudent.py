class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []
        self.final_mark = 0
        self.condition = ''

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

    
    def check_condition(final_mark):
        return 'Aprovado' if final_mark >= 7 else 'Reprovado'