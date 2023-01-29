# Получение содержимого файла.
def read_file(file_path):
    with open(file_path, 'r', encoding = 'utf-8') as f:
        text_file = f.read()
    return text_file

# Получение данных из файла в виде словаря.
def get_data_file(text_file, div_el, div_str):
    data_dict = {}
    text_file = text_file.split(div_str)
    text_file = text_file[:-1]
    for i in text_file:
        i = i.split(div_el)
        data_dict[i[0]] = i[1]
    return data_dict

# Запись данных в журнал.
def update_journal(student, subject, score, journal):
    search_text = str(student) + '-'
    data = open('hw8_journal.txt', 'r')
    new_str = ''
    old_str = ''
    if search_text in journal:
        # print('student found')
        if search_text + str(subject) in journal:
            # print('student and subject found')
            for line in data:
                if search_text + str(subject) in line:
                    old_str = line.replace('\n', '')
                    break
            new_str = old_str + ' ' + score
        else:
            # print('student found and subject NOT found')
            for line in data:
                if search_text in line:
                    old_str = line.replace('\n', '')
                    line = line.split(':')
                    line = line[0].split('-')
                    if int(line[1]) > subject:
                        new_str = f'{student}-{subject}:{score}\n' + old_str
                        break
                    new_str = old_str + f'\n{student}-{subject}:{score}'
        # print(f'old: {old_str}')
        # print(f'new: {new_str}')
        new_data = journal.replace(old_str, new_str)
        # print(new_data)
        # print(f'{old_str} replaced to {new_str}')
        with open ('hw8_journal.txt', 'w', encoding = 'utf-8') as f:
            f.write(new_data)
    else:
        # print('student not found')
        search_text = str(student + 1) + '-'
        if search_text in journal:
            for line in data:
                if search_text in line:
                    old_str = line.replace('\n', '')
                    new_str = f'{student}-{subject}:{score}\n' + old_str
                    break
            new_data = journal.replace(old_str, new_str)
            with open ('hw8_journal.txt', 'w', encoding = 'utf-8') as f:
                f.write(new_data)
        else:
            new_str = f'{student}-{subject}:{score}\n'
            with open ('hw8_journal.txt', 'a', encoding = 'utf-8') as f:
                f.write(new_str)
    data.close()
    print('Данные успешно добавлены!')
