# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

n = abs(int(input('Enter count of elements in the list: ')))
lst = [round(random.uniform(1, 10), 2) for _ in range(n)]
print(lst)

max = 0
min = 1
for i in lst:
    if i - int(i) > max:
        max = round(i - int(i), 2)
    if i - int(i) < min:
        min = round(i - int(i), 2)

print(f'Max = {max}')     
print(f'Min = {min}')
print(f'Diff = {round((max - min), 2)}')
