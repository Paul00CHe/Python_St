def stringCount(A, B):
    F = []
    with open(A, 'r') as f:
        L = f.readlines()
        for i in L:
            F.append(i.strip())
    return F.count(B)
print(stringCount("пример чтения из текста.txt", "Venus"))
