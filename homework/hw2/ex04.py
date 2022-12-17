# Требуется посчитать сумму чётных чисел, 
# расположенных между числами 1 и N включительно.

n = abs(int(input('Enter n: ')))
sum_even_numbers = 0

#for i in range(n):
#    if (i + 1) % 2 == 0:
#        sum_even_numbers += i + 1
#        print(i + 1, end = ' ')

i = 2
while i <= n:
    sum_even_numbers += i
    print(i, end = ' ')
    i += 2

print()
print(sum_even_numbers)
