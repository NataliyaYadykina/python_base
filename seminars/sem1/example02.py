# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.    
#    Примеры:   
#    - 1, 4, 8, 7, 5 -> 8
#    - 78, 55, 36, 90, 2 -> 90

a, b, c, d, e = int(input('a = ')), int(input('b = ')), int(input('c = ')), int(input('d = ')), int(input('e = '))

print(f'Max number: {max(a,b,c,d,e)}')
