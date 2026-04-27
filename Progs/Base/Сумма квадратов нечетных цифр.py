y = input("Введите число:")
y2 = list(y)
t = 0
for i in y2:
    if int(i) % 2 == 0:
        continue
    t = t + int(i)**2
print(t)
