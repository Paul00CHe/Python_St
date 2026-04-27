def outer():  # внешняя функция
    n = 5  # лексическое окружение - локальная переменная

    def inner():  # локальная функция
        nonlocal n
        n += 1  # операции с лексическим окружением
        print(n)

    return inner


fn = outer()  # fn = inner, так как функция outer возвращает функцию inner
# вызываем внутреннюю функцию inner
fn()  # 6
fn()  # 7
fn()  # 8


def multiply(n):
    def inner(m): return n * m

    return inner


fn = multiply(5)
print(fn(5))  # 25
print(fn(6))  # 30
print(fn(7))  # 35


def multiply(n): return lambda m: n * m


fn = multiply(5)
print(fn(5))  # 25
print(fn(6))  # 30
print(fn(7))  # 35