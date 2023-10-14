# Доля чисел: императивный вариант
#
# Условие
# На вход подается: список целых чисел arr
#
# Задача
# Реализовать императивную функцию, которая возвращает три числа:
# ○ Долю позитивных чисел
# ○ Долю нулей
# ○ Долю отрицательных чисел


def fractions_numbers(array):
    positive, zero, negative = 0, 0, 0
    len_array = array.__len__()

    if not len_array:
        return 0, 0, 0

    for num in array:
        if num == 0:
            zero += 1
        elif num > 0:
            positive += 1
        else:
            negative += 1

    return positive/len_array, zero/len_array, negative/len_array


arr = [0, 1, -2, 3, -4, 0, 5, -6, 7, -8, 9, 0]

print(*fractions_numbers(arr), sep='\n')
