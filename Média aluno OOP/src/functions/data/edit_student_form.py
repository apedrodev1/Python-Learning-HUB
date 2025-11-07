"""
Handles the user interface for editing a single student.

This module provides the "form" (a console menu) that allows a user
to modify the attributes of a single, selected Student object and
persist those changes to the database via the repository.
"""

def show_edit_form(student, repository):
    """
    Displays an interactive menu to edit a single student's data.

    This function loops until the user cancels (0) or completes an
    action (1-4). It handles user input, validates business logic
    (like matching grade/weight counts), and calls the repository
    to update or delete the student's record in the database.

    Args:
        student (Student): The Student object to be updated.
        repository (StudentRepository): The repository object to save changes.

    Returns:
        None
    """
    print(f"\n✏️  Updating data for student: {student.name} (ID: {str(student.student_id).zfill(2)})")

    while True:
        print("\nWhat would you like to update?")
        print("1 - Name")
        print("2 - Grades")
        print("3 - Weights (only for weighted average)")
        print("4 - Delete student")
        print("0 - Cancel\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                # 1. Update the object in memory (via setter)
                student.name = input("Enter new name: ") 
                 #students_list.sort(key=lambda s: s.name) usei a mesma linha  de código do index, porém aqui não importamos students_list, esse é o caminho? importar?
                # 2. Persist change to the database
                repository.update_student(student)

                print(f"✅ Name updated to: {student.name}")
                break # Exit form loops
            except ValueError as e:
                # This catches validation errors from the Student.name setter
                print(f"❌ {e}") 

        elif choice == "2":
            try:
                new_grades_input = input("Enter new grades (separated by space): ").split()
                
                # UI-specific business rule validation
                current_marks_count = len(student.marks)
                if len(new_grades_input) != current_marks_count:
                    print(f"❌ You must enter exactly {current_marks_count} grades.")
                    continue # Re-ask the user

                # 1. Update the object in memory (via setter)
                student.marks = new_grades_input
                # 2. Persist change to the database
                repository.update_student(student)

                print(f"✅ Grades updated. Average: {student.average:.2f}")
                break
            except ValueError as e:
                # This catches validation errors from the Student.marks setter
                print(f"❌ {e}")

        elif choice == "3" and student.is_weighted:
            try:
                new_weights_str = input("Enter new weights (separated by space): ")
                new_weights_input = new_weights_str.split() 

                # UI-specific business rule validation
                current_marks_count = len(student.marks)
                if len(new_weights_input) != current_marks_count:
                    print(f"❌ You must enter exactly {current_marks_count} weights (to match the {current_marks_count} grades).")
                    continue
                
                new_weights_list = [float(w) for w in new_weights_input]
                
                # 1. Update the object in memory (via setter)
                student.weights_marks = new_weights_list
                # 2. Persist change to the database
                repository.update_student(student)

                print(f"✅ Weights updated.")
                break
            except ValueError as e:
                # Catches errors from the setter OR the float() conversion
                print(f"❌ Error to update the weights : {e}")
            except Exception as e:
                # Catches non-float inputs (e.g., 'a b c')
                print(f"❌ Invalid output. Make sure to write only numbers: {e}")

        elif choice == '4':
            confirm = input(f"⚠️  Are you sure you want to delete {student.name}? (y/n): ").lower()
            if confirm == 'y':
                try:
                    # 1. Delete from the database
                    repository.delete_student(student.student_id)
                    # 2. Update the in-memory object (for the manage_students loop)
                    student.mark_as_deleted()
                    
                    print("\n🗑️  Student successfully deleted.") 
                    break
                except Exception as e:
                    # Catch any potential DB errors
                    print(f"❌ Error while deleting student: {e}")
            else:
                print("❌ Deletion canceled.")

        elif choice == "0":
            print("❌ Update canceled.")
            break

        else:
            print("⚠️  Invalid choice. Please choose a number between 0 and 4.")