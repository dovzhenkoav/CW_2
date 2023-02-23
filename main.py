import random

from utils import get_words
from basic_word import BasicWord


def main():
    while True:
        username = input('Введите имя игрока: ')
        if username:
            break

    words_bank: dict = random.choice(get_words())
    basic_word = BasicWord(words_bank['word'], words_bank['subwords'])


if __name__ == '__main__':
    main()
