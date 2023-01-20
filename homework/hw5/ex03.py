# 3) Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные данные хранятся в отдельных текстовых файлах.
# stroka = "aaabbbbccbbb"
# ....
# stroka = "3a4b2c3b"

# Вывод: stroka = "aaabbbbccbbb"

data = open('hw5_ex03.txt', 'r')
string = data.readline()
data.close()

print(string)

new_string = ''
symbol = string[0]
count = 0
for i in range(len(string)):
    if string[i] == symbol:
        count += 1
    else:
        if count != 0:
            new_string += str(count) + symbol
        count = 1
        symbol = string[i]
    if i == len(string) - 1:
        new_string += str(count) + symbol

print(new_string)

count = ''
res = ''
for i in range(len(new_string)):
    if new_string[i].isdigit():
        count += new_string[i]
    else:
        res += new_string[i] * int(count)
        count = ''

print(res)
