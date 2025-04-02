#modulos


print('Bem vindo ao xxxx (nome do programa)!\n')
students_quantity = input('Voce deseja calcular a medias de quantos alunos hoje? ') 
way_to_calculate = input('Deseja usar a media aritimetica ou ponderada? (Use 0 para aritmetica e 1 para ponderada)')
passing_grade = input('Qual sera a nota da media?')

while students_quantity != 0:
    student_name = input('Qual o nome do Aluno?')
    
    student = Student(student_name, passing_grade, way_to_calculate)  
    fill_marks(student) 
        
