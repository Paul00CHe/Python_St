from random import randint
while True:
    x = randint(0, 5)
    y = input("Какое я загадал число? ")
    if y == "Выход":
        print("Выход из программы!")
        break
    elif int(y) == x:
        print("Вы ПОБЕДИЛИ, поздравляю!")
    else:
        if int(y) > x:
            print("Ваше число больше загаданного!")
        elif int(y) < x:
            print("Ваше число меньше загаданного!")
