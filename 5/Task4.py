list_tutor = []
lastname = input("Введите фамилию: ")
title = input("Введите должность: ")
studentsgroup = input("Введите кол-во студентов во всех группах: ")
while lastname != '0':
    inf = []
    inf.append(lastname)
    inf.append(title)
    inf.append(studentsgroup)
    list_tutor.insert(1, inf)
    print(list_tutor)
    lastname = input("Введите фамилию: ")
    title = input("Введите должность: ")
    studentsgroup = input("Введите кол-во студентов во всех группах: ")
print(list_tutor)