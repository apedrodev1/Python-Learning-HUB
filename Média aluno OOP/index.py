from classes.classStudent import Student
from functions.function import clear_screen

while True:

    clear_screen()
    
    aluno_nome = input('Digite o nome do Aluno: ')
    
    if aluno_nome.isalpha():
        aluno = Student(aluno_nome)
        aluno.fill_marks()

        print(f'Boletim de {aluno.name}')
        print('#############################')
        print(f'{"Notas":<10} | {"Valores":>10}')
        print('-----------------------------')

        for i, nota in enumerate(aluno.marks, 1):
            print(f'Nota {i:<7} | {nota:>10.2f}')

        print('-----------------------------')
        print(f'{"Média":<10} | {aluno.final_mark:>10.2f}')
        print(f'{"Situação":<10} | {aluno.condition:>10}')

        aluno.marks.clear()

        continuar = input('Deseja adicionar outro aluno? (S/N): ').lower()
        if continuar == 'n':
            print('Encerrando o programa...')
            break
    