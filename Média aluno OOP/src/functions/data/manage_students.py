from .edit_student_form import show_edit_form
from ..loop_control import clear_screen
from .. .utils.formatters import format_student_line_for_edit
from ..validations import (
    validate_id,
    validate_yes_no
)

def edit_student_edits(student_list, repository):
    '''
    Allows the user to edit one or more students in the list. Also receives the database repository to save changes.

    Args:
        student_list (list): List containing all Student instances.

    Returns:
        bool: True if at least one edition occurred, else False.
    '''

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
        active_students = [s for s in student_list if not s.is_deleted]

        print("\n📋 Students Available for Editing:\n")
        print("─" * 100)

        if not active_students:
            print("❌ No students available for editing.")
            return edited 

         
        for student in active_students:
            print(format_student_line_for_edit(student))

        print("─" * 100)

        while True:
            input_raw = input('\n🔍  Please type the student ID to edit: ')
            input_id, error = validate_id(input_raw)
            if error:
                print(f'❌ {error}')
            else:
                break

        found = False
        for student in student_list:
            if student.student_id == input_id:
                show_edit_form(student, repository)
                edited = True
                found = True

                if student.is_deleted: 
                    student_list.remove(student)
                break

        if not found:
            print("❌ No student found with that ID.")

        while True:
            another_input = input('\n✏️  Would you like to edit another student? (y/n): ')
            another, error = validate_yes_no(another_input)
            clear_screen()
            if error:
                print(f"❌ {error}")
            else:
                break

        if another == 'n':
            break

    return edited
