# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = abs(int(input('Enter number: ')))
print(n)

res = ''
while n > 0:
    res = str(n % 2) + res
    n //= 2
print(res)
