games = []
game = input("Введите игру: (или 0 для завершения) ")
while game != '0':
    if game not in games:
        games.append(game)
    else:
        print("Эта игра уже записана")
    game = input("Введите игру: (или 0 для завершения) ")

games.sort()
print(games)