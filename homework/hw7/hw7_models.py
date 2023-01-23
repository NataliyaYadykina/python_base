# Получение содержимого телефонной книги.
def read_phone_book(file_path):
    with open(file_path, 'r', encoding = 'utf-8') as f:
        text_book = f.read()
    return text_book

# Получение данных из телефонной книги в виде списка.
def get_data_phone_book(text_book, div_el, div_contact):
    lst_contacts = []
    text_book = text_book.split(div_contact)
    text_book = text_book[:-1]
    for i in text_book:
        i = i.split(div_el)
        lst_contacts.append(i)
    return lst_contacts

# Формирование строки контакта для записи в телефонную книгу.
def str_contact(contact_data, div_el, div_contact):
    str_contact = ''
    for i in range(len(contact_data)):
        str_contact += contact_data[i]
        if i != len(contact_data) - 1:
            str_contact += div_el
    str_contact += div_contact
    return str_contact

# Добавление контакта в телефонную книгу.
def add_contact(str_contact, file_path):
    with open(file_path, 'a', encoding = 'utf-8') as f:
        f.write(str_contact)

# Поиск контакта в телефонной книге.
def search_contact(search_info, contacts):
    result_search = []
    for i in contacts:
        for j in range(len(i)):
            if search_info in i[j]:
                result_search.append(i)
    # print(result_search)
    if not result_search:
        print('Возможно, Вы ввели неверные данные. Попробуйте снова.')
    return result_search

# Редактирование телефонной книги
def edit_contact(old_contact, new_contact, file_path):
    with open (file_path, 'r', encoding = 'utf-8') as f:
        old_data = f.read()

    new_data = old_data.replace(old_contact, new_contact)
    with open (file_path, 'w', encoding = 'utf-8') as f:
        f.write(new_data)
