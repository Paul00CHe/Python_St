

def summator(*numbers):
    """
    Возвращает сумму всех переданных числовых аргументов.
    Внутри функции 'numbers' является кортежем.
    """
    print(f"Получен кортеж: {numbers}")  # Демонстрация типа данных

    total = 0
    for number in numbers:
        total += number
    return total


# Примеры вызовов функции
print(f"Сумма: {summator(1, 2, 3)}")
print("-" * 20)
print(f"Сумма: {summator(10, 20, 30, 40, 50)}")
print("-" * 20)
print(f"Сумма: {summator()}\n")  # Функция корректно работает и без аргументов
print("=" * 39 + "=\n")


def create_connection_config(host, **options):
    """
    Формирует словарь конфигурации.
    'host' - обязательный позиционный аргумент.
    'options' - словарь, содержащий все остальные именованные аргументы.
    """
    config = {'host': host}
    print(f"Получен словарь опций: {options}")  # Демонстрация типа данных

    # Метод update() словаря идеально подходит для слияния
    config.update(options)
    return config

# Пример 1: передача базовых параметров
config1 = create_connection_config("localhost", user="admin", port=5432)
print(f"Итоговая конфигурация 1: {config1}\n")

# Пример 2: передача расширенного набора параметров
config2 = create_connection_config(
    "db.example.com",
    user="readonly_user",
    password="secure_password",
    timeout=30,
    ssl_mode="require"
)
print(f"Итоговая конфигурация 2: {config2}")