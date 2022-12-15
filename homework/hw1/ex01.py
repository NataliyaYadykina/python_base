# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

day_number = int(input('Write day number: '))

if day_number > 0 and day_number < 8:
    if day_number == 6 or day_number == 7:
        print('Weekend!!! :)')
    else:
        print('Work!')
else:
    print('Wrong number!')
