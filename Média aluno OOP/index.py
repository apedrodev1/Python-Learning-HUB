from classes.classStudent import Student
from functions.function import clear_screen, fill_marks

while True:
    aluno_nome = input('Digite o nome do Aluno: ')
    
    # verifica:  nome do aluno
    if aluno_nome.isalpha():  
        while True:
            try:
                passing_mark = float(input("Digite a média necessária para aprovação (entre 0 e 10): "))
                if 0 <= passing_mark <= 10:  
                    break  
                else:
                    print("A média deve estar entre 0 e 10. Tente novamente.")
            except ValueError:
                print("Por favor, insira um número válido para a média.")
        
        # decide se será aritmética ou ponderada
        while True:
            media_type = input("Escolha o tipo de média: Aritmética (A) ou Ponderada (P): ").upper()
            if media_type in ('A', 'P'):
                is_weighted = (media_type == 'P')
                break
            else:
                print("Por favor, escolha 'A' para Aritmética ou 'P' para Ponderada.")

        aluno = Student(aluno_nome, passing_mark, is_weighted)  
        fill_marks(aluno) 

        # Exibe boletim
        print(f'Boletim de {aluno.name}')
        print('#############################')
        print(f'{"Notas":<12} | {"Valores":>10}')
        print('-----------------------------')

        for i, grade in enumerate(aluno.marks, 1):
            print(f'Nota {i:<7} | {grade:>10.2f}')

        print('-----------------------------')
        print(f'{"Média Necessária":<15} | {aluno.passing_mark:>10.2f}')
        print(f'{"Média do Aluno ":<15} | {aluno.final_mark:>10.2f}')
        print('-----------------------------')
        print(f'{"Situação":<15} | {aluno.condition:>10}')

        aluno.marks.clear()  # Limpa as notas após exibição

    else:
        print('Por favor, insira um nome válido contendo apenas letras.')
        continue  

    continuar = input('Deseja adicionar outro aluno? (S/N): ').lower()
    clear_screen()  
    if continuar == 'n':
        print('Encerrando o programa... Até a próxima vez!')
        break  
