# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и вывести многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 
# k = 6
#    ix^6 + ax^5 + bx^4+ cx^3 + dx^2 + ex + h
#    a, b, c, d, e, h - рандом

from random import randint

k = abs(int(input('Enter power number k: ')))
lst = [randint(0, 100) for _ in range(k + 1)]
#lst[0] = 1
#lst[2] = 0
#lst[3] = 1
print(lst)

polynomial = ''
for i in range(k + 1):
    if i > 1 and lst[len(lst) - i - 1] != 0:
        polynomial = '^' + str(i) + polynomial
    if lst[len(lst) - i - 1] != 0 and i != 0:
        polynomial = 'x' + polynomial
    if (lst[len(lst) - i - 1] != 1 and lst[len(lst) - i - 1] != 0) or (lst[len(lst) - i - 1] == 1 and i == 0):
        polynomial = str(lst[len(lst) - i - 1]) + polynomial
    if i != k and lst[len(lst) - i - 1] != 0: 
        polynomial = ' + ' + polynomial
    
print(polynomial)    