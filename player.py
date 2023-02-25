class Player:
    """Класс, описывающий игрока"""
    def __init__(self, name):
        self.name = name
        self.used_words = []  # Использованные слова

    def get_used_words_len(self) -> int:
        """Возвращает количество использованных слов"""
        return len(self.used_words)

    def append_used_word(self, word: str):
        """Добавляет слово в использованное"""
        self.used_words.append(word)

    def check_used_word(self, word: str) -> bool:
        """Проверяет наличие слова в использованных"""
        return word in self.used_words

    def __repr__(self):
        return f'Имя: {self.name}, использованные слова: {self.used_words}'
