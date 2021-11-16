from random import randint
m = int(input("Введите длину списка: "))
L = [randint(0, 100) for i in range(m)]
A = []
for i in L:
    A.append(abs(i - sum(L) / len(L)))
# print(L, A)
print("Наиболее близкий элемент к среднему списка: ", L[A.index(min(A))])
