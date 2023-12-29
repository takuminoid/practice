from abc import ABC, abstractmethod


class Pot(ABC):
    pass


class Soup(ABC):
    pass


class Protein(ABC):
    pass


class Vegetable(ABC):
    pass


class Ingredients(ABC):
    pass


class HotPot:
    def __init__(self, pot: Pot):
        self.pot = pot

    def add_soup(self, soup: Soup):
        self.soup = soup

    def add_main(self, protein: Protein):
        self.protein = protein

    def add_vegetables(self, vegetables: list[Vegetable]):
        self.vegetables = vegetables

    def add_other_ingredients(self, other_ingredients: list[Ingredients]):
        self.other_ingredients = other_ingredients


class ChickenBoneSoup(Soup):
    pass


class Chicken(Protein):
    pass


class ChineseCabbage(Vegetable):
    pass


class Leek(Vegetable):
    pass


class Chrysanthemum(Vegetable):
    pass


class Tofu(Ingredients):
    pass


# class SampleClass:
#     def main(self):
#         hot_pot: HotPot = HotPot()
#         hot_pot.add_soup(ChickenBoneSoup())
#         hot_pot.add_main(Chicken())
#         vegetables: list[Vegetable] = []
#         vegetables.append(ChineseCabbage())
#         vegetables.append(Leek())
#         vegetables.append(Chrysanthemum())
#         hot_pot.add_vegetables(vegetables)
#         other_ingredients: list[Ingredients] = []
#         other_ingredients.append(Tofu())
#         hot_pot.add_other_ingredients(other_ingredients)


class Factory(ABC):
    @abstractmethod
    def get_soup(self) -> Soup:
        pass

    @abstractmethod
    def get_main(self) -> Protein:
        pass

    @abstractmethod
    def get_vegetables(self) -> list[Vegetable]:
        pass

    @abstractmethod
    def get_other_ingredients(self) -> list[Ingredients]:
        pass


class MizutakiFactory(Factory):
    def get_soup(self):
        return ChickenBoneSoup()

    def get_main(self):
        return Chicken()

    def get_vegetables(self):
        vegetables: list[Vegetable] = []
        vegetables.append(ChineseCabbage)
        vegetables.append(Leek())
        vegetables.append(Chrysanthemum())
        return vegetables

    def get_other_ingredients(self):
        other_ingredients: list[Ingredients] = []
        other_ingredients.append(Tofu())
        return other_ingredients


class KimuchiFactory(Factory):
    pass


class SukiyakiFactory(Factory):
    pass


class SampleClass:
    def main(self):
        arg = "水炊き"  # 本来は引数をここに渡す
        hot_pot: HotPot = HotPot()
        factory = self.create_factory(arg)
        hot_pot.add_soup(factory.get_soup())
        hot_pot.add_main(factory.get_main())
        hot_pot.add_vegetables(factory.get_vegetables())
        hot_pot.add_other_ingredients(factory.get_other_ingredients())

    def create_factory(str: str) -> Factory:
        if str == "キムチ鍋":
            return KimuchiFactory()
        elif str == "すき焼き":
            return SukiyakiFactory()
        elif str == "水炊き":
            return MizutakiFactory()
