def ask_to_retry():
    retry = input("\n🔁 Deseja rodar o programa novamente? (s/n): ").lower()
    return retry == 's'

#clear.screen - fazer depois