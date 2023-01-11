def f(x):
    return x ** 2

g = f

print(type(f))
print(type(g))

print(f(4))
print(g(4))