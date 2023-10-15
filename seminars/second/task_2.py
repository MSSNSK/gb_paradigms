# Десятичное в двоичное
#
# Условие
# На вход подается число в десятичной системе счисления
#
# ● Задача
# Написать скрипт в любой парадигме, который возвращает полученное число переведенное в двоичную систему счисления.
# Обоснуйте сделанный выбор парадигм.


def convert_number(num, sys):
    result = []

    while num >= sys:
        result.append(num % sys)
        num = num//sys
    result.append(num)

    return result[::-1]


number = int(input(''))
system = int(input(''))

print(*convert_number(number, system), sep='')


# ***********
#
#
# from string import ascii_uppercase, digits
#
# DIGITS = digits + ascii_uppercase
#
#
# def bin_octa(num, prod):
#     result = []
#     while num > 0:
#         temp = num % prod
#         result.append(DIGITS[temp])
#         num //= prod
#     return "".join(result[::-1])
#
#
# number = int(input("Введите число: "))
# res = bin_octa(number, 16)
# print(res)
