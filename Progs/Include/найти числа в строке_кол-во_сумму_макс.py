L = input('Введите строку:')
a = []
for i in range(len(L)):
    if L[i].isalpha():
        continue
    else:
        a.append(int(L[i]))
print('Сумма чисел: ', sum(a))
print('Максимальное число: ', max(a))
print('Количество чисел: ', len(a))
