# file = open('пример чтения из текста.txt', 'r')
# contents = file.read()
# print(contents)
# file.close()
with open('пример чтения из текста.txt', 'r') as f:
    L = f.readlines()
    # в последней строке redlines() не ставит \n, поэтому последняя строка нужна пустая
    L.sort()
    # for i in L:
        # print(i.strip())
with open('сортированный пример.txt', 'w') as s_f:
    for line in L:
        s_f.write(line)
print(L)
