def display_students(student_list):
    """
    Displays the processed data of students in a readable format.
    
    Args:
        student_list (list): A list of student objects to be displayed.
    """
    
    print("\n📊 Students Report:")

    if not student_list:
        print('❌ No students found.')
        return

    # Loop through each student and display their data
    for student in student_list:
        print(f"\n🆔 {str(student.student_id).zfill(2)} | 📘 Name: {student.name}")
        print(f"📋 Status: {student.condition}")
        print(f"📈 Grades: {student.marks}")
        
        if student.is_weighted:
            print(f"⚖️ Weights: {student.weights_marks}")
        
        print(f"🔢 Average: {student.calculate_average():.2f}")
        print(f"💯 Passing Grade: {student.passing_grade}")
        print("-" * 40)
