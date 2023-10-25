def recommend_food(input_str):
    if input_str == "Завтрак":
        return "кашу"
    elif "плотно поесть" in input_str:
        return "плов"
    else:
        return "котлеты с пюре"

input_str = input("Введите ваш запрос: ")
print(recommend_food(input_str))
