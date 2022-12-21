# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint

n = abs(int(input('Enter count of elements in the list: ')))
lst = [randint(0, 10) for _ in range(n)]
print(lst)

lst_multi = []
multi = 1
for i in range(n // 2):
    lst_multi.append(lst[i] * lst[len(lst) - 1 - i])
if n % 2 != 0:
    lst_multi.append(lst[n // 2] ** 2)
print(lst_multi)
