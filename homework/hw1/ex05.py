# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

x1 = int(input('Write x1: '))
y1 = int(input('Write y1: '))

x2 = int(input('Write x2: '))
y2 = int(input('Write y2: '))

distance = math.sqrt((x2 - x1) ** 2 + (y2 -y1) ** 2)
print(f'Distance = {distance}')