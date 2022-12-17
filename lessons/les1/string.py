# Работа со строками 

text = 'съешь ещё этих мягких французских булок'

print(len(text))                   # 39
print('ещё' in text)               # True
print(text.isdigit())              # False
print(text.islower())              # True
print(text.replace('ещё', 'ЕЩЁ'))  #
print(text[0])                     # с
print(text[1])                     # ъ
# print(text[len(text)])           # IndexError
print(text[-5])                    # б
print(text[:])                     # print(text)
print(text[:2])                    # cъ
print(text[len(text) - 2:])        # ок
print(text[2:9])                   # ешь ещё
print(text[6:-18])                 # ещё этих мягких
print(text[0:len(text):6])         # сеикакл
print(text[::6])                   # сеикакл
text = text[2:9] + text[-5] + text[:2] # ........

for c in text:
    print(c)