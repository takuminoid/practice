from abc import ABC, abstractmethod


class Icecream(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def how_sweet(self) -> str:
        pass


class CashewNutsToppinIcecream(Icecream):
    def __init__(self, ice: Icecream):
        self.ice = ice

    def get_name(self):
        name = "カシューナッツ"
        name += self.ice.get_name()
        return name

    def how_sweet(self):
        return self.ice.how_sweet()
