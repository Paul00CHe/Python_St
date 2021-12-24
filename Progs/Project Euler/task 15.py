# Начиная в левом верхнем углу сетки 2×2 и имея возможность двигаться только вниз или вправо,
# существует ровно 6 маршрутов до правого нижнего угла сетки.
# Сколько существует таких маршрутов в сетке 20×20?


def ways(n):
    A = []
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0:
                A.append(1)
            else:
                A[i][j] = A[i - 1][j] + A[i][j - 1]
    return A[n - 1][n - 1]


print(ways(20))
