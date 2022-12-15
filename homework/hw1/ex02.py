# (!!!Доп!!!) Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# (0,0,0), (0,0,1) и тд.

my_set = [0, 1]

for i in my_set:
    for j in my_set:
        for k in my_set:
            if (not(my_set[i] or my_set[j] or my_set[k])) == (not my_set[i] and not my_set[j] and not my_set[k]):
                print('True')
                
            else:
                print('False')
            print(f'x = {my_set[i]} y = {my_set[j]} z = {my_set[k]}')
            print(f'{not(my_set[i] or my_set[j] or my_set[k])} = {not my_set[i] and not my_set[j] and not my_set[k]}')
            print()
