from ..utils.formatters import format_student_row_for_show

def display_students(student_list):
    """
    Displays the processed data of students in a readable table format.
    
    Args:
        student_list (list): A list of student objects to be displayed.
    """
    print("\n📊 Students Report:")

    if not student_list:
        print('❌ No students found.')
        return

    # Agora seguro: só acessa o primeiro elemento após checar se lista não está vazia
    type_label = "Weighted" if student_list[0].is_weighted else "Arithmetic"
    print(f"\n🧮 Average Calculation Type: {type_label}")

    print("─" * 100)
    print(f"{'ID':<5} {'Name':<20} {'Grades':<20} {'Average':<10} {'Status':<15} {'Passing Grade'}")
    print("─" * 100)

    for student in student_list:
        print(format_student_row_for_show(student))

    print("─" * 100)
