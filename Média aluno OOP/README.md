
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

</br>

2. Filling in information for each student:

- Name

- Grades

</br>

3. Displaying the list with:

- Student's name,

- Final average,

- Status (Passed/Failed)

</br>

4. Data correction (if the user desires):

- Name and/or grades,

- Re-display the list with corrected data

</br>

5. Exporting data (if the user desires):

- Possible formats: JSON or XML

</br>

6. Asking if the user wants to run the program again

</br>

## 🚀 Features:

- Object-Oriented Design: Core functionality is built around a Student class that encapsulates student data and behaviors, such as calculating arithmetic and weighted averages.

- User Choice for Average Type: Flexibly choose between an arithmetic or weighted average, depending on grading needs.

- Dynamic Grade and Weight Entry: Enter any number of grades, and if using weighted averages, specify individual weights for each grade. The system ensures input validation and consistency.

- Clear and Clean User Interface: Incorporates screen-clearing between inputs (where supported) for a more organized and user-friendly experience.

-Report Card Display: After processing, the system displays a detailed report for each student, including:

    - Name

    - Grades

    - Weights (if applicable)

    - Required passing grade

    - Calculated average

    - Final pass/fail status

- Data Export in JSON and XML Formats: Student data can be easily exported in JSON and XML formats for backup, sharing, or integration with external systems.

- Modular Organization (PEP 257 Compliance):

 - The codebase is cleanly separated into modules and packages (e.g., functions/, classes/), promoting readability, maintainability, and scalability.

 - All functions and classes follow PEP 257 guidelines, meaning they include clear, concise, and standardized docstrings.


- Scalability with Design Patterns:

 - The current architecture allows easy integration of new features, such as editing students by ID, additional data exports, or new calculation types.

- Future development can leverage patterns like Abstract Factory for creating different types of students (e.g., regular, scholarship students) without altering existing code.

<br>

## 🗂️ Folder structure:

- The folder structure was organized as follows:

![image](https://github.com/user-attachments/assets/6e380cbb-c447-4e9d-ac91-4d678e3c2879)

</br>
<div style="text-align:center;">






