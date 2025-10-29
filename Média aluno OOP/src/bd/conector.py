# Args:
        #     student_id: The student's id.
        #     name (str): The student's name.
        #     passing_grade (float): Minimum grade to pass.
        #     weights_marks (list, optional): Weights for each mark if using weighted average.
        #     is_weighted (bool, optional): Indicates if calculation should be weighted.



import sqlite3

conector = sqlite3.connect('banco_de_dados.db')
cursor = conector.cursor()

# Criando a tabela (mantive o nome Alunos como no seu exemplo)
sql_create = """
CREATE TABLE IF NOT EXISTS Alunos (
    codigo INTEGER,
    descricao TEXT,                                                             
    preco REAL,
    quantidade INTEGER
)
"""
cursor.execute(sql_create)

# Inserindo dados
sql_insert = """
INSERT INTO Alunos (codigo, descricao, preco, quantidade) 
VALUES (1138, 'Lápis Preto', 1.90, 376)
"""
cursor.execute(sql_insert)

# 🔥 IMPORTANTE: Confirmar as alterações no banco
conector.commit()

cursor.close()
conector.close()