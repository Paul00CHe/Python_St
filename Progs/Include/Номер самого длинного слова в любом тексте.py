L = input("Введите предложение: ")
y = L.replace(',', '').replace('.', '').split()
m = y[0]
pos = 0
for j in range(len(y)):
    if len(y[j]) > len(m):
        m = y[j]
        pos = j
print(m, pos + 1)
