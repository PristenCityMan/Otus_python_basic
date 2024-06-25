"""
Домашнее задание №1
Функции и структуры данных
"""

def is_prime (number):
    if number < 2:
        return False
    for i in range (2,number // 2 + 1):
        if number % i == 0:
            return False
    return True

def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    [1, 4, 25, 49]
    """
    items_sqr = []
    for item in args:
        items_sqr.append(item**2)
    return items_sqr

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(numbers, param):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    [2, 4]
    """
    if param == ODD:
        return list(filter(lambda x: x % 2 == 1, numbers))
    elif param == EVEN:
        return list(filter(lambda x: x % 2 == 0, numbers))
    elif param == PRIME:
        return list(filter(is_prime, numbers))
    return None

