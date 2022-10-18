# n! означает n × (n − 1) × ... × 3 × 2 × 1
# Например, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# и сумма цифр в числе 10! равна 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Найдите сумму цифр в числе 100!.


def factorial(n):
    m = n
    for i in range(1, n):
        n = n * (m - i)
    return n


f = list(str(factorial(100)))
S = 0
for i in f:
    S += int(i)
print(S)
