"""
Utility functions for formatting student data into colored console strings.

This module provides helper functions that take a Student object
and return a formatted, color-coded string suitable for
different parts of the console UI (e.g., reports, edit lists).
"""

from .colors import GREEN, RED, BLUE, YELLOW, RESET

def format_student_line_for_edit(student):
    """
    Returns a concise formatted line for the student editing interface.

    Shows ID, name, average, condition, and passing grade with colors.

    Args:
        student (Student): The Student object to format.

    Returns:
        str: A formatted, colored string for the editing list.
    """
    avg = student.average
    condition = student.condition

    avg_color = GREEN if avg >= student.passing_grade else RED
    condition_color = GREEN if condition == "Approved" else RED

    return (f"ID:{BLUE} {str(student.student_id).zfill(2):<3}{RESET} | "
            f"Name: {student.name:<20} | "
            f"Average: {avg_color}{avg:<6.2f}{RESET} | "
            f"Status: {condition_color}{condition:<9}{RESET} | "
            f"Passing Grade: {YELLOW}({str(student.passing_grade).rjust(4)}){RESET}")


def format_student_row_for_show(student): 
    """
    Returns a detailed formatted row for display in the main report table.

    Ideal for the `display_students` function. Shows ID, name, full marks list,
    average, condition, and passing grade with colors.

    Args:
        student (Student): The Student object to format.

    Returns:
        str: A formatted, colored string for the main report table.
    """
    avg = student.average
    condition = student.condition

    avg_color = GREEN if avg >= student.passing_grade else RED
    condition_color = GREEN if condition == "Approved" else RED

    return (f"{BLUE}{str(student.student_id).zfill(2):<5}{RESET} "
            f"{student.name:<20} "
            f"{str(student.marks):<20} "
            f"{avg_color}{avg:<10.2f}{RESET} "
            f"{condition_color}{condition:<15}{RESET} "
            f"{YELLOW}({str(student.passing_grade).rjust(4)}){RESET}")