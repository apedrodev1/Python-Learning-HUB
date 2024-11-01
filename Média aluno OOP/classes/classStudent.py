class Student:
    def __init__(self, name, passing_mark):
        self.name = name
        self.passing_mark = passing_mark
        self.marks = []
        self.weighted_marks = []
        self.final_mark = 0
        self.condition = ''

    def calculate_media_arithmetic(self):
        if self.marks:
            return sum (self.marks * self.weigthted_marks) / len(self.marks)

    
        print('Nenhuma nota foi inserida.')
        return 0 
    

    def calculate_weighted_media(self):
        if self.marks and self.weighted_marks:
            total = sum (m * w for m, w in zip(self.marks, self.weighted_marks))

            return total / sum (self.weighted_marks)
        else:
            print('Nenhuma nota foi inserida.')
        return 0
        

    def check_condition(self):
        return 'Aprovado' if self.final_mark >= self.passing_mark else 'Reprovado'
