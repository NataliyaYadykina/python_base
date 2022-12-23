# 3. Задайте два числа. Напишите программу, которая найдёт 
# НОК (наименьшее общее кратное) этих двух чисел.

n1, n2 = int(input('Enter numbers: ')), int(input())

if n1 == 0 or n2 == 0: 
    print('Error. Try again.')
else:
    for kr in range(max(n1, n2), n1 * n2 + 1):
        if kr % n1 == 0 and kr % n2 == 0: 
            break
    print(kr)
