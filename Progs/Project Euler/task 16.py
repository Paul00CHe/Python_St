# 2^15 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.
# Какова сумма цифр числа 2^1000?
import math
a = list(str(int(math.pow(2, 1000))))
b = 0
for i in a:
    b += int(i)
print(a)
print(b)
