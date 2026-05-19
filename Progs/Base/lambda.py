S = ['aa', 'bb', 'cc']


def e(a, b):
    for c in a:
        print (b(c))


def f(c):
    return c.capitalize() + '!?+'


print(e(S, f))
print(e(S, lambda g:g.capitalize() + '!+!')) # lambda - фун-ция, которая передается в другую
                                             # функцию как переменная + краткая запись
