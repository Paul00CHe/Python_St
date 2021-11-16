from random import randint
#A = [randint(0, 100) for i in range(int(input("Введите кол-во элементов n: ")))]
#Генерирует список размером n из случайных чисел
n = int(input('Введите размерность матрицы N: '))
m = int(input("Введите размерность матрицы M: "))
#b = []
#for i in range(n):
    #b.append([randint(0, 100) for j in range(m)])
#print(b)
M = [[randint(0, 20) for j in range(m)] for i in range(n)]
print(M)
pos = 0
d = 0
for k in M:
    for g in range(len(k)):
        dd = k.count(k[g])
        if dd > d:
            d = dd
            # Сохраняет послед индекс столбца, где было наиб. кол-во совпадений
            pos = M.index(k)
        else:
            continue
print("Максимальное кол-во повторений: ", d, "Столбец: ", pos + 1)
