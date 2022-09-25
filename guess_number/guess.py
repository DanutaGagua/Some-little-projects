import random

def is_valid(s, right_number):
    if s.isdigit():
        if 1 <= int(s) <= right_number:
            return True
    return False

print('Добро пожаловать в числовую угадайку.')

while True:
    right_number = int(input('Введите максимальное число диапазона: '))

    number = random.randint(1, right_number)
    try_count = 0

    while True:
        try_count += 1
        s = input('Введите целое число от 1 по ' + str(right_number) + ': ')
        
        if is_valid(s, right_number):
            n = int(s)

            if n == number:
                print('Вы угадали, поздравляем!')
                break
            elif n > number:
                print('Ваше число больше загаданного, попробуйте ещё разок.')
            else:
                print('Ваше число меньше загаданного, попробуйте ещё разок.')
        else:
            print('А может быть всё-таки введем целое число от 1 до ' + str(right_number) + '?')

    print('Количество сделанных попыток:', try_count)
    if input('Хотите ещё сыграть? [Д/Н] ') == 'Н':
        break

print('Спасибо, что играли в числовую угадайку. Ещё увидимся...')
