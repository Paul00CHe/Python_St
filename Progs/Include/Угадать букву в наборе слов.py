import random
a = ['будущий', 'трафик', 'полощи', 'продюсер', 'грейпфрут', 'СОЖ', 'apple', 'pink']
b = random.choice(a)
c = list(b)
d = random.choice(c)
e = b.find(d)
c[e] = '?'
f = ''.join(c)
print(f)
x = input('Какая пропущена буква? ')
if x == d:
    print("Кот ученый")
else:
    print("Незнайка")
