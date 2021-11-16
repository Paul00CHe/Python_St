from random import randint
m = int(input("Введите длину списка: "))
L = [randint(-100, 100) for i in range(m)]
k = 0
j = 0
for i in L:
    o = list(str(i))
    if i % 2 == 0:
        k = k + 1
    elif int(o[-1]) == 5:
        j = j + 1
    else:
        continue
print(L)
print("Количество четных элементов: ", k)
print("Количество элементов заканчивающихся на 5: ", j)
