# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math

xA = float(input('Координата xA: '))
yA = float(input('Координата yA: '))
xB = float(input('Координата xB: '))
yB = float(input('Координата yB: '))


distance = round(math.sqrt((xB - xA)**2 + (yB - yA)**2), 2)
print(distance)