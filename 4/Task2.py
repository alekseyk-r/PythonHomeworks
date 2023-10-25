games = input("Введите game (off - завершить) ")
if games == "game":
    while True:
        print("Угадай число")
        for i in range(3):
            number = input("Введите число: (или введите off)")
            if number == "5":
                print("Вы выиграли билет на концерт!")
                break
            elif number == "off":
                exit()