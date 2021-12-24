# Начиная в левом верхнем углу сетки 2×2 и имея возможность двигаться только вниз или вправо,
# существует ровно 6 маршрутов до правого нижнего угла сетки.
# Сколько существует таких маршрутов в сетке 20×20?


# 1-й вариант
def ways(n):
    net = [[0 for i in range(m * n, m * n + n)] for m in range(n)]
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0:
                net[i][j] = 1
            else:
                net[i][j] = net[i - 1][j] + net[i][j - 1]
    return net[len(net) - 1][len(net) - 1]


print(ways(200))

# 2-й вариант
memory = {(1, 0): 1, (0, 1): 1}


def func(x, y):
    if (x, y) not in memory:
        if x == 0:
            memory[(x, y)] = func(x, y - 1)
        elif y == 0:
            memory[(x, y)] = func(x - 1, y)
        else:
            memory[(x, y)] = func(x - 1, y) + func(x, y - 1)
    return memory[(x, y)]


print(func(199, 199))
