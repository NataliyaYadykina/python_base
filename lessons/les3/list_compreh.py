# list = []

# for i in range(1, 101):
#     # if(i % 2 == 0):
#     list.append(i)

# print(list)

# list = [i for i in range(1, 21) if i % 2 == 0]
# list = [(i, i) for i in range(1, 21) if i % 2 == 0]

def f(x):
    return x ** 3

# list = [f(i) for i in range(1, 21) if i % 2 == 0]

list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]

print(list)