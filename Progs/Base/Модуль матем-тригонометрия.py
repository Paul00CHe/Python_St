import math
          
def z(x, y) :
    return (x + (2 + y)/x**2) / (y + (1 / (math.sqrt(x**2 + 10))))
def q(x, y) :
    return (2.8 * math.sin(x)) + abs(y)                              

x = float(input("Введите х: "))
y = float(input("Введите у: "))

print("z = ", round(z(x, y), 3))
print("q = ", round(q(x,y), 3))
