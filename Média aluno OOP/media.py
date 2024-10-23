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


while True:
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

    continuar = input('Deseja adicionar outro aluno? (S/N): ').lower()
    if continuar == 'n':
        print('Encerrando o programa...')
        break