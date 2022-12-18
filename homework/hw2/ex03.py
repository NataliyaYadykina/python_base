# Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. 
# Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]
# Ввод: 4
# [-4, -3, -2, -1, 0, 1, 2, 3,4]

from random import randint

n = abs(int(input('Enter n: ')))
lst_index = [randint(0, 2 * n) for _ in range(5)]
print(lst_index)

lst_numbers = [i for i in range(-n, n + 1)]
print(lst_numbers)

multi = 1
for i in range(len(lst_index)):
    multi *= lst_numbers[lst_index[i]]
    print(lst_numbers[lst_index[i]], end = ' ')

print()
print(multi)
