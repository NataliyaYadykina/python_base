# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension
# 2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.
# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]

lst = [12,'sadf',5643]
lst_letter = list(filter(lambda e: type(e) == str, lst))
lst_numbers = list(filter(lambda e: type(e) == int, lst))

print(f'List of letters: {lst_letter}')
print(f'List of numbers: {lst_numbers}')
