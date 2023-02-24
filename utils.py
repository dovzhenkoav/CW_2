import requests
import random

from settings import WORDS_ENDPOINT
from basic_word import BasicWord
from player import Player


def show_statistics(user: Player):
    """Отображает статистику отгаданных слов"""
    print(f'Игра завершена, вы угадали {user.get_used_words_len()} слов!')

def load_random_word() -> BasicWord:
    """Получаем список слов с внешнего ресурса, берём случайное слово и запихиваем его в экземпляр BasicWord"""
    words_bank: dict = random.choice(get_words())
    basic_word: BasicWord = BasicWord(words_bank['word'], words_bank['subwords'])
    return basic_word


def get_words() -> list[dict]:
    """Берём с  эндпоинта JSON и возвращаем его в формате python"""
    response = requests.get(WORDS_ENDPOINT)
    return response.json()
