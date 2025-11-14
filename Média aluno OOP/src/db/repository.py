"""
Database Repository Module for the Student Grade System.

This module defines the Repository class, which abstracts all
database interactions (CRUD operations) using a data access layer pattern.
It handles the connection lifecycle via the DatabaseManager context manager
and maps database rows to Student objects.
"""

import sqlite3
from . import queries
from src.utils.db_connection import DatabaseManager
from src.classes.Student import Student

class Repository:
    """
    Manages all database operations for Student objects.

    Acts as a wrapper around DatabaseManager to provide specific
    methods for Student CRUD (Create, Read, Update, Delete).
    """

    def __init__(self, db_file: str):
        """
        Initializes the repository.

        Args:
            db_file (str): The path to the SQLite database file.
        """
        self.db_manager = DatabaseManager(db_file)
        self.conn = None # Will hold the active connection inside a 'with' block
        self._create_tables()

    # --- Context Manager Protocol ---
    # Permite que o index.py use "with repo:"

    def __enter__(self):
        """Starts the DB connection when entering the 'with' block."""
        self.conn = self.db_manager.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Closes the DB connection when exiting the 'with' block."""
        self.db_manager.__exit__(exc_type, exc_val, exc_tb)
        self.conn = None

    # --- Table Setup ---

    def _create_tables(self):
        """Ensures necessary tables exist using a temporary connection."""
        # We use a temporary 'with' block here because the main 'with repo'
        # might not have started yet during __init__.
        try:
            with self.db_manager as conn:
                conn.execute(queries.CREATE_TABLE_STUDENTS)
                conn.execute(queries.CREATE_TABLE_GRADES)
        except sqlite3.Error as e:
            print(f"❌ Error creating tables: {e}")

    # --- Helper: Get Cursor ---

    def _get_cursor(self):
        """
        Returns a cursor from the active connection (inside 'with')
        or creates a temporary one if used standalone.
        """
        if self.conn:
            return self.conn.cursor()
        else:
            # Fallback if methods are called outside "with repo:"
            # (Not recommended for the main loop, but good for safety)
            return self.db_manager.__enter__().cursor()

    # --- CRUD Operations ---

    def add_student(self, student: Student):
        """
        Saves a Student object and their marks to the database.
        
        Args:
            student (Student): The student object to save.
        """
        cursor = self._get_cursor()
        try:
            # 1. Insert Student
            cursor.execute(queries.INSERT_STUDENT, (student.name,))
            student_id = cursor.lastrowid
            
            # 2. Insert Marks (Relational)
            if student.marks:
                # Prepare a list of tuples: (student_id, mark_value)
                grades_data = [(student_id, mark) for mark in student.marks]
                cursor.executemany(queries.INSERT_GRADE, grades_data)
            
            # Commit is handled by the Context Manager (__exit__)
            
        except sqlite3.Error as e:
            print(f"❌ Error adding student: {e}")
            raise

    def get_all_students(self):
        """
        Retrieves all students and their grades, returning hydrated objects.

        Returns:
            list[Student]: List of Student objects with IDs, names, and marks.
        """
        cursor = self._get_cursor()
        students_map = {} # Dictionary to group marks by student_id

        try:
            # 1. Get all students
            cursor.execute(queries.SELECT_ALL_STUDENTS)
            student_rows = cursor.fetchall()

            for row in student_rows:
                s_id, name = row
                # Instantiate the Dumb Class (Data Container)
                student = Student(student_id=s_id, name=name)
                students_map[s_id] = student

            # 2. Get all grades
            # Assuming queries.SELECT_ALL_GRADES returns (student_id, mark_value)
            cursor.execute(queries.SELECT_ALL_GRADES)
            grade_rows = cursor.fetchall()

            for row in grade_rows:
                s_id, mark = row
                if s_id in students_map:
                    students_map[s_id].marks.append(mark)

            return list(students_map.values())

        except sqlite3.Error as e:
            print(f"❌ Error retrieving students: {e}")
            return []

    def update_student(self, student: Student):
        """
        Updates a student's name and overwrites their grades.
        """
        cursor = self._get_cursor()
        try:
            # 1. Update Name
            cursor.execute(queries.UPDATE_STUDENT_DATA, (student.name, student.student_id))

            # 2. Update Grades (Strategy: Delete all old, insert all new)
            cursor.execute(queries.DELETE_GRADES_FOR_STUDENT, (student.student_id,))
            
            if student.marks:
                grades_data = [(student.student_id, mark) for mark in student.marks]
                cursor.executemany(queries.INSERT_GRADE, grades_data)
                
        except sqlite3.Error as e:
            print(f"❌ Error updating student: {e}")
            raise

    def delete_student(self, student_id: int):
        """Deletes a student (Cascading delete handles grades)."""
        cursor = self._get_cursor()
        try:
            cursor.execute(queries.DELETE_STUDENT_BY_ID, (student_id,))
        except sqlite3.Error as e:
            print(f"❌ Error deleting student: {e}")
            raise