# Поиск: декларативный
#
# Контекст
# Предположим, что нам хочется для любого массива чисел array и любого числа target узнать содержится
# ли target в array. Такую процедуру будем называть поиском.
#
# Задача
# Реализовать декларативную функцию поиска элементов на языке Python


def search_target(arr, targ):
    return targ in arr


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5

if search_target(array, target):
    print('YES')
else:
    print('NO')
