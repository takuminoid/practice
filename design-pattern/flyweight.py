# インスタンスを共有することでリソースを無駄なく使いプログラム全体を軽くする

from typing import Dict


class HumanLetterFactory:
    _instance = None
    _init = True

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if self._init:
            self.human_letters: Dict[str, HumanLetter] = {}
            self._init = False

    def get_human_letter(self, letter: str) -> "HumanLetter":
        human_letter: HumanLetter = self.human_letters.get(letter, None)
        if not human_letter:
            human_letter = HumanLetter(letter)
            self.human_letters[letter] = human_letter
        return human_letter


class HumanLetter:
    def __init__(self, letter: str):
        self._letter = letter

    @property
    def letter(self):
        return self._letter


class Teacher:
    def __init__(self):
        pass

    @staticmethod
    def take_photo(human_letter: HumanLetter):
        print(human_letter.letter)


if __name__ == "__main__":
    factory = HumanLetterFactory()
    a = factory.get_human_letter("あ")
    Teacher.take_photo(a)
    i = factory.get_human_letter("い")
    Teacher.take_photo(i)
    Teacher.take_photo(a)
    u = factory.get_human_letter("う")
    Teacher.take_photo(u)
