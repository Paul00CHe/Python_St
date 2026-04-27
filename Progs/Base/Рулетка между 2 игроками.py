from random import randint
x = randint(0, 10)
x2 = randint(0, 10)
print("Первый игрок выбросил: ", x)
print("Второй игрок выбросил: ", x2)

if x > x2:
    print("Победил первый игрок")
else:
    print("Победил второй игрок")
