from random import randint
try:
    n = int(input('Введите размерность матрицы N: '))
    m = int(input("Введите размерность матрицы M: "))
    k = int(input("Введите начало диапазона генерируемых элементов: "))
    g = int(input("Введите конец диапазона генерируемых элементов: "))
    M = [[randint(k, g) for j in range(m)] for i in range(n)]
    print(M)
except ValueError as v:
    print('Ошибка значения')
    print(v)
