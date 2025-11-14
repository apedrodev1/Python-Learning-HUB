"""
Contains the Classroom class, the Logic Engine of the application.

This class holds the business rules (calculation type, weights, passing grade)
and is responsible for processing Student objects to determine their results.
"""

from src.utils.validations import (
    validate_calculation_type, 
    validate_grade, 
    validate_weights
)

class Classroom:
    """
    Represents a class/course with specific evaluation rules.

    It acts as the 'Context' for the strategy. It holds the configuration
    for how students should be evaluated.

    Attributes:
        _name (str): Name of the classroom (e.g., "Math 101").
        _passing_grade (float): The cutoff grade.
        _calc_type (str): '0' (Arithmetic), '1' (Weighted), '2' (Median).
        _weights (list): Weights corresponding to marks (only for type '1').
    """

    def __init__(self, name, passing_grade=7.0, calc_type="0", weights=None):
        """
        Args:
            name (str): Classroom name.
            passing_grade (float): Minimum grade to pass.
            calc_type (str): Calculation method.
            weights (list, optional): Weights for weighted average.
        """
        self.name = name
        self.passing_grade = passing_grade
        self.calc_type = calc_type
        # Set weights directly or empty list if None
        self.weights = weights if weights else []

    # --- Configuration Properties (with Validation) ---

    @property
    def passing_grade(self):
        return self._passing_grade

    @passing_grade.setter
    def passing_grade(self, value):
        val, error = validate_grade(str(value))
        if error:
            raise ValueError(f"Invalid passing grade: {error}")
        self._passing_grade = val

    @property
    def calc_type(self):
        return self._calc_type

    @calc_type.setter
    def calc_type(self, value):
        val, error = validate_calculation_type(str(value))
        if error:
            raise ValueError(error)
        self._calc_type = val

    @property
    def weights(self):
        return self._weights

    @weights.setter
    def weights(self, value):
        # Only validate weights if we are in Weighted mode (type '1')
        # But we allow setting them anytime to keep state consistent.
        if value:
            # Convert to string for the validator if it's a list
            str_input = " ".join(map(str, value)) if isinstance(value, list) else str(value)
            val, error = validate_weights(str_input)
            if error:
                raise ValueError(error)
            self._weights = val
        else:
            self._weights = []

    # --- The Core Logic Method ---

    def calculate_student(self, student):
        """
        Applies the Classroom's rules to a specific Student instance.

        This method reads the student's marks, calculates the average
        based on self.calc_type, determines the condition based on
        self.passing_grade, and UPDATES the student object.

        Args:
            student (Student): The student object to process.
        """
        marks = student.marks
        if not marks:
            student.final_average = 0.0
            student.condition = "Failed" # Or "N/A"
            return

        avg = 0.0

        try:
            # 1. Arithmetic Mean
            if self._calc_type == '0':
                avg = sum(marks) / len(marks)

            # 2. Weighted Mean
            elif self._calc_type == '1':
                # Business Rule Check: Do we have enough weights?
                # If marks > weights, we can't calculate correctly.
                # For simplicity, we might truncate or error. Here we behave safely:
                if not self._weights or len(marks) != len(self._weights):
                    # Fallback or Error? 
                    # Let's assume simple arithmetic if config is broken temporarily
                    avg = sum(marks) / len(marks) 
                else:
                    weighted_sum = sum(m * w for m, w in zip(marks, self._weights))
                    # Validate_weights ensures sum is 10, but safe division is good
                    total_w = sum(self._weights)
                    avg = weighted_sum / total_w if total_w else 0

            # 3. Median
            elif self._calc_type == '2':
                sorted_marks = sorted(marks)
                n = len(sorted_marks)
                if n % 2 == 1:
                    avg = float(sorted_marks[n // 2])
                else:
                    mid1 = sorted_marks[n // 2 - 1]
                    mid2 = sorted_marks[n // 2]
                    avg = (float(mid1) + float(mid2)) / 2

            # Rounding rule is part of the Classroom policy
            student.final_average = round(avg, 2)

            # Condition rule
            if student.final_average >= self.passing_grade:
                student.condition = "Approved"
            else:
                student.condition = "Failed"

        except Exception as e:
            print(f"Error calculating student {student.name}: {e}")
            student.final_average = 0.0
            student.condition = "Error"