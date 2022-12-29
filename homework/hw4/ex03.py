# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод:
# 3 1 2 3
# Вывод:
# 2 1

from random import randint

n = abs(int(input('Enter count of elements in the list: ')))
lst = [randint(0, 10) for _ in range(n)]
print(lst)

lst_res = []

for i in range(len(lst)):
    if lst[i] not in lst_res:
        lst_res.append(lst[i])
print(lst_res)