# Builderパターン = 同じ作成過程で異なる表現形式の結果を得るためのパターン
from abc import ABC, abstractmethod


# 食塩水
class SaltWater:
    def __init__(self, salt_amount: float, water_amount: float):
        self.__salt = salt_amount
        self.__water = water_amount

    @property
    def salt(self):
        return self.__salt

    @salt.setter
    def salt(self, amount: float):
        self.__salt = amount

    @property
    def water(self):
        return self.__water

    @water.setter
    def water(self, amount: float):
        self.__water = amount


# 溶媒と溶質に何を使うかを決定するインターフェイス
class Builder(ABC):
    @abstractmethod
    def add_solute(self, solute_amount: float):
        pass

    @abstractmethod
    def add_solvent(self, solvent_amount: float):
        pass

    @abstractmethod
    def abandon_solution(self, solution_amount: float):
        pass

    @abstractmethod
    def get_result(self):
        pass


class SaltWaterBuilder(Builder):
    def __init__(self):
        self.salt_water = SaltWater(0, 0)

    def add_solute(self, salt_amount: float):
        self.salt_water.salt += salt_amount

    def add_solvent(self, water_amount: float):
        self.salt_water.water += water_amount

    def abandon_solution(self, salt_water_amount: float):
        salt_delta = salt_water_amount * (
            self.salt_water.salt / (self.salt_water.salt + self.salt_water.water)
        )
        water_delta = salt_water_amount * (
            self.salt_water.water / (self.salt_water.salt + self.salt_water.water)
        )
        self.salt_water.salt -= salt_delta
        self.salt_water.water -= water_delta

    def get_result(self) -> SaltWater:
        return self.salt_water


# Builderインターフェイスを利用して「作成過程」に則ってインスタンスを組み立てる
class Director(ABC):
    def __init__(self, builder: Builder):
        self.builder = builder

    def constract(self):
        self.builder.add_solvent(100)
        self.builder.add_solute(40)
        self.builder.abandon_solution(70)
        self.builder.add_solvent(100)
        self.builder.add_solute(15)


if __name__ == "__main__":
    builder = SaltWaterBuilder()
    dir = Director(builder)
    dir.constract()
    salt_water = builder.get_result()
    print(salt_water.salt, salt_water.water)
