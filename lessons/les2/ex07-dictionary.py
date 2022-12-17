dictionary = {}
dictionary = \
    {
        'up': 'u',
        'left': 'l',
        'down': 'd',
        'right': 'r'
    }

print(dictionary['up'])
dictionary['up'] = 'Up'
print(dictionary['up'])
print()

print(dictionary) # 'up':'u', 'left':'l'...
print()
print(dictionary['left']) # l
print()

for k in dictionary.keys(): # keys
    print(k)
print()

for k in dictionary.values(): # values
    print(k)
print()

for v in dictionary: # values
    print(dictionary[v])
print()

for k in dictionary: # full dictionary
    print(dictionary)
print()