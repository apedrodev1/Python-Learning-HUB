# Calculating Student Averages 🌐

<br>

## Description

This project calculates student averages using Object-Oriented Programming (OOP) principles in Python. The system allows for both arithmetic and weighted averages based on user input and provides a simple report card with each student's status (pass or fail) based on a customizable passing average.

The application has evolved into a modular and scalable solution, now supporting full CRUD operations on student records and strict adherence to [PEP 257](https://peps.python.org/pep-0257/) conventions for documentation.

<br>

## How to Use

1. **Clone the Repository**

<br>

2. Clone this repository to your local environment:

- Copy code:

  ```bash
  git clone https://github.com/apedrodev1/Python-Learning-HUB/tree/main/M%C3%A9dia%20aluno%20OOP
  ```

<br>

3. **Open the Project in Your IDE**  
   *(Make sure you have the Python extension installed)*

<br>

4. Open the `index.py` file in your preferred IDE.

<br>

5. Open a terminal, navigate to the project directory, and start the program:

```bash
python index.py
```

<br>

6. **Interact with the Program**

<br>

---

## ✅ Logical Order Summary

### 🧠 Program Flow

```python
get_main_parameters()
process_students(students_quantity, way_to_calculate, passing_grade, weights)
show_student_list()

if user_wants_to_correct:
    correct_students()
    show_student_list()  # after correction

if user_wants_to_export:
    export_students()

ask_to_retry()
```

<br>

### 👤 User Flow

1. **Input of Initial Data**
   - Type of average (simple or weighted)
   - Minimum passing grade
   - Weights of the grades (if weighted)
   - Number of students

2. **Filling Student Data**
   - Name
   - Grades

3. **Displaying Report**
   - Student's name
   - Final average
   - Status (Passed/Failed)

4. **Optional Correction**
   - Name and/or grades
   - Re-displays corrected report

5. **Optional Export**
   - JSON or XML format

6. **Program Repeat Option**

---

## 🚀 Features

- **Object-Oriented Design**  
  Centralized in a `Student` class with behaviors like average calculation and data editing.

- **CRUD Support**  
  Students can now be created, read, updated, and deleted dynamically during execution.

- **Modular & Scalable Structure**  
  - Files separated by responsibility: `data/`, `export/`, `utils/`, and `validations/`
  - Easily extensible for new features like filtering, sorting, or different user roles.

- **PEP 257 Compliance**  
  All functions and classes include clear, standardized docstrings.

- **User Choice for Average Type**  
  Arithmetic or weighted, based on your criteria.

- **Validated Input Flow**  
  Input is thoroughly validated for type and bounds.

- **Clean Terminal UI**  
  Screens are cleared between steps (where supported) to avoid clutter.

- **Detailed Report Card Output**  
  Includes:
  - Name  
  - Grades and Weights (if any)  
  - Required average  
  - Calculated final average  
  - Final pass/fail status

- **Data Export in JSON/XML**  
  Supports integration or backup in standard formats.

---

## 🗂️ Folder Structure

```
Média aluno OOP/
│
├── index.py
├── README.md
│
├── src/
│   ├── classes/
│   │   └── Student.py
│   │
│   ├── functions/
│   │   ├── data/
│   │   │   ├── edit_student.py
│   │   │   └── update_student_data.py
│   │   │
│   │   ├── export/
│   │   │   ├── export_wrapper.py
│   │   │   ├── json_exporter.py
│   │   │   └── xml_exporter.py
│   │   │
│   │   ├── loop_control.py
│   │   ├── main_function.py
│   │   ├── parameters.py
│   │   ├── show_students.py
│   │   └── validations.py
│   │
│   └── utils/
│       ├── colors.py
│       └── formatters.py
```