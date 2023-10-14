# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.


def sort_list_imperative(array):
    for _ in range(len(array)):
        for num in range(len(array) - 1):
            if array[num] < array[num + 1]:
                array[num], array[num + 1] = array[num + 1], array[num]

    return array


numbers = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8]

print(*sort_list_imperative(numbers), sep=', ')
