from random import randint
m = int(input("Введите длину списка: "))
L = [randint(-100, 100) for i in range(m)]
A = []
B = []
c = None
gg = []
for i in L:
    if c is None or i > c:
        B.append(i)
    else:
        A.append(B)
        B = [i]
    c = i
if B:
    A.append(B)
for j in range(len(A)):
    if len(A[j]) > 1:
        gg.append(A[j])
    else:
        continue
print(L)
print(gg)
print("Участков с монотонным возрастанием: ", len(gg))
