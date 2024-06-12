# Jokenpo - Pedra, Papel, Tesoura

Sendo uma reprodução de um jogo infantil japonês, disponível no YouTube, criado pelo canal [Iury Rosal](https://www.youtube.com/watch?v=kO_lUkeQm4c) e disponibilizado no [repositório do GitHub](https://github.com/iuryrosal/projetos-python/tree/main/level-a/03).


</br>

## Descrição:

Este projeto é um jogo de Pedra, Papel e Tesoura em Python. Ele permite que os usuários joguem contra o computador, escolhendo entre Pedra, Papel e Tesoura através de abreviações simplificadas (R, P, S). O jogo valida as entradas do usuário, calcula os resultados e exibe um placar atualizado após cada rodada. O usuário também pode definir quantos rounds deseja jogar. O código é organizado em funções modulares para facilitar a manutenção e melhorar a legibilidade.

</br>

## Como utilizar: 
1. Clone o repositório:
   ```bash
   git clone https://github.com/apedrodev1/Python-Learning-HUB/tree/main/Pedra%20Papel%20Tesoura
  
2. Abra o console da sua IDE.

3. Navegue até o diretório do projeto:
    ```bash
   cd Pedra Papel Tesoura
4. Execute o jogo com o seguinte comando:
     ```bash
     python rock_paper_scissor.py
</br>

# Melhorias propostas em rock_paper_scissor_V2.py:
</br>

## 1 - Estrutura Modular:

- Funções Separadas: No código melhorado, as funcionalidades são separadas em funções (get_user_choice, get_computer_choice, determine_winner, play_game). Isso facilita a manutenção, leitura e testes individuais das partes do código.
Responsabilidade Única: Cada função tem uma responsabilidade clara, seguindo o princípio da responsabilidade única.
Melhoria na Entrada do Usuário:

</br>

## 2 - Controle de Pontuação:

- Dicionário de Pontuação: O código melhorado usa um dicionário para rastrear o número de vitórias, derrotas e empates. Isso facilita a atualização e impressão do placar.

</br>

## 3 - Iteração Controlada:

- Número de Rounds: O código melhorado permite ao usuário especificar o número de rounds antes de iniciar o jogo (timesToPlay). O jogo roda um número fixo de vezes, o que é mais amigável para o usuário.
Mensagens Detalhadas:

</br>

## 4 - Abreviações Simplificadas:

- No código melhorado, o usuário pode escolher entre "r", "p" e "s" para Pedra, Papel e Tesoura, respectivamente. Isso simplifica a entrada.
Validação de Entrada: A função get_user_choice valida a entrada e repete o prompt até receber uma escolha válida.
Dicionários para Clareza:

- Mapeamento com Dicionário: CHOICES_DICT mapeia as abreviações para seus nomes completos. Isso melhora a legibilidade nas mensagens ao usuário (Você escolheu: Pedra).

</br>

## 5 -  Feedback Claro:

 - As mensagens no código melhorado são mais detalhadas e incluem o nome completo da escolha do usuário e do computador, o que melhora a compreensão do resultado.

</br>

## 6 - Loop Principal:

- Estrutura do Loop: No código melhorado, o loop principal está dentro da função play_game, facilitando a leitura e a estrutura do programa.
</br>

</br>

## Layout do projeto:
</br>
<p align="center"> 
<img src="https://github.com/apedrodev1/Python-Learning-HUB/assets/104085801/54d75725-723e-4867-9901-d3b8d02d67cf"
<\p>



  ---
  
<p align="center">
  Esse README fornece uma descrição clara do projeto, seus objetivos, tecnologias utilizadas e como utilizá-lo, juntamente com os devidos créditos ao criador original do projeto.
</p>
