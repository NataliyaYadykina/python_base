# 1.Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.

lst = ['6', 'str', '123', '4str']
num = input('input number: ')

if num in lst:
    print('Yes')
else:
    print('No')
