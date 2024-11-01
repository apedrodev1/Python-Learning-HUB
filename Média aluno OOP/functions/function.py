import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def fill_marks(self):
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
                mark = float(input(f'Digite a nota {i} de {self.name}: '))
                if 0 <= mark <= 10:
                    self.marks.append(mark)
                    break
                else:
                    print("Por favor, insira um número entre 0 e 10.")
            except ValueError:
                print("Por favor, insira um número válido.")

        # Agora pedimos o peso de cada nota
        while True:
            try:
                weight = float(input(f'Digite o peso para a nota {i} (exemplo: 1.0, 2.5): '))
                if weight > 0:
                    self.weighted_marks.append(weight)
                    break
                else:
                    print("O peso deve ser um número positivo.")
            except ValueError:
                print("Por favor, insira um peso válido.")

    # Escolha de média
    while True:
        choice = input("Deseja calcular a média (A)ritmética ou (P)onderada? ").strip().upper()
        if choice == 'A':
            self.final_mark = self.calculate_media_arithmetic()
            break
        elif choice == 'P':
            self.final_mark = self.calculate_weighted_media()
            break
        else:
            print("Opção inválida! Digite 'A' para Aritmética ou 'P' para Ponderada.")

    self.condition = self.check_condition()
