from random import randint
m = int(input("Введите длину списка: "))
L = [randint(-100, 100) for i in range(m)]
# Ind = []
# for i in L:
    # if i >= 0:
        # continue
    # else:
        # Ind.append(L.index(i))
m = 0
# for j in range(1, len(Ind)):
    # k = Ind[m]
    # if Ind[j] - k == 1:
        # print("Номера элементов первой пары отр. чисел: ", k, ',', Ind[j])
        # break
    # else:
        # m = m + 1
        # continue
print(L)
for i in range(1, len(L)):
    k = L[m]
    if k < 0 and L[i] < 0:
        print("Номера элементов первой пары отр. чисел: ", L.index(k), ',', L.index(L[i]))
        break
    else:
        m = m + 1
        continue
