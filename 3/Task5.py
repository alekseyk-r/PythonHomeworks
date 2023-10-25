def divisible_by_6(num):
    digits = [int(d) for d in str(num)]
    if digits[-1] % 2 == 0 and sum(digits) % 3 == 0:
        return True
    return False

num = int(input("Введите число: "))
if divisible_by_6(num):
    print("Число делится на 6.")
else:
    print("Число не делится на 6.")
