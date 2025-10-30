def generate_student_ids(start=1):
    """
    Um gerador que produz IDs sequenciais, começando em 'start'.
    
    Quando migrarmos para o banco de dados, esta função
    será substituída por uma que gera IDs a partir do banco.
    """
    current_id = start
    while True:
        yield current_id
        current_id += 1