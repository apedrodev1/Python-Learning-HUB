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

    
        
def validation_input(value, min_value, max_value, value_type="input"):
    if min_value <= value <= max_value:
        return True
    else:
        print(f"The {value_type} must be between {min_value} and {max_value}. Please try again.")
        return False
    


def validation_weigth(weigth):
    if weigth > 0:
        return True
    else:
        print("Please enter a valid positive number for the weight.")
        return False
