# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.   
# *Примеры:*   
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

from math import *
a = float(input('a = '))

if a - floor(a) != 0:
    print(floor(a * 10)%10)
else:
    print('No')
