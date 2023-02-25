import requests
import random

from settings import WORDS_ENDPOINT
from basic_word import BasicWord
from player import Player
from settings import SAFEWORD


def quiz_brain(quiz_word, user):
    """Обработчик ответов"""
    while True:
        if quiz_word.len_subwords() == len(user.used_words):
            break

        user_input = input('').lower().strip()

        if user_input in SAFEWORD:
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


def show_statistics(user: Player):
    """Отображает статистику отгаданных слов"""
    print(f'Игра завершена, вы угадали {user.get_used_words_len()} слов!')


def get_user() -> Player:
    """Получаем имя пользователя и создаём с ним экземпляр класса Player"""
    while True:
        username = input('Введите имя игрока: ')
        if username:
            print(f'Привет, {username}')
            user: Player = Player(username)
            break
    return user


def load_random_word() -> BasicWord:
    """Получаем список слов с внешнего ресурса, берём случайное слово и запихиваем его в экземпляр BasicWord"""
    words_bank: dict = random.choice(get_words())
    basic_word: BasicWord = BasicWord(words_bank['word'], words_bank['subwords'])
    return basic_word


def get_words() -> list[dict]:
    """Берём с  эндпоинта JSON и возвращаем его в формате python"""
    response = requests.get(WORDS_ENDPOINT)
    return response.json()
