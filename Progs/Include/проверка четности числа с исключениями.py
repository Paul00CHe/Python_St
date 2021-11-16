try:
    x = float(input("Введите число: "))
    if x % 2 == 0:
        print("Число является четным")
    else:
        print("Число является нечетным")
except ValueError as v:
    print("Ошибка преобразования типов")
    print(v)
