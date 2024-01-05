# Colleagueクラスは直接他のColleagueと通信するのではなくMediatorクラスを介して通信する
# そのため、オブジェクト間の結合度を低く保ち柔軟性が向上される

from abc import ABC, abstractmethod
import random


class Colleague(ABC):
    def __init__(self, name: str):
        self._name = name
        self._mediator = None

    @property
    def name(self) -> str:
        return self._name

    @abstractmethod
    def needs_advice(self):
        pass

    @abstractmethod
    def set_secret_lover(self, colleague: "Colleague"):
        pass

    def set_mediator(self, mediator: "Mediator"):
        self._mediator = mediator


class Mediator(ABC):
    @abstractmethod
    def consultation(self, colleague_in_love: Colleague, secret_lover: Colleague):
        pass


class Saito(Mediator):
    def __init__(self):
        self.colleagues = {}

    def add_colleague(self, colleague: Colleague):
        self.colleagues[colleague.name] = colleague

    def consultation(self, colleague_in_love: Colleague, secret_lover: Colleague):
        # ここで恋愛成就可能性の値を算出
        return random.randint(0, 100)


class Nitta(Colleague):
    def __init__(self):
        super().__init__("Nitta")
        self._tension = 0
        self._secret_lover: Colleague = None

    def set_secret_lover(self, colleague: Colleague):
        self.secret_lover = colleague

    def needs_advice(self):
        if self._mediator and self.secret_lover:
            self.tension = self._mediator.consultation(self, self.secret_lover)
            if self.tension > 50:
                print(f"{self.name}はアドバイスが必要です！")


if __name__ == "__main__":
    saito = Saito()
    nitta = Nitta()
    nitta.set_secret_lover(saito)
    nitta.set_mediator(saito)

    nitta.needs_advice()
