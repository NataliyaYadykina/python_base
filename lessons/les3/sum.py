# def sum(x, y):
#     return x + y

# sum = lambda x, y: x + y

def mult(x, y):
    return x * y

def calc(op, a, b):
    print(op(a, b))
    # return op(a, b)

# calc(sum, 4, 5)
calc(lambda x, y: x + y, 4, 5)