# 1) � ����� ��������� N ����������� �����, ���������� ����� ������. 
# ����� ����� �� ������� ������, ����� ����������� ������� A[i] - 1 = A[i-1]. 
# ������� ��� �����.

def get_missing(lst: list[int]):
    for i in range(1, len(lst)):
        if lst[i] - 1 != lst[i - 1]:
            return lst[i - 1] + 1

with open('numbers_sem5_ex01.txt') as f:
    lst_in = list(map(int, f.read().split()))

print(get_missing(lst_in))
