# Количество жизней
import random

lives = 10
# Список слов
# word_variants = ['dog', 'cat', 'cow']
word_variants = ['ddd', 'ccc', 'aaa']

# Слово, которое выбрано для игры
word_right = random.choice(word_variants)

# Слово из "_" с угаданными символами
word_in_game = '_' * len(word_right)

while ("_" in word_in_game) and (lives > 0):
    print(f'{lives=}')
    print(f'{word_in_game=}')
    letter = input('Input character:')

    # Проверка, есть ли выбранная пользователем буква в слове.
    if letter in word_right:
        index = -1
        print('You are right! We have this letter in word.')
        # Замена символов на игровом поле на правильную букву
        while word_in_game.count(letter) != word_right.count(letter):
            index = word_right.find(letter, index + 1)
            word_in_game = word_in_game[:index] + letter + word_in_game[index + 1:]
    else:
        lives -= 1
        print("You've lost one life.")
    print('*' * 10)

if lives > 0:
    print(word_right)
else:
    print('you are lost!')
    print(f'{word_right=}')
