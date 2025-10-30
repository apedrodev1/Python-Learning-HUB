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
            try:
                # 1. Pede o novo nome
                new_name_input = input("Enter new name: ")
                # 2. Tenta atribuir. O setter @name.setter na classe Student
                #    vai rodar a validação.
                student.name = new_name_input
                
                # 3. Se chegou aqui, a validação passou
                print(f"✅ Name updated to: {student.name}")
                break # Sucesso, sai do loop de update
            except ValueError as e:
                # 4. Se a atribuição falhou, o setter levantou um ValueError.
                #    Nós o capturamos aqui e mostramos ao usuário.
                print(f"❌ {e}")
                # O loop continua, pedindo uma nova escolha.

        elif choice == "2":
            try:
                new_grades_input = input("Enter new grades (separated by space): ").split()
                
                # valida se quantidade de novas notas inseridas é == a quantidade de notas setadas inicialmente testar
                if len(new_grades_input) != len(student.marks): 
                    print(f"❌ You must enter exactly {len(student.marks)} grades.")
                    continue
                # Tenta atribuir a lista de strings. O setter @marks.setter
                # na classe Student vai lidar com a validação de cada item.
                student.marks = new_grades_input
                
                # Se passou, usa a property .average para mostrar o resultado
                print(f"✅ Grades updated. Average: {student.average:.2f}")
                break
            except ValueError as e:
                # O @marks.setter falhou em UMA ou mais notas
                print(f"❌ {e}")

        elif choice == "3" and student.is_weighted:
            try:
                new_weights_str = input("Enter new weights (separated by space): ")
                if len(new_weights_str.strip().split()) != len(student.marks):
                    print(f"❌ You must enter exactly {len(student.marks)} weights.")
                    continue
                # O setter @weights_marks.setter espera uma lista de floats,
                # não de strings. Precisamos convertê-la primeiro.
                new_weights_list = [float(w) for w in new_weights_str.split()]
                
                # Agora sim, passamos a lista de floats para o setter
                student.weights_marks = new_weights_list
                print(f"✅ Weights updated.")
                break
            except ValueError as e:
                # Pode dar erro na conversão float(w) ou no setter
                print(f"❌ Erro ao atualizar pesos: {e}")
            except Exception as e:
                # Captura outros erros, ex: digitar 'a b c'
                print(f"❌ Entrada inválida. Certifique-se de digitar apenas números: {e}")

        elif choice == '4':
            # Esta lógica está perfeita e não mexe com os setters
            # que nós criamos, então não precisa de try...except
            confirm = input(f"⚠️  Are you sure you want to delete {student.name}? (y/n): ").lower()
            if confirm == 'y':
                student.deleted = True # Cria o atributo 'deleted'
                print("\n🗑️  Student successfully deleted.") 
                break
            else:
                print("❌ Deletion canceled.")

        elif choice == "0":
            print("❌ Update canceled.")
            break

        else:
            print("⚠️  Invalid choice. Please choose a number between 0 and 4.")