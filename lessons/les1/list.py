# Списки: введение
## list = list

numbers = [1, 2, 3, 4, 5]
print(numbers)                   # [1, 2, 3, 4, 5]
ran = range(1, 6)
numbers = list(ran)              # приведение типа range к типу list
print(numbers)                   
numbers[0] = 10
print(numbers)                   # [10, 2, 3, 4, 5]
for i in numbers:
    i *= 2
    print(i)                     # [20, 4, 6, 8, 10]
print(numbers)                   # [10, 2, 3, 4, 5]