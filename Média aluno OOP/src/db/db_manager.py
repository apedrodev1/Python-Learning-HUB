import os
from ..utils.input_handler import get_valid_input
from ..utils.validations import validate_yes_no
from ..db.repository import StudentRepository

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DB_FILES_DIR = os.path.join(BASE_DIR, 'src', 'db', 'db_files')


def _prompt_create_new_db() -> str:
    """
    Prompt the user to create a new database file.
    Validates that the name is not empty.
    
    Returns:
        str: The full path to the new database file.
    """
    # Simple validation for the filename
    def validate_db_filename(name: str) -> (str, str | None):
        name = name.strip()
        if not name:
            return None, "File name cannot be empty."
        # Ensures the file ends with .db
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
    
    # Create menu options
    options = {}
    for i, filename in enumerate(db_files):
        options[str(i + 1)] = filename
    
    options['n'] = "Create a new classroom"
    options['s'] = "Exit program"

    # Local validator to check the menu choice
    def validate_menu_choice(choice: str) -> (str, str | None):
        choice = choice.strip().lower()
        if choice in options:
            return choice, None
        return None, "Invalid choice. Please select from the options above."

    # Display the menu
    for key, value in options.items():
        if key.isdigit():
            print(f"  [{key}] Load '{value}'")
        elif key == 'n':
            print(f"  [N] {value}")
        elif key == 's':
            print(f"  [S] {value}")
    
    choice, _ = get_valid_input("\nYour choice: ", validate_menu_choice)

    # Process the choice
    if choice == 's':
        return None, False # Exit
    
    if choice == 'n':
        db_path = _prompt_create_new_db()
        return db_path, True # Create New
    
    # If it's a number, it's for loading
    filename = options[choice]
    db_path = os.path.join(DB_FILES_DIR, filename)
    print(f"✅ Loading classroom: {filename}")
    return db_path, False # Loading existing


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
 # 1. Ensure the directory exists
    os.makedirs(DB_FILES_DIR, exist_ok=True)
    
    # 2. List existing .db files
    try:
        db_files = [f for f in os.listdir(DB_FILES_DIR) if f.endswith('.db')]
    except OSError as e:
        print(f"❌ Critical error reading database directory: {e}")
        return None, False

    db_path = None
    is_new_db = False

    # 3. Decide which flow to follow
    if not db_files:
        # Scenario 1: Empty folder (Flow 1)
        print("🔍 No existing classrooms found.")
        choice, _ = get_valid_input(
            "Would you like to create a new one? (y/n): ",
            validate_yes_no
        )
        
        if choice == 'y':
            db_path = _prompt_create_new_db()
            is_new_db = True
        else:
            return None, False # User decided to quit
    else:
        # Scenario 2: Folder with files (Flow 2)
        db_path, is_new_db = _prompt_load_or_create(db_files)

    # 4. If the user didn't exit (S) or quit (n), create the repository
    if db_path:
        try:
            repo = StudentRepository(db_path)
            return repo, is_new_db
        except Exception as e:
            print(f"❌ Critical error initializing repository: {e}")
            return None, False
    
    # If the user exited from the load/create menu
    return None, False