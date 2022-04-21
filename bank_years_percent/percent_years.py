
x = 0
y = 0


def bank(a, b):
    a = int(input("Введите сумму: "))
    b = int(input("Введите количество лет: "))
    while b != 0:
        a = a * 1.1
        b = b - 1
    print("Итоговая сумма вклада =", a)


bank(x, y)
