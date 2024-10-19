from copy import deepcopy

def apply_all_func(int_list, *functions):
    """Функция Вызывает каждую функцию к переданному списку int_list.
        Возвращает словарь, где ключом будет название вызванной функции,
        а значением - её результат работы со списком int_list."""
    result = {}
    for func in functions:
        result[func.__name__] = func(int_list)
    return result

def min_(int_list):
    """Функция принимает список чисел
    и возвращает минимальное значение из него"""
    res = int_list[0]
    for i in range(1, len(int_list)):
        if int_list[i] < res:
            res = int_list[i]
    return res

def max_(int_list):
    """Функция принимает список чисел
    и возвращает максимальное значение из него"""
    res = int_list[0]
    for i in range(1, len(int_list)):
        if int_list[i] > res:
            res = int_list[i]
    return res


def sum_(int_list):
    """Функция принимает список чисел и возвращает сумму его элементов"""
    res = int_list[0]
    for i in range(1, len(int_list)):
        res += int_list[i]
    return res


def len_(int_list):
    """Функция принимает список чисел и возвращает кол-во элементов в нём"""
    res = 0
    for i in range(len(int_list)):
        res += 1
    return res


def sorted_(int_list:list):
    """Функция принимает список чисел
    и возвращает новый отсортированный список на основе переданного"""
    res = deepcopy(int_list)

    # метод сортировки вставками
    for i in range(1, len(res)):
        x = res[i]
        j = i - 1
        while j >= 0 and res[j] > x:
            res[j + 1] = res[j]
            j -= 1
        res[j + 1] = x

    return res


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
