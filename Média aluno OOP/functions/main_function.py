from functions.data_validation import validation_grade, validation_input, validation_weigth

def fill_marks(student):
    while True:
        try:
            num_grades = int(input('How many grades would you like to enter? '))
            valid_num_grades = validation_grade(num_grades)

            if valid_num_grades:
                break
        except ValueError:
            print('Please enter a valid number.')

        for i in range(1, num_grades + 1):
            while True:
                try:
                    grade = float(input(f'Enter grade {i} for {student.name}: '))
                    
                    if validation_input(grade, 0, 10, "grade"):
                        student.marks.append(grade)
                        break  
                except ValueError:
                    print("Please enter a valid number for the grade.")

        # nao funciona!!! VER! 
        if student.is_weighted:
         for i in range(num_grades):
            while True:
                try:
                    weight = float(input(f'Enter the weight for grade {i+1}: '))
                    if validation_weigth(weight):
                        student.weighted_marks.append(weight)
                    break

                except ValueError:
                    print("Please enter a valid number for the weight.")

        if student.is_weighted:
            while True:
                try:
                    weight = float(input(f'Enter the weight for grade {i}: '))
                    if validation_weigth(weight):
                        student.weighted_marks.append(weight)
                        break  
                except ValueError:
                    print("Please enter a valid number for the weight.")

                
    # Decidir qual média calcular com base no tipo escolhido 
    student.final_mark = (student.calculate_weighted_mean() if student.is_weighted 
                          else student.calculate_arithmetic_mean())
    student.condition = student.check_condition()