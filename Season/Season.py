month = 0
exit = ("")


def season(a, b):
    while b != ("выход"):
        b = input("Введите номер месяца: ")
        if b == "выход":
            continue
        a = int(b)
        if a == 12 or a >= 1 and a <= 2:
            print("Зима.")
        elif a >= 3 and a <= 5:
            print("Весна.")
        elif a >= 6 and a <= 8:
            print("Лето.")
        elif a >= 9 and a <= 11:
            print("Осень.")
        else:
            print("Введен неверный месяц.")
        print(" ")


season(month, exit)
