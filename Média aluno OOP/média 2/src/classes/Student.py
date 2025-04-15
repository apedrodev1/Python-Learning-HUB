from src.functions.validations import validate_grade  # Remover validate_marks, já que não está mais em uso

class Student:
    def __init__(self, name, passing_grade, weights_marks=None, is_weighted=False):
        self.name = name
        self.passing_grade = passing_grade
        self.marks = []
        self.weights_marks = weights_marks if weights_marks else []
        self.condition = ''
        self.is_weighted = is_weighted

    def add_marks(self, marks):
        # Verifica se todas as notas são válidas com validate_grade
        validated_marks = []
        for mark in marks:
            valid_mark = validate_grade(mark)
            if valid_mark is not None:
                validated_marks.append(valid_mark)
            else:
                print(f"❌ Invalid mark: {mark}. Marks must be between 0 and 10.")
        if validated_marks:
            self.marks = validated_marks
        else:
            print(f"❌ No valid marks for student {self.name}.")

    def calculate_average(self):
        if self.is_weighted and self.weights_marks:
            total_weight = sum(self.weights_marks)
            weighted_sum = sum(mark * weight for mark, weight in zip(self.marks, self.weights_marks))
            return weighted_sum / total_weight if total_weight else 0
        else:
            return sum(self.marks) / len(self.marks) if self.marks else 0

    def check_condition(self):
        average = self.calculate_average()
        self.condition = "Approved" if average >= self.passing_grade else "Failed"
