import math

def S(a,b,c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

if __name__ == "__main__":
    a = float(input("Введите значение стороны а: "))
    b = float(input("Введите значение стороны b: "))
    c = float(input("Введите значение стороны c: "))
    print(S(a,b,c))
print(round(math.pi,2))

def func(x):
    return math.sqrt(1 - (math.sin(x))**2)

if __name__ == "__main__":
    x = float(input("Введите значение стороны x: "))
    print(func(x))
