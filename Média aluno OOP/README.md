
# Calculating Student Averages

<br>

## Description
This project calculates student averages using Object-Oriented Programming (OOP) principles in Python. The system allows for both arithmetic and weighted averages based on user input and provides a simple report card with each student's status (pass or fail) based on a customizable passing average.

<br>

## How to Use

1. Clone the Repository

<br>

2. Clone this repository to your local environment:
   
- Copy code:
  
  - <code>git clone <https://github.com/apedrodev1/Python-Learning-HUB/tree/main/M%C3%A9dia%20aluno%20OOP></code>

<br>

3. Open the Project in Your IDE
 (make sure you have the python extention installed)  

<br>

4. Open the `index.py` file in your preferred IDE.

<br>

5. Open a terminal, navigate to the project directory, and start the program:  <code>python index.py</code>


<br>

6. Interact with the Program

<br>

## Run the Program:

- Set how many students, You would like to calculate averages.
- Choose the type of average calculation: arithmetic or weighted.
- Set the required passing average.
- Enter the desired grades (and weights, if weighted average is chosen).
- View the generated report card, showing grades, required average, student’s average, and pass/fail status.
- Edit or correct grade or student's name.
- Repeat or Exit
- The program will prompt you to add another student or exit.

<br>


# ✅ Logical Order Summary

## 🧠 Program Flow

<code>get_main_parameters()
process_students(students_quantity, way_to_calculate, passing_grade, weights)
show_student_list()

if user_wants_to_correct:
    correct_students()
    show_student_list()  # após correção

if user_wants_to_export:
    export_students()

ask_to_retry()</code>

<br>

## 👤 User Flow

1. Input of initial data:

    - Type of average (simple or weighted)

 - Minimum passing grade

- Weights of the grades (if weighted)

- Number of students

2. Filling in information for each student:

- Name

- Grades

3. Displaying the list with:

- Student's name

- Final average

- Status (Passed/Failed)

4. Data correction (if the user desires):

- Name and/or grades

- Re-display the list with corrected data

5. Exporting data (if the user desires):

- Possible formats: JSON or XML

6. Asking if the user wants to run the program again

## Features:

- Object-Oriented Design: Utilizes a Student class with methods for calculating arithmetic and weighted averages.
- User Choice for Average Type: Choose between an arithmetic or weighted average based on your needs.
- Dynamic Grade and Weight Entry: Allows you to enter multiple grades, with optional weights for each grade if a weighted average is selected.
- Clear Screen Functionality: For a cleaner and more organized user experience.
- Report Card Display: Shows each student’s name, grades, required average, calculated average, and pass/fail status.
- Data Export in JSON and XML: Provides the option to export student data in JSON and XML formats, making it easy to save, share, and integrate with other systems.

<br>

## Folder structure:

- The folder structure was organized as follows:

![image](https://github.com/user-attachments/assets/6e380cbb-c447-4e9d-ac91-4d678e3c2879)

</br>
<div style="text-align:center;">






