# �������� ���������, ������� ��������� �� ���� ����� N 
# � ������ ����� ������������ ����� �� 1 �� N.
# ������:
# ����� N = 4, ����� [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Enter n: '))
lst_numbers = []
multi = 1
for i in range(n):
    lst_numbers.append((i + 1) * multi)
    multi *= (i + 1)
print(lst_numbers)