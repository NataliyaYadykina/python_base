# ������� ������ �� (2*N+1) ���������, ����������� ������� �� ���������� [-N, N].
# ������� ������������ ��������� �� ��������� ��������. 
# ���� �������� �������� � ������, ������� �� ���� ����������.
# ������ ������ �������� [2, 2, 3, 1, 8]
# ����: 4
# [-4, -3, -2, -1, 0, 1, 2, 3,4]

from random import randint

n = abs(int(input('Enter n: ')))
lst_index = [randint(0, 2 * n) for _ in range(5)]
print(lst_index)

lst_numbers = []
for i in range(2 * n + 1):
   lst_numbers.append(- n + i)
print(lst_numbers)

multi = 1
for i in range(len(lst_index)):
    multi *= lst_numbers[lst_index[i]]
    print(lst_numbers[lst_index[i]], end = ' ')

print()
print(multi)