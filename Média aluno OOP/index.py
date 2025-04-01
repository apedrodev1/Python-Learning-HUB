from classes.classStudent import Student
from functions.main_function import fill_marks
from functions.data_validation import validation_grade, validation_input, validation_weigth
from functions.clear_screen import clear_screen
from functions.export_functions import export_to_json, export_to_xml


students_list = []

while True:
    student_name = input('Enter the student\'s name: ')
    
    if student_name.isalpha():  
        while True:
            try:
                passing_grade = float(input("Enter the required average for passing (between 0 and 10): "))
                if validation_input(passing_grade, 0, 10, "required average"):
                    break  
            except ValueError:
             print("Please enter a valid number for the average.")
        
        student = Student(student_name, passing_grade)  
        fill_marks(student) 

        # Display the report card
        print(f'Report card for {student.name}')
        print('#############################')
        print(f'{"Grades":<12} | {"Values":>10}')
        print('-----------------------------')

        for i, grade in enumerate(student.marks, 1):
            print(f'Grade {i:<7} | {grade:>10.2f}')

        print('-----------------------------')
        print(f'{"Required Average":<15} | {student.passing_grade:>10.2f}')
        label = "Student's Average"
        print(f"{label:<15} | {student.final_mark:>10.2f}")

 
        print('-----------------------------')
        print(f'{"Status":<15} | {student.condition:>10}')

        # Export data after showing the report
        export_to_json(students_list)
        export_to_xml(students_list)

        student.marks.clear()  # Clears marks after display

    else:
        print('Please enter a valid name containing only letters.')
        continue  

    continue_input = input('Do you want to add another student? (Y/N): ').lower()
    clear_screen()  
    if continue_input == 'n':
        print('Closing the program... See you next time!')
        break  


students_list.append(student)

