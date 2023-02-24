from utils import load_random_word

from player import Player


def main():
    while True:
        username = input('Введите имя игрока: ')
        if username:
            break

    quiz_word = load_random_word()



if __name__ == '__main__':
    main()
