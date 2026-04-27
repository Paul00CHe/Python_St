from random import randint
m = int(input("Введите длину списка: "))
L = [randint(0, 1000) for i in range(m)]
a = int(input('Введите max сумму скольких соседних элементов посчитать: '))
B = []
Summ = []
for i in range(len(L) - (a - 1)):
    E = []
    S = []
    for j in range(i, i + a):
        E.append(L[j])
    S.append(sum(E))
    B.append(E)
    Summ.append(S)
print(L)
print(B)
print("Элементы с максимальной суммой: ", B[Summ.index(max(Summ))])
print("Сумма этих элементов: ", max(Summ))
