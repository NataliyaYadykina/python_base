# даны два числа, проверить, что a / b.

a, b = int(input('a = ')), int(input('b = '))

if b != 0:
    if a % b == 0:
        print('Yes')
    else:
        print('No')

else:
    print('Error!')