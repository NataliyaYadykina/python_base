# data = list(map(int, input().split()))
# print(data)

data = list(map(int, input('Enter numbers: ').split()))
# без list пробежаться по элементам map можно только один раз, поэтому мы и сохраняем в list

for e in data:
    print(e * 2)

print('----')

for e in data:
    print(e * 2)