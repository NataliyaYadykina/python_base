# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

n = abs(int(input('Enter count of elements in the list: ')))
lst = [randint(0, 100) for _ in range(n)]
print(lst)

sum = 0
for i in range(1, n, 2):
    sum += lst[i]
    print(lst[i])

print(f'Sum = {sum}')
