### Projeto Quiz

Este projeto consiste na criação de um quiz interativo, utilizando a linguagem Python.

Iury Rosal e disponibilizado no repositório do GitHub.

https://www.youtube.com/watch?v=MRYlWPrsMYk&list=PLshkB4NQEfC7jz8Ig-JcqwjZz8WSI2s8W&index=1 

https://github.com/iuryrosal/projetos-python/tree/main/level-a/01

## Melhorias sugeridas no quiz_V2.py:

#1 Dicionário para perguntas e respostas: O uso de um dicionário torna o código mais fácil de expandir. Você pode adicionar novas perguntas apenas adicionando novos - itens ao dicionário.

<code>questions = {
"Quem desenvolveu o jogo Grand Theft Auto (GTA)?": {
"opcoes": ["A) Rockstar Games", "B) Ubisoft", "C) Activision", "D) EA"],
"resposta": "A"
}
}</code>


#2 Validação da entrada: O método upper() é usado para garantir que as respostas do usuário sejam tratadas de forma consistente, indiferente de serem maiúsculas ou minúsculas.

<code>answer_user = input('Deseja começar? (S/N): ').upper()</code>


#3 O loop for com enumerate permite iterar sobre as perguntas e respostas armazenadas no dicionário questions. Ele exibe um contador de progresso (index) e atribui a pergunta atual à variável pergunta, enquanto detalhes contém as opções de resposta (opcoes) e a resposta correta (resposta).

<code>for index, (pergunta, detalhes) in enumerate(questions.items(), start=1:
    print(f'\nPergunta {index}/{total_questions}:')
    print(pergunta)
for opcao in detalhes["opcoes"]:
    print(opcao)
resposta = input('Resposta: ').upper()</code>
</br>
Este loop garante que cada pergunta seja apresentada ao usuário com suas respectivas opções de resposta, e valida a resposta fornecida pelo usuário, fornecendo feedback imediato e atualizado a pontuação.

#4 Feedback personalizado: A resposta correta é exibida se o usuário errar, fornecendo feedback educativo.

<code>if resposta == detalhes["resposta"]:
print('Parabéns!!! Você acertou!')
score += 1
else:
print(f'Que pena! Você errou... A resposta correta é a letra {detalhes["resposta"]}') </code>

## Como utilizar: 
-1 Clone o repo

![image](https://github.com/apedrodev1/Python-Learning-HUB/assets/104085801/ae0c9c0e-0d44-4c33-862c-e06e15283020)

