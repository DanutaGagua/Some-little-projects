import random

word_list = ['атлас', 'бабочка', 'вентилятор', 'готика', 'дерево', 
             'ель', 'ёжик', 'живот', 'змея', 'земля',
             'ирис', 'йогурт', 'квартира', 'лента', 'лак',
             'маньяк', 'норма', 'очки', 'олимпиада', 'пушка',
             'план', 'ромашка', 'ракета', 'сок', 'система',
             'сон', 'тетрадь', 'торт', 'улитка', 'фракция',
             'химера', 'цирк', 'цыплёнок', 'цыган', 'чай',
             'чашка', 'шишка', 'шашка', 'щепка', 'щетина',
             'эму', 'юбка', 'юла', 'яблоко', 'як']

def get_word():
    return random.choice(word_list).upper()

# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def print_curr_result(tries, word_completion):
    print(display_hangman(tries))
    print('Осталось попыток:', tries)
    print(word_completion)

def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток

    print('Давайте играть в угадайку слов!')
    print_curr_result(tries, word_completion)

    while not guessed and tries > 0:
        c = input('Введите букву или слово: ')
        c = c.upper()

        if not c.isalpha():
            print('Вы ввели не букву и не слово.')
            continue
        elif c in guessed_letters or c in guessed_words:
            print('Вы уже вводили эту букву или слово.')
            continue

        if len(c) == 1 and c in word:
            w = word
            while c in w:
                ind = w.find(c) + word.find(w)
                word_completion = word_completion[:ind] + c + word_completion[ind + 1:]
                w = w[ind + 1:]
        elif len(c) == 1:
            guessed_letters.append(c)
            tries -= 1
        if c != word and len(c) > 1:   
            guessed_words.append(c)
            tries -= 1

        if word_completion == word or c == word:
            guessed = True

        print_curr_result(tries, word_completion)

    if guessed:
        print('Поздравляем, вы угадали слово! Вы победили!')
    else:
        print('К сожалению, у вас кончились попытки.')
    print(word)

while True:
    play(get_word())

    if input('Хотите ещё сыграть? (д/н') == 'н':
        break
