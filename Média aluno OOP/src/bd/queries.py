CREATE_STUDENTS_TABLE = """
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    passing_grade REAL NOT NULL,
    is_weighted INTEGER NOT NULL DEFAULT 0
);
"""

# SQL para criar a tabela de notas
CREATE_GRADES_TABLE = """
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    mark_value REAL NOT NULL,
    weight_value REAL NOT NULL DEFAULT 1,
    FOREIGN KEY (student_id) REFERENCES students (id) ON DELETE CASCADE
);
"""

# --- Queries de CRUD ---

INSERT_STUDENT = """
INSERT INTO students (name, passing_grade, is_weighted) 
VALUES (?, ?, ?);
"""

INSERT_GRADE = """
INSERT INTO grades (student_id, mark_value, weight_value) 
VALUES (?, ?, ?);
"""

SELECT_ALL_STUDENTS = "SELECT * FROM students;"

SELECT_GRADES_FOR_STUDENT = "SELECT mark_value, weight_value FROM grades WHERE student_id = ?;"

# (Adicionaremos UPDATE e DELETE depois)