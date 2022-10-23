eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
len_al = 26

new_text = ''

if input('Введите направление (шифрование или дешифрование)(ш/д): ') == 'ш':
    encode = True
else:
    encode = False

if input('Введите язык алфавита (русский или английский)(р/а): ') == 'а':
    lower_alphabet = eng_lower_alphabet
    upper_alphabet = eng_upper_alphabet
    len_al = 26
else:
    lower_alphabet = rus_lower_alphabet
    upper_alphabet = rus_upper_alphabet
    len_al = 32

k = int(input('Введите шаг сдвига: '))

text = input('Введите текст для преобразования: ')
if encode:
    for c in text:
        if c in lower_alphabet:
            new_text += lower_alphabet[(lower_alphabet.index(c) + k) % len_al]
        elif c in upper_alphabet:
            new_text += upper_alphabet[(upper_alphabet.index(c) + k) % len_al]
        else:
            new_text += c
else:
    for c in text:
        if c in lower_alphabet:
            new_text += lower_alphabet[(lower_alphabet.index(c) - k) % len_al]
        elif c in upper_alphabet:
            new_text += upper_alphabet[(upper_alphabet.index(c) - k) % len_al]
        else:
            new_text += c

print(f'Полученный текст: {new_text}')