def min_(int_list):
    """Функция принимает список чисел
    и возвращает минимальное значение из него"""
    return min(int_list)

def max_(int_list):
    """Функция принимает список чисел
    и возвращает максимальное значение из него"""
    return max(int_list)

def sum_(int_list):
    """Функция принимает список чисел и возвращает сумму его элементов"""
    return sum(int_list)

def len_(int_list):
    """Функция принимает список чисел и возвращает кол-во элементов в нём"""
    return len(int_list)

def sorted_(int_list:list):
    """Функция принимает список чисел
    и возвращает новый отсортированный список на основе переданного"""
    return sorted(int_list)

def apply_all_func(int_list, *functions):
    """Функция Вызывает каждую функцию к переданному списку int_list.
        Возвращает словарь, где ключом будет название вызванной функции,
        а значением - её результат работы со списком int_list."""
    result = {}
    for func in functions:
        result[func.__name__] = func(int_list)
    return result


# Пример работы кода:
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))