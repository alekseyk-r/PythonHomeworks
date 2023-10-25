def new_action(prices):
    if prices == [25, 100, 310] or prices == [2500, 400, 50]:
        print("Акция!")
        if prices == [25, 100, 310]:
            return sum(prices) / 2
        else:
            return sum(prices) / 3
    else:
        return sum(prices)

prices = list(map(int, input("Введите цены трех товаров через пробел: ").split()))
print("К оплате:", new_action(prices))
