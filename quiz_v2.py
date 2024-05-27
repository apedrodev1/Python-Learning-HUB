print('Bem-vindo ao Quiz!')

answer_user = input('Deseja começar? (S/N): ').upper()

if answer_user != 'S':
    quit()

score = 0
total_questions = 2

print('Começando...')

# Dicionário de perguntas e respostas
questions = {
    "Quem desenvolveu o jogo Grand Theft Auto (GTA)?": {
        "opcoes": ["A) Rockstar Games", "B) Ubisoft", "C) Activision", "D) EA"],
        "resposta": "A"
    },
    "Qual o nome do protagonista em GTA San Andreas?": {
        "opcoes": ["A) Carlos John", "B) Carl Johnson", "C) Cassius Joe", "D) Carlos Jay"],
        "resposta": "B"
    }
}

# Loop para iterar sobre as perguntas
for index, (pergunta, detalhes) in enumerate(questions.items(), start=1):
    print(f'\nPergunta {index}/{total_questions}:')
    print(pergunta)
    for opcao in detalhes["opcoes"]:
        print(opcao)
    resposta = input('Resposta: ').upper()

    if resposta == detalhes["resposta"]:
        print('Parabéns!!! Você acertou!')
        score += 1
    else:
        print(f'Que pena! Você errou... A resposta correta é a letra {detalhes["resposta"]}')

print(f'\nO Quiz acabou... Pontuação: {score}/{total_questions}')
