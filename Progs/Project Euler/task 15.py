# Начиная в левом верхнем углу сетки 2×2 и имея возможность двигаться только вниз или вправо,
# существует ровно 6 маршрутов до правого нижнего угла сетки.
# Сколько существует таких маршрутов в сетке 20×20?
import copy
n = 21 # не корректно задано условие (6 маршрутов у сетки 3х3, а не 2х2)
A = [[i for i in range(m * n, m * n + n)] for m in range(n)]
print(A)


def opr_puti(x, y):
    z = copy.deepcopy(x)
    x.append(x[-1] + 1)
    z.append(x[-1] + y)
    return x, z


#i = 0
#v = []
#while True:

    #if i < A[-1]:


#b = opr_puti(v, n)[1]
#print(v)
#print(b)
