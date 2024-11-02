import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def fill_marks(student):
    while True:
        try:
            qtd_marks = int(input('Quantas notas deseja inserir? '))
            if qtd_marks > 0:
                break
            else:
                print('Por favor, insira um número inteiro positivo.')
        except ValueError:
            print('Por favor, insira um número válido.')

    for i in range(1, qtd_marks + 1):
        while True:
            try:
                grade = float(input(f'Digite a nota {i} de {student.name}: '))
                if 0 <= grade <= 10:
                    student.marks.append(grade)
                    break
                else:
                    print("Por favor, insira um número entre 0 e 10.")
            except ValueError:
                print("Por favor, insira um número válido.")

        # Se média ponderada for selecionada, pergunte o peso
        if student.is_weighted:
            while True:
                try:
                    weight = float(input(f'Digite o peso para a nota {i}: '))
                    student.weighted_marks.append(weight)
                    break
                except ValueError:
                    print("Por favor, insira um número válido para o peso.")

    # Decide qual média calcular com base no tipo escolhido
    student.final_mark = (student.calculate_weighted_media() if student.is_weighted 
                          else student.calculate_media_arithmetic())
    student.condition = student.check_condition()
