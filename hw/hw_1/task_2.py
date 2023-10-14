# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле.


def sort_list_declarative(array):
    return reversed(sorted(array))


numbers = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8]

print(*sort_list_declarative(numbers), sep=', ')
