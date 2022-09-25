import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz;'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

n = int(input('Введите количество паролей для генерации: '))
len = int(input('Введите длину одного пароля: '))
if input('Включать ли цифры 0123456789? [Д/Н] ') == 'Д':
    chars += digits
if input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? [Д/Н] ') == 'Д':
    chars += lowercase_letters
if input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? [Д/Н] ') == 'Д':
    chars += uppercase_letters
if input('Включать ли символы !#$%&*+-=?@^_? [Д/Н] ') == 'Д':
    chars += punctuation
if input('Исключать ли неоднозначные символы il1Lo0O? [Д/Н] ') == 'Д':
    for c in 'il1Lo0O':
        chars.replace(c, '')

print('Пароли:')
for _ in range(n):
    for _ in range(len):
        print(random.choice(chars), end='')
    print()

print('Все пароли сгенерированы.')