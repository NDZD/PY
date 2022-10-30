# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

n = int(input('enter the quarter number 1 of 4 '))


if n == 1:
    str = 'x > 0 and y > 0'
elif n == 2:
    str = 'x < 0 and y > 0'
elif n == 3:
    str = 'x < 0 and y < 0'
elif n == 4:
    str = 'x > 0 and y < 0'


print(f"range - {str}")

