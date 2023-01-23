# Получение номера действия с телефонной книгой.
def get_move_type():
    move_type = input('''Выберите действие:
  1. Посмотреть телефонную книгу.
  2. Добавить контакт.
  3. Найти контакт.
  4. Изменить контакт.
  5. Удалить контакт.
  6. Завершить работу с книгой.
Укажите номер действия: ''')
    if move_type.isdigit():
        move_type = int(move_type)
        if move_type < 1 or move_type > 6:
            print('ОШИБКА! Введите значения от 1 до 6.')
    else:
        print('ОШИБКА! Нужно ввести номер действия.')
    return move_type

# Просмотр всей телефонной книги или результатов поиска контактов в книге.
def view_phone_book(lst_contacts, move_type):
    if move_type == 1:
        title = 'ТЕЛЕФОННАЯ КНИГА:'
    elif move_type == 3:
        title = 'РЕЗУЛЬТАТЫ ПОИСКА:'
    elif move_type == 4:
        title = 'РЕДАКТИРОВАНИЕ КОНТАКТА:'
    elif move_type == 5:
        title = 'УДАЛЕНИЕ КОНТАКТА:'
    print('-----------------')
    print(title)
    print('-----------------')
    if lst_contacts:
        for i in lst_contacts:
            for j in range(len(i)):
                div = ', '
                if j == len(i) -  1:
                    div = ''
                print(f'{i[j]}{div}', end = '')
            print()
    else:
        print('Контакты не найдены!')
    print('-----------------')

# Получение от пользователя данных контакта для телефонной книги.
def get_contact(move_type):
    if move_type == 2:
        title = 'Добавление нового контакта:'
        result_msg = 'Данные успешно введены!'
    elif move_type == 4:
        title = 'Изменение контакта. Введите новые данные контакта:'
        result_msg = 'Данные успешно изменены!'
    contact = []
    print('-----------------')
    print(title)
    print('-----------------')
    contact.append(input('Введите фамилию: '))
    contact.append(input('Введите имя: '))
    contact.append(input('Введите телефон: '))
    contact.append(input('Введите описание: '))
    print(contact, '\n', result_msg)
    return contact

# Получение данных для поиска контакта в телефонной книге.
def get_search_info(move_type):
    if move_type == 3:
        message = 'Введите фамилию, имя или телефон для поиска контакта: '
    elif move_type == 4:
        message = 'Введите номер телефона контакта, который хотите изменить: '
    elif move_type == 5:
        message = 'Введите номер телефона контакта, который хотите удалить: '
    search_info = input(message)
    if move_type == 4 or move_type == 5:
        if not search_info.isdigit():
            print('ОШИБКА!\nДля редактирования или удаления контакта необходимо ввести НОМЕР ТЕЛЕФОНА.')
    return search_info

# Подтверждение удаления контакта
def get_confirm():
    confirm = input('Подвердите удаление выбранного контакта: 0 - отменить, 1 - удалить: ')
    if confirm == '0' or confirm == '1':
        confirm = int(confirm)
        if confirm == 1:
            print('Данные успешно удалены!')
        else:
            print('Действие отменено.')
    else:
        print('Ошибка! Введено неверное значение.')
    return confirm