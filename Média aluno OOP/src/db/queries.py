"""
Contains all SQL query constants used by the Repository.

Storing queries as constants in a separate module makes the
repository logic cleaner and easier to maintain.
"""

# --- Table Creation Queries ---

CREATE_TABLE_STUDENTS = """
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
"""

# SQL to create the grades table (Refactored)
# 'weight_value' was removed, as weights are now a Classroom config,
# not a per-grade property.
CREATE_TABLE_GRADES = """
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    mark_value REAL NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students (id) ON DELETE CASCADE
);
"""

# SQL to create the new class config table (Fase 3)
# This table will store classroom-wide settings like
# calc_type, passing_grade, and weights_marks as key-value pairs.
CREATE_TABLE_CLASSROOM_CONFIG = """
CREATE TABLE IF NOT EXISTS classroom_config (
    key TEXT PRIMARY KEY,
    value TEXT
);
"""

# --- Config Queries (New for Fase 3) ---

SELECT_CONFIG = "SELECT value FROM classroom_config WHERE key = ?;"
INSERT_CONFIG = "INSERT INTO classroom_config (key, value) VALUES (?, ?);"
UPDATE_CONFIG = "UPDATE classroom_config SET value = ? WHERE key = ?;"


# --- Student/Grade CRUD Queries (Refactored) ---

# INSERT_STUDENT no longer includes 'passing_grade' or 'is_weighted'.
INSERT_STUDENT = "INSERT INTO students (name) VALUES (?);"

# INSERT_GRADE no longer includes 'weight_value'.
INSERT_GRADE = "INSERT INTO grades (student_id, mark_value) VALUES (?, ?);"

SELECT_ALL_STUDENTS = "SELECT id, name FROM students;"

# SELECT_GRADES_FOR_STUDENT no longer selects 'weight_value'.
SELECT_GRADES_FOR_STUDENT = "SELECT mark_value FROM grades WHERE student_id = ?;"

# UPDATE_STUDENT_DATA no longer updates 'passing_grade' or 'is_weighted'.
UPDATE_STUDENT_DATA = "UPDATE students SET name = ? WHERE id = ?;"


# --- DELETE Queries (Unchanged) ---

# This query deletes ALL old grades for a student
# so we can insert the newly edited ones.
DELETE_GRADES_FOR_STUDENT = "DELETE FROM grades WHERE student_id = ?;"

# (Thanks to 'ON DELETE CASCADE', associated grades will be deleted automatically)
DELETE_STUDENT_BY_ID = "DELETE FROM students WHERE id = ?;"