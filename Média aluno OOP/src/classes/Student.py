from src.functions.validations import validate_grade  

class Student:
    '''
    Represents a student with name, grades, weights, and passing condition.
    
    Attributes:
        name (str): The student's name.
        passing_grade (float): The minimum grade required to pass.
        marks (list): List of the student's grades.
        weights_marks (list): List of the weights for each grade (optional).
        condition (str): The final status ("Approved" or "Failed").
        is_weighted (bool): Whether the average calculation should be weighted.
    '''
    
    def __init__(self, student_id, name, passing_grade, weights_marks=None, is_weighted=False):
        '''
        Initialize a Student instance with student's id, name, passing grade, and optional weights.
        
        Args:
            student_id: The student's id.
            name (str): The student's name.
            passing_grade (float): Minimum grade to pass.
            weights_marks (list, optional): Weights for each mark if using weighted average.
            is_weighted (bool, optional): Indicates if calculation should be weighted.
        '''

        self.student_id = student_id
        self.name = name
        self.passing_grade = passing_grade
        self.marks = []
        self.weights_marks = weights_marks if weights_marks else []
        self.condition = ''
        self.is_weighted = is_weighted

    def add_marks(self, marks):
        '''
        Validate each mark using validate_grade and add valid marks to the student.
        
        Args:
            marks (list): List of marks to be validated and added.
        
        Returns:
            None
        '''
        validated_marks = []
        for mark in marks:
            mark_value, error = validate_grade(mark)
            if error is None:
                validated_marks.append(mark_value)
            else:
                print(f"❌ Invalid mark: {mark}. Marks must be between 0 and 10.")
        if validated_marks:
            self.marks = validated_marks
        else:
            print(f"❌ No valid marks for student {self.name}.")

    def calculate_average(self):
        '''
        Calculate the student's final average, considering weights if needed.
        
        Returns:
            float: The calculated average or 0 if no valid marks exist.
        '''
        if self.is_weighted and self.weights_marks:
            total_weight = sum(self.weights_marks)
            weighted_sum = sum(mark * weight for mark, weight in zip(self.marks, self.weights_marks))
            return weighted_sum / total_weight if total_weight else 0
        else:
            return sum(self.marks) / len(self.marks) if self.marks else 0

    def check_condition(self):
        '''
        Determine whether the student is Approved or Failed based on the final average.
        
        Returns:
            None
        '''
        average = self.calculate_average()
        self.condition = "Approved" if average >= self.passing_grade else "Failed"
        return self.condition