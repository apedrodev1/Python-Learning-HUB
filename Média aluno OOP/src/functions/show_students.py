def display_students(student_list):
    
    print("\n📊 Students Report:")

    if not student_list:
        print('❌ No students found.')
        return


    for student in student_list:
        print(f"\n📘 Name: {student.name}")
        print(f"📋 Status: {student.condition}")
        print(f"📈 Grades: {student.marks}")
        if student.is_weighted:
            print(f"⚖️  Weights: {student.weights_marks}")
        print(f"🔢 Average: {student.calculate_average():.2f}")
        print(f"💯 Passing Grade: {student.passing_grade}")
        print("-" * 40)  