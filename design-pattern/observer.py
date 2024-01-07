# あるインスタンスの状態が変化した際にそのインスタンス自身が「観察者」に状態の変化を「通知」する仕組み
# 状態が変化するインスタンス自体が自ら「通知」する仕組みを持つことで、観察者は常に観察しなければいけない状態から解放される

from abc import ABC, abstractmethod
from typing import Dict


class Observer(ABC):
    @abstractmethod
    def update(self, increment: int):
        pass


class Subject(ABC):
    @abstractmethod
    def add_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class Teacher(Observer):
    def __init__(self):
        self._run_record: Dict[str, int] = {}

    def update(self, student: Subject, increment: int):
        self._run_record[student.name] = self._run_record.get(student.name, 0) + increment

    @property
    def run_record(self) -> Dict[str, int]:
        return self._run_record


class Student(Subject):
    def __init__(self, name: str):
        self._observers: list[Observer] = []
        self._run_count = 0
        self._name = name

    def add_observer(self, observer: Observer):
        self._observers.append(observer)

    def notify_observers(self):
        for o in self._observers:
            o.update(self, self._run_count)

    def run(self, run_count: int):
        self._run_count += run_count
        self.notify_observers()

    @property
    def run_count(self) -> int:
        return self._run_count

    @property
    def name(self) -> str:
        return self._name


if __name__ == "__main__":
    suzuki = Teacher()
    sato = Student("sato")
    sato.add_observer(suzuki)
    sato.run(100)
    print(suzuki.run_record)
