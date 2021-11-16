from random import randint
m = int(input("Введите длину списка: "))
L = [randint(0, 1000000) for i in range(m)]
A = []
b = []
for k in L:
    b.clear()
    # используется метод перебора делителей
    for j in range(1, k):
        if k % j == 0 and k > 1:
            b.append(k)
        else:
            continue
    if len(b) == 1:
        A.append(k)
    else:
        continue
print(L)
print("Всего простых чисел: ", len(A))
print("Сумма простых чисел: ", sum(A))
