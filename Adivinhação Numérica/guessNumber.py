import random

print('Seja Bem vindo ao Guess Number!')

choiceNumber = input('Digite o número limite do desafio: ')

if choiceNumber.isdigit(): 
    choiceNumber =  int (choiceNumber)
else: 
    print('Erro: valor informado não é numérico. Por favor execute novamente e informe um número!') 
    quit()

randomNumber = random.randint(0, choiceNumber)

nChoices = 0 

while True:
    answerUser = input('Adivinhe o número: ')
    
    if answerUser.isdigit():
         answerUser = int(answerUser)
     
    else:
        print('Erro: valor informado não é númerico. Favor informar um número')
        continue

    nChoices = nChoices +1 

    if answerUser == randomNumber:
        print('Parabens! Voce acertou!')
        break
    elif answerUser > randomNumber: 
        print('Chutou alto, o número randomico e menor do que o valor inserido')
    else:
        print('Chutou baixo, o número randomico é maior do que o valor inserido')

    print("N° de tentativas: " + str(nChoices))
