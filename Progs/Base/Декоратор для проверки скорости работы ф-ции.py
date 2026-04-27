import time


def timer(func): # Сам таймер по времени компа
    def tmp(*args, **kwargs):
        t = time.time()
        res = func(*args, **kwargs)
        print('Время выполнения ф-ции: %func'%(time.time() - t))
        return res
    return tmp


def pause(func): # Делаем паузу перед началом выполнения ф-ции
    def tmp(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return tmp


@timer
@pause
def f(x, y):
    return x ** y


f(5, 6)
