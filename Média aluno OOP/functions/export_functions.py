import json
import xml.etree.ElementTree as ET

def export_to_json(student, filename='student_data.json'):
    data = {
        'name': student.name,
        'passing_grade': student.passing_grade,
        'marks': student.marks,
        'final_mark': student.final_mark,
        'condition': student.condition,
        'weighted_marks': student.weighted_marks if student.is_weighted else None,
    }
    
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Data exported to {filename}")


def export_to_xml(student, filename='student_data.xml'):
    student_element = ET.Element('Student')
    ET.SubElement(student_element, 'Name').text = student.name
    ET.SubElement(student_element, 'PassingGrade').text = str(student.passing_grade)
    
    marks_element = ET.SubElement(student_element, 'Marks')
    for mark in student.marks:
        ET.SubElement(marks_element, 'Mark').text = str(mark)

    ET.SubElement(student_element, 'FinalMark').text = str(student.final_mark)
    ET.SubElement(student_element, 'Condition').text = student.condition

    if student.is_weighted:
        weights_element = ET.SubElement(student_element, 'WeightedMarks')
        for weight in student.weighted_marks:
            ET.SubElement(weights_element, 'Weight').text = str(weight)
    
    tree = ET.ElementTree(student_element)
    tree.write(filename, encoding='utf-8', xml_declaration=True)
    print(f"Data exported to {filename}")