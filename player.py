class Player:
    def __init__(self, name):
        self.name = name
        self.used_words = []  # Использованные слова

    def get_used_words_len(self) -> int:
        return len(self.used_words)

    def append_used_word(self, word):
        self.used_words.append(word)

    def check_used_word(self, word) -> bool:
        return word in self.used_words

    def __repr__(self):
        return f'Имя: {self.name}, использованные слова: {self.used_words}'
