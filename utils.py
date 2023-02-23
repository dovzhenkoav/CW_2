import requests
from settings import WORDS_ENDPOINT


def get_words() -> list[dict]:
    """Берём с  эндпоинта JSON и возвращаем его в формате python"""
    response = requests.get(WORDS_ENDPOINT)
    return response.json()
