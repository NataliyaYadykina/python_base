# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 6 | N = 12    | 32                | 13 | 9     | 18        | 21
# 2 * 3 | 2 * 2 * 3 | 2 * 2 * 2 * 2 * 2 | 13 | 3 * 3 | 2 * 3 * 3 | 3*7

n = abs(int(input('Enter number > 1: ')))

if n > 1:
    list_simple_divider = []

    div = 2
    while div != n:
        if n % div == 0:
            list_simple_divider.append(div)
            n /= div
        else:
            div += 1
    else:
        list_simple_divider.append(div)
    print(list_simple_divider)
else:
    print('Wrong number! Try again.')