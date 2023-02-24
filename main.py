from utils import load_random_word, show_statistics
from basic_word import BasicWord
from player import Player
from settings import SAFEWORD


def main():
    while True:
        username = input('Введите имя игрока: ')
        if username:
            print(f'Привет, {username}')
            user: Player = Player(username)
            break

    quiz_word: BasicWord = load_random_word()

    print(f'Составьте {quiz_word.len_subwords()} слов из слова {quiz_word.basic_word}\n'
          f'Слова должны быть не короче 3 букв\n'
          f'Чтобы закончитть игру, угадайте все слова или напишите "{SAFEWORD}"\n'
          f'Поехали, ваше первое слово?')

    while True:
        user_input = input('').lower().strip()

        if quiz_word.len_subwords() == len(user.used_words):
            break
        elif user_input == SAFEWORD:
            break
        elif len(user_input) < 3:
            print('слишком короткое слово')
        elif user.check_used_word(user_input):
            print('уже использовано')
        elif not quiz_word.is_word_in_subwords(user_input):
            print('неверно')
        elif user_input in quiz_word.subwords:
            print('верно')
            user.append_used_word(user_input)
        else:
            raise Exception('Unknown exception')

    show_statistics(user)


if __name__ == '__main__':
    main()
