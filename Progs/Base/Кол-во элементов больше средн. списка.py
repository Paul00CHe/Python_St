from random import randint
m = int(input("Введите длину списка: "))
L = [randint(-100, 100) for i in range(m)]
k = 0
for i in L:
    if i > sum(L) / len(L):
        k = k + 1
    else:
        continue
print(L, k, sum(L) / len(L))
print("Элементов больше среднеарифметического списка: ", k * 100 / len(L), "%")
