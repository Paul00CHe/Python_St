# Начиная в вершине треугольника (см. пример ниже) и перемещаясь вниз на смежные числа, максимальная сумма до основания составляет 23.
# 3
# 7 4
# 2 4 6
# 8 5 9 3
# То есть, 3 + 7 + 4 + 9 = 23.
# Найдите максимальную сумму пути от вершины до основания следующего треугольника:
# в файле task 18.txt
import copy
with open('task 18', 'r') as f:
    L = f.readlines()
A = []
for i in L:
    B = []
    x = i.split( )
    for j in x:
        B.append(int(j))
    A.append(B)
B = A[::-1]
for i in B:
    for j in range(len(i) - 1):
        if i[j] > i[j + 1]:
            B[B.index(i) + 1][j] = B[B.index(i) + 1][j] + i[j]
        else:
            B[B.index(i) + 1][j] = B[B.index(i) + 1][j] + i[j + 1]
print(B[len(B) - 1][0])