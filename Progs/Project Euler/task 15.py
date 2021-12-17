# Начиная в левом верхнем углу сетки 2×2 и имея возможность двигаться только вниз или вправо,
# существует ровно 6 маршрутов до правого нижнего угла сетки.
# Сколько существует таких маршрутов в сетке 20×20?
import copy
#import time


#def timer(f):
    #def tmp(*args, **kwargs):
        #t = time.time()
        #res = f(*args, **kwargs)
        #print('Время выполнения ф-ции:%f'%(time.time()-t))
        #return res
    #return tmp


#@timer
def find_pos(num, list):
    for i in list:
        if len(i) > 1:
            for j in i:
                if num == j:
                    strin = list.index(i)
                    col = i.index(j)
                    break
                else:
                    continue
        else:
            if num == i:
                strin = list.index(i)
    return strin, col


n = 21
net = [[i for i in range(m * n, m * n + n)] for m in range(n)]
all_knot = [i for i in range(n * n)]
ways = []
while True:
    z = []
    if not ways:
        ways.append([net[0][0], net[0][1]])
        ways.append([net[0][0], net[1][0]])
    elif len(ways) > 1 and all_knot[len(all_knot) - 1] != ways[0][len(ways[0]) - 1]:
        for i in ways:
            strin = find_pos(i[len(i) - 1], net)[0]
            col = find_pos(i[len(i) - 1], net)[1]
            if strin != n - 1 and col != n - 1:
                z = copy.deepcopy(i)
                i.append(net[strin][col + 1])
                z.append(net[strin + 1][col])
                ways.append(z)
            elif strin == n - 1 and col != n - 1:
                i.append(net[strin][col + 1])
            elif strin != n - 1 and col == n - 1:
                i.append(net[strin + 1][col])
    else:
        break
# print(net, len(net))
# print(all_knot)
print(len(ways))
# print(ways)
