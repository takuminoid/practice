from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def morning_greet(self) -> str:
        pass

    @abstractmethod
    def get_protection_for_cold(self) -> str:
        pass


class BadMoodState(State):
    def morning_greet(self) -> str:
        return "うるさい"

    def get_protection_for_cold(self) -> str:
        return "は？"


class OrdinaryState(State):
    def morning_greet(self) -> str:
        return "おはよう！"

    def get_protection_for_cold(self) -> str:
        return "カイロかな！"


class Yumi:
    def __init__(self):
        self._state: State = OrdinaryState()

    def change_state(self, state: State) -> None:
        self._state = state

    def morning_greet(self) -> str:
        return self._state.morning_greet()

    def get_protection_for_cold(self) -> str:
        return self._state.get_protection_for_cold()

    def main(self):
        print("私は今通常です")
        print(self.morning_greet())
        print(self.get_protection_for_cold())

        self.change_state(BadMoodState())
        print("私は今機嫌が悪いです")
        print(self.morning_greet())
        print(self.get_protection_for_cold())


if __name__ == "__main__":
    yumi = Yumi()
    yumi.main()
