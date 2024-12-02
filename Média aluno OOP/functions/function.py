import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def validation_grade(num_grades):
    while True:
        try:
            if num_grades > 0:
                return num_grades
            else: 
                print('Please enter a positive integer.')
                return None
        except ValueError: 
            print('Please enter a valid number.')
            return None

def fill_marks(student):
    while True:
        try:
            num_grades = int(input('How many grades would you like to enter? '))
            valid_num_grades = validation_grade(num_grades)

            if valid_num_grades:
                break
            else:
                continue
        except ValueError:
              print('Please enter a valid number.')

    for i in range(1, valid_num_grades + 1):
        while True: 
            try:
                grade = float(input(f'Enter grade {i} for {student.name}: '))
                if 0 <= grade <= 10:
                    student.marks.append(grade)
                    break

                else:
                    print("Please enter a number between 0 and 10.")

            except ValueError:
                print("Please enter a valid number.")

        # If weighted mean is selected, ask for weight
        if student.is_weighted:
            while True:
                try:
                    weight = float(input(f'Enter the weight for grade {i}: '))
                    student.weighted_marks.append(weight)
                    break
                except ValueError:
                    print("Please enter a valid number for the weight.")

    # Decide which average to calculate based on the chosen type
    student.final_mark = (student.calculate_weighted_mean() if student.is_weighted 
                          else student.calculate_arithmetic_mean())
    student.condition = student.check_condition()










