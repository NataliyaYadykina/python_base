a = {1, 2, 3, 5, 7}
b = {23, 1, 2, 6, 67}

c = a.copy() # c = {1, 2, 3, 5, 7}
print(c)
u = a.union(b) # u = {1, 2, 3, 5, 7, 23, 6, 67}
print(u)
i = a.intersection(b) # i = {1, 2}
print(i)
dl = a.difference(b) # dl = {3, 5, 7}
print(dl)
dr = b.difference(a) # dr = {67, 6, 23}
print(dr)

q = a \
	.union(b) \
	.difference(a.intersection(b))
print(q) # q = {67, 3, 5, 6, 7, 23}

# замороженное (неизменяемое множество), 
# с которым никакие методы добавления/удаления... не работают

s = frozenset(a)