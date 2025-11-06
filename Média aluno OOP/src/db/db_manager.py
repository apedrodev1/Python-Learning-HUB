import os
from .input_handler import get_valid_input
from .validations import validate_yes_no
from ..bd.repository import StudentRepository

# Define o caminho para o diretório de arquivos de banco de dados
# BASE_DIR -> .../Média aluno OOP/
# DB_FILES_DIR -> .../Média aluno OOP/src/bd/bd_files/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DB_FILES_DIR = os.path.join(BASE_DIR, 'src', 'db', 'bd_files')


def _prompt_create_new_db() -> str:
    """
    Prompt the user to create a new database file.
    Validates that the name is not empty.
    
    Returns:
        str: The full path to the new database file.
    """
    # Validação simples para o nome do arquivo
    def validate_db_filename(name: str) -> (str, str | None):
        name = name.strip()
        if not name:
            return None, "File name cannot be empty."
        # Garante que o arquivo termine com .db
        if not name.endswith(".db"):
            name += ".db"
        return name, None

    filename, _ = get_valid_input(
        "Enter a name for the new classroom file (e.g., 'class_a_2024'): ",
        validate_db_filename
    )
    
    full_path = os.path.join(DB_FILES_DIR, filename)
    print(f"✅ New classroom file will be created at: {filename}")
    return full_path


def _prompt_load_or_create(db_files: list) -> (str | None, bool):
    """
    Shows the menu to load an existing DB or create a new one.
    
    Returns:
        tuple (str | None, bool): (db_path, is_new_db)
        Returns (None, False) if the user chooses to exit.
    """
    print("\n--- Existing Classrooms Found ---")
    
    # Cria as opções do menu
    options = {}
    for i, filename in enumerate(db_files):
        options[str(i + 1)] = filename
    
    options['n'] = "Create a new classroom"
    options['s'] = "Exit program"

    # Validador local para verificar a escolha do menu
    def validate_menu_choice(choice: str) -> (str, str | None):
        choice = choice.strip().lower()
        if choice in options:
            return choice, None
        return None, "Invalid choice. Please select from the options above."

    # Exibe o menu
    for key, value in options.items():
        if key.isdigit():
            print(f"  [{key}] Load '{value}'")
        elif key == 'n':
            print(f"  [N] {value}")
        elif key == 's':
            print(f"  [S] {value}")
    
    choice, _ = get_valid_input("\nYour choice: ", validate_menu_choice)

    # Processa a escolha
    if choice == 's':
        return None, False # Sair
    
    if choice == 'n':
        db_path = _prompt_create_new_db()
        return db_path, True # Criar Novo
    
    # Se for um número, é para carregar
    filename = options[choice]
    db_path = os.path.join(DB_FILES_DIR, filename)
    print(f"✅ Loading classroom: {filename}")
    return db_path, False # Carregando existente


def setup_repository() -> (StudentRepository | None, bool):
    """
    Orchestrates the database (classroom) setup.
    
    Ensures the DB directory exists, then asks the user to either
    load an existing classroom DB or create a new one.
    
    Returns:
        tuple (StudentRepository | None, bool):
            (repository_instance, is_new_db)
            - 'repository_instance' is None if the user quits.
            - 'is_new_db' is True if a new DB is being created.
    """
    # 1. Garante que o diretório exista
    os.makedirs(DB_FILES_DIR, exist_ok=True)
    
    # 2. Lista os arquivos .db existentes
    try:
        db_files = [f for f in os.listdir(DB_FILES_DIR) if f.endswith('.db')]
    except OSError as e:
        print(f"❌ Critical error reading database directory: {e}")
        return None, False

    db_path = None
    is_new_db = False

    # 3. Decide qual fluxo seguir
    if not db_files:
        # Cenário 1: Pasta vazia (Flow 1)
        print("🔍 No existing classrooms found.")
        choice, _ = get_valid_input(
            "Would you like to create a new one? (y/n): ",
            validate_yes_no
        )
        
        if choice == 'y':
            db_path = _prompt_create_new_db()
            is_new_db = True
        else:
            return None, False # Usuário desistiu
    else:
        # Cenário 2: Pasta com arquivos (Flow 2)
        db_path, is_new_db = _prompt_load_or_create(db_files)

    # 4. Se o usuário não saiu (S) ou não desistiu (n), cria o repositório
    if db_path:
        try:
            repo = StudentRepository(db_path)
            return repo, is_new_db
        except Exception as e:
            print(f"❌ Critical error initializing repository: {e}")
            return None, False
    
    # Se o usuário saiu no menu de carregamento/criação
    return None, False