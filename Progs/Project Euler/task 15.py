# Начиная в левом верхнем углу сетки 2×2 и имея возможность двигаться только вниз или вправо,
# существует ровно 6 маршрутов до правого нижнего угла сетки.
# Сколько существует таких маршрутов в сетке 20×20?
import copy


def find_pos(list):
    index = dict()
    for i in list:
        try:
            if len(i) > 1:
                for j in i:
                   index[j] = (list.index(i), i.index(j))
        except:
            index[i] = list.index(i)
    return index


n = 12
net = [[i for i in range(m * n, m * n + n)] for m in range(n)]
all_knot = [i for i in range(n * n)]
ways = []
indexes = find_pos(net)
while True:
    z = []
    if not ways:
        ways.append([net[0][0], net[0][1]])
        ways.append([net[0][0], net[1][0]])
    elif len(ways) > 1 and all_knot[len(all_knot) - 1] != ways[0][len(ways[0]) - 1]:
        for i in ways:
            strin = indexes[i[len(i) - 1]][0]
            col = indexes[i[len(i) - 1]][1]
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
