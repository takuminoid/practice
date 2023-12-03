from abc import ABC, abstractmethod


# インターフェイス
class Chairperson(ABC):
    @abstractmethod
    def organize_class(self):
        pass


class Taro:
    def enjoy_with_all_classmate(self):
        print("みんなで楽しむ")


# 利用したいメソッドが持つクラスを拡張し、
# 利用したいメソッドを定義するインターフェイスを実装する
# 継承を利用したAdapterパターン
class NewTaro(Taro, Chairperson):
    def organize_class(self):
        super().enjoy_with_all_classmate()


class Teacher:
    def __init__(self):
        # chairperson = NewTaro()
        chairperson = Hanako()
        chairperson.organize_class()


# 委譲を利用したAdapterパターン
class Hanako(Chairperson):
    def __init__(self):
        self.taro = Taro()

    def organize_class(self):
        self.taro.enjoy_with_all_classmate()


if __name__ == "__main__":
    Teacher()
