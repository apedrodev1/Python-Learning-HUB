import random

difficultyLevel = {
    '1': 50,
    '2': 100,
    '3': 200
}

maxAttempts = 10 

def main():
    print('Seja Bem-vindo ao Guess Number!')
    print('Escolha um nível de dificuldade:')
    print('1. Fácil (0-50)')
    print('2. Médio (0-100)')
    print('3. Difícil (0-200)')

nivel = input('Digite o número do nível desejado: ')


if nivel in difficultyLevel:
    choiceNumber = difficultyLevel[nivel]
else:
    print('Erro: nível inválido. Por favor, execute novamente e escolha um nível válido!')
    quit()

randomNumber = random.randint(0, choiceNumber)

nChoices = 0
previous_guesses = []

while nChoices < maxAttempts:
    answerUser = input('Adivinhe o número: ')
    
    if answerUser.isdigit():
        answerUser = int(answerUser)
    else:
        print('Erro: valor informado não é numérico. Favor informar um número')
        continue

    nChoices += 1
    previous_guesses.append(answerUser)

    if answerUser == randomNumber:
        print(f'Parabéns! Você acertou o número {randomNumber} em {nChoices} tentativas!')
        break

    diff = abs(answerUser - randomNumber)
    percentage_diff = (diff / randomNumber) * 100  # Porcentagem de diferença

    if answerUser > randomNumber:
            if percentage_diff > 50:
                print(f'Não foi desta vez! O número procurado é muito menor do que {answerUser}.')
            elif percentage_diff > 20:
                print(f'Não foi desta vez! O número procurado é menor do que {answerUser}, mas não muito.')
            else:
                print(f'Não foi desta vez! O número procurado é um pouco menor do que {answerUser}.')
    else:  # answerUser < randomNumber
            if percentage_diff > 50:
                print(f'Não foi desta vez! O número procurado é muito maior do que {answerUser}.')
            elif percentage_diff > 20:
                print(f'Não foi desta vez! O número procurado é maior do que {answerUser}, mas não muito.')
            else:
                print(f'Não foi desta vez! O número procurado é um pouco maior do que {answerUser}.')
    
    print(f"N° de tentativas: {nChoices}")
    print(f"Palpites anteriores: {previous_guesses}")

if nChoices == maxAttempts and answerUser != randomNumber:
    print(f'Você atingiu o número máximo de tentativas ({maxAttempts}). O número correto era {randomNumber}.')

if __name__ == '__main__':
    main()