# Agora importamos as validações DIRETAMENTE na classe
from src.functions.validations import validate_grade, validate_names, validate_weights

class Student:
    '''
    Representa um aluno com nome, notas, pesos e condição de aprovação.
    Os atributos são protegidos e validados através de setters.
    
    Attributes (privados):
        _student_id (int): O ID do aluno (read-only).
        _name (str): O nome do aluno.
        _passing_grade (float): A nota mínima para aprovação.
        _marks (list): Lista de notas do aluno.
        _weights_marks (list): Lista de pesos para cada nota.
        _is_weighted (bool): Se o cálculo da média deve ser ponderado.
    
    Properties (públicas):
        student_id (int): Getter para o ID.
        name (str): Getter e Setter para o nome (valida ao setar).
        passing_grade (float): Getter e Setter para a nota de corte (valida ao setar).
        marks (list): Getter e Setter para as notas (valida ao setar).
        weights_marks (list): Getter e Setter para os pesos (valida ao setar).
        is_weighted (bool): Getter e Setter para o flag de média ponderada.
        condition (str): Getter (read-only) para a condição ("Approved" ou "Failed").
        average (float): Getter (read-only) para a média calculada.
    '''
    
    def __init__(self, student_id, name, passing_grade, weights_marks=None, is_weighted=False):
        '''
        Inicializa a instância do Aluno.
        O __init__ agora usa os setters públicos, garantindo que
        mesmo os dados iniciais sejam validados.
        '''
        self._student_id = student_id  # ID é definido como "privado" e não terá setter (read-only)
        
        # Chama os setters públicos para validar os dados de entrada
        self.name = name
        self.passing_grade = passing_grade
        self.is_weighted = is_weighted
        self.weights_marks = weights_marks if weights_marks else []
        self._marks = []  # Começa com uma lista de notas vazia (será setada via .marks)

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
        validated_name, error = validate_names(new_name)
        if error:
            raise ValueError(error)  # Levanta um erro em vez de imprimir
        self._name = validated_name

    # --- Propriedade passing_grade (Read/Write com Validação) ---
    @property
    def passing_grade(self):
        return self._passing_grade

    @passing_grade.setter
    def passing_grade(self, new_grade):
        # validate_grade espera uma string, então convertemos
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
        # NOTA: A sua função `validate_weights` original
        # espera uma string separada por espaços. Uma classe deve
        # idealmente receber uma lista. Aqui, validamos a lista diretamente
        # para um melhor design OOP.
        
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
    # Renomeei de calculate_average para 'average' para seguir o padrão
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