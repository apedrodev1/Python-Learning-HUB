#refator class Student um arquivo, funcoes outro, e o while como o script
#checar validacoes de entrada, definir range de notas p/ 0 a 10
#criar a funcao calcMediaPonderada e criar um swtich case para o usuario escolher
#criacao de um relatorio final e tambem Implementar a possibilidade de salvar os dados em um arquivo (ex: CSV, JSON) para manter o registro dos alunos e notas.
#opcao de edicao das notas 

import os

class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []
        self.final_mark = 0
        self.condition = ''

    
    def fillMarks(self):
        try:
            qtd_marks = int(input('Quantas notas deseja inserir? '))
            i = 0
            for _ in range(qtd_marks):
                i += 1 
                while True:
                    #remover os inputs apos entrada dos dados - fazer
                    try:
                        nota = float(input(f'Digite a nota {i} de {self.name}: '))
                        self.marks.append(nota)
                        break
                    except ValueError:
                        print("Por favor, insira um número válido.")
            self.calcMedia()  
        except ValueError:
            print("Por favor, insira um número válido.")    


    def calcMedia(self):
        if self.marks:
            self.final_mark = sum(self.marks) / len(self.marks)

            if self.final_mark >= 7:
                self.condition = 'Aprovado'
            else:
                self.condition = 'Reprovado'

            return self.condition
        else:
            print('Nenhuma nota foi inserida.')
            return None

#talvez mover o while para outro arquivo

while True:
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    aluno = Student(str(input('Digite o nome do Aluno: ')))
    aluno.fillMarks() 
    
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