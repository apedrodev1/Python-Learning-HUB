class Student:
    def __init__(self, name, passing_mark, is_weighted=False):  
        self.name = name
        self.passing_mark = passing_mark
        self.is_weighted = is_weighted  
        self.marks = []
        self.weighted_marks = []  # Adiciona lista para pesos
        self.final_mark = 0
        self.condition = ''

    def calculate_media_arithmetic(self):
        if self.marks:
            return sum(self.marks) / len(self.marks)
        else:
            print('Nenhuma nota foi inserida.')
            return 0

    def calculate_weighted_media(self):
        if self.marks and self.weighted_marks:
            weighted_sum = sum(m * w for m, w in zip(self.marks, self.weighted_marks))
            return weighted_sum / sum(self.weighted_marks)
        else:
            print('Pesos ou notas ausentes para cálculo ponderado.')
            return 0

    def check_condition(self):
        return 'Aprovado' if self.final_mark >= self.passing_mark else 'Reprovado'
