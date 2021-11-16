from random import randint
m = int(input("Введите длину списка: "))
S = [randint(-100, 100) for i in range(m)]
R = max(S) - min(S)
if S.index(min(S)) > S.index(max(S)):
    A = S[S.index(max(S)):S.index(min(S)) + 1]
else:
    A = S[S.index(min(S)):S.index(max(S)) + 1]
pos = 0
for k in range(len(A)):
    if A[k] < 0:
        pos = pos + 1
    else:
        continue
# print(S)
# print(A)
print("Разница между максимальным и минимальным значением: ", R)
print("Отрицательных элементов между макс и мин списка: ", pos)
