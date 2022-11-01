# 1 – Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# num = input('Введите вещественное число: ')
# n = 'str'
# print(list(num))
# for i in list(num):
#
#     n = n + num + ' '
# print(n)

num = input('Введите вещественное число: ')


def sum(num):
    n = 0
    for i in str(num):
        if i != '.':
            n += int(i)
    return n


print(f'Сумма цифр {sum(num)}')
