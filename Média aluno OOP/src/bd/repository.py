import sqlite3
from . import queries  
from src.classes.Student import Student 


class StudentRepository:
    def __init__(self, db_file):
        """
        Inicializa o repositório, conectando ao banco de dados
        e criando as tabelas se não existirem.
        """
        self.db_file = db_file
        try:
            self.conn = sqlite3.connect(db_file)
            self.conn.execute("PRAGMA foreign_keys = ON;") # Habilita chaves estrangeiras
            self._create_tables()
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            raise
            
    def _create_tables(self):
        """Cria as tabelas do banco de dados usando as queries."""
        try:
            cursor = self.conn.cursor()
            cursor.execute(queries.CREATE_STUDENTS_TABLE)
            cursor.execute(queries.CREATE_GRADES_TABLE)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Erro ao criar tabelas: {e}")

    def add_student(self, student):
        """
        Adiciona um novo Student (objeto) ao banco de dados.
        Isso inclui salvar o aluno principal e suas notas/pesos.
        """
        try:
            cursor = self.conn.cursor()
            
            # 1. Insere o Aluno na tabela 'students'
            cursor.execute(queries.INSERT_STUDENT, (
                student.name,
                student.passing_grade,
                1 if student.is_weighted else 0
            ))
            
            # Pega o ID que o banco acabou de gerar para este aluno
            student_db_id = cursor.lastrowid
            
            # 2. Insere as Notas e Pesos na tabela 'grades'
            
            # Prepara os pesos (se não for ponderada, usa 1 como peso padrão)
            weights = student.weights_marks if student.is_weighted else [1] * len(student.marks)
            
            for mark, weight in zip(student.marks, weights):
                cursor.execute(queries.INSERT_GRADE, (
                    student_db_id,
                    mark,
                    weight
                ))
                
            self.conn.commit()
            print(f"Aluno {student.name} adicionado ao banco com ID {student_db_id}.")
            return student_db_id # Retorna o ID do banco
            
        except sqlite3.Error as e:
            self.conn.rollback() # Desfaz qualquer mudança se der erro
            print(f"Erro ao adicionar aluno {student.name}: {e}")
            return None

    def get_all_students(self):
        """
        Busca TODOS os alunos no banco e os "reconstrói"
        como uma lista de objetos Student.
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(queries.SELECT_ALL_STUDENTS)
            student_rows = cursor.fetchall() # Ex: [(1, 'Ana', 6.0, 0), (2, 'Beto', 7.0, 1)]
            
            student_list = []
            for row in student_rows:
                student_db_id, name, passing_grade, is_weighted_int = row
                is_weighted = bool(is_weighted_int) # Converte 0/1 para False/True
                
                # Busca as notas e pesos correspondentes
                cursor.execute(queries.SELECT_GRADES_FOR_STUDENT, (student_db_id,))
                grade_rows = cursor.fetchall() # Ex: [(8.0, 1.0), (7.5, 1.0)]
                
                # Descompacta as tuplas de (nota, peso)
                marks = [g[0] for g in grade_rows]
                weights = [g[1] for g in grade_rows]
                
                # Recria o objeto Student
                student = Student(
                    student_id=student_db_id, # Usa o ID do banco
                    name=name,
                    passing_grade=passing_grade,
                    weights_marks=weights if is_weighted else [], # Só passa pesos se for ponderada
                    is_weighted=is_weighted
                )
                student.marks = marks # O setter validará as notas
                
                student_list.append(student)
                
            return student_list
            
        except sqlite3.Error as e:
            print(f"Erro ao buscar alunos: {e}")
            return [] # Retorna lista vazia em caso de erro

    def close(self):
        """Fecha a conexão com o banco de dados."""
        if self.conn:
            self.conn.close()