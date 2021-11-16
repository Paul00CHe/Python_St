L = [-8, 8, 6.0, 5, 'строка', -3.1]
t = 0
for i in L:
    if type(i) == str:
        continue
    t = t + i
print(t)
