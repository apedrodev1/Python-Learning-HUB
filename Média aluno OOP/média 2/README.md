## ✅ Resumo da Ordem Lógica

# 🧠 Fluxo do Programa

<code>get_main_parameters()
process_students(students_quantity, way_to_calculate, passing_grade, weights)
show_student_list()

if user_wants_to_correct:
    correct_students()
    show_student_list()  # após correção

if user_wants_to_export:
    export_students()

ask_to_retry()</code>

<br>

# 👤 Fluxo do Usuário

1. Entrada dos dados iniciais:

    - Tipo de média (simples ou ponderada)

    - Nota mínima de aprovação

    - Pesos das notas (caso ponderada)

    - Quantidade de alunos

2. Preenchimento das informações de cada aluno:

    - Nome

    - Notas


3. Exibição da lista com:

    - Nome do aluno

    - Média final

    - Status (Aprovado/Reprovado)

4. Correção de dados (caso o usuário deseje):

    - Nome e/ou notas

    - Reexibição da lista com os dados corrigidos

5. Exportação dos dados (caso o usuário deseje):

    - Formatos possíveis: JSON ou XML


6. Pergunta se o usuário deseja rodar o programa novamente