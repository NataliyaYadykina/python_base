# Напишите программу вычисления арифметического выражения заданного строкой. # Используйте операции +,-,/,*. приоритет операций стандартный. #    *Пример:* #    2+2 => 4;   #    1+2*3 => 7;     #    1-2*3 => -5;

string = '-3 * 20 + 5 - 3 * 3 * 2'
lst = string.split()

def multi(lst):

    while '/' in lst:
        ind = lst.index('/')
        res = int(lst[ind - 1]) / int(lst[ind + 1])
        del lst[(ind - 1) : (ind + 2)]
        lst.insert(ind - 1, res)

    while '*' in lst:
        ind = lst.index('*')
        res = int(lst[ind - 1]) * int(lst[ind + 1])
        del lst[(ind - 1) : (ind + 2)]
        lst.insert(ind - 1, res)

    while '-' in lst:
        ind = lst.index('-')
        res = int(lst[ind - 1]) - int(lst[ind + 1])
        del lst[(ind - 1) : (ind + 2)]
        lst.insert(ind - 1, res)

    while '+' in lst:
        ind = lst.index('+')
        res = int(lst[ind - 1]) + int(lst[ind + 1])
        del lst[(ind - 1) : (ind + 2)]
        lst.insert(ind - 1, res)
    
    return lst

multi(lst)
print(lst)
