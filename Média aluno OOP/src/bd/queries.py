"""
Contains all SQL query constants used by the StudentRepository.

Storing queries as constants in a separate module makes the
repository logic cleaner and easier to maintain.
"""

# --- Table Creation Queries ---

CREATE_STUDENTS_TABLE = """
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    passing_grade REAL NOT NULL,
    is_weighted INTEGER NOT NULL DEFAULT 0
);
"""

# SQL to create the grades table
CREATE_GRADES_TABLE = """
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    mark_value REAL NOT NULL,
    weight_value REAL NOT NULL DEFAULT 1,
    FOREIGN KEY (student_id) REFERENCES students (id) ON DELETE CASCADE
);
"""

# --- CRUD Queries ---

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

UPDATE_STUDENT_DATA = """
UPDATE students
SET name = ?, passing_grade = ?, is_weighted = ?
WHERE id = ?;
"""

# --- DELETE Queries ---

# This query deletes ALL old grades for a student
# so we can insert the newly edited ones.
DELETE_GRADES_FOR_STUDENT = "DELETE FROM grades WHERE student_id = ?;"

# (Thanks to 'ON DELETE CASCADE', associated grades will be deleted automatically)
DELETE_STUDENT_BY_ID = "DELETE FROM students WHERE id = ?;"