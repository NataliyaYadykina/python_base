# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter_number = int(input('Write quarter number: '))

if 0 < quarter_number < 5:
    if quarter_number == 1:
        print('Range x = (0, infinity), range y = (0, infinity)')
    elif quarter_number == 2:
        print('Range x = (-infinity, 0), range y = (0, infinity)')
    elif quarter_number == 3:
        print('Range x = (-infinity, 0), range y = (-infinity, 0)')
    elif quarter_number == 4:
        print('Range x = (0, infinity), range y = (-infinity, 0)')
else:
    print('Error! Wrong quarter number!')
