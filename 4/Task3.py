login = input("Введите логин: ")
simbols = ["=", "?", "*", "^", "$", "№", "@", "_"]
for simbol in simbols:
    if simbol in login:
        print(simbol)