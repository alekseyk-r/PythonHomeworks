def happy_hours(summa, hour):
    if 10 <= hour < 12:
        summa /= 2
    elif 20 <= hour < 22:
        summa /= 4
    return summa

summa = float(input("Введите сумму к оплате: "))
hour = int(input("Введите текущий час: "))

if 8 <= hour < 22:
    print("К оплате:", happy_hours(summa, hour))
else:
    print("Магазин закрыт!")
