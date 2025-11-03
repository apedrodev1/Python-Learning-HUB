def show_edit_form(student, repository):
    """
    Updates the data of a single student object.
    Args:
        student (Student): The student object to be updated.
    Returns:
        None
    """
    print(f"\n✏️ Updating data for student: {student.name} (ID: {str(student.student_id).zfill(2)})")

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
                student.name = input("Enter new name: ") 
                repository.update_student(student)

                print(f"✅ Name updated to: {student.name}")
                break 
            except ValueError as e:
                print(f"❌ {e}") 

        elif choice == "2":
            try:
                new_grades_input = input("Enter new grades (separated by space): ").split()
                current_marks_count = len(student.marks)
                if len(new_grades_input) != current_marks_count:
                    print(f"❌ You must enter exactly {current_marks_count} grades.")
                    continue

                student.marks = new_grades_input
                repository.update_student(student)

                print(f"✅ Grades updated. Average: {student.average:.2f}")
                break
            except ValueError as e:
                print(f"❌ {e}")

        elif choice == "3" and student.is_weighted:
            try:
                new_weights_str = input("Enter new weights (separated by space): ")
                new_weights_input = new_weights_str.split() 

                current_marks_count = len(student.marks)
                if len(new_weights_input) != current_marks_count:
                    print(f"❌ You must enter exactly {current_marks_count} weights (to match the {current_marks_count} grades).")
                    continue
                
                new_weights_list = [float(w) for w in new_weights_input]
                
                student.weights_marks = new_weights_list
                repository.update_student(student)

                print(f"✅ Weights updated.")
                break
            except ValueError as e:
                print(f"❌ Error to update the weights : {e}")
            except Exception as e:
                print(f"❌ Invalid output. Make sure to write only numbers: {e}")

        elif choice == '4':
            confirm = input(f"⚠️  Are you sure you want to delete {student.name}? (y/n): ").lower()
            if confirm == 'y':
                repository.delete_student(student.student_id)
                student.mark_as_deleted()
                
                print("\n🗑️  Student successfully deleted.") 
                break
            else:
                print("❌ Deletion canceled.")

        elif choice == "0":
            print("❌ Update canceled.")
            break

        else:
            print("⚠️  Invalid choice. Please choose a number between 0 and 4.")