from .colors import GREEN, RED, BLUE, YELLOW, RESET

def format_student_line_for_edit(student):
    """
    Returns a concise formatted and aligned line for student editing interface.
    Shows ID, name, average, condition, and passing grade.
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
    Returns a detailed formatted and colored row for display in a report table.
    Ideal for show_students.
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
