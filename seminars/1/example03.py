# найти сумму 3-значного числа

a = int(input('a = '))

print((a % 100 // 10) + (a % 10) + (a // 100))