

def dek(func): # Сам Декоратор
    def new_func(*args, **kwargs):
        result = func(*args, **kwargs) ** 2 # Декорирование (изменение исходной ф-ции)
        return result
    return new_func


@dek # Декорирование (если выше будут еще декораторы, то этот будет выполнен первым)
def s(a, b):
    return a + b


print(s(6, 3))
