def recommend_product():
    category = input("Введите категорию товара: ")
    if category == "продукты":
        price = float(input("Введите цену продукта: "))
        if price < 100:
            print("Попробуйте нашу выпечку!")
        elif 100 <= price < 500:
            print("Как насчёт орехов в шоколаде?")
        else:
            print("Попробуйте экзотические фрукты!")
    else:
        print("Загляните в товары для дома!")

recommend_product()
