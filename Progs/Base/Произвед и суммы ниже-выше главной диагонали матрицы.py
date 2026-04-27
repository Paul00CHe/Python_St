from random import randint
n = int(input('Введите размерность матрицы N: '))
m = int(input("Введите размерность матрицы M: "))
M = [[randint(1, 10) for j in range(m)] for i in range(n)]
print(M)
P = 1
S = 0
# Ищет произведение чисел ниже главной диагонали
for k in M:
    for g in range(len(k)):
        if M.index(k) < g:
            P = P * k[g]
        else:
            continue
print(P)
# Ищет сумму элементов выше главной диагонали
for k in M:
    for g in range(len(k)):
        if M.index(k) > g:
            S = S + k[g]
        else:
            continue
print(S)
