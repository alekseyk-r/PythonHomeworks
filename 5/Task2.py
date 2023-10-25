mark = list(input("Введите оценки через пробел: ").split(" "))
print(sorted(mark))
print((mark.count("5") + mark.count("4") + mark.count("3")) / len(mark) * 100)