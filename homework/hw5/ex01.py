# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'абвбмдлал врпорлт еапвитд шгоьл прабв абв'
text_del = 'абв'

text_lst = text.split(' ')

new_text = ''
for i in range(len(text_lst) - 1):
    if text_del not in text_lst[i]:
        new_text = new_text + text_lst[i] + ' '

print(new_text)
