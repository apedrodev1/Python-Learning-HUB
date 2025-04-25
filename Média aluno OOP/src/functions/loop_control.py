import os

def clear_screen(): #limpa a tela
         os.system('cls' if os.name == 'nt' else 'clear')

def ask_to_retry(): #repete o programa
    retry = input("\n🔁 Deseja rodar o programa novamente? (s/n): ").lower()
    if retry == 's':
           clear_screen()
           return True
    elif retry == 'n':
        print("\n👋 Programa finalizado. Até a próxima!")
        return False
    else:
          print("❌ Por favor, digite 's' para sim ou 'n' para não.")
          
    

  
    





