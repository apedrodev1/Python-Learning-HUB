from .update_student_data import update_student
from ..validations import validate_id


def edit_student_data(student_list):
    '''
    Allows the user to edit one or more students in the list.

    Args:
        student_list (list): List containing all Student instances.

    Returns:
        bool: True if at least one edition occurred, else False.
    '''
    edit_any = input('\n✏️ Would you like to edit any student? (y/n):  ').lower()
    edited = False

    if edit_any == 'y':
        while True:
            # Exibe a lista de IDs disponíveis
            print("\n📋 Available student IDs:\n")
            for student in student_list:
                print(f"• 🆔 {str(student.student_id).zfill(2)} - 📘 Name: {student.name} - 💯 Passing Grade: {student.passing_grade}  ")

            while True:
                input_raw = input('\nPlease type the student ID: ')
                input_id, error = validate_id(input_raw)
                if error:
                    print(f'❌ {error}')
                else:
                    break

            found = False
            for student in student_list:
                if student.student_id == input_id:
                    update_student(student)
                    edited = True
                    found = True
                    break

            if not found:
                print("❌ No student found with that ID.")

            another = input('\n✏️ Would you like to edit another student? (y/n): ').lower()
            if another != 'y':
                break

    return edited