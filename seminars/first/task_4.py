# Доля чисел: декларативный вариант
#
# Условие
# На вход подается: список целых чисел arr
#
# Задача
# Реализовать декларативную функцию, которая возвращает три числа:
# ○ Долю позитивных чисел
# ○ Долю нулей
# ○ Долю отрицательных чисел


def fractions_numbers(array):
    len_array = len(array)

    if not len_array:
        return 0, 0, 0

    positive = len(list(filter(lambda x: x > 0, array)))
    zero = len(list(filter(lambda x: x == 0, array)))
    negative = len(list(filter(lambda x: x < 0, array)))
    counts = [positive, zero, negative]
    return list(map(lambda count: count / len_array, counts))


arr = [0, 1, -2, 3, -4, 0, 5, -6, 7, -8, 9, 0]

print(*fractions_numbers(arr), sep='\n')
