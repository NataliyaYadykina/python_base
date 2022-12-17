﻿# Петя и катя - брат и сестра. Петя - студент, а Катя - школьница. 
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа, а Катя должна их отгадать
# Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P
# Помогите Кате отгадать задуманные Петей числа.

# Пример
# Ввод: 4 4
# Вывод: 2 2

# *Пример*
# Ввод: 5 6
# Вывод: 2 3

a = int(input('Enter the sum of x and y: '))
b = int(input('Enter the multiplication of x and y: '))

x = 0
y = 1

while (x + y != a) or (x * y != b):
    y += 1
    x = a - y

print(f'The numbers are: x = {x}, y = {y}.')
