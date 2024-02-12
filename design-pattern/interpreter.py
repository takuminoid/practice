from abc import ABC, abstractmethod, abstractproperty


class Operand(ABC):
    @abstractproperty
    def operand_str(self):
        pass


class Ingredient(Operand):
    def __init__(self, operand_str: str):
        self.__operand_str = operand_str

    @property
    def operand_str(self):
        return self.__operand_str


class Expression(Operand):
    def __init__(self, operator: "Operator"):
        self.__operator = operator

    @property
    def operand_str(self):
        return self.__operator.__class__.__name__


class Operator(ABC):
    @abstractmethod
    def execute(self):
        pass


class Plus(Operator):
    def __init__(self, operand1: Operand, operand2: Operand):
        self.__operand1 = operand1
        self.__operand2 = operand2

    def execute(self):
        return Ingredient(
            self.__operand1.operand_str
            + "と"
            + self.__operand2.operand_str
            + "を足したもの"
        )


class Wait(Operator):
    def __init__(self, minutes: int, operand: Operand):
        self.__minutes = minutes
        self.__operand = operand

    def execute(self):
        return Ingredient(
            self.__operand.operand_str + "を" + str(self.__minutes) + "分間待ったもの"
        )


if __name__ == "__main__":
    liquid_soup = Ingredient("液体スープ")
    hot_water = Ingredient("お湯")
    noodle = Ingredient("麺")
    powdered_soup = Ingredient("粉末スープ")

    def cook_cup_noodle() -> Ingredient:
        one = Plus(liquid_soup, hot_water).execute()
        two = Wait(3, one).execute()
        three = Plus(two, hot_water).execute()
        four = Plus(three, noodle).execute()
        five = Plus(four, powdered_soup).execute()
        return five

    print(cook_cup_noodle().operand_str)
