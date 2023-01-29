# Проверка введенных для выбора варианта данных.
def check_value(value, data):
    if value.isdigit():
        value = int(value)
        if value not in data:
            print('Ошибка! Нет такого значения. Попробуйте снова')
            value = 0
    else:
        print('Введено неверное значение.')
        value = 0
    return value    

# Выбор варианта.
def select_from_list(data, text):
    selected = 0
    while not selected:
        selected = input(text)
        selected = check_value(selected, data)
    return selected

# Учитель или ученик?
def get_type_user():
    type_user = select_from_list([1, 2], 'Представьтесь: 1 - учитель, 2 - ученик: ')
    return type_user

# Учитель: выбор действия - поставить оценку или просмотреть оценки.
def get_type_action():
    type_action = select_from_list([1, 2, 3], 'Выберите действие:\n 1 - поставить оценку,\n 2 - посмотреть оценки\n 3 - Завершить работу\nВведите значение: ')
    return type_action

# Учитель: выбор предмета.
def get_subject():
    subject = select_from_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 'Введите ID предмета из списка: ')
    return subject

# Учитель: выбор ученика.
def get_student(type_user):
    if type_user == 1:
        text = 'Введите ID ученика из списка: '
    else:
        text = 'Введите свой ID: '
    student = select_from_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], text)
    return student

# Учитель: поставить оценку.
def get_score():
    scores = input('Введите оценки через пробел: ')
    return scores

# Учитель и ученик: посмотреть оценки.
def view_journal(path_file, type_user, dict_students, dict_subjects, id_user = 0):
    print('--------------')
    print('ЖУРНАЛ ОЦЕНОК:')
    print('--------------')
    data = open(path_file, 'r')
    showed_user = []
    for line in data:
        line = line.replace('\n', '').split(':')
        line[0] = line[0].split('-')
        if type_user == 1:
            if line[0][0] not in showed_user:
                print(f'\n{line[0][0]}. {dict_students[line[0][0]]}:')
                showed_user.append(line[0][0])
            print(f'{dict_subjects[line[0][1]]}: {line[1]}')
        else:
            if line[0][0] == str(id_user):
                if line[0][0] not in showed_user:
                    print(f'\n{line[0][0]}. {dict_students[line[0][0]]}:')
                    showed_user.append(line[0][0])
                print(f'{dict_subjects[line[0][1]]}: {line[1]}')
    data.close()
    print()
