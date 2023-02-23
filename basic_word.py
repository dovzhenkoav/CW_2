class BasicWord:
    def __init__(self, basic_word: str, subwords: list[str]):
        self.basic_word: str = basic_word
        self.subwords: list[str] = subwords

    def is_word_in_subwords(self, word: str) -> bool:
        """Проверяем наличие введённого слова в подсловах"""
        return word in self.subwords

    def len_subwords(self) -> int:
        """Возвращает количество подслов у базового слова"""
        return len(self.subwords)

    def __repr__(self):
        return f'Basic word: {self.basic_word}, subwords: {self.subwords}'
