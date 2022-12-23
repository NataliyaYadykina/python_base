# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя # используйте пробел.Без min и max
my_str = input('Enter numbers: ').split(' ')
min = int(my_str[0])
max = int(my_str[0])

for i in range(len(my_str)):
    if int(my_str[i]) > max:
        max = int(my_str[i])
    if int(my_str[i]) < min:
        min = int(my_str[i])

print(max, min)