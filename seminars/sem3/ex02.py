# 2. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

lst = ['6', 'str', '123', '4str']
my_str = input('Input string: ')

#count = 0
#for i in range(len(lst)):
#    if lst[i] == my_str:
#        count += 1
#        if count == 2:
#            print('index of element is ', i)
#            break
#if count < 2:
#    print('-1')

if lst.count(my_str) < 2:
    print(-1)
else:
    ind = lst.index(my_str)
    lst.pop(ind)
    print(lst.index(my_str) + 1)
