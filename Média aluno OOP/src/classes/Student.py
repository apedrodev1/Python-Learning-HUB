"""
Contains the Student class, serving as a data container.

This class holds the student's personal data and their marks.
It does NOT contain calculation logic or passing criteria.
Those responsibilities have been moved to the Classroom class.
"""

from src.utils.validations import validate_grade, validate_names

class Student:
    """
    Represents a student with ID, name, and marks.
    
    It acts as a 'dumb' data object. It knows WHO it is and WHAT it scored,
    but relies on an external entity (Classroom) to determine if it passed.

    Attributes:
        _student_id (int): Unique database ID (read-only).
        _name (str): Student's full name.
        _marks (list): List of grades (floats).
        _final_average (float): Calculated average (set by Classroom).
        _condition (str): Final status like "Approved" (set by Classroom).
        _is_deleted (bool): Soft delete flag.
    """

    def __init__(self, student_id, name):
        """
        Initializes a Student.
        
        Args:
            student_id (int): The DB ID.
            name (str): The student's name.
        """
        self._student_id = student_id
        
        # Setter will validate the name
        self.name = name
        
        self._marks = []
        self._is_deleted = False
        
        # Placeholders for values calculated by the Classroom
        self._final_average = 0.0
        self._condition = "N/A"

    # --- ID (Read-Only) ---
    @property
    def student_id(self):
        return self._student_id

    # --- Name (Validated) ---
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        validated_name, error = validate_names(new_name)
        if error:
            raise ValueError(error)
        self._name = validated_name

    # --- Marks (Validated) ---
    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, new_marks_list):
        """Validates and sets the list of marks."""
        validated_marks = []
        errors = []

        for mark in new_marks_list:
            # Validate each grade individually
            val, error = validate_grade(str(mark))
            if error:
                errors.append(f"Invalid mark '{mark}': {error}")
            else:
                validated_marks.append(val)
        
        if errors:
            raise ValueError("\n".join(errors))
            
        self._marks = validated_marks

    # --- Results (Set by Classroom) ---
    # These are simple getters/setters allowing the Classroom to "stamp" results.

    @property
    def final_average(self):
        return self._final_average

    @final_average.setter
    def final_average(self, value):
        self._final_average = float(value)

    @property
    def condition(self):
        return self._condition

    @condition.setter
    def condition(self, value):
        self._condition = str(value)

    # --- Soft Delete ---
    @property
    def is_deleted(self):
        return self._is_deleted

    def mark_as_deleted(self):
        self._is_deleted = True

    def to_dict(self):
        """Exports student data (cleaner now, without rules)."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "marks": self.marks,
            "final_average": self.final_average,
            "condition": self.condition
        }