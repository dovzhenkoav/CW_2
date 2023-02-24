from utils import load_random_word, show_statistics, get_user, quiz_brain
from basic_word import BasicWord
from player import Player
from settings import SAFEWORD


def main():
    user: Player = get_user()
    quiz_word: BasicWord = load_random_word()

    print(f'Составьте {quiz_word.len_subwords()} слов из слова {quiz_word.basic_word}\n'
          f'Слова должны быть не короче 3 букв\n'
          f'Чтобы закончитть игру, угадайте все слова или напишите "{SAFEWORD}"\n'
          f'Поехали, ваше первое слово?')

    quiz_brain(quiz_word, user)
    show_statistics(user)


if __name__ == '__main__':
    main()
