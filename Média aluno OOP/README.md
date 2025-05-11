# Calculating Student Averages 🌐

<br>

## Description

This project calculates student averages using Object-Oriented Programming (OOP) principles in Python. The system allows for both arithmetic and weighted averages based on user input and provides a simple report card with each student's status (pass or fail) based on a customizable passing average.

The application has evolved into a modular and scalable solution, now supporting full CRUD operations on student records and strict adherence to [PEP 257](https://peps.python.org/pep-0257/) conventions for documentation.

<br>

## How to Use

1. **Clone the Repository**

2. Clone this repository to your local environment:

```bash
git clone https://github.com/apedrodev1/Python-Learning-HUB/tree/main/M%C3%A9dia%20aluno%20OOP
```

3. **Open the Project in Your IDE**  
   *(Make sure you have the Python extension installed)*

4. Open the `index.py` file in your preferred IDE.

5. Open a terminal, navigate to the project directory, and start the program:

```bash
python index.py
```

6. **Interact with the Program**

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

- **Object-Oriented Design:** Core functionality is built around a `Student` class that encapsulates student data and behaviors, such as calculating arithmetic and weighted averages.

- **User Choice for Average Type:** Flexibly choose between an arithmetic or weighted average, depending on grading needs.

- **Dynamic Grade and Weight Entry:** Enter any number of grades, and if using weighted averages, specify individual weights for each grade. The system ensures input validation and consistency.

- **Clear and Clean User Interface:** Incorporates screen-clearing between inputs (where supported) for a more organized and user-friendly experience.

- **Consistent Visual Layout:** The interface uses color formatting through `utils/colors.py`, improving readability and user engagement without making the layout visually overwhelming.

- **Report Card Display:** After processing, the system displays a detailed report for each student, including:
  - Name
  - Grades
  - Weights (if applicable)
  - Required passing grade
  - Calculated average
  - Final pass/fail status

- **Data Export in JSON and XML Formats:** Student data can be easily exported in JSON and XML formats for backup, sharing, or integration with external systems.

- **Modular Organization (PEP 257 Compliance):**  
  The codebase is cleanly separated into modules and packages (e.g., `functions/`, `classes/`), promoting readability, maintainability, and scalability.  
  All functions and classes follow PEP 257 guidelines, meaning they include clear, concise, and standardized docstrings.

- **Scalability with Design Patterns:**  
  The current architecture allows easy integration of new features, such as editing students by ID, additional data exports, or new calculation types.  
  Future development can leverage patterns like Abstract Factory for creating different types of students (e.g., regular, scholarship students) without altering existing code.

---

## 🔮 Future Features

- `test_validations.py`: Unit tests for all validation routines.
- Send the results via email.
- Add graphs or other types of reports.
- User interface (GUI or web-based).

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