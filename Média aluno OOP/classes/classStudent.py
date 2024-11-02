class Student:
    def __init__(self, name, passing_grade):
        self.name = name
        self.passing_grade = passing_grade
        self.marks = []
        self.final_mark = 0
        self.condition = ''
        self.weighted_marks = []
        self.is_weighted = False

    def calculate_arithmetic_mean(self):
        if self.marks:
            return sum(self.marks) / len(self.marks)
        else:
            print('No grades were entered.')
        return 0
    
    def calculate_weighted_mean(self):
        if self.marks and self.weighted_marks:
            weighted_sum = sum(mark * weight for mark, weight in zip(self.marks, self.weighted_marks))
            return weighted_sum / sum(self.weighted_marks)
        print('No grades or weights were entered.')
        return 0
    
    def check_condition(self):
        return 'Passed' if self.final_mark >= self.passing_grade else 'Failed'
