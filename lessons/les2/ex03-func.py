def concatenatio(*params):
	res: str = ""
	for item in params:
		res += item
	return res

print(concatenatio('a', 's', 'd', 'w')) # asdw
print(concatenatio('a', '1')) # a1
#print(concatenatio(1, 2, 3, 4)) # TypeError...