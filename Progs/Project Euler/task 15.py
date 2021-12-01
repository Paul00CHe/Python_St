# Начиная в левом верхнем углу сетки 2×2 и имея возможность двигаться только вниз или вправо,
# существует ровно 6 маршрутов до правого нижнего угла сетки.
# Сколько существует таких маршрутов в сетке 20×20?

# используя формулу комбинаторики https://ichi.pro/ru/ponimanie-kombinatoriki-kolicestvo-putej-v-setke-208765624419204
n = 20


def factorial(x):
    a = 1
    for i in range(2, x + 1):
        a *= i
    return a


putei = factorial(2 * (n - 1)) / (factorial(n - 1) * factorial(n - 1))
print(putei)
