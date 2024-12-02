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

    
        
def validation_grade_value(grade):
    if 0 <= grade <= 10:  
        return True
    else:
        print("Please enter a grade between 0 and 10.")
        return False
    


def validation_weigth(weigth):
    if weigth > 0:
        return True
    else:
        print("Please enter a valid positive number for the weight.")
        return False
