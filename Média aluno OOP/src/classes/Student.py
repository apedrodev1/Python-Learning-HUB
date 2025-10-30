from src.functions.validations import validate_grade, validate_names, validate_weights  

class Student:
    '''
    Represents a student with name, grades, weights, and passing condition.
    
    Attributes:
        name (str): The student's name.
        passing_grade (float): The minimum grade required to pass.
        marks (list): List of the student's grades.
        weights_marks (list): List of the weights for each grade (optional).
        is_weighted (bool): Whether the average calculation should be weighted.


    Properties:     
       condition (str): "Approved" if average >= passing_grade, else "Failed".
    
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

        self._student_id = student_id
        self.name = name
        self.passing_grade = passing_grade
        self.weights_marks = weights_marks if weights_marks else []
        self.is_weighted = is_weighted
        self._marks = []



# --- Propriedade student_id (Read-Only) ---
    @property
    def student_id(self):
        return self._student_id



# --- Propriedades Name (Read/Write com Validação) ---
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        valid_name, error = validate_names(new_name)
        if error:
            raise ValueError(error)
        self._name = validated_name



# --- Propriedade passing_grade (Read/Write com Validação) ---
    @property
    def passing_grade(self):
        return self._passing_grade

    @passing_grade.setter
    def passing_grade(self, new_grade):
        validated_grade, error = validate_grade(str(new_grade))
        if error:
            raise ValueError(error)
        self._passing_grade = validated_grade



# --- Propriedade marks (Read/Write com Validação) ---
    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, new_marks_list):
    '''
        Setter para as notas. Valida cada nota na lista.
        Levanta um ValueError se qualquer nota for inválida.
        '''
        validated_marks = []
        errors = []
        for mark in new_marks_list:
            # validate_grade espera string
            mark_value, error = validate_grade(str(mark))
            if error:
                errors.append(f"Nota inválida: '{mark}'. {error}")
            else:
                validated_marks.append(mark_value)
        
        if errors:
            # Se houver UM erro, rejeita a lista inteira
            raise ValueError("\n".join(errors))
            
        if not validated_marks and len(new_marks_list) > 0:
             raise ValueError("Nenhuma nota válida foi fornecida.")
             
        self._marks = validated_marks



    # --- Propriedade weights_marks (Read/Write com Validação) ---
    @property
    def weights_marks(self):
        return self._weights_marks

    @weights_marks.setter
    def weights_marks(self, new_weights_list):
        '''
        Setter para os pesos. Valida a lista de pesos.
        '''
        
        if not isinstance(new_weights_list, list):
            raise ValueError("Pesos devem ser uma lista de números.")

        if self._is_weighted:
            if not new_weights_list:
                raise ValueError("A lista de pesos não pode estar vazia para média ponderada.")
            if any(w <= 0 for w in new_weights_list):
                raise ValueError("Todos os pesos devem ser maiores que zero.")
            if sum(new_weights_list) != 10:
                raise ValueError(f"A soma dos pesos deve ser 10, mas foi {sum(new_weights_list)}.")
        
        self._weights_marks = new_weights_list



# --- Propriedade is_weighted (Read/Write) ---
    @property
    def is_weighted(self):
        return self._is_weighted

    @is_weighted.setter
    def is_weighted(self, value):
        if not isinstance(value, bool):
            raise ValueError("is_weighted deve ser um valor booleano (True/False).")
        self._is_weighted = value



# --- Propriedade "average" (Calculada, Read-Only) ---
    @property
    def average(self):
        '''
        Calcula e retorna a média final do aluno.
        '''
        if self._is_weighted and self._weights_marks:
            # Garante que temos o mesmo número de notas e pesos
            if len(self._marks) != len(self._weights_marks):
                # Isso pode ser um erro ou pode ser que as notas ainda não foram setadas
                # Por agora, retornamos 0 para evitar um crash
                return 0.0 
                
            total_weight = sum(self._weights_marks)
            weighted_sum = sum(mark * weight for mark, weight in zip(self._marks, self._weights_marks))
            return weighted_sum / total_weight if total_weight else 0.0
        else:
            return sum(self._marks) / len(self._marks) if self._marks else 0.0



# --- Propriedade "condition" (Calculada, Read-Only) ---
    @property
    def condition(self):
        '''
        Calcula e retorna a condição ATUAL (Approved/Failed)
        baseado na média e na nota de corte.
        '''
        # Agora ela usa a propriedade 'average' e 'passing_grade'
        return "Approved" if self.average >= self.passing_grade else "Failed"