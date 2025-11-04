"""
Manages the high-level student editing workflow.

This module acts as the orchestrator for editing. It displays the
list of students, prompts for an ID, and then calls the
'edit_student_form' (show_edit_form) for the selected student.
"""

from .edit_student_form import show_edit_form
from ..loop_control import clear_screen
from .. .utils.formatters import format_student_line_for_edit
from ..validations import (
    validate_id,
    validate_yes_no
)

def edit_student_edits(student_list, repository):
    """
    Manages the interactive loop for editing and deleting students.

    This function first asks the user if they wish to edit any students.
    If yes, it displays a list of active (non-deleted) students and
    prompts for an ID. It then calls 'show_edit_form' for the selected
    student, passing the repository to persist changes.

    It also handles the local (in-memory) removal of students who are
    marked as deleted by the form, so they do not re-appear in the
    "Available for Editing" list during the same session.

    Args:
        student_list (list[Student]): The current in-memory list of
                                      Student objects (from get_all_students).
        repository (StudentRepository): The database repository object,
                                        which will be passed to the edit form.

    Returns:
        bool: True if at least one edit was initiated, False otherwise.
    """

    if not student_list:
        print("❌ No students available to edit.")
        return False

    while True:
        edit_any_input = input('\n ✏️  Would you like to edit any student? (y/n): ')
        edit_any, error = validate_yes_no(edit_any_input)
        if error:
            print(f"❌ {error}")
        else:
            break

    if edit_any == 'n':
        return False

    edited = False

    while True:
        clear_screen()
        # Filter out students marked as deleted during this session
        active_students = [s for s in student_list if not s.is_deleted]

        print("\n📋 Students Available for Editing:\n")
        print("─" * 100)

        if not active_students:
            print("❌ No students available for editing.")
            return edited 

        
        for student in active_students:
            print(format_student_line_for_edit(student))

        print("─" * 100)

        # Loop to get a valid student ID from the user
        while True:
            input_raw = input('\n🔍  Please type the student ID to edit: ')
            input_id, error = validate_id(input_raw)
            if error:
                print(f'❌ {error}')
            else:
                break

        # Find the student in the list
        found = False
        for student in student_list:
            if student.student_id == input_id:
                # Call the edit form, passing the specific student and the repo
                show_edit_form(student, repository)
                edited = True
                found = True

                # If the form deleted the student, remove them from the
                # in-memory list so they don't appear in the next loop.
                if student.is_deleted: 
                    student_list.remove(student)
                break

        if not found:
            print("❌ No student found with that ID.")

        # Loop to ask the user if they want to edit another student
        while True:
            another_input = input('\n✏️  Would youD like to edit another student? (y/n): ')
            another, error = validate_yes_no(another_input)
            clear_screen()
            if error:
                print(f"❌ {error}")
            else:
                break

        if another == 'n':
            break # Exit the main editing loop

    return edited