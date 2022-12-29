# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# 2*x^2 + 4*x      5*x^2 + 2*x
#    7x^2 + 6x

# 2*x^6 + 4*x      5*x^2 + 2*x
#    2*x^6 + 5x^2 + 6x

polinomial1 = '- 2*x^6 +7*x^5 - 5*x^3 + 4*x+9'
polinomial2 = '8*x^5-5*x^2 + 2*x - 3'

with open('polynomial1.txt', 'w') as data:
    data.write(polinomial1)

with open('polynomial2.txt', 'w') as data:
    data.write(polinomial2)

def read_file(path):
    data = open(path, 'r')
    polinomial = data.readline()
    data.close()
    return polinomial

def poli_splt(polinomial):
    first_negative = 0
    polinomial = polinomial.replace(' ', '')
    if polinomial[:1] == '-':
        first_negative = 1
        polinomial = polinomial[1:]
    if '+' in polinomial:
        polinomial = polinomial.split('+')
    for i in range(len(polinomial)):
        if '-' in polinomial[i]:
            polinomial[i] = polinomial[i].split('-')
    if first_negative == 1:
        first_new = '-' + polinomial[0]
        polinomial[0] = first_new
    return polinomial

def new_dict(polinomial):
    dictionary = {}
    for i in range(len(polinomial)):
        if isinstance(polinomial[i], list):
            for j in range(len(polinomial[i])):
                if 'x' in polinomial[i][j]:
                    polinom = polinomial[i][j].split('*')
                    polinom[0] = int(polinom[0])
                    if j > 0:
                        polinom[0] *= -1
                    dictionary[polinom[1]] = polinom[0]
                else:
                    polinom = int(polinomial[i][j])
                    if j > 0:
                        polinom *= -1
                    dictionary['no'] = polinom
        else:
            if 'x' in polinomial[i]:
                    polinom = polinomial[i].split('*')
                    dictionary[polinom[1]] = int(polinom[0])
            else:
                dictionary['no'] = int(polinomial[i])
    return dictionary

poli1 = read_file('polynomial1.txt')
poli2 = read_file('polynomial2.txt')

poli1 = poli_splt(poli1)
print('poli1: ', poli1)
poli2 = poli_splt(poli2)
print('poli2: ', poli2)
print()

dict1 = new_dict(poli1)
print('dict1: ', dict1)
dict2 = new_dict(poli2)
print('dict2: ', dict2)
print()

result_dict = dict1
for key in result_dict:
    if key in dict2:
        result_dict[key] = result_dict[key] + dict2[key]

for key in dict2:
    if key not in result_dict:
        result_dict[key] = dict2[key]
print('result dict: ', result_dict)

sorted_res_dict = sorted(result_dict.items(), key=lambda x: x[0])
result_dict = dict(sorted_res_dict)
print('sorted result dict: ', result_dict)
print()

res_polinom = ''
for key, values in result_dict.items():
    if key != 'no':
        res_polinom = key + res_polinom
    res_polinom = str(abs(values)) + res_polinom
    if values < 0:
        res_polinom = ' - ' + res_polinom
    else:
        res_polinom = ' + ' + res_polinom
print('result polinom: ', res_polinom)

with open('result_polynom.txt', 'w') as data:
    data.write(res_polinom)