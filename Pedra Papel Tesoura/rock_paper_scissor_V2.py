import random

CHOICES = ["r", "p", "s"]
CHOICES_DICT = {"r": "Pedra", "p": "Papel", "s": "Tesoura"}

def get_user_choice():
    user_input = input("Escolha [R] para Pedra, [P] para Papel ou [S] para Tesoura: ").lower()
    if user_input in CHOICES:
        return user_input
    else:
        print("Escolha inválida! Tente novamente.")
        return get_user_choice()

def get_computer_choice():
    return random.choice(CHOICES)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return f"Empate! Ambos escolheram {CHOICES_DICT[user_choice]}."
    elif (user_choice == "r" and computer_choice == "s") or \
         (user_choice == "p" and computer_choice == "r") or \
         (user_choice == "s" and computer_choice == "p"):
        return f"Você ganhou! {CHOICES_DICT[user_choice]} vence {CHOICES_DICT[computer_choice]}."
    else:
        return f"Você perdeu! {CHOICES_DICT[computer_choice]} vence {CHOICES_DICT[user_choice]}."

def play_game():
    score = {"Vitórias": 0, "Derrotas": 0, "Empates": 0}
    
    timesToPlay = int(input('Quantos rounds iremos jogar? '))
    
    for _ in range(timesToPlay):
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Você escolheu: {CHOICES_DICT[user_choice]}")
        print(f"O computador escolheu: {CHOICES_DICT[computer_choice]}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if "ganhou" in result:
            score['Vitórias'] += 1
        elif "perdeu" in result:
            score['Derrotas'] += 1
        else:
            score['Empates'] += 1
        
        print(f"Placar: Vitórias: {score['Vitórias']}, Derrotas: {score['Derrotas']}, Empates: {score['Empates']}")
    
    print("Jogo encerrado!")
    print(f"Resultado final: Vitórias: {score['Vitórias']}, Derrotas: {score['Derrotas']}, Empates: {score['Empates']}")

if __name__ == "__main__":
    play_game()