# ��������� ����� ���������� ����������� �������� ������ ����� N, �������� �� 1.
# ������:
# ��� n = 15: �����: 3
# ��� n = 35: �����: 5

n = abs(int(input('Enter n > 1: ')))
min_divider = 2
if n > 1:
    for i in range(n):
        if n % (i + 2) == 0:
            min_divider = i + 2
            print(f'The minimal divider = {min_divider}')
            break
else:
    print('Error: wrong the number! Try again.')
