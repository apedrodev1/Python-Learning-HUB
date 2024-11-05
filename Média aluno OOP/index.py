from classes.classStudent import Student
from functions.function import clear_screen, fill_marks
from functions.export_functions import export_to_json, export_to_xml

while True:
    student_name = input('Enter the student\'s name: ')
    
    # Validate student name
    if student_name.isalpha():  
        while True:
            try:
                passing_grade = float(input("Enter the required average for passing (between 0 and 10): "))
                if 0 <= passing_grade <= 10:  
                    break  
                else:
                    print("The average must be between 0 and 10. Please try again.")
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
        print(f'{"Required Average":<15} | {student.final_mark:>10.2f}')
        print(f'{"Student s Average":<15} | {student.final_mark:>10.2f}') # Resover o Student's depois dificuldade com ' e "
        print('-----------------------------')
        print(f'{"Status":<15} | {student.condition:>10}')

        # Export data after showing the report
        export_to_json(student)
        export_to_xml(student) #laco while sobrescreve o arquivo com o ultimo aluno inserido, criar lista next feature 

        student.marks.clear()  # Clears marks after display

    else:
        print('Please enter a valid name containing only letters.')
        continue  

    continue_input = input('Do you want to add another student? (Y/N): ').lower()
    clear_screen()  
    if continue_input == 'n':
        print('Closing the program... See you next time!')
        break  


