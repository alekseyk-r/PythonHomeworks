discount = int(input("Введите скидку: ")) / 100
print(discount)
price = int(input("Введите сумму к оплате: "))
while price != 0:
    print("Сумма к оплате без скидки:", price)
    print("Скидка:", discount * price)
    print("Сумма к оплате со скидкой:", price - (discount * price))
    price = int(input("Введите сумму к оплате: "))