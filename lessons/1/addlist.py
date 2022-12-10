colors = ['red', 'green', 'blue']

for e in colors:
    print(e)   # red green blue

for e in colors:
    print(e * 2)  # redred greengreen blueblue

colors.append('gray') # add to end
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') # del colors[0] # delete element

del colors[0]