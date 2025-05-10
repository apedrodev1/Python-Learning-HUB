from src.functions.validations import ( 
    validate_names,
    validate_weights
)


def update_student(student):
    """
    Updates the data of a single student object.

    Args:
        student (Student): The student instance to be updated.

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
            new_name, error = validate_names(input("Enter new name: "))
            if error:
                print(f"❌ {error}")
            else:
                student.name = new_name
                print(f"✅ Name updated to: {student.name}")
                break

        elif choice == "2":
            new_grades = input("Enter new grades (separated by space): ").split()
            student.add_marks(new_grades)
            if error:
                print(f"❌ {error}")
            else:
                student.add_marks(new_grades)
                student.check_condition()
                print(f"✅ Grades updated. Average: {student.calculate_average():.2f}")
                break

        elif choice == "3" and student.is_weighted:
            new_weights_str = input("Enter new weights (separated by space): ")
            new_weights, error = validate_weights(new_weights_str)
            if error:
                print(f"❌ {error}")
            else:
                student.weights_marks = new_weights
                print(f"✅ Weights updated.")
                break

        elif choice == '4':
            confirm = input(f"❗ Are you sure you want to delete {student.name}? (y/n): ").lower()
            if confirm == 'y':
                student.deleted = True
                print("\n🗑️  Student successfully deleted.") #Quando deleta todos, o mesmo nao exibe nada, ver o que sera feito, pois e uma situacao comum, talvez exibir uma mensagem dizendo que a lista de estudates esta vazia e sair da funcao edit, cair na ask to retry, e de se pensar de integrar uma condicao na proxima funcao(exportar), pois se estiver vazia, pulamos ela e perguntamos se o usario que rodar o programa novamente
                break
            else:
                print("❌ Deletion canceled.")

        elif choice == "0":
            print("❌ Update canceled.")
            break

        else:
            print("❌ Invalid choice. Please choose a number between 0 and 4.")
