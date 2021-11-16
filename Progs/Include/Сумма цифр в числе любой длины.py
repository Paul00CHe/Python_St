while True:
    y = input("Введите число любой длины: ")
    if y == "Стоп":
        break
    else:
        y2 = list(y)
        t = 0
        for i in y2:
            t = t + int(i)
        print(t)
