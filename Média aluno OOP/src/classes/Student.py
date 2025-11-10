"""
Contains the Student class, the core data model for the application.

This module defines the Student data structure, including its
self-validating properties and calculated attributes.
"""

from src.utils.validations import validate_grade, validate_names, validate_weights

class Student:
    
    """
    Represents a student with name, grades, weights, and passing condition.

    This class is self-validating, using setters and properties to ensure
    data integrity.

    Attributes:
        _student_id (int): The student's read-only database ID.
        _name (str): The student's name.
        _passing_grade (float): The minimum grade to pass.
        _marks (list): List of the student's grades (as floats).
        _weights_marks (list): List of weights for each grade (as floats).
        _calc_type (str): The calculation type ('0', '1', or '2').
        _is_deleted (bool): Flag for soft delete status.
    """
    
    def __init__(self, student_id, name, passing_grade, calc_type: str, weights_marks=None):
        
        """
        Initializes a new Student instance.

        The constructor uses public setters to ensure that even
        initial data is validated.

        Args:
            student_id (int or None): The student's database ID.
            name (str): The student's name.
            passing_grade (float): The minimum grade to pass.
            calc_type (str): The calculation type ('0', '1', or '2').
            weights_marks (list, optional): List of weights for weighted average.
        """
    
        self._student_id = student_id  # Read-only private attribute
        
        # Public setters validate the incoming data
        self.name = name
        self.passing_grade = passing_grade
        
        # Store the calculation type. This MUST be set before weights_marks.
        self._calc_type = calc_type 
        
        # The setter for weights_marks depends on the 'is_weighted' property,
        # which now correctly derives its value from self._calc_type.
        self.weights_marks = weights_marks if weights_marks else []
        
        self._marks = []  # Default to empty list
        self._is_deleted = False


    # --- student_id Property (Read-Only) ---

    @property
    def student_id(self):
        """int: The student's unique database identifier."""
        return self._student_id


    # --- Name Property (Read/Write with Validation) ---

    @property
    def name(self):
        """str: The student's full name."""
        return self._name


    @name.setter
    def name(self, new_name):
        """
        Sets the student's name after validation.

        Args:
            new_name (str): The new name for the student.

        Raises:
            ValueError: If the name is invalid (e.g., contains numbers).
        """
        validated_name, error = validate_names(new_name)
        if error:
            raise ValueError(error)  # Raise an error instead of printing
        self._name = validated_name


    # --- passing_grade Property (Read/Write with Validation) ---

    @property
    def passing_grade(self):
        """float: The minimum grade required to pass."""
        return self._passing_grade


    @passing_grade.setter
    def passing_grade(self, new_grade):
        """
        Sets the passing grade after validation.

        Args:
            new_grade (str or float): The new passing grade (0-10).

        Raises:
            ValueError: If the grade is not a valid number between 0-10.
        """
        # The validation function expects a string, so we convert it
        validated_grade, error = validate_grade(str(new_grade))
        if error:
            raise ValueError(error)
        self._passing_grade = validated_grade


    # --- marks Property (Read/Write with Validation) ---
    
    @property
    def marks(self):
        """list: The list of the student's grades (as floats)."""
        return self._marks


    @marks.setter
    def marks(self, new_marks_list):

        """
        Sets the student's list of marks, validating each item.

        Args:
            new_marks_list (list): A list of marks (can be str or float).

        Raises:
            ValueError: If any mark in the list is invalid or if
                no valid marks were provided.
        """

        validated_marks = []
        errors = []

        for mark in new_marks_list:
            # The validation function expects a string
            mark_value, error = validate_grade(str(mark))
            if error:
                errors.append(f"Invalid mark: '{mark}'. {error}")
            else:
                validated_marks.append(mark_value)
        
        if errors:
            # If there's ANY error, reject the whole list
            raise ValueError("\n".join(errors))
            
        if not validated_marks and len(new_marks_list) > 0:
             raise ValueError("No valid marks were provided.")


        self._marks = validated_marks


    # --- weights_marks Property (Read/Write with Validation) ---
    
    @property
    def weights_marks(self):
        """list: The list of weights (as floats) for each mark."""
        return self._weights_marks


    @weights_marks.setter
    def weights_marks(self, new_weights_list):
        """
        Sets the list of weights, validating the list.

        Args:
            new_weights_list (list): A list of weights (as floats).

        Raises:
            ValueError: If the list of weights is invalid (e.g., not a
                list, contains values <= 0, or sum is not 10 if weighted).
        """
        if not isinstance(new_weights_list, list):
            raise ValueError("Weights must be a list of numbers.")

        # This check now uses the 'is_weighted' PROPERTY,
        # which correctly reads 'self._calc_type'
        if self.is_weighted:
            if not new_weights_list:
                raise ValueError("The weights list cannot be empty for a weighted average.")
            if any(w <= 0 for w in new_weights_list):
                raise ValueError("All weights must be greater than zero.")
            if sum(new_weights_list) != 10:
                raise ValueError(f"The sum of weights must be 10, but got {sum(new_weights_list)}.")
        
        self._weights_marks = new_weights_list


    # --- is_weighted Property (Read-Only, DERIVED) ---

    @property
    def is_weighted(self):
        """bool: True if the calculation type is weighted ('1')."""
        return self._calc_type == '1'
    

    # --- Calculated Properties (Read-Only) ---


    @property
    def average(self):
        """
        float: The student's calculated final average, rounded to 2 decimals.
        Calculates based on the self._calc_type ('0', '1', or '2').
        """
        
        if not self._marks:
            return 0.0

        try:
            # --- TIPO 1: Média Ponderada ---
            if self._calc_type == '1': 
                if len(self._marks) != len(self._weights_marks):
                    return 0.0  # Ou levante um erro
                
                total_weight = sum(self._weights_marks)
                if total_weight == 0:
                    return 0.0
                        
                weighted_sum = sum(mark * weight for mark, weight in zip(self._marks, self._weights_marks))
                avg = weighted_sum / total_weight

            # --- TIPO 2: Mediana ---
            elif self._calc_type == '2':
                sorted_marks = sorted(self._marks)
                n = len(sorted_marks)
                
                if n % 2 == 1:
                    # Ímpar: pega o valor do meio
                    avg = float(sorted_marks[n // 2])
                else:
                    # Par: média dos dois valores do meio
                    mid1 = sorted_marks[n // 2 - 1]
                    mid2 = sorted_marks[n // 2]
                    avg = (float(mid1) + float(mid2)) / 2
            
            # --- 0: Média Aritmética (Default) ---
            else: 
                avg = sum(self._marks) / len(self._marks)
            
            return round(avg, 2)

        except Exception:
            # Pega qualquer erro de divisão por zero ou outro
            return 0.0


    @property
    def condition(self):
        """
        str: The student's calculated condition ("Approved" or "Failed").

        Compares the 'average' property against the 'passing_grade' property.
        """
        return "Approved" if self.average >= self.passing_grade else "Failed"


    @property
    def is_deleted(self):
        """bool: True if the student has been marked for deletion (soft delete)."""
        return self._is_deleted



    # --- Public Methods ---

    def mark_as_deleted(self):
        """Marks the student as deleted (soft delete)."""
        self._is_deleted = True

    def to_dict(self):
        """
        Returns a serializable dictionary representation of the student.

        This helps ../functions/export/export_wrapper.py to export to JSON or XML.

        Returns:
            dict: A dictionary containing the student's public data.
        """
        return {
            "student_id": self.student_id,
            "name": self.name,
            "marks": self.marks,
            "weights_marks": self.weights_marks,
            "is_weighted": self.is_weighted, 
            "passing_grade": self.passing_grade,
            "average": self.average, 
            "condition": self.condition
        }