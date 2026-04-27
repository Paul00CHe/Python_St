A = [int(input()) for i in range(int(input()))]
b = []
c = []
for i in range(int(len(A)/2)):
    n = A[i]
    b.append(n)
A.reverse()
for i in range(int(len(A)/2)):
    n2 = A[i]
    c.append(n2)
print(c + b)
