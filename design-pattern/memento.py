# インスタンスのある時鵜の状態をスナップショットとしての保存を可能にするパターン

from abc import ABC, abstractmethod
from typing import Dict


class Memento:
    def __init__(self, temp: int):
        self._state = temp

    @property
    def state(self) -> int:
        return self._state


class Originator(ABC):
    @abstractmethod
    def create_memento(self) -> Memento:
        pass

    @abstractmethod
    def set_memento(self, memento: Memento) -> None:
        pass


class Calc(Originator):
    def __init__(self):
        self._temp: int = 0
        self._memento: Memento = Memento(self._temp)

    def create_memento(self) -> Memento:  # その時点の状態を保持したMementoオブジェクトを返す
        return Memento(self._temp)

    def set_memento(self, memento: Memento):  # 保存したMementoオブジェクトを元のオブジェクトの状態に戻す
        self._temp = memento.state

    def plus(self, n: int) -> None:
        self._temp += n

    def get_temp(self) -> int:
        return self._temp


class Caretaker:
    def __init__(self):
        self._memento_map: Dict[str, Memento] = {}

    def main(self):
        calc = Calc()
        for n in range(5):
            calc.plus(n)
        print(calc.get_temp())
        self._memento_map["5までの足し算"] = calc.create_memento()

        calc2 = Calc()
        calc2.set_memento(self._memento_map["5までの足し算"])
        for n in range(10):
            calc2.plus(n)
        print(calc2.get_temp())
        self._memento_map["10までの足し算"] = calc2.create_memento()


if __name__ == "__main__":
    sato = Caretaker()
    sato.main()
