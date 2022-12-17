# Напишите программу, в которой пользователь будет задавать две строки, 
# одна из них - буква, а вторая фраза/слово,
# программа должна посчитать сколько раз буква встретилась 
# буква во второй строке. (Не используя встроенные функции)

letter, word = input('Enter the letter: '), input('Enter the phrase: ')

count = 0
for ltr in word:
    if ltr == letter:
        count += 1

print(f'Found {count} letters {letter} in phrase {word}.')
