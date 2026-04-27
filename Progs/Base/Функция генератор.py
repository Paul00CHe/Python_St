

def my_range(first=0, last=20, step=1):
    n = first
    while n < last:
        yield n
        n += step


r = my_range(1, 30, 2)


for i in r:
    print(i)
