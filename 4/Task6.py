price = int(input("Введите сумму к оплате: "))
discount = 15 / 100
while price != 0:
    if price % 2 == 0:
        while price % 2 == 0:
            price = price / 2
        print("К оплате:", price)
    else:
        print("К оплате со скидкой:", price * discount)
    price = int(input("Введите сумму к оплате: "))