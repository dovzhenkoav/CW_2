from utils import get_words


def main():
    while True:
        username = input('Введите имя игрока: ')
        if username:
            break

    words_bank = get_words()


if __name__ == '__main__':
    main()
