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

for v in lst:
    if lst.count(v) < 2:
        lst_res.append(v)
print(lst_res)
