"""
Database Repository Module for the Student Grade System.

This module defines the Repository class, which abstracts all
database interactions (CRUD operations) using a data access layer pattern.
It is the only part of the application that should directly execute SQL.
"""

import sqlite3
import json
from . import queries
from src.utils.db_connection import DatabaseManager
from src.classes.Student import Student


class Repository:
    """
    Manages all database operations for Student and Classroom objects.

    This class handles the connection, cursor management, and translation
    between Student objects and the SQL database tables using the
    DatabaseManager context manager.

    Attributes:
        db_manager (DatabaseManager): The manager for the SQLite database file.
    """

    def __init__(self, db_file: str):
        """
        Initializes the repository and ensures tables are created.

        Args:
            db_file (str): The path to the SQLite database file.
        """
        # Use the DatabaseManager instead of manual connection
        self.db_manager = DatabaseManager(db_file)
        self._create_tables()

    def _create_tables(self):
        """
        Creates the database tables if they do not already exist.

        This is an internal method called during initialization.
        """
        try:
            # Use the context manager for the connection
            with self.db_manager as conn:
                conn.execute(queries.CREATE_TABLE_STUDENTS)
                conn.execute(queries.CREATE_TABLE_GRADES)
                # Ensure the new config table is created
                conn.execute(queries.CREATE_TABLE_CLASSROOM_CONFIG)
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")

    # --- Config Methods (New for Fase 3) ---

    def get_classroom_config(self, key: str) -> str | None:
        """
        Fetches a specific configuration value by its key.

        Args:
            key (str): The name of the configuration key (e.g., "calc_type").

        Returns:
            str or None: The stored value as a string, or None if not found. 
            
            Possible keys:
            - 0 for Arithmetic (also the default option),
            - 1 for Weighted,
            - 2 for Median
        """
        try:
            with self.db_manager as conn:
                cursor = conn.execute(queries.SELECT_CONFIG, (key,))
                result = cursor.fetchone()
                # Return the value (result[0]) if a result was found
                return result[0] if result else None
        except sqlite3.Error as e:
            print(f"Error getting config for key {key}: {e}")
            return None

    def set_classroom_config(self, key: str, value: str):
        """
        Sets (Inserts or Updates) a configuration value.

        This performs an "UPSERT" operation: it attempts to UPDATE
        a key, and if it doesn't exist (rowcount = 0), it INSERTS it.

        Args:
            key (str): The key to set (e.g., "passing_grade").
            value (str): The value to store (must be a string).
        """
        try:
            with self.db_manager as conn:
                # First, try to update the key
                cursor = conn.execute(queries.UPDATE_CONFIG, (value, key))
                # If no rows were affected, the key doesn't exist
                if cursor.rowcount == 0:
                    # Insert it instead
                    conn.execute(queries.INSERT_CONFIG, (key, value))
        except sqlite3.Error as e:
            print(f"Error setting config for key {key}: {e}")

    # --- Student/Grade Methods (Refactored for Fase 3) ---

    def add_student(self, name: str, marks: list[float]):
        """
        Adds a new Student to the database (simplified).

        Classroom rules (passing_grade, weights) are no longer
        saved with the student, as they are in 'classroom_config'.

        Args:
            name (str): The student's name.
            marks (list[float]): The list of marks.

        Returns:
            int or None: The new student's ID, or None on failure.
        """
        try:
            with self.db_manager as conn:
                # 1. Insert the student (name only) using the refactored query
                cursor = conn.cursor()
                cursor.execute(queries.INSERT_STUDENT, (name,))
                student_db_id = cursor.lastrowid

                # 2. Insert the grades (mark_value only)
                if marks:
                    # Prepare data for executemany (more efficient)
                    grades_data = [(student_db_id, mark) for mark in marks]
                    conn.executemany(queries.INSERT_GRADE, grades_data)

                print(f"Student {name} added with ID {student_db_id}.")
                return student_db_id

        except sqlite3.Error as e:
            # Rollback is handled automatically by DatabaseManager's __exit__
            print(f"Error adding student {name}: {e}")
            return None

    def get_all_students(self) -> list[Student]:
        """
        Fetches all students and reconstructs them using classroom config.

        *** This method contains the critical bug fix for Fase 3 ***
        It reads from 'classroom_config' first, then instantiates
        Student objects using the new constructor signature.

        Returns:
            list[Student]: A list of all Student objects.
        """
        student_list = []
        try:
            # 1. Get classroom config from the DB
            calc_type = self.get_classroom_config("calc_type")
            passing_grade_str = self.get_classroom_config("passing_grade")
            weights_marks_str = self.get_classroom_config("weights_marks")

            # 2. Validate config
            if not all((calc_type, passing_grade_str, weights_marks_str)):
                print("\n[CRITICAL ERROR] Classroom config not found in DB.")
                print("Delete the .db file and restart the app to set up.")
                return []  # Return empty list to prevent crash

            # 3. Parse config values
            passing_grade = float(passing_grade_str)
            weights_marks = json.loads(weights_marks_str)

            with self.db_manager as conn:
                # 4. Get all students (id, name)
                student_rows = conn.execute(queries.SELECT_ALL_STUDENTS).fetchall()

                for row in student_rows:
                    student_db_id, name = row

                    # 5. Fetch the corresponding grades for this student
                    cursor_grades = conn.execute(
                        queries.SELECT_GRADES_FOR_STUDENT, (student_db_id,)
                    )
                    # Unpack list of tuples: [(8.0,), (7.5,)] -> [8.0, 7.5]
                    marks = [g[0] for g in cursor_grades.fetchall()]

                    # 6. Re-create the Student object using the NEW constructor
                    # This fixes the TypeError bug from Fase 2.
                    student = Student(
                        student_id=student_db_id,
                        name=name,
                        marks=marks,
                        calc_type=calc_type,
                        passing_grade=passing_grade,
                        weights_marks=weights_marks,
                    )
                    student_list.append(student)

            return student_list

        except (sqlite3.Error, json.JSONDecodeError, TypeError) as e:
            print(f"Error fetching students or parsing config: {e}")
            return []  # Return an empty list on failure

    def update_student(self, student: Student):
        """
        Updates an existing student in the database (simplified).

        This now only updates the student's name and grades, as
        classroom rules are no longer stored here.

        Args:
            student (Student): The Student object with updated data.
        """
        try:
            with self.db_manager as conn:
                # 1. Update the 'students' table (name only)
                conn.execute(queries.UPDATE_STUDENT_DATA, (
                    student.name,
                    student.student_id
                ))

                # 2. Delete ALL old grades for this student
                conn.execute(queries.DELETE_GRADES_FOR_STUDENT, (student.student_id,))

                # 3. Re-insert the (now updated) grades (mark_value only)
                if student.marks:
                    grades_data = [(student.student_id, mark) for mark in student.marks]
                    conn.executemany(queries.INSERT_GRADE, grades_data)

                print(f"Student {student.name} (ID: {student.student_id}) updated.")

        except sqlite3.Error as e:
            print(f"Error updating student {student.name}: {e}")

    def delete_student(self, student_id: int):
        """
        Deletes a student from the database using their ID.

        'ON DELETE CASCADE' handles deleting associated grades.

        Args:
            student_id (int): The ID of the student to delete.
        """
        try:
            with self.db_manager as conn:
                conn.execute(queries.DELETE_STUDENT_BY_ID, (student_id,))
                print(f"Student (ID: {student_id}) deleted from database.")

        except sqlite3.Error as e:
            print(f"Error deleting student (ID: {student_id}): {e}")
