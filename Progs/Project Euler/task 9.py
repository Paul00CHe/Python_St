# Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство
# a^2 + b^2 = c^2
# Например, 3^2 + 4^2 = 9 + 16 = 25 = 52.
# Существует только одна тройка Пифагора, для которой a + b + c = 1000.
# Найдите произведение abc.
for a in range(2, 996):
    for b in range(3, 997):
        for c in range(4, 998):
            if a < b < c \
                    and a + b + c == 1000 \
                    and a ** 2 + b ** 2 == c ** 2:
                print(a * b * c)
                print(a, b, c)
            else:
                continue
